#!/usr/bin/env python3
"""Validate the DSA Mastery bootstrap using only the Python standard library."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import sysconfig
import tempfile
import tomllib
import unicodedata
import zipfile
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

UNIT_ID_RE = re.compile(r"DSA-[A-Z]{2,3}-\d{3}")
PROJECT_ID_RE = re.compile(r"DSA-PRJ-\d{3}")
PYTHON_ID_RE = re.compile(r"PY-[A-Z]{3}-\d{3}")
LC_URL_RE = re.compile(r"https://leetcode\.com/problems/([a-z0-9-]+)/")
EXPECTED_UNIT_COUNT = 125
EXPECTED_PROJECT_COUNT = 7
EXPECTED_PROBLEM_COUNT = 121
EXPECTED_PATH_COUNT = 12
EXPECTED_DOMAINS = {
    "FND": 10, "PY": 8, "SEQ": 12, "ORD": 7, "LNK": 6, "SQH": 10,
    "REC": 7, "TRE": 10, "GRA": 15, "GRD": 5, "DP": 14, "BMS": 10,
    "ADV": 4, "SYN": 7,
}
EXPECTED_PROJECT_IDS = [f"DSA-PRJ-{n:03d}" for n in range(10, 80, 10)]
EXPECTED_PATHS = [
    ("absolute-dsa-foundations", "Absolute DSA foundations"),
    ("emergency-interview-revision", "Emergency interview revision"),
    ("seven-day-interview-refresher", "7-day interview refresher"),
    ("fourteen-day-interview-preparation", "14-day interview preparation"),
    ("thirty-day-core-interview-foundation", "30-day core interview foundation"),
    ("ninety-day-comprehensive-interview", "90-day comprehensive interview preparation"),
    ("complete-dsa-mastery", "Complete DSA mastery"),
    ("arrays-strings-repair", "Arrays and strings repair path"),
    ("trees-graphs-repair", "Trees and graphs repair path"),
    ("dynamic-programming-repair", "Dynamic-programming repair path"),
    ("senior-python-backend-interview", "Senior Python/backend coding-interview path"),
    ("mixed-mocks-final-revision", "Mixed mocks and final revision"),
]
REQUIRED_FILES = [
    ".gitignore", ".python-version", "AGENTS.md", "BUNDLE_MANIFEST.md", "CURRICULUM.md",
    "LEARNING_PATHS.md", "PATTERN_INDEX.md", "PROBLEM_BANK.md", "INTERVIEW_PLAYBOOK.md",
    "PYTHON_REFERENCES.md", "NOTEBOOKLM.md", "PROGRESS.md", "PROJECTS.md", "README.md",
    "START_HERE.md", "pyproject.toml", "uv.lock", "data/problems.json",
    "docs/COPYRIGHT_AND_LICENSE.md", "docs/LEETCODE_REFERENCE_POLICY.md",
    "docs/NOTEBOOKLM.md", "docs/SOURCE_AND_VERSION_POLICY.md", "docs/WORKFLOW.md",
    "templates/experiment.md", "templates/mock_interview.md", "templates/practice.md",
    "templates/problem_attempt.md", "templates/project.md", "templates/review.md",
    "templates/unit.md", "scripts/validate_repo.py",
]
# Working checkouts contain local development artifacts that are not repository
# content. Ignore only this narrow allowlist in bootstrap/live profiles.
WORKING_IGNORED_ROOT_DIRECTORIES = {".venv", "venv", "env", "ENV"}
WORKING_IGNORED_DIRECTORY_NAMES = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".hypothesis", "htmlcov",
}
WORKING_IGNORED_FILE_NAMES = {".coverage", "coverage.xml", "coverage.json", "lcov.info"}
WORKING_IGNORED_FILE_SUFFIXES = {".pyc", ".pyo"}
WORKING_FORBIDDEN_COMPONENTS = {
    "private", "tokens", "secrets", "credentials", "transcripts", "chat-exports", ".idea", ".vscode",
}
ARCHIVE_FORBIDDEN_COMPONENTS = (
    WORKING_FORBIDDEN_COMPONENTS
    | WORKING_IGNORED_ROOT_DIRECTORIES
    | WORKING_IGNORED_DIRECTORY_NAMES
)
WORKING_BOOTSTRAP_FORBIDDEN_ROOTS = {"units", "projects", "solutions", "attempts"}
LIVE_FORBIDDEN_ROOTS = {"solutions", "attempts"}
ARCHIVE_FORBIDDEN_ROOTS = {".git", "units", "projects", "solutions", "attempts"}
WORKING_PROFILES = {"bootstrap", "live"}
VALIDATION_PROFILES = {"auto", "bootstrap", "live", "archive"}
DOMAIN_SLUGS = {
    "FND": "problem-solving-foundations",
    "PY": "python-mechanics",
    "SEQ": "sequences-arrays-strings",
    "ORD": "searching-ordering",
    "LNK": "linked-structures",
    "SQH": "stacks-queues-heaps-intervals",
    "REC": "recursion-backtracking",
    "TRE": "trees-tries",
    "GRA": "graphs",
    "GRD": "greedy",
    "DP": "dynamic-programming",
    "BMS": "bits-math-string-algorithms",
    "ADV": "advanced-structures",
    "SYN": "composite-designs",
}
FORBIDDEN_LICENSE_NAMES = {"LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"}
SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".kdbx"}
ALLOWED_PRIORITIES = {"C", "P", "A", "R"}
ALLOWED_FREQUENCIES = {"H", "M", "L"}
ALLOWED_DEPTHS = {"D1", "D2", "D3", "D4"}
ALLOWED_DIFFICULTIES = {1, 2, 3, 4, 5}
ALLOWED_SIZES = {"S", "M", "L", "XL"}
ALLOWED_EVIDENCE = {"E", "T", "I", "P", "D", "X", "(X)", "R", "M"}
ALLOWED_ARTIFACT_STATES = {"Absent", "Draft", "Approved"}
ALLOWED_LEARNING_STATES = {"Not started", "Learning", "Practiced", "Recalled", "Demonstrated", "Retained"}
ALLOWED_PROJECT_STATES = {"Planned", "Active", "Complete"}
ALLOWED_PROBLEM_DIFFICULTIES = {"Easy", "Medium", "Hard"}
ALLOWED_ACCESS = {"free", "premium"}
ALLOWED_TIERS = {"mandatory", "optional", "stretch"}
ALLOWED_VISIBILITY = {"teaching", "mixed", "mock"}
ALLOWED_RESERVE_POOLS = {"teaching", "unlabeled_easy_medium", "hard_stretch_mock"}
REQUIRED_DEV_TOOLS = {"hypothesis", "mypy", "pytest", "pytest-cov", "ruff"}
SIZE_HOURS = {
    "S": ((1, 2), (2, 4)), "M": ((2, 4), (4, 8)),
    "L": ((4, 7), (8, 14)), "XL": ((7, 12), (14, 24)),
}
RAPID_MINUTES = {"S": (20, 30), "M": (30, 45), "L": (45, 65), "XL": (65, 90)}
REQUIRED_PATTERN_UNITS = {
    "linear scans": "DSA-SEQ-010", "frequency maps": "DSA-SEQ-020", "read/write pointers": "DSA-SEQ-030",
    "two pointers": "DSA-SEQ-040", "fixed sliding window": "DSA-SEQ-050", "variable sliding window": "DSA-SEQ-060",
    "prefix sums": "DSA-SEQ-070", "suffix aggregates": "DSA-SEQ-080", "difference arrays": "DSA-SEQ-090",
    "Kadane": "DSA-SEQ-100", "cyclic placement": "DSA-SEQ-110", "matrices": "DSA-SEQ-120",
    "binary search": "DSA-ORD-010", "boundary search": "DSA-ORD-020", "rotated search": "DSA-ORD-030",
    "binary search on answer": "DSA-ORD-040", "merge sort": "DSA-ORD-050", "quickselect": "DSA-ORD-060",
    "counting/buckets": "DSA-ORD-070", "linked reversal": "DSA-LNK-020", "linked cycle detection": "DSA-LNK-030",
    "monotonic stack": "DSA-SQH-030", "monotonic deque": "DSA-SQH-040", "interval merge": "DSA-SQH-050",
    "sweep line": "DSA-SQH-060", "heaps": "DSA-SQH-070", "top K": "DSA-SQH-080", "K-way merge": "DSA-SQH-090",
    "backtracking": "DSA-REC-040", "tree DFS": "DSA-TRE-020", "tree BFS": "DSA-TRE-030", "BST": "DSA-TRE-060",
    "tries": "DSA-TRE-090", "graph BFS": "DSA-GRA-020", "graph DFS": "DSA-GRA-030", "components": "DSA-GRA-040",
    "multi-source BFS": "DSA-GRA-050", "bipartite": "DSA-GRA-060", "graph cycles": "DSA-GRA-070",
    "topological sort": "DSA-GRA-080", "union-find": "DSA-GRA-090", "shortest path selection": "DSA-GRA-100",
    "Dijkstra": "DSA-GRA-110", "Bellman-Ford/Floyd-Warshall": "DSA-GRA-120", "MST": "DSA-GRA-130",
    "0-1 BFS": "DSA-GRA-140", "low-link DFS": "DSA-GRA-150", "SCC": "DSA-GRA-150", "greedy proofs": "DSA-GRD-020",
    "DP state modeling": "DSA-DP-010", "memoization/tabulation": "DSA-DP-020", "knapsack": "DSA-DP-050",
    "LIS": "DSA-DP-080", "string DP": "DSA-DP-090", "interval DP": "DSA-DP-100", "state-machine DP": "DSA-DP-110",
    "tree DP": "DSA-DP-120", "bitmask DP": "DSA-DP-130", "digit DP": "DSA-DP-140", "bits": "DSA-BMS-010",
    "XOR": "DSA-BMS-020", "sieve": "DSA-BMS-050", "rolling hash": "DSA-BMS-080", "KMP": "DSA-BMS-090",
    "Z/suffix": "DSA-BMS-100", "Fenwick": "DSA-ADV-010", "segment tree": "DSA-ADV-020",
}
REQUIRED_DATA_STRUCTURE_UNITS = {
    "arrays/dynamic arrays": "DSA-PY-010", "strings": "DSA-PY-010", "hash tables": "DSA-PY-020",
    "linked lists": "DSA-LNK-010", "stacks/queues/deques": "DSA-SQH-010", "heaps": "DSA-SQH-070",
    "trees": "DSA-TRE-010", "BST": "DSA-TRE-060", "tries": "DSA-TRE-090", "graphs": "DSA-GRA-010",
    "DSU": "DSA-GRA-090", "Fenwick": "DSA-ADV-010", "segment tree": "DSA-ADV-020",
}
APPROVED_PYTHON_IDS = {
    "PY-FND-020", "PY-BLT-020", "PY-BLT-040", "PY-BLT-050", "PY-BLT-060", "PY-BLT-080", "PY-BLT-090",
    "PY-FIT-060", "PY-FIT-070", "PY-FIT-080", "PY-FIT-090", "PY-LIB-010", "PY-LIB-020", "PY-LIB-040",
    "PY-LIB-050", "PY-LIB-060", "PY-OBJ-010", "PY-TYP-020", "PY-TYP-030", "PY-MOD-010",
    "PY-TST-020", "PY-TST-030", "PY-TST-050", "PY-MPR-070", "PY-MPR-080",
}

REQUIRED_UNIT_SEMANTICS = {
    "DSA-GRA-150": {
        "title_keywords": {"low-link", "bridges", "articulation", "strongly connected"},
        "outcome_keywords": {"discovery", "low-link", "bridges", "articulation", "undirected", "directed", "scc"},
    },
}
GENERIC_FOLLOW_UP_MARKERS = {
    "change one constraint", "solve a variation", "adapt the solution",
    "add one requirement", "follow-up variation", "modify the problem",
}
ONLINE_VERIFICATION_STATUSES = {"not_started", "partial", "complete"}
IMPORTANT_REPORT_STATISTICS = (
    "domains", "domain_unit_counts", "curriculum_units", "unique_unit_ids",
    "prerequisite_edges", "required_algorithmic_patterns",
    "required_data_structure_families", "learning_paths",
    "learning_path_topic_links", "learning_path_problem_links",
    "learning_path_project_callouts", "projects", "unique_problem_references",
    "problem_tiers", "problem_difficulties", "problem_access",
    "problem_visibility", "problem_reserve_pools",
    "renewable_easy_medium_reserve", "hard_stretch_mock_pool",
    "renewable_ten_problem_sets_before_recycling", "practice_coverage_rows",
    "practice_micro_labs", "python_mastery_references", "markdown_files",
    "markdown_tables", "markdown_links", "code_fence_blocks",
    "template_relative_links", "development_dependencies", "locked_packages",
    "required_files", "required_files_present",
    "official_problem_pages_confirmed", "official_problem_pages_remaining",
    "online_verification_status",
)

MANUAL_ITEMS = [
    "Pedagogical excellence and visual clarity of future generated units",
    "Interview realism and correctness of future generated solutions",
    "Idiomatic quality of future AI-generated Python code",
    "Copyright originality of future generated explanations and examples",
]


REQUIRED_UNIT_README_HEADINGS = (
    "## Physical Notebook Core",
    "## 1. Learning outcomes and evidence",
    "## 3. Intuition and problem shape",
    "## 4. Brute force and bottleneck",
    "## 5. Derivation and invariant",
    "## 6. Detailed visual trace",
    "## 8. Correctness reasoning",
    "## 9. Complexity derivation",
    "## 10. Implementations",
    "## 11. Edge-case matrix",
    "## 12. Comparisons and anti-signals",
    "## 13. Common bugs and debugging",
    "## 14. Practice ladder",
    "## 15. Interview questions, traps, and follow-ups",
    "## 16. Explanation exercises",
    "## 17. Experiment decision",
    "## 19. Python Mastery references",
    "## 20. Authoritative sources",
)
REQUIRED_REVIEW_HEADINGS = (
    "## Closed-book reconstruction questions",
    "## Delayed-recall questions",
    "## Interview retrieval",
    "## One-question-at-a-time evidence record",
    "## Evidence",
    "## Error log update",
    "## State decision",
)
PREMATURE_SOLUTION_MARKERS = (
    "## complete solution",
    "### complete solution",
    "## full solution",
    "### full solution",
    "here is the complete solution",
    "final solution code",
    "<!-- solution revealed -->",
)
INITIALIZED_FILLER_MARKERS = (
    "explain the concept in simple language",
    "include only when educational",
    "record genuine uncertainty",
    "add only after rahul closes",
)

@dataclass(frozen=True)
class Unit:
    unit_id: str; title: str; outcome: str; prerequisites: tuple[str, ...]
    priority: str; interview: str; practical: str; python: str; depth: str
    difficulty: int; scopes: tuple[str, ...]; size: str
    first_hours: tuple[int, int]; practice_hours: tuple[int, int]
    evidence: tuple[str, ...]; anchor: str

@dataclass(frozen=True)
class ProgressEntry:
    unit_id: str
    title: str
    priority: str
    artifact_state: str
    learning_state: str

@dataclass(frozen=True)
class RouteDecision:
    status: str
    action: str | None = None
    error_code: str | None = None
    detail: str | None = None

@dataclass
class Report:
    root: Path
    profile: str = "auto"
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: dict[str, str] = field(default_factory=dict)
    statistics: dict[str, object] = field(default_factory=dict)
    archive: dict[str, object] | None = None
    skipped_external_checks: list[str] = field(default_factory=list)
    self_tests: dict[str, object] | None = None
    def error(self, message: str) -> None: self.errors.append(message)
    def warning(self, message: str) -> None: self.warnings.append(message)
    def mark(self, name: str, result: bool | str) -> None:
        if isinstance(result, str):
            if result not in {"passed", "failed", "skipped"}: raise ValueError(result)
            self.checks[name] = result
        else: self.checks[name] = "passed" if result else "failed"
    def as_dict(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "status": "passed" if not self.errors else "failed",
            "repository_root": ".",
            "validation_profile": self.profile,
            "validation_scope": {"automated": "completed", "manual_inspection": {"status": "not_performed", "items": MANUAL_ITEMS}},
            "checks": self.checks, "statistics": self.statistics, "archive": self.archive,
            "skipped_external_checks": self.skipped_external_checks, "self_tests": self.self_tests,
            "errors": self.errors, "warnings": self.warnings,
        }

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""): h.update(block)
    return h.hexdigest()

def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")): return []
    body = stripped[1:-1]; cells = []; current = []; escaped = False
    for ch in body:
        if escaped: current.append(ch); escaped = False
        elif ch == "\\": current.append(ch); escaped = True
        elif ch == "|": cells.append("".join(current).strip()); current = []
        else: current.append(ch)
    cells.append("".join(current).strip())
    return cells

def parse_range(text: str, suffix: str = "h") -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)–(\d+)\s*" + re.escape(suffix), text.strip())
    if not match: raise ValueError(text)
    return int(match.group(1)), int(match.group(2))

def resolve_profile(root: Path, profile: str) -> str:
    if profile not in VALIDATION_PROFILES:
        raise ValueError(f"Unknown validation profile: {profile}")
    if profile != "auto":
        return profile
    if (root / "units").exists() or (root / "projects").exists():
        return "live"
    return "bootstrap"


def forbidden_roots_for_profile(profile: str) -> set[str]:
    if profile == "bootstrap":
        return WORKING_BOOTSTRAP_FORBIDDEN_ROOTS
    if profile == "live":
        return LIVE_FORBIDDEN_ROOTS
    if profile == "archive":
        return ARCHIVE_FORBIDDEN_ROOTS
    raise ValueError(f"Unknown resolved validation profile: {profile}")


def is_ignored_root_git_metadata(root: Path, path: Path, profile: str) -> bool:
    """Return True only for repository-root Git metadata in working profiles."""
    if profile not in WORKING_PROFILES:
        return False
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    return bool(relative.parts and relative.parts[0] == ".git")


def is_working_ignored_directory(root: Path, path: Path, profile: str) -> bool:
    """Return True for an explicitly allowed local-only directory in a working profile."""
    if profile not in WORKING_PROFILES:
        return False
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    if not relative.parts:
        return False
    if relative.parts[0] == ".git":
        return True
    if len(relative.parts) == 1 and relative.name in WORKING_IGNORED_ROOT_DIRECTORIES:
        return True
    return any(part in WORKING_IGNORED_DIRECTORY_NAMES for part in relative.parts)


def is_working_ignored_file(root: Path, path: Path, profile: str) -> bool:
    """Return True for an explicitly allowed local-only file in a working profile."""
    if profile not in WORKING_PROFILES:
        return False
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    if not relative.parts:
        return False
    if relative.parts[0] == ".git":
        return True
    if len(relative.parts) > 1 and (
        relative.parts[0] in WORKING_IGNORED_ROOT_DIRECTORIES
        or any(part in WORKING_IGNORED_DIRECTORY_NAMES for part in relative.parts[:-1])
    ):
        return True
    name = relative.name
    return (
        name in WORKING_IGNORED_FILE_NAMES
        or name.startswith(".coverage.")
        or path.suffix.lower() in WORKING_IGNORED_FILE_SUFFIXES
    )


def is_archive_working_artifact(parts: tuple[str, ...]) -> bool:
    """Return True for an environment/cache/bytecode/coverage path forbidden in ZIPs."""
    if not parts:
        return False
    name = parts[-1]
    return (
        any(part in WORKING_IGNORED_ROOT_DIRECTORIES for part in parts)
        or any(part in WORKING_IGNORED_DIRECTORY_NAMES for part in parts)
        or name in WORKING_IGNORED_FILE_NAMES
        or name.startswith(".coverage.")
        or PurePosixPath(name).suffix.lower() in WORKING_IGNORED_FILE_SUFFIXES
    )


def is_sensitive_env_file(path: Path | PurePosixPath) -> bool:
    name = path.name
    return name == ".env" or name.startswith(".env.")


def iter_repository_files(root: Path, profile: str) -> list[Path]:
    """List repository content while pruning explicit local-only artifacts in working profiles."""
    files_found: list[Path] = []
    for current, directories, files in os.walk(root):
        current_path = Path(current)
        if is_working_ignored_directory(root, current_path, profile):
            directories[:] = []
            continue
        directories[:] = [
            name
            for name in directories
            if not is_working_ignored_directory(root, current_path / name, profile)
        ]
        for filename in files:
            path = current_path / filename
            if is_working_ignored_file(root, path, profile):
                continue
            files_found.append(path)
    return sorted(files_found)


def pytest_prerequisite_error(operation: str) -> str | None:
    if shutil.which("uv") is None:
        return (
            f"[EXTENDED_TEST_PREREQUISITE_MISSING] {operation} requires the uv executable and "
            "the locked development group. Install uv, run `uv sync --group dev`, then retry "
            "through `uv run --group dev python scripts/validate_repo.py ...`."
        )
    if importlib.util.find_spec("pytest") is not None:
        return None
    return (
        f"[EXTENDED_TEST_PREREQUISITE_MISSING] {operation} requires pytest from the locked "
        "development group. Run `uv sync --group dev`, then rerun through "
        "`uv run --group dev python scripts/validate_repo.py ...`."
    )


def validate_required_files_and_hygiene(report: Report) -> None:
    missing = [name for name in REQUIRED_FILES if not (report.root / name).is_file()]
    if missing:
        report.error(f"Missing required files: {missing}")
    for name in FORBIDDEN_LICENSE_NAMES:
        if (report.root / name).exists():
            report.error(f"Forbidden license file present: {name}")
    gitignore_text = (report.root / ".gitignore").read_text(encoding="utf-8") if (report.root / ".gitignore").is_file() else ""
    for required_private_ignore in ("private/", "tokens/"):
        if required_private_ignore not in gitignore_text:
            report.error(f"[GITIGNORE_PRIVATE_PATH_MISSING] .gitignore must include {required_private_ignore}")

    forbidden_roots = forbidden_roots_for_profile(report.profile)
    for current, directories, files in os.walk(report.root):
        current_path = Path(current)
        if is_working_ignored_directory(report.root, current_path, report.profile):
            directories[:] = []
            continue
        directories[:] = [
            name
            for name in directories
            if not is_working_ignored_directory(report.root, current_path / name, report.profile)
        ]

        for directory in list(directories):
            rel = (current_path / directory).relative_to(report.root)
            if rel.parts and rel.parts[0] == ".git" and report.profile == "archive":
                report.error(f"[PROFILE_FORBIDDEN_GIT_METADATA] archive profile forbids Git metadata: {rel}")
                directories.remove(directory)
                continue
            if rel.parts and rel.parts[0] in forbidden_roots:
                report.error(f"[PROFILE_FORBIDDEN_ROOT_PATH] {report.profile} profile forbids: {rel}")
                directories.remove(directory)
                continue
            components = ARCHIVE_FORBIDDEN_COMPONENTS if report.profile == "archive" else WORKING_FORBIDDEN_COMPONENTS
            if any(part in components for part in rel.parts):
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] {report.profile} profile forbids: {rel}")
                directories.remove(directory)

        for filename in files:
            path = current_path / filename
            rel = path.relative_to(report.root)
            if is_working_ignored_file(report.root, path, report.profile):
                continue
            if ".git" in rel.parts and report.profile == "archive":
                report.error(f"[PROFILE_FORBIDDEN_GIT_METADATA] archive profile forbids Git metadata: {rel}")
                continue
            if rel.parts and rel.parts[0] in forbidden_roots:
                report.error(f"[PROFILE_FORBIDDEN_ROOT_PATH] {report.profile} profile forbids: {rel}")
            if report.profile == "archive" and is_archive_working_artifact(rel.parts):
                report.error(f"[PROFILE_FORBIDDEN_WORKING_ARTIFACT] archive profile forbids local artifact: {rel}")
            components = ARCHIVE_FORBIDDEN_COMPONENTS if report.profile == "archive" else WORKING_FORBIDDEN_COMPONENTS
            if any(part in components for part in rel.parts):
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] {report.profile} profile forbids: {rel}")
            if is_sensitive_env_file(rel):
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] {report.profile} profile forbids environment file: {rel}")
            if path.suffix.lower() in SENSITIVE_SUFFIXES:
                report.error(f"Sensitive file type present: {rel}")

    report.statistics["required_files"] = len(REQUIRED_FILES)
    report.statistics["required_files_present"] = len(REQUIRED_FILES) - len(missing)
    report.statistics["validation_profile"] = report.profile
    report.mark(
        "required_files_and_hygiene",
        not missing and not any(
            "FORBIDDEN_ROOT_PATH" in error
            or "FORBIDDEN_GIT_METADATA" in error
            or "FORBIDDEN_PRIVATE_PATH" in error
            or "FORBIDDEN_WORKING_ARTIFACT" in error
            or "Forbidden" in error
            or "Sensitive" in error
            for error in report.errors
        ),
    )

def parse_units(report: Report) -> tuple[list[Unit], dict[str, Unit]]:
    text = (report.root / "CURRICULUM.md").read_text(encoding="utf-8")
    row_re = re.compile(
        r'^\| <a id="(?P<anchor>dsa-[a-z]{2,3}-\d{3})"></a>`(?P<id>DSA-[A-Z]{2,3}-\d{3})` — \*\*(?P<title>.+?)\*\* '
        r'\| (?P<outcome>.*?) \| (?P<prereqs>.*?) \| `(?P<class>[^`]+)` \| (?P<difficulty>\d) '
        r'\| (?P<scope>.*?) \| `(?P<size>S|M|L|XL)` \| (?P<first>\d+–\d+ h) '
        r'\| (?P<practice>\d+–\d+ h) \| `(?P<evidence>[^`]+)` \|$', re.MULTILINE)
    rows: list[Unit] = []
    for m in row_re.finditer(text):
        g = m.groupdict(); class_parts = g["class"].split("/")
        if len(class_parts) != 5:
            report.error(f"Invalid class code for {g['id']}: {g['class']}"); class_parts = ["?" for _ in range(5)]
        try: first, practice = parse_range(g["first"]), parse_range(g["practice"])
        except ValueError:
            report.error(f"Invalid time range for {g['id']}"); first = practice = (0, 0)
        rows.append(Unit(
            g["id"], g["title"], g["outcome"], tuple(UNIT_ID_RE.findall(g["prereqs"])),
            class_parts[0], class_parts[1], class_parts[2], class_parts[3], class_parts[4],
            int(g["difficulty"]), tuple(re.findall(r"`([^`]+)`", g["scope"])), g["size"], first, practice,
            tuple(g["evidence"].split("+")), g["anchor"],
        ))
    by_id = {u.unit_id: u for u in rows}
    if len(rows) != EXPECTED_UNIT_COUNT: report.error(f"Expected {EXPECTED_UNIT_COUNT} curriculum units, found {len(rows)}")
    if len(by_id) != len(rows): report.error(f"Duplicate curriculum IDs: {[x for x,c in Counter(u.unit_id for u in rows).items() if c>1]}")
    declared = re.search(r"canonical catalog of \*\*(\d+) independently", text)
    if not declared or int(declared.group(1)) != len(rows): report.error("Declared curriculum unit count does not match parsed rows")
    domains = Counter(u.unit_id.split("-")[1] for u in rows)
    if dict(domains) != EXPECTED_DOMAINS: report.error(f"Domain counts differ: {dict(domains)}")
    for u in rows:
        if u.anchor != u.unit_id.lower(): report.error(f"Wrong anchor for {u.unit_id}: {u.anchor}")
        if u.priority not in ALLOWED_PRIORITIES: report.error(f"Invalid priority for {u.unit_id}: {u.priority}")
        for name,value in (("interview",u.interview),("practical",u.practical),("python",u.python)):
            if value not in ALLOWED_FREQUENCIES: report.error(f"Invalid {name} frequency for {u.unit_id}: {value}")
        if u.depth not in ALLOWED_DEPTHS: report.error(f"Invalid depth for {u.unit_id}: {u.depth}")
        if u.difficulty not in ALLOWED_DIFFICULTIES: report.error(f"Invalid difficulty for {u.unit_id}: {u.difficulty}")
        if u.size not in ALLOWED_SIZES or SIZE_HOURS.get(u.size) != (u.first_hours,u.practice_hours): report.error(f"Invalid size/time contract for {u.unit_id}")
        if not u.scopes: report.error(f"No scope for {u.unit_id}")
        invalid_evidence = set(u.evidence) - ALLOWED_EVIDENCE
        if invalid_evidence: report.error(f"Invalid evidence for {u.unit_id}: {sorted(invalid_evidence)}")
        for p in u.prerequisites:
            if p not in by_id: report.error(f"Unknown prerequisite {p} for {u.unit_id}")
    order = {u.unit_id:i for i,u in enumerate(rows)}
    for u in rows:
        for p in u.prerequisites:
            if p in order and order[p] >= order[u.unit_id]: report.error(f"Curriculum prerequisite appears after dependent: {p} -> {u.unit_id}")
    graph: dict[str,list[str]] = defaultdict(list); indegree = {u.unit_id:0 for u in rows}
    for u in rows:
        for p in u.prerequisites:
            if p in by_id: graph[p].append(u.unit_id); indegree[u.unit_id] += 1
    q = deque([uid for uid,d in indegree.items() if d==0]); visited=0
    while q:
        node=q.popleft(); visited+=1
        for nxt in graph[node]:
            indegree[nxt]-=1
            if indegree[nxt]==0: q.append(nxt)
    if visited != len(rows): report.error("Curriculum prerequisite cycle detected")
    report.statistics.update({
        "domains":len(domains), "domain_unit_counts":dict(domains), "curriculum_units":len(rows),
        "unique_unit_ids":len(by_id), "prerequisite_edges":sum(len(u.prerequisites) for u in rows),
    })
    report.mark("curriculum", not any("curriculum" in e.lower() or "prerequisite" in e.lower() for e in report.errors))
    return rows, by_id


def validate_required_coverage(report: Report, units: dict[str, Unit]) -> None:
    for label, uid in {**REQUIRED_PATTERN_UNITS, **REQUIRED_DATA_STRUCTURE_UNITS}.items():
        if uid not in units:
            report.error(f"Missing required coverage {label}: {uid}")
    for uid, contract in REQUIRED_UNIT_SEMANTICS.items():
        unit = units.get(uid)
        if not unit:
            report.error(f"Missing semantic required unit: {uid}")
            continue
        title = unit.title.lower()
        outcome = unit.outcome.lower()
        missing_title = [word for word in contract["title_keywords"] if word not in title]
        missing_outcome = [word for word in contract["outcome_keywords"] if word not in outcome]
        if missing_title or missing_outcome:
            report.error(
                f"Semantic required-unit mismatch for {uid}: missing title keywords {missing_title}; "
                f"missing outcome keywords {missing_outcome}"
            )
    combined = ((report.root / "CURRICULUM.md").read_text() + (report.root / "PATTERN_INDEX.md").read_text()).lower()
    for phrase in [
        "sliding window vs prefix sum", "two pointers vs binary search", "bfs vs dfs", "heap vs sorting",
        "greedy vs dynamic programming", "backtracking vs dynamic programming", "union-find vs graph traversal",
        "monotonic stack vs heap", "memoization vs tabulation", "trie vs hash map",
        "shortest-path algorithm selection", "bridges", "articulation points", "strongly connected components",
    ]:
        if phrase not in combined:
            report.error(f"Missing comparison/coverage phrase: {phrase}")
    report.statistics["required_algorithmic_patterns"] = len(REQUIRED_PATTERN_UNITS)
    report.statistics["required_data_structure_families"] = len(REQUIRED_DATA_STRUCTURE_UNITS)
    report.mark("coverage_matrix", not any("coverage" in e.lower() or "semantic required-unit" in e.lower() for e in report.errors))

def load_problem_data(report: Report, units: dict[str, Unit]) -> tuple[dict[str, object], dict[int, dict[str, object]]]:
    path = report.root / "data/problems.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        report.error(f"Cannot parse data/problems.json: {exc}")
        return {}, {}
    if payload.get("schema_version") != 1:
        report.error("Problem metadata schema_version must be 1")
    policy = payload.get("metadata_policy", {})
    online = policy.get("online_verification", {}) if isinstance(policy, dict) else {}
    if not isinstance(online, dict):
        report.error("Problem metadata online_verification must be an object")
        online = {}
    confirmed_raw = online.get("official_pages_confirmed", [])
    confirmed_numbers: list[int] = []
    if not isinstance(confirmed_raw, list):
        report.error("Online verification official_pages_confirmed must be a list")
    else:
        for value in confirmed_raw:
            if not isinstance(value, int) or value <= 0:
                report.error(f"Online verification contains an invalid confirmed problem number: {value}")
            else:
                confirmed_numbers.append(value)
    items = payload.get("problems")
    if not isinstance(items, list):
        report.error("Problem metadata must contain a problems list")
        return payload, {}
    required = {
        "number", "title", "slug", "url", "difficulty", "access", "owner_unit", "primary_pattern",
        "secondary_concepts", "prerequisites", "learning_purpose", "selection_reason", "tier", "visibility",
        "first_attempt_minutes", "trap_categories", "review_requirements", "original_follow_up_variations",
        "free_alternative", "secondary_units", "reserve_pool",
    }
    by_number: dict[int, dict[str, object]] = {}
    exact_followups: Counter[str] = Counter()
    exact_traps: Counter[tuple[str, ...]] = Counter()
    exact_reviews: Counter[tuple[str, ...]] = Counter()
    for idx, problem in enumerate(items):
        if not isinstance(problem, dict):
            report.error(f"Problem entry {idx} is not an object")
            continue
        missing = required - set(problem)
        if missing:
            report.error(f"Problem entry {idx} missing fields: {sorted(missing)}")
            continue
        number = problem["number"]
        if not isinstance(number, int) or number <= 0:
            report.error(f"Invalid problem number at entry {idx}: {number}")
            continue
        if number in by_number:
            report.error(f"Duplicate problem number/ownership: {number}")
        by_number[number] = problem
        title, slug, url = problem["title"], problem["slug"], problem["url"]
        if not isinstance(title, str) or not title.strip():
            report.error(f"Missing title for LC {number}")
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9-]+", slug):
            report.error(f"Malformed slug for LC {number}: {slug}")
        if url != f"https://leetcode.com/problems/{slug}/" or not LC_URL_RE.fullmatch(str(url)):
            report.error(f"Malformed canonical LeetCode URL for LC {number}: {url}")
        if problem["difficulty"] not in ALLOWED_PROBLEM_DIFFICULTIES:
            report.error(f"Invalid difficulty for LC {number}: {problem['difficulty']}")
        if problem["access"] not in ALLOWED_ACCESS:
            report.error(f"Invalid access for LC {number}: {problem['access']}")
        if problem["tier"] not in ALLOWED_TIERS or problem["visibility"] not in ALLOWED_VISIBILITY:
            report.error(f"Invalid tier/visibility for LC {number}")
        if problem["reserve_pool"] not in ALLOWED_RESERVE_POOLS:
            report.error(f"Invalid reserve_pool for LC {number}: {problem['reserve_pool']}")
        if problem["owner_unit"] not in units:
            report.error(f"Unknown owner {problem['owner_unit']} for LC {number}")
        for uid in problem["prerequisites"] + problem["secondary_units"]:
            if uid not in units:
                report.error(f"Unknown unit reference {uid} for LC {number}")
        if not isinstance(problem["first_attempt_minutes"], int) or problem["first_attempt_minutes"] <= 0:
            report.error(f"Invalid timebox for LC {number}")
        if problem["tier"] == "mandatory" and problem["access"] == "premium":
            alt = problem.get("free_alternative")
            if not isinstance(alt, int) or alt == number:
                report.error(f"Premium-only mandatory problem lacks a free alternative: LC {number}")
        for key in ("secondary_concepts", "prerequisites", "trap_categories", "review_requirements", "original_follow_up_variations", "secondary_units"):
            value = problem[key]
            if not isinstance(value, list):
                report.error(f"{key} must be a list for LC {number}")
                continue
            if any(not isinstance(item, str) or not item.strip() for item in value):
                report.error(f"{key} contains a semantically empty item for LC {number}")
        traps = problem["trap_categories"]
        if (problem["visibility"] == "teaching" or problem["tier"] == "mandatory") and not traps and not problem.get("trap_omission_reason"):
            report.error(f"Empty trap metadata for teaching/mandatory LC {number}")
        followups = problem["original_follow_up_variations"]
        if not followups:
            report.error(f"No problem-specific follow-up variation for LC {number}")
        for followup in followups:
            lower = followup.strip().lower()
            if len(lower) < 25 or lower in GENERIC_FOLLOW_UP_MARKERS or any(lower == marker for marker in GENERIC_FOLLOW_UP_MARKERS):
                report.error(f"Generic or empty follow-up placeholder for LC {number}: {followup}")
            exact_followups[lower] += 1
        reviews = problem["review_requirements"]
        if not reviews or any(len(item.strip()) < 20 for item in reviews):
            report.error(f"Missing or shallow review requirements for LC {number}")
        exact_traps[tuple(str(x).strip().lower() for x in traps)] += 1
        exact_reviews[tuple(str(x).strip().lower() for x in reviews)] += 1
        if not isinstance(problem["learning_purpose"], str) or len(problem["learning_purpose"].strip()) < 25:
            report.error(f"Shallow learning purpose for LC {number}")
        if not isinstance(problem["selection_reason"], str) or len(problem["selection_reason"].strip()) < 25:
            report.error(f"Shallow selection reason for LC {number}")
    repeated_followups = {text: count for text, count in exact_followups.items() if count > 2}
    repeated_traps = {text: count for text, count in exact_traps.items() if text and count > 3}
    repeated_reviews = {text: count for text, count in exact_reviews.items() if text and count > 3}
    if repeated_followups:
        report.error(f"Excessive repeated follow-up boilerplate: {list(repeated_followups.values())[:5]}")
    if repeated_traps:
        report.error(f"Excessive repeated trap boilerplate: {list(repeated_traps.values())[:5]}")
    if repeated_reviews:
        report.error(f"Excessive repeated review boilerplate: {list(repeated_reviews.values())[:5]}")
    if len(items) != EXPECTED_PROBLEM_COUNT or len(by_number) != EXPECTED_PROBLEM_COUNT:
        report.error(f"Expected {EXPECTED_PROBLEM_COUNT} unique problems, found {len(items)} rows/{len(by_number)} unique")

    confirmed_unique = set(confirmed_numbers)
    if len(confirmed_unique) != len(confirmed_numbers):
        report.error("Online verification official_pages_confirmed must contain unique problem numbers")
    unknown_confirmed = sorted(confirmed_unique - set(by_number))
    if unknown_confirmed:
        report.error(f"Online verification confirms problem numbers absent from the bank: {unknown_confirmed}")
    expected_confirmed = len(confirmed_unique)
    expected_remaining = len(by_number) - expected_confirmed
    confirmed_count = online.get("confirmed_count")
    remaining_count = online.get("remaining_count")
    verification_status = online.get("status")
    if confirmed_count != expected_confirmed:
        report.error(
            f"Online verification confirmed_count mismatch: declared {confirmed_count}, "
            f"expected {expected_confirmed}"
        )
    if remaining_count != expected_remaining:
        report.error(
            f"Online verification remaining_count mismatch: declared {remaining_count}, "
            f"expected {expected_remaining}"
        )
    if not isinstance(confirmed_count, int) or not isinstance(remaining_count, int):
        report.error("Online verification confirmed_count and remaining_count must be integers")
    elif confirmed_count + remaining_count != len(by_number):
        report.error(
            f"Online verification counts do not sum to total problems: "
            f"{confirmed_count} + {remaining_count} != {len(by_number)}"
        )
    expected_status = (
        "complete" if expected_remaining == 0 and expected_confirmed == len(by_number)
        else "partial" if expected_confirmed > 0
        else "not_started"
    )
    if verification_status not in ONLINE_VERIFICATION_STATUSES:
        report.error(f"Invalid online-verification status: {verification_status}")
    elif verification_status != expected_status:
        report.error(
            f"Online-verification status mismatch: declared {verification_status}, "
            f"expected {expected_status}"
        )
    report.statistics["official_problem_pages_sampled"] = expected_confirmed
    report.statistics["official_problem_pages_confirmed"] = expected_confirmed
    report.statistics["official_problem_pages_remaining"] = expected_remaining
    report.statistics["online_verification_status"] = verification_status

    coverage = payload.get("practice_coverage")
    expected_coverage = {
        uid for uid, unit in units.items()
        if unit.priority in {"C", "P"} and unit.unit_id.split("-")[1] not in {"FND", "PY"}
    }
    seen_coverage: set[str] = set()
    if not isinstance(coverage, list):
        report.error("practice_coverage must be a list")
        coverage = []
    for entry in coverage:
        if not isinstance(entry, dict):
            report.error("Malformed practice_coverage entry")
            continue
        uid = entry.get("unit_id")
        if uid in seen_coverage:
            report.error(f"Duplicate practice_coverage unit: {uid}")
        seen_coverage.add(uid)
        if uid not in expected_coverage:
            report.error(f"Unexpected or unknown practice_coverage unit: {uid}")
            continue
        refs = entry.get("problem_numbers")
        if not isinstance(refs, list) or any(not isinstance(n, int) for n in refs):
            report.error(f"Malformed problem_numbers in practice coverage for {uid}")
            continue
        if refs:
            for number in refs:
                problem = by_number.get(number)
                if not problem:
                    report.error(f"Unknown practice problem LC {number} for {uid}")
                elif problem["owner_unit"] != uid and uid not in problem.get("secondary_units", []):
                    report.error(f"LC {number} does not canonically or secondarily cover {uid}")
        else:
            if not isinstance(entry.get("micro_lab"), str) or len(entry["micro_lab"].strip()) < 30:
                report.error(f"Missing runnable micro-lab for uncovered unit {uid}")
            if not isinstance(entry.get("reason"), str) or len(entry["reason"].strip()) < 25:
                report.error(f"Missing micro-lab reason for uncovered unit {uid}")
    if seen_coverage != expected_coverage:
        report.error(f"Practice coverage parity mismatch: missing {sorted(expected_coverage - seen_coverage)}")

    easy_medium_reserve = [p for p in by_number.values() if p["reserve_pool"] == "unlabeled_easy_medium"]
    hard_pool = [p for p in by_number.values() if p["reserve_pool"] == "hard_stretch_mock"]
    if not 24 <= len(easy_medium_reserve) <= 40:
        report.error(f"Easy/Medium unlabeled reserve must contain 24–40 problems, found {len(easy_medium_reserve)}")
    if len(easy_medium_reserve) < 30:
        report.error("Easy/Medium reserve cannot provide three non-overlapping ten-problem readiness sets")
    if any(p["difficulty"] not in {"Easy", "Medium"} or p["visibility"] != "mixed" for p in easy_medium_reserve):
        report.error("Easy/Medium reserve contains an invalid difficulty or visible label")
    if any(p["difficulty"] != "Hard" for p in hard_pool):
        report.error("Hard stretch/mock pool contains a non-Hard problem")
    reserve_domains = Counter(str(p["owner_unit"]).split("-")[1] for p in easy_medium_reserve)
    if len(reserve_domains) < 8:
        report.error(f"Easy/Medium reserve lacks major-family balance: {dict(reserve_domains)}")
    if reserve_domains and max(reserve_domains.values()) > len(easy_medium_reserve) * 0.4:
        report.error(f"Easy/Medium reserve is excessively concentrated: {dict(reserve_domains)}")

    report.statistics.update({
        "unique_problem_references": len(by_number),
        "problem_tiers": dict(Counter(str(p["tier"]) for p in by_number.values())),
        "problem_difficulties": dict(Counter(str(p["difficulty"]) for p in by_number.values())),
        "problem_access": dict(Counter(str(p["access"]) for p in by_number.values())),
        "problem_visibility": dict(Counter(str(p["visibility"]) for p in by_number.values())),
        "problem_reserve_pools": dict(Counter(str(p["reserve_pool"]) for p in by_number.values())),
        "practice_coverage_rows": len(coverage),
        "practice_micro_labs": sum(not entry.get("problem_numbers") for entry in coverage if isinstance(entry, dict)),
        "renewable_easy_medium_reserve": len(easy_medium_reserve),
        "hard_stretch_mock_pool": len(hard_pool),
        "renewable_ten_problem_sets_before_recycling": len(easy_medium_reserve) // 10,
    })
    report.mark("problem_metadata", not any("LC " in e or "problem" in e.lower() or "reserve" in e.lower() or "practice coverage" in e.lower() for e in report.errors))
    return payload, by_number

def validate_problem_bank(report: Report, problems: dict[int, dict[str, object]]) -> None:
    text = (report.root / "PROBLEM_BANK.md").read_text(encoding="utf-8")
    anchors = re.findall(r'<a id="lc-(\d{4})"></a>', text)
    if len(anchors) != len(problems) or len(set(anchors)) != len(problems):
        report.error("Problem-bank anchor count/parity mismatch")
    linked = re.findall(r'<a id="lc-(\d{4})"></a>\[(\d+) — ([^\]]+)\]\((https://leetcode\.com/problems/[a-z0-9-]+/)\)', text)
    if len(linked) != len(problems):
        report.error(f"Problem-bank linked row count mismatch: {len(linked)} vs {len(problems)}")
    for anchor_num, num_text, title, url in linked:
        number = int(num_text)
        problem = problems.get(number)
        if not problem:
            report.error(f"PROBLEM_BANK contains unknown LC {number}")
            continue
        if anchor_num != f"{number:04d}" or title != problem["title"] or url != problem["url"]:
            report.error(f"Problem-bank parity mismatch for LC {number}")
    reserve = text.split("## Renewable Easy/Medium unlabeled reserve", 1)[-1].split("## Separate Hard stretch and mock pool", 1)[0]
    hard = text.split("## Separate Hard stretch and mock pool", 1)[-1].split("## Practice-coverage audit", 1)[0]
    for section_name, section in (("Easy/Medium reserve", reserve), ("Hard pool", hard)):
        if "Canonical owner" in section or "Primary learning purpose" in section or "Primary pattern" in section:
            report.error(f"{section_name} exposes hidden pattern ownership")
    expected = {
        "Unique problems": len(problems),
        "Mandatory core": sum(p["tier"] == "mandatory" for p in problems.values()),
        "Optional expansion and reserve": sum(p["tier"] == "optional" for p in problems.values()),
        "Hard stretch/mock": sum(p["tier"] == "stretch" for p in problems.values()),
        "Free": sum(p["access"] == "free" for p in problems.values()),
        "Premium": sum(p["access"] == "premium" for p in problems.values()),
        "Easy": sum(p["difficulty"] == "Easy" for p in problems.values()),
        "Medium": sum(p["difficulty"] == "Medium" for p in problems.values()),
        "Hard": sum(p["difficulty"] == "Hard" for p in problems.values()),
        "Renewable unlabeled Easy/Medium reserve": sum(p["reserve_pool"] == "unlabeled_easy_medium" for p in problems.values()),
        "Separate Hard stretch/mock pool": sum(p["reserve_pool"] == "hard_stretch_mock" for p in problems.values()),
    }
    for label, count in expected.items():
        if f"| {label} | {count} |" not in text:
            report.error(f"PROBLEM_BANK count mismatch for {label}")
    report.mark("problem_bank_parity", not any("Problem-bank" in e or "PROBLEM_BANK" in e or "exposes hidden" in e for e in report.errors))

def validate_progress(report: Report, units: dict[str, Unit]) -> dict[str, ProgressEntry]:
    text = (report.root / "PROGRESS.md").read_text(encoding="utf-8")
    rows = re.findall(
        r'^\| \[(DSA-[A-Z]{2,3}-\d{3})\]\(CURRICULUM\.md#(dsa-[a-z]{2,3}-\d{3})\) '
        r'\| (.*?) \| (Core|Professional|Advanced|Reference) \| (Absent|Draft|Approved) '
        r'\| (Not started|Learning|Practiced|Recalled|Demonstrated|Retained) \|',
        text,
        re.MULTILINE,
    )
    if len(rows) != len(units):
        report.error(f"Progress unit-row count mismatch: {len(rows)} vs {len(units)}")
    map_priority = {"C": "Core", "P": "Professional", "A": "Advanced", "R": "Reference"}
    entries: dict[str, ProgressEntry] = {}
    for uid, anchor, title, priority, artifact, learning in rows:
        unit = units.get(uid)
        if not unit or title != unit.title or priority != map_priority[unit.priority] or anchor != unit.anchor:
            report.error(f"Progress parity mismatch for {uid}")
        if artifact not in ALLOWED_ARTIFACT_STATES or learning not in ALLOWED_LEARNING_STATES:
            report.error(f"Invalid progress state for {uid}")
        entries[uid] = ProgressEntry(uid, title, priority, artifact, learning)
    if set(entries) != set(units):
        report.error("Curriculum/progress ID parity mismatch")
    report.mark("progress_parity", not any("Progress" in error or "progress" in error for error in report.errors))
    return entries

def parse_projects(report: Report, units: dict[str, Unit]) -> dict[str, str]:
    text = (report.root / "PROJECTS.md").read_text(encoding="utf-8")
    headings = re.findall(r'<a id="(dsa-prj-\d{3})"></a>\n## `?(DSA-PRJ-\d{3})`? — (.+)', text)
    projects = {pid: title for anchor, pid, title in headings if anchor == pid.lower()}
    if len(projects) != EXPECTED_PROJECT_COUNT or sorted(projects) != EXPECTED_PROJECT_IDS:
        report.error(f"Project IDs/anchors mismatch: {sorted(projects)}")
    overview = re.findall(r'\| \[(DSA-PRJ-\d{3}) — ([^\]]+)\]\(#(dsa-prj-\d{3})\) \|', text)
    if len(overview) != EXPECTED_PROJECT_COUNT:
        report.error("Project overview link count mismatch")
    for pid, title, anchor in overview:
        if projects.get(pid) != title or anchor != pid.lower():
            report.error(f"Project overview parity mismatch for {pid}")
    for uid in [x for x in UNIT_ID_RE.findall(text) if not x.startswith("DSA-PRJ-")]:
        if uid not in units:
            report.error(f"Unknown unit reference in PROJECTS.md: {uid}")
    progress = (report.root / "PROGRESS.md").read_text(encoding="utf-8")
    tracker = re.findall(r'^\| \[(DSA-PRJ-\d{3})\]\(PROJECTS\.md#(dsa-prj-\d{3})\) \| (.*?) \| (Planned|Active|Complete) \| `project/(DSA-PRJ-\d{3})` \|', progress, re.MULTILINE)
    if len(tracker) != EXPECTED_PROJECT_COUNT:
        report.error("Project tracker row count mismatch")
    for pid, anchor, title, state, branch_pid in tracker:
        if projects.get(pid) != title or anchor != pid.lower() or branch_pid != pid or state not in ALLOWED_PROJECT_STATES:
            report.error(f"Project tracker parity mismatch for {pid}")
    sections = re.split(r'(?=<a id="dsa-prj-\d{3}"></a>)', text)
    detail_sections = [section for section in sections if section.startswith('<a id="dsa-prj-')]
    required_heads = ["Staged change pressure", "Core invariants", "Seeded defects", "Adversarial tests and oracle", "Required visual traces", "Refactoring checkpoint", "Rejected alternatives", "Complexity analysis", "Senior interview walkthrough", "Definition of done"]
    normalized_blocks: dict[str, list[str]] = defaultdict(list)
    token_sets: list[tuple[str, set[str]]] = []
    for section in detail_sections:
        pid_match = PROJECT_ID_RE.search(section)
        if not pid_match:
            continue
        pid = pid_match.group(0)
        for head in required_heads:
            match = re.search(rf'^### {re.escape(head)}\n\n(.*?)(?=^### |\Z)', section, re.MULTILINE | re.DOTALL)
            if not match or len(match.group(1).strip()) < 40:
                report.error(f"Project {pid} has missing or shallow section: {head}")
                continue
            normalized = re.sub(r'\s+', ' ', re.sub(r'[`*_#\-\[\]()]', ' ', match.group(1).lower())).strip()
            normalized_blocks[head].append(normalized)
        tokens = set(re.findall(r'[a-z]{4,}', section.lower()))
        token_sets.append((pid, tokens))
    for head, blocks in normalized_blocks.items():
        if len(blocks) != len(set(blocks)):
            report.error(f"Identical project boilerplate detected in section: {head}")
    high_similarity: list[str] = []
    for i, (pid_a, tokens_a) in enumerate(token_sets):
        for pid_b, tokens_b in token_sets[i + 1:]:
            union = tokens_a | tokens_b
            score = len(tokens_a & tokens_b) / len(union) if union else 1.0
            if score > 0.72:
                high_similarity.append(f"{pid_a}/{pid_b}:{score:.2f}")
    if high_similarity:
        report.error(f"Projects are excessively similar: {high_similarity}")
    report.statistics["projects"] = len(projects)
    report.statistics["project_pair_similarity_threshold"] = 0.72
    report.mark("projects", not any("Project" in e or "project" in e for e in report.errors))
    return projects

def validate_learning_paths(report: Report, units: dict[str, Unit], problems: dict[int, dict[str, object]], projects: dict[str, str]) -> None:
    text = (report.root / "LEARNING_PATHS.md").read_text(encoding="utf-8")
    selector = text.split("## Choose a path", 1)[-1].split("## Two study-depth contracts", 1)[0]
    for anchor, _title in EXPECTED_PATHS:
        if f"](#{anchor})" not in selector:
            report.error(f"Missing path selector link: {anchor}")
    if "complete first attempt at a selected leetcode problem is not included in unit time" not in text.lower():
        report.error("Rapid-pass contract does not explicitly prevent double-counting selected problem attempts")
    comments = list(re.finditer(r'<!-- PATH_META (\{.*?\}) -->', text))
    if len(comments) != EXPECTED_PATH_COUNT:
        report.error(f"Expected {EXPECTED_PATH_COUNT} PATH_META records, found {len(comments)}")
    seen: list[tuple[object, object]] = []
    total_units = total_problems = total_projects = 0
    for i, match in enumerate(comments):
        try:
            meta = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            report.error(f"Invalid PATH_META JSON: {exc}")
            continue
        path_id, title = meta.get("id"), meta.get("title")
        seen.append((path_id, title))
        start = match.start()
        end = comments[i + 1].start() if i + 1 < len(comments) else len(text)
        section = text[start:end]
        if f'<a id="{path_id}"></a>' not in text[max(0, start - 300):start]:
            report.error(f"Missing stable anchor before path {path_id}")
        unit_links = re.findall(r'\[(DSA-[A-Z]{2,3}-\d{3}) — ([^\]]+)\]\(CURRICULUM\.md#(dsa-[a-z]{2,3}-\d{3})\)', section)
        problem_links = re.findall(r'\[LC (\d+) — ([^\]]+)\]\(PROBLEM_BANK\.md#lc-(\d{4})\)', section)
        project_links = re.findall(r'\[(DSA-PRJ-\d{3}) — ([^\]]+)\]\(PROJECTS\.md#(dsa-prj-\d{3})\)', section)
        total_units += len(unit_links); total_problems += len(problem_links); total_projects += len(project_links)
        unit_ids = [item[0] for item in unit_links]
        problem_numbers = [int(item[0]) for item in problem_links]
        project_ids = [item[0] for item in project_links]
        if len(unit_ids) != len(set(unit_ids)):
            report.error(f"Duplicate unit link in path {path_id}")
        if len(problem_numbers) != len(set(problem_numbers)):
            report.error(f"Duplicate problem link in path {path_id}")
        if meta.get("unit_count") != len(unit_ids) or meta.get("problem_count") != len(problem_numbers) or meta.get("project_count") != len(project_ids):
            report.error(f"Declared counts do not match links for path {path_id}")
        for uid, linked_title, anchor in unit_links:
            unit = units.get(uid)
            if not unit or unit.title != linked_title or unit.anchor != anchor:
                report.error(f"Unit link/title/anchor mismatch in path {path_id}: {uid}")
        for number_text, linked_title, anchor_number in problem_links:
            number = int(number_text)
            problem = problems.get(number)
            if not problem or problem["title"] != linked_title or anchor_number != f"{number:04d}":
                report.error(f"Problem link/title mismatch in path {path_id}: LC {number}")
        for project_id, linked_title, anchor in project_links:
            if projects.get(project_id) != linked_title or anchor != project_id.lower():
                report.error(f"Project link mismatch in path {path_id}: {project_id}")
        assumed = set(meta.get("assumed_or_bridge_prerequisites", []))
        positions = {uid: position for position, uid in enumerate(unit_ids)}
        for assumed_uid in assumed:
            if assumed_uid not in units:
                report.error(f"Unknown assumed prerequisite {assumed_uid} in path {path_id}")
        for uid in unit_ids:
            for prerequisite in units[uid].prerequisites:
                if prerequisite in positions and positions[prerequisite] >= positions[uid]:
                    report.error(f"Path prerequisite order violation in {path_id}: {prerequisite} -> {uid}")
                elif prerequisite not in positions and prerequisite not in assumed:
                    report.error(f"Path {path_id} omits prerequisite {prerequisite} without bridge/assumption")
        # Every selected problem must be owned and prerequisite-covered before its scheduled attempt.
        for number in problem_numbers:
            problem = problems[number]
            required_units = [problem["owner_unit"], *problem["prerequisites"]]
            for required_uid in required_units:
                if required_uid not in positions and required_uid not in assumed:
                    report.error(f"Path {path_id} selects LC {number} without owner/prerequisite {required_uid}")
        concept = [0, 0]; full = [0, 0]
        for uid in unit_ids:
            rapid = RAPID_MINUTES[units[uid].size]
            concept[0] += rapid[0]; concept[1] += rapid[1]
            full[0] += units[uid].first_hours[0] + units[uid].practice_hours[0]
            full[1] += units[uid].first_hours[1] + units[uid].practice_hours[1]
        problem_minutes = sum(int(problems[number]["first_attempt_minutes"]) for number in problem_numbers)
        activities = meta.get("activities", {})
        if not isinstance(activities, dict) or not activities:
            report.error(f"Path {path_id} has no explicit activity breakdown")
            activities = {}
        activity_min = activity_max = 0
        for label, value in activities.items():
            if not (isinstance(value, list) and len(value) == 2 and all(isinstance(x, int) and x >= 0 for x in value)):
                report.error(f"Invalid activity timing {label} in path {path_id}")
                continue
            if re.search(r'\b(first attempt|problem attempt|mixed problem|unseen problem)\b', label.lower()):
                report.error(f"Path {path_id} double-counts selected problem attempt time in activity: {label}")
            activity_min += value[0]; activity_max += value[1]
        expected = {
            "concept_minutes": concept,
            "problem_minutes": problem_minutes,
            "activity_minutes": [activity_min, activity_max],
            "rapid_total_minutes": [concept[0] + problem_minutes + activity_min, concept[1] + problem_minutes + activity_max],
            "full_unit_hours": full,
        }
        for key, value in expected.items():
            if meta.get(key) != value:
                report.error(f"Timing mismatch for {path_id} {key}: declared {meta.get(key)}, calculated {value}")
    if seen != EXPECTED_PATHS:
        report.error(f"Path IDs/titles/order mismatch: {seen}")
    report.statistics.update({
        "learning_paths": len(comments),
        "learning_path_topic_links": total_units,
        "learning_path_problem_links": total_problems,
        "learning_path_project_callouts": total_projects,
    })
    report.mark("learning_paths", not any("path" in e.lower() or "PATH_META" in e or "double-counts" in e for e in report.errors))

def validate_python_references(report: Report) -> None:
    text=(report.root/"PYTHON_REFERENCES.md").read_text(encoding="utf-8")
    links=re.findall(r'https://github\.com/rahulyadev/python-mastery/blob/main/CURRICULUM\.md#(py-[a-z]{3}-\d{3})',text)
    ids=set(PYTHON_ID_RE.findall(text)); unknown=ids-APPROVED_PYTHON_IDS
    if unknown: report.error(f"Unapproved or invented Python Mastery IDs: {sorted(unknown)}")
    for anchor in links:
        if anchor.upper() not in APPROVED_PYTHON_IDS: report.error(f"Unknown Python Mastery anchor: {anchor}")
    if not links: report.error("No Python Mastery absolute links found")
    report.statistics["python_mastery_references"]=len(set(links)); report.mark("python_references",not any("Python Mastery" in e for e in report.errors))

def iter_markdown_files(report: Report) -> list[Path]:
    return [path for path in iter_repository_files(report.root, report.profile) if path.suffix == ".md"]

def extract_anchors(text: str) -> set[str]:
    anchors=set(re.findall(r'<a id="([^"]+)"></a>',text))
    for line in text.splitlines():
        if line.startswith("#"):
            heading=re.sub(r"^#+\s*","",line).strip(); heading=re.sub(r"`|\*|\[|\]|\([^)]*\)","",heading)
            slug=re.sub(r"[^a-z0-9\s-]","",heading.lower()); slug=re.sub(r"\s+","-",slug).strip("-")
            if slug: anchors.add(slug)
    return anchors

def validate_markdown(report: Report) -> None:
    markdown=iter_markdown_files(report); table_count=link_count=fence_blocks=0; anchors:dict[Path,set[str]]={}
    for path in markdown: anchors[path.resolve()]=extract_anchors(path.read_text(encoding="utf-8"))
    for path in markdown:
        text=path.read_text(encoding="utf-8"); active:tuple[str,int]|None=None
        for line in text.splitlines():
            m=re.match(r"^\s*(`{3,}|~{3,})",line)
            if not m: continue
            token=m.group(1); char=token[0]
            if active is None: active=(char,len(token)); fence_blocks+=1
            elif active[0]==char and len(token)>=active[1]: active=None
        if active is not None: report.error(f"Unclosed code fence in {path.relative_to(report.root)}")
        lines=text.splitlines(); in_fence=False; fchar=""; flen=0; i=0
        while i<len(lines):
            line=lines[i]; fm=re.match(r"^\s*(`{3,}|~{3,})",line)
            if fm:
                token=fm.group(1)
                if not in_fence: in_fence=True; fchar=token[0]; flen=len(token)
                elif token[0]==fchar and len(token)>=flen: in_fence=False
                i+=1; continue
            if not in_fence and line.strip().startswith("|") and i+1<len(lines):
                header=split_table_row(line); sep=split_table_row(lines[i+1])
                if header and sep and all(re.fullmatch(r":?-{3,}:?",c.replace(" ","")) for c in sep):
                    table_count+=1; cols=len(header)
                    if len(sep)!=cols: report.error(f"Table header/separator mismatch in {path.relative_to(report.root)}:{i+1}")
                    j=i+2
                    while j<len(lines) and lines[j].strip().startswith("|"):
                        cells=split_table_row(lines[j])
                        if len(cells)!=cols: report.error(f"Table column mismatch in {path.relative_to(report.root)}:{j+1}: {len(cells)} vs {cols}")
                        j+=1
                    i=j; continue
            i+=1
        if "templates" in path.parts: continue
        for m in re.finditer(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            target=m.group(1).strip(); link_count+=1
            if target.startswith(("http://","https://","mailto:")): continue
            target=target.split(" ",1)[0]
            if target.startswith("#"):
                if unquote(target[1:]) not in anchors[path.resolve()]: report.error(f"Missing internal anchor {target} in {path.relative_to(report.root)}")
                continue
            file_part,_,anchor=target.partition("#")
            if "{{" in file_part or "<" in file_part: continue
            resolved=(path.parent/unquote(file_part)).resolve()
            try: resolved.relative_to(report.root.resolve())
            except ValueError: report.error(f"Link escapes repository in {path.relative_to(report.root)}: {target}"); continue
            if not resolved.exists(): report.error(f"Missing internal link target in {path.relative_to(report.root)}: {target}")
            elif anchor and resolved.suffix==".md" and unquote(anchor) not in anchors.get(resolved,extract_anchors(resolved.read_text(encoding="utf-8"))): report.error(f"Missing target anchor in {path.relative_to(report.root)}: {target}")
        if "templates" not in path.parts and re.search(r"\{\{[^}]+\}\}",text): report.error(f"Unexpected template placeholder outside templates: {path.relative_to(report.root)}")
    report.statistics.update({"markdown_files":len(markdown),"markdown_tables":table_count,"markdown_links":link_count,"code_fence_blocks":fence_blocks})
    report.mark("markdown",not any("Table" in e or "fence" in e.lower() or "link" in e.lower() or "anchor" in e.lower() for e in report.errors))


def validate_template_relative_links(report: Report) -> None:
    simulations={
        "templates/unit.md":Path("units/arrays/DSA-SEQ-010-linear-scans/README.md"),
        "templates/practice.md":Path("units/arrays/DSA-SEQ-010-linear-scans/practice/README.md"),
        "templates/problem_attempt.md":Path("units/arrays/DSA-SEQ-010-linear-scans/attempts/LC-0001-2026-08-27.md"),
        "templates/review.md":Path("units/arrays/DSA-SEQ-010-linear-scans/REVIEW.md"),
        "templates/experiment.md":Path("units/arrays/DSA-SEQ-010-linear-scans/experiments/EXP-01-trace/README.md"),
        "templates/project.md":Path("projects/DSA-PRJ-010-invariants/README.md"),
    }; checked=0
    for name,simulated in simulations.items():
        text=(report.root/name).read_text(encoding="utf-8")
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(("http://","https://","#")): continue
            file_part=target.partition("#")[0]
            if not file_part or "{{" in file_part: continue
            checked+=1; resolved=(report.root/simulated.parent/file_part).resolve()
            try: rel=resolved.relative_to(report.root.resolve())
            except ValueError: report.error(f"Template link escapes repository: {name} -> {target}"); continue
            if rel.parts and rel.parts[0] not in {"units","projects"} and not resolved.exists(): report.error(f"Broken template-relative link: {name} -> {target}")
    report.statistics["template_relative_links"]=checked; report.mark("template_relative_links",not any("Template link" in e or "template-relative" in e for e in report.errors))


def validate_ids(report: Report) -> None:
    shortened=re.compile(r'(?<!DSA-)(?<!PY-)\b(?:FND|SEQ|ORD|LNK|SQH|REC|TRE|GRA|GRD|DP|BMS|ADV|SYN)-\d{3}\b'); malformed=[]
    for path in iter_repository_files(report.root, report.profile):
        if path.suffix not in {".md",".json",".toml",".py",""}: continue
        try: text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        if shortened.search(text): report.error(f"Shortened DSA ID in {path.relative_to(report.root)}")
        for token in re.findall(r"\bDSA-[A-Za-z]{2,3}-\d+\b",text):
            if token.startswith("DSA-PRJ-"):
                if not PROJECT_ID_RE.fullmatch(token): malformed.append((path,token))
            elif not UNIT_ID_RE.fullmatch(token): malformed.append((path,token))
    for path,token in malformed: report.error(f"Malformed DSA ID {token} in {path.relative_to(report.root)}")
    report.statistics["shortened_ids"]=sum("Shortened DSA ID" in e for e in report.errors); report.mark("id_consistency",not malformed and not any("Shortened DSA ID" in e for e in report.errors))


def validate_toml_and_tools(report: Report, run_external: bool = True) -> None:
    try:
        project_data = tomllib.loads((report.root / "pyproject.toml").read_text(encoding="utf-8"))
        report.mark("pyproject_toml", True)
    except Exception as exc:
        report.error(f"pyproject.toml parsing failed: {exc}")
        report.mark("pyproject_toml", False)
        return
    try:
        lock_data = tomllib.loads((report.root / "uv.lock").read_text(encoding="utf-8"))
        report.mark("uv_lock_toml", True)
    except Exception as exc:
        report.error(f"uv.lock parsing failed: {exc}")
        report.mark("uv_lock_toml", False)
        return
    dev = project_data.get("dependency-groups", {}).get("dev", [])
    names = {re.split(r"[<>=!~\[]", item, maxsplit=1)[0].lower() for item in dev if isinstance(item, str)}
    missing = REQUIRED_DEV_TOOLS - names
    if missing:
        report.error(f"Missing development tools: {sorted(missing)}")
    packages = lock_data.get("package", [])
    report.statistics["development_dependencies"] = sorted(names)
    report.statistics["locked_packages"] = len(packages) if isinstance(packages, list) else 0
    pinned = (report.root / ".python-version").read_text(encoding="utf-8").strip()
    uv = shutil.which("uv")
    uv_results: list[dict[str, object]] = []
    if not run_external:
        report.mark("uv_lock_check_pinned", "skipped")
        report.mark("uv_lock_check_substituted", "skipped")
        return
    if not uv:
        report.mark("uv_lock_check_pinned", "skipped")
        report.mark("uv_lock_check_substituted", "skipped")
        reason = "uv executable unavailable"
        report.skipped_external_checks.append(f"uv lock checks: {reason}")
        uv_results.append({"command": "uv lock --check", "status": "skipped", "reason": reason})
    else:
        listing = subprocess.run([uv, "python", "list"], cwd=report.root, text=True, capture_output=True)
        pinned_installed = any(
            line.startswith(f"cpython-{pinned}-") and "<download available>" not in line
            for line in listing.stdout.splitlines()
        )
        pinned_command = [uv, "lock", "--check", "--python", pinned]
        if pinned_installed:
            proc = subprocess.run(pinned_command, cwd=report.root, text=True, capture_output=True)
            uv_results.append({"command": " ".join(pinned_command), "status": "passed" if proc.returncode == 0 else "failed", "output": (proc.stderr or proc.stdout).strip()})
            report.mark("uv_lock_check_pinned", proc.returncode == 0)
            if proc.returncode != 0:
                report.error(f"Pinned uv lock check failed: {(proc.stderr or proc.stdout).strip()}")
        else:
            reason = f"Pinned CPython {pinned} is not installed; the command was not run to avoid an implicit interpreter download"
            report.mark("uv_lock_check_pinned", "skipped")
            report.skipped_external_checks.append(f"{' '.join(pinned_command)}: {reason}")
            uv_results.append({"command": " ".join(pinned_command), "status": "skipped", "reason": reason})
        substituted_command = [uv, "lock", "--check", "--python", sys.executable]
        proc = subprocess.run(substituted_command, cwd=report.root, text=True, capture_output=True)
        uv_results.append({"command": " ".join(substituted_command), "status": "passed" if proc.returncode == 0 else "failed", "qualification": "substituted available interpreter", "output": (proc.stderr or proc.stdout).strip()})
        report.mark("uv_lock_check_substituted", proc.returncode == 0)
        if proc.returncode != 0:
            report.error(f"Substituted-interpreter uv lock check failed: {(proc.stderr or proc.stdout).strip()}")
    report.statistics["uv_validation"] = uv_results
    report.mark("development_tools", not missing)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.replace("–", "-").replace("—", "-").replace("&", " and "))
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")


def expected_unit_directory(root: Path, unit: Unit) -> Path:
    code = unit.unit_id.split("-")[1]
    return root / "units" / DOMAIN_SLUGS[code] / f"{unit.unit_id}-{slugify(unit.title)}"


def extract_markdown_section(text: str, heading: str) -> str:
    pattern = re.compile(rf'^{re.escape(heading)}\s*$\n(.*?)(?=^##\s|\Z)', re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def parse_python_syntax(report: Report, path: Path, code: str) -> None:
    try:
        ast.parse(code, filename=str(path))
    except SyntaxError as exc:
        report.error(f"[UNIT_PYTHON_SYNTAX_ERROR] {path.relative_to(report.root)}: {exc}")


def validate_unit_pack(report: Report, unit: Unit, entry: ProgressEntry, unit_dir: Path) -> None:
    relative = unit_dir.relative_to(report.root)
    readme = unit_dir / "README.md"
    practice_readme = unit_dir / "practice" / "README.md"
    review = unit_dir / "REVIEW.md"
    if not readme.is_file():
        report.error(f"[UNIT_MISSING_README] {unit.unit_id}: {relative}/README.md")
        return
    readme_text = readme.read_text(encoding="utf-8")
    if not readme_text.startswith(f"# {unit.unit_id} — {unit.title}\n"):
        report.error(f"[UNIT_ID_TITLE_MISMATCH] {unit.unit_id}: README heading must use the exact canonical title")
    if f"| Artifact state | {entry.artifact_state} |" not in readme_text:
        report.error(f"[UNIT_ARTIFACT_STATE_MISMATCH] {unit.unit_id}: README and tracker differ")
    for heading in REQUIRED_UNIT_README_HEADINGS:
        if heading not in readme_text:
            report.error(f"[UNIT_REQUIRED_SECTION_MISSING] {unit.unit_id}: {heading}")
    physical = extract_markdown_section(readme_text, "## Physical Notebook Core")
    if len(physical) < 500 or "```" not in physical:
        report.error(f"[UNIT_PHYSICAL_CORE_SHALLOW] {unit.unit_id}: Physical Notebook Core is not substantive")
    for heading in ("#### How to read this visual", "#### Key insight", "#### Simplification or limitation"):
        if heading not in readme_text:
            report.error(f"[UNIT_VISUAL_CONTRACT_MISSING] {unit.unit_id}: {heading}")
    if re.search(r"\{\{[^}]+\}\}|<UNIT-ID>|<PROJECT-ID>|<TOPIC-ID>", readme_text):
        report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: README contains unresolved template placeholders")
    lowered = readme_text.lower()
    for marker in INITIALIZED_FILLER_MARKERS:
        if marker in lowered:
            report.error(f"[UNIT_TEMPLATE_FILLER] {unit.unit_id}: README retains template instruction {marker!r}")
            break
    interview = extract_markdown_section(readme_text, "## 15. Interview questions, traps, and follow-ups")
    interview_terms = ("invariant", "complexity", "changed-constraint", "trap", "explain")
    if interview.count("?") < 8 or any(term not in interview.lower() for term in interview_terms):
        report.error(f"[UNIT_INTERVIEW_COVERAGE_MISSING] {unit.unit_id}: concrete questions/traps/follow-ups are incomplete")
    explanation = extract_markdown_section(readme_text, "## 16. Explanation exercises")
    if len(re.findall(r'^\d+\.', explanation, re.MULTILINE)) < 3:
        report.error(f"[UNIT_EXPLANATION_EXERCISES_MISSING] {unit.unit_id}: explanation drills are incomplete")

    if not practice_readme.is_file():
        report.error(f"[UNIT_MISSING_PRACTICE] {unit.unit_id}: practice/README.md is required")
    else:
        practice_text = practice_readme.read_text(encoding="utf-8")
        if re.search(r"\{\{[^}]+\}\}|<UNIT-ID>|<PROJECT-ID>|<TOPIC-ID>", practice_text):
            report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: practice contains unresolved placeholders")
        exercises = list(re.finditer(rf'^## {re.escape(unit.unit_id)}-P\d{{2}} — .+$', practice_text, re.MULTILINE))
        if len(exercises) < 2:
            report.error(f"[UNIT_PRACTICE_TASK_SHALLOW] {unit.unit_id}: at least two concrete exercises are required")
        for index, exercise in enumerate(exercises):
            end = exercises[index + 1].start() if index + 1 < len(exercises) else len(practice_text)
            section = practice_text[exercise.end():end]
            task_match = re.search(r'^### Task\s*$\n(.*?)(?=^### |\Z)', section, re.MULTILINE | re.DOTALL)
            task = task_match.group(1).strip() if task_match else ""
            required_parts = ("### Constraints and expected behavior", "### Required edge cases", "### Acceptance criteria", "### Progressive hints")
            if len(task) < 100 or any(part not in section for part in required_parts):
                report.error(f"[UNIT_PRACTICE_TASK_SHALLOW] {unit.unit_id}: {exercise.group(0)} lacks a concrete task contract")
        if any(marker in practice_text.lower() for marker in PREMATURE_SOLUTION_MARKERS):
            report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: practice reveals a complete solution")

    if not review.is_file():
        report.error(f"[UNIT_MISSING_REVIEW] {unit.unit_id}: REVIEW.md is required at initialization")
    else:
        review_text = review.read_text(encoding="utf-8")
        if not review_text.startswith(f"# Review Record — {unit.unit_id} {unit.title}\n"):
            report.error(f"[UNIT_REVIEW_TITLE_MISMATCH] {unit.unit_id}: REVIEW.md title mismatch")
        if re.search(r"\{\{[^}]+\}\}|<UNIT-ID>|<PROJECT-ID>|<TOPIC-ID>", review_text):
            report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: REVIEW.md contains unresolved placeholders")
        for heading in REQUIRED_REVIEW_HEADINGS:
            if heading not in review_text:
                report.error(f"[UNIT_REVIEW_SECTION_MISSING] {unit.unit_id}: {heading}")
        if review_text.count("?") < 12:
            report.error(f"[UNIT_REVIEW_QUESTIONS_SHALLOW] {unit.unit_id}: closed-book and delayed-recall questions are incomplete")

    priority_requires_lab = unit.priority in {"C", "P"}
    practice_dir = unit_dir / "practice"
    lab_candidates = [practice_dir / name for name in ("micro_lab.py", "trace_lab.py", "lab.py")]
    existing_labs = [candidate for candidate in lab_candidates if candidate.is_file()]
    if priority_requires_lab and not existing_labs:
        report.error(f"[UNIT_MISSING_MICRO_LAB] {unit.unit_id}: Core/Professional units require a runnable micro-lab or trace exercise")
    for lab in existing_labs:
        code = lab.read_text(encoding="utf-8")
        parse_python_syntax(report, lab, code)
        if "__main__" not in code:
            report.error(f"[UNIT_MICRO_LAB_NOT_RUNNABLE] {unit.unit_id}: {lab.name} lacks a runnable __main__ entry point")

    if "I" in unit.evidence:
        starter = practice_dir / "starter.py"
        examples = practice_dir / "test_examples.py"
        challenge = practice_dir / "test_challenge.py"
        missing = [path.name for path in (starter, examples, challenge) if not path.is_file()]
        if missing:
            report.error(f"[UNIT_MISSING_STARTER_TESTS] {unit.unit_id}: missing {missing}")
        for python_file in (starter, examples, challenge):
            if python_file.is_file():
                parse_python_syntax(report, python_file, python_file.read_text(encoding="utf-8"))
        if starter.is_file() and "NotImplementedError" not in starter.read_text(encoding="utf-8") and re.search(r'^\s*pass\s*$', starter.read_text(encoding="utf-8"), re.MULTILINE) is None:
            report.error(f"[UNIT_STARTER_NOT_UNSOLVED] {unit.unit_id}: starter.py does not preserve an unsolved boundary")
        if examples.is_file() and "test_" not in examples.read_text(encoding="utf-8"):
            report.error(f"[UNIT_EXAMPLE_TESTS_EMPTY] {unit.unit_id}: test_examples.py lacks passing scaffold tests")
        if challenge.is_file() and "test_" not in challenge.read_text(encoding="utf-8"):
            report.error(f"[UNIT_CHALLENGE_TESTS_EMPTY] {unit.unit_id}: test_challenge.py lacks the learner contract")

    experiment_dirs = sorted((unit_dir / "experiments").glob("*/README.md")) if (unit_dir / "experiments").exists() else []
    experiment_required = "X" in unit.evidence or ("(X)" in unit.evidence and unit.unit_id.startswith("DSA-PY-"))
    if experiment_required and not experiment_dirs:
        report.error(f"[UNIT_MISSING_EXPERIMENT] {unit.unit_id}: the evidence/runtime contract requires an experiment")
    for experiment_readme in experiment_dirs:
        experiment_dir = experiment_readme.parent
        scripts = list(experiment_dir.glob("*.py"))
        if not scripts:
            report.error(f"[UNIT_EXPERIMENT_NOT_RUNNABLE] {unit.unit_id}: {experiment_dir.relative_to(report.root)} has no Python script")
        for script in scripts:
            parse_python_syntax(report, script, script.read_text(encoding="utf-8"))

    for path in iter_repository_files(report.root, report.profile):
        try:
            path.relative_to(unit_dir)
        except ValueError:
            continue
        if "solution" in path.name.lower() or "answer" in path.name.lower():
            report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: premature solution-like file {path.relative_to(report.root)}")
            continue
        if path.suffix in {".md", ".py", ".txt"}:
            file_text = path.read_text(encoding="utf-8")
            if any(marker in file_text.lower() for marker in PREMATURE_SOLUTION_MARKERS):
                report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: leaked solution marker in {path.relative_to(report.root)}")


def parse_project_tracker(root: Path) -> dict[str, tuple[str, str]]:
    text = (root / "PROGRESS.md").read_text(encoding="utf-8")
    rows = re.findall(
        r'^\| \[(DSA-PRJ-\d{3})\]\(PROJECTS\.md#dsa-prj-\d{3}\) \| (.*?) '
        r'\| (Planned|Active|Complete) \| `project/DSA-PRJ-\d{3}` \|',
        text,
        re.MULTILINE,
    )
    return {project_id: (title, state) for project_id, title, state in rows}


def validate_live_content(report: Report, units: dict[str, Unit], progress: dict[str, ProgressEntry], projects: dict[str, str]) -> None:
    installed_units = 0
    units_root = report.root / "units"
    if units_root.exists():
        for candidate in sorted(path for path in units_root.glob("*/*") if path.is_dir()):
            match = re.match(r'^(DSA-[A-Z]{2,3}-\d{3})-', candidate.name)
            if not match or match.group(1) not in units:
                report.error(f"[UNIT_UNKNOWN_DIRECTORY] {candidate.relative_to(report.root)}")
                continue
            unit = units[match.group(1)]
            expected = expected_unit_directory(report.root, unit)
            if candidate.resolve() != expected.resolve():
                report.error(f"[UNIT_CANONICAL_PATH_MISMATCH] {unit.unit_id}: expected {expected.relative_to(report.root)}, found {candidate.relative_to(report.root)}")
            entry = progress[unit.unit_id]
            if entry.artifact_state == "Absent":
                report.error(f"[UNIT_TRACKER_DIRECTORY_MISMATCH] {unit.unit_id}: folder exists while Artifact state is Absent")
            else:
                validate_unit_pack(report, unit, entry, candidate)
                installed_units += 1
    for unit_id, entry in progress.items():
        expected = expected_unit_directory(report.root, units[unit_id])
        if entry.artifact_state in {"Draft", "Approved"} and not expected.is_dir():
            report.error(f"[UNIT_TRACKER_DIRECTORY_MISMATCH] {unit_id}: {entry.artifact_state} tracker row lacks canonical directory")

    installed_projects = 0
    project_tracker = parse_project_tracker(report.root)
    projects_root = report.root / "projects"
    if projects_root.exists():
        for candidate in sorted(path for path in projects_root.iterdir() if path.is_dir()):
            match = re.match(r'^(DSA-PRJ-\d{3})-', candidate.name)
            if not match or match.group(1) not in projects:
                report.error(f"[PROJECT_UNKNOWN_DIRECTORY] {candidate.relative_to(report.root)}")
                continue
            project_id = match.group(1)
            title, state = project_tracker[project_id]
            expected = report.root / "projects" / f"{project_id}-{slugify(title)}"
            if candidate.resolve() != expected.resolve():
                report.error(f"[PROJECT_CANONICAL_PATH_MISMATCH] {project_id}: expected {expected.relative_to(report.root)}")
            if state == "Planned":
                report.error(f"[PROJECT_TRACKER_DIRECTORY_MISMATCH] {project_id}: directory exists while state is Planned")
            readme = candidate / "README.md"
            if not readme.is_file():
                report.error(f"[PROJECT_MISSING_README] {project_id}")
            else:
                project_text = readme.read_text(encoding="utf-8")
                if not project_text.startswith(f"# {project_id} — {title}\n"):
                    report.error(f"[PROJECT_ID_TITLE_MISMATCH] {project_id}")
                if re.search(r"\{\{[^}]+\}\}", project_text):
                    report.error(f"[PROJECT_TEMPLATE_PLACEHOLDER] {project_id}")
            installed_projects += 1
    for project_id, (title, state) in project_tracker.items():
        expected = report.root / "projects" / f"{project_id}-{slugify(title)}"
        if state in {"Active", "Complete"} and not expected.is_dir():
            report.error(f"[PROJECT_TRACKER_DIRECTORY_MISMATCH] {project_id}: {state} row lacks canonical directory")

    report.statistics["installed_units"] = installed_units
    report.statistics["installed_projects"] = installed_projects
    report.mark("live_content", not any(error.startswith("[UNIT_") or error.startswith("[PROJECT_") for error in report.errors))


def validate_workflow_contract(report: Report) -> None:
    agents = (report.root / "AGENTS.md").read_text(encoding="utf-8")
    start = (report.root / "START_HERE.md").read_text(encoding="utf-8")
    workflow = (report.root / "docs/WORKFLOW.md").read_text(encoding="utf-8")
    templates = "\n".join((report.root / name).read_text(encoding="utf-8") for name in (
        "templates/unit.md", "templates/practice.md", "templates/experiment.md", "templates/review.md"
    ))
    combined = "\n".join((agents, start, workflow))
    if "must identify the same synchronized baseline" in combined or "Never require an existing exact topic or project branch to equal `main`." not in agents:
        report.error("[WORKFLOW_EXACT_BRANCH_MAIN_EQUALITY_BLOCK] Exact owning branches must resume independently of later main movement")
    if "If the current branch is another `topic/...` or `project/...`, stop." not in workflow:
        report.error("[WORKFLOW_OCCUPIED_WORKTREE_GUARD_MISSING] A Worktree occupied by another unit/project must stop")
    if "git merge-base --is-ancestor HEAD refs/remotes/origin/main" not in workflow or "git switch -c topic/<UNIT-ID> refs/remotes/origin/main" not in workflow:
        report.error("[WORKFLOW_STALE_MAIN_RECOVERY_MISSING] Clean safely fast-forwardable Worktrees must create new branches at refreshed origin/main")
    if "Preserve all existing notes, examples, attempts, experiments, review evidence, and learner files." not in combined or "If the pack is already complete, make no file change, commit, or push." not in combined:
        report.error("[WORKFLOW_REPAIR_PRESERVATION_MISSING] Repair initialization must preserve learner work and be idempotent")
    if "local-only commit list equals the current-operation commit list exactly" not in workflow:
        report.error("[WORKFLOW_INIT_PUSH_BOUNDARY_MISSING] Initialization push must exclude older local-only commits")
    for required in ("practice/README.md", "REVIEW.md", "micro_lab.py", "test_examples.py", "test_challenge.py"):
        if required not in combined + templates:
            report.error(f"[WORKFLOW_COMPLETE_PACK_CONTRACT_MISSING] Missing initialization artifact contract: {required}")
    if "uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py" not in workflow:
        report.error("[WORKFLOW_CHALLENGE_TEST_SEPARATION_MISSING] Challenge tests must be collected separately from passing scaffold tests")
    required_working_artifacts = (".venv/", "__pycache__/", ".pytest_cache/", ".mypy_cache/", ".ruff_cache/", ".hypothesis/", "htmlcov/", ".coverage")
    if any(token not in workflow for token in required_working_artifacts):
        report.error("[WORKFLOW_WORKING_ARTIFACT_ALLOWLIST_MISSING] Working profiles must document the narrow pruned local-artifact allowlist")
    if "uv run --group dev python scripts/validate_repo.py --self-test" not in workflow:
        report.error("[WORKFLOW_UV_RUN_EXTENDED_CHECK_MISSING] Extended validator checks must run inside the uv project environment")
    if "uv run --group dev python -m pytest -q practice/test_examples.py" not in workflow:
        report.error("[WORKFLOW_UV_RUN_PYTEST_MISSING] Scaffold tests must run through the uv project environment")
    report.mark("workflow_contract", not any(error.startswith("[WORKFLOW_") for error in report.errors))


def decide_initialization_route(
    *,
    current_branch: str,
    exact_branch: str,
    clean: bool,
    local_exists: bool,
    remote_exists: bool,
    local_ahead: int = 0,
    remote_ahead: int = 0,
    branch_owned_elsewhere: bool = False,
    selected_is_ancestor_of_origin_main: bool = True,
) -> RouteDecision:
    if not clean:
        return RouteDecision("blocked", error_code="INIT_DIRTY_WORKTREE", detail="Pre-existing work must be resolved explicitly")
    if branch_owned_elsewhere:
        return RouteDecision("blocked", error_code="INIT_BRANCH_OWNED_ELSEWHERE", detail="Use the original pinned Worktree")
    if current_branch.startswith(("topic/", "project/")) and current_branch != exact_branch:
        return RouteDecision("blocked", error_code="WORKTREE_OCCUPIED_BY_DIFFERENT_BRANCH", detail=current_branch)
    if local_ahead and remote_ahead:
        return RouteDecision("blocked", error_code="INIT_BRANCH_DIVERGED", detail=f"{local_ahead}/{remote_ahead}")
    if current_branch == exact_branch:
        if remote_ahead and not local_ahead:
            return RouteDecision("allowed", action="fast_forward_exact_remote")
        return RouteDecision("allowed", action="resume_exact_branch")
    if local_exists:
        return RouteDecision("allowed", action="attach_exact_local_branch")
    if remote_exists:
        return RouteDecision("allowed", action="track_exact_remote_branch")
    if not selected_is_ancestor_of_origin_main:
        return RouteDecision("blocked", error_code="INIT_NEW_BRANCH_BASELINE_UNSAFE", detail="Selected commit cannot safely fast-forward to origin/main")
    return RouteDecision("allowed", action="create_exact_branch_from_origin_main")


def evaluate_initialization_push(
    local_only_commits: list[str],
    current_operation_commits: list[str],
    *,
    initialized_version_already_remote: bool = False,
) -> RouteDecision:
    if initialized_version_already_remote and not current_operation_commits:
        return RouteDecision("allowed", action="no_push_required")
    if local_only_commits != current_operation_commits:
        return RouteDecision("blocked", error_code="INIT_PUSH_INCLUDES_OLDER_LOCAL_COMMITS", detail="Local-only commits are not exactly the current operation")
    if not current_operation_commits:
        return RouteDecision("allowed", action="no_commit_no_push")
    return RouteDecision("allowed", action="push_current_operation_only")

def validate_online_scope(report: Report) -> None:
    confirmed = int(report.statistics.get("official_problem_pages_confirmed", 0))
    remaining = int(report.statistics.get("official_problem_pages_remaining", 0))
    status = report.statistics.get("online_verification_status")
    if status == "complete" and remaining == 0:
        report.mark("leetcode_full_online_metadata", "passed")
        return
    report.mark("leetcode_full_online_metadata", "skipped")
    report.skipped_external_checks.append(
        "Full current official LeetCode metadata revalidation was not completed in this "
        f"packaging run. The metadata file records {confirmed} unique official pages "
        f"confirmed and {remaining} remaining; offline schema, canonical URL form, "
        "parity, access rules, ownership, and reserve policy were validated for all records."
    )


def validate_repository(root: Path, run_external: bool = True, profile: str = "auto") -> Report:
    resolved_root = root.resolve()
    resolved_profile = resolve_profile(resolved_root, profile)
    report = Report(root=resolved_root, profile=resolved_profile)
    validate_required_files_and_hygiene(report)
    _rows, units = parse_units(report)
    validate_required_coverage(report, units)
    _payload, problems = load_problem_data(report, units)
    validate_problem_bank(report, problems)
    progress = validate_progress(report, units)
    projects = parse_projects(report, units)
    validate_learning_paths(report, units, problems, projects)
    validate_python_references(report)
    validate_workflow_contract(report)
    if resolved_profile == "live":
        validate_live_content(report, units, progress, projects)
    validate_markdown(report)
    validate_template_relative_links(report)
    validate_ids(report)
    validate_toml_and_tools(report, run_external=run_external)
    validate_online_scope(report)
    report.mark("overall_repository", not report.errors)
    return report

def validate_archive(report: Report, archive: Path, run_external: bool = True) -> None:
    archive = archive.resolve()
    if not archive.is_file():
        report.error(f"Archive does not exist: {archive}")
        return
    info: dict[str, object] = {"path": archive.name, "sha256": sha256_file(archive), "size_bytes": archive.stat().st_size}
    try:
        with zipfile.ZipFile(archive) as zf:
            bad = zf.testzip()
            names = zf.namelist()
            info["entry_count"] = len(names)
            info["corrupt_entry"] = bad
            if bad:
                report.error(f"Corrupt ZIP entry: {bad}")
            if any(name.startswith("/") or ".." in PurePosixPath(name).parts for name in names):
                report.error("Archive contains unsafe absolute or parent path")
            for name in names:
                parts = PurePosixPath(name).parts
                if ".git" in parts:
                    report.error(f"[ARCHIVE_FORBIDDEN_GIT_METADATA] Archive contains Git metadata: {name}")
                elif parts and parts[0] in ARCHIVE_FORBIDDEN_ROOTS:
                    report.error(f"[ARCHIVE_FORBIDDEN_GENERATED_PATH] Archive contains forbidden generated path: {name}")
                if is_archive_working_artifact(parts):
                    report.error(f"[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT] Archive contains local development artifact: {name}")
                if any(part in WORKING_FORBIDDEN_COMPONENTS for part in parts) or is_sensitive_env_file(PurePosixPath(name)):
                    report.error(f"[ARCHIVE_FORBIDDEN_PRIVATE_PATH] Archive contains private/sensitive path: {name}")
                if PurePosixPath(name).name in FORBIDDEN_LICENSE_NAMES:
                    report.error(f"Archive contains license file: {name}")
            if not set(REQUIRED_FILES).issubset(set(names)):
                report.error("Archive is missing required files")
            if "README.md" not in names or "CURRICULUM.md" not in names:
                report.error("Archive appears to have a wrapper directory")
            with tempfile.TemporaryDirectory(prefix="dsa-archive-") as temp:
                extracted = Path(temp)
                zf.extractall(extracted)
                extracted_report = validate_repository(extracted, run_external=run_external, profile="archive")
                info["extracted_validation"] = "passed" if not extracted_report.errors else "failed"
                info["extracted_profile"] = extracted_report.profile
                info["extracted_errors"] = extracted_report.errors
                info["extracted_warnings"] = extracted_report.warnings
                if extracted_report.errors:
                    report.errors.extend(f"Extracted archive: {error}" for error in extracted_report.errors)
    except zipfile.BadZipFile as exc:
        report.error(f"Bad ZIP archive: {exc}")
    report.archive = info
    report.mark("archive_integrity", not any("Archive" in error or "ZIP" in error or "archive" in error for error in report.errors))

def verify_validation_report(
    report_path: Path,
    archive_path: Path,
    *,
    verify_self_tests: bool = True,
    allow_renamed_archive: bool = False,
) -> dict[str, object]:
    """Verify that a saved report describes the exact archive and fresh contents."""
    verification_errors: list[str] = []

    def mismatch(code: str, detail: str) -> None:
        verification_errors.append(f"{code}: {detail}")

    report_path = report_path.resolve()
    archive_path = archive_path.resolve()
    self_test_prerequisite = "skipped_by_option"
    if verify_self_tests:
        prerequisite_error = pytest_prerequisite_error("Full validation-report verification")
        if prerequisite_error:
            mismatch("REPORT_EXTENDED_TEST_PREREQUISITE_MISSING", prerequisite_error)
            return {
                "schema_version": 1,
                "status": "failed",
                "report_path": report_path.name,
                "archive": {"path": archive_path.name},
                "filename_verification": "content_identity_only" if allow_renamed_archive else "canonical_filename_and_content",
                "statistics_compared": [],
                "self_tests_compared": False,
                "self_test_prerequisite": "missing",
                "setup_command": "uv sync --group dev",
                "run_command": "uv run --group dev python scripts/validate_repo.py --verify-report <report.json> --archive dsa-mastery-bootstrap.zip",
                "errors": verification_errors,
                "warnings": [],
            }
        self_test_prerequisite = "available"
    if not report_path.is_file():
        mismatch("REPORT_FILE_MISSING", str(report_path))
        return {"schema_version": 1, "status": "failed", "errors": verification_errors}
    if not archive_path.is_file():
        mismatch("REPORT_ARCHIVE_MISSING", str(archive_path))
        return {"schema_version": 1, "status": "failed", "errors": verification_errors}
    try:
        saved = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception as exc:
        mismatch("REPORT_JSON_PARSE_ERROR", str(exc))
        return {"schema_version": 1, "status": "failed", "errors": verification_errors}
    if not isinstance(saved, dict):
        mismatch("REPORT_JSON_TYPE_ERROR", "top-level JSON value must be an object")
        return {"schema_version": 1, "status": "failed", "errors": verification_errors}
    if saved.get("schema_version") != 1:
        mismatch("REPORT_SCHEMA_VERSION_MISMATCH", f"recorded {saved.get('schema_version')!r}, expected 1")
    if saved.get("repository_root") != ".":
        mismatch("REPORT_REPOSITORY_ROOT_MISMATCH", f"recorded {saved.get('repository_root')!r}, expected '.'")
    manual = saved.get("validation_scope", {}).get("manual_inspection") if isinstance(saved.get("validation_scope"), dict) else None
    if not isinstance(manual, dict) or manual.get("status") != "not_performed":
        mismatch("REPORT_MANUAL_SCOPE_MISMATCH", "validation_scope.manual_inspection.status must be 'not_performed'")

    actual_archive: dict[str, object] = {
        "path": archive_path.name,
        "sha256": sha256_file(archive_path),
        "size_bytes": archive_path.stat().st_size,
    }
    fresh_report: Report | None = None
    fresh_self_tests: dict[str, object] | None = None
    archive_errors: list[str] = []
    try:
        with zipfile.ZipFile(archive_path) as zf:
            names = zf.namelist()
            bad = zf.testzip()
            actual_archive["entry_count"] = len(names)
            actual_archive["corrupt_entry"] = bad
            if bad:
                archive_errors.append(f"Corrupt ZIP entry: {bad}")
            if any(name.startswith("/") or ".." in PurePosixPath(name).parts for name in names):
                archive_errors.append("Archive contains unsafe absolute or parent path")
            if not set(REQUIRED_FILES).issubset(set(names)):
                archive_errors.append("Archive is missing required files")
            if any(".git" in PurePosixPath(name).parts for name in names):
                archive_errors.append("Archive contains forbidden Git metadata")
            if any(
                PurePosixPath(name).parts
                and PurePosixPath(name).parts[0] in (ARCHIVE_FORBIDDEN_ROOTS - {".git"})
                for name in names
            ):
                archive_errors.append("Archive contains generated or forbidden root content")
            if any(is_archive_working_artifact(PurePosixPath(name).parts) for name in names):
                archive_errors.append("Archive contains forbidden local development artifact")
            if any(
                any(part in WORKING_FORBIDDEN_COMPONENTS for part in PurePosixPath(name).parts)
                or is_sensitive_env_file(PurePosixPath(name))
                for name in names
            ):
                archive_errors.append("Archive contains private or sensitive content")
            if "README.md" not in names or "CURRICULUM.md" not in names:
                archive_errors.append("Archive appears to have a wrapper directory")
            with tempfile.TemporaryDirectory(prefix="dsa-report-verify-") as temp:
                extracted = Path(temp)
                zf.extractall(extracted)
                fresh_report = validate_repository(extracted, run_external=False, profile="archive")
                if verify_self_tests:
                    fresh_self_tests = run_negative_self_tests(extracted)
    except zipfile.BadZipFile as exc:
        mismatch("REPORT_ARCHIVE_INVALID", str(exc))

    recorded_archive = saved.get("archive")
    if not isinstance(recorded_archive, dict):
        mismatch("REPORT_ARCHIVE_METADATA_MISSING", "archive must be an object")
        recorded_archive = {}
    if not allow_renamed_archive and recorded_archive.get("path") != actual_archive.get("path"):
        mismatch("REPORT_ARCHIVE_FILENAME_MISMATCH", f"recorded {recorded_archive.get('path')!r}, actual {actual_archive.get('path')!r}")
    for field_name, code in (
        ("sha256", "REPORT_ARCHIVE_SHA256_MISMATCH"),
        ("size_bytes", "REPORT_ARCHIVE_SIZE_MISMATCH"),
        ("entry_count", "REPORT_ARCHIVE_ENTRY_COUNT_MISMATCH"),
    ):
        if recorded_archive.get(field_name) != actual_archive.get(field_name):
            mismatch(code, f"recorded {recorded_archive.get(field_name)!r}, actual {actual_archive.get(field_name)!r}")

    if fresh_report is not None:
        expected_status = "passed" if not fresh_report.errors and not archive_errors else "failed"
        if saved.get("status") != expected_status:
            mismatch("REPORT_STATUS_MISMATCH", f"recorded {saved.get('status')!r}, fresh {expected_status!r}")
        if recorded_archive.get("extracted_validation") != expected_status:
            mismatch("REPORT_EXTRACTED_STATUS_MISMATCH", f"recorded {recorded_archive.get('extracted_validation')!r}, fresh {expected_status!r}")
        saved_statistics = saved.get("statistics")
        if not isinstance(saved_statistics, dict):
            mismatch("REPORT_STATISTICS_MISSING", "statistics must be an object")
            saved_statistics = {}
        for key in IMPORTANT_REPORT_STATISTICS:
            if saved_statistics.get(key) != fresh_report.statistics.get(key):
                mismatch("REPORT_STATISTIC_MISMATCH", f"{key}: recorded {saved_statistics.get(key)!r}, fresh {fresh_report.statistics.get(key)!r}")
        if saved.get("errors") != fresh_report.errors:
            mismatch("REPORT_ERRORS_MISMATCH", f"recorded {saved.get('errors')!r}, fresh {fresh_report.errors!r}")
        if saved.get("warnings") != fresh_report.warnings:
            mismatch("REPORT_WARNINGS_MISMATCH", f"recorded {saved.get('warnings')!r}, fresh {fresh_report.warnings!r}")

    if verify_self_tests:
        recorded_self_tests = saved.get("self_tests")
        if not isinstance(recorded_self_tests, dict):
            mismatch("REPORT_SELF_TESTS_MISSING", "self_tests must be present in a final validation report")
        elif fresh_self_tests is not None:
            for key in ("status", "count", "passed"):
                if recorded_self_tests.get(key) != fresh_self_tests.get(key):
                    mismatch("REPORT_SELF_TEST_SUMMARY_MISMATCH", f"{key}: recorded {recorded_self_tests.get(key)!r}, fresh {fresh_self_tests.get(key)!r}")
            recorded_cases = {item.get("name"): item for item in recorded_self_tests.get("cases", []) if isinstance(item, dict) and isinstance(item.get("name"), str)}
            fresh_cases = {item.get("name"): item for item in fresh_self_tests.get("cases", []) if isinstance(item, dict) and isinstance(item.get("name"), str)}
            if set(recorded_cases) != set(fresh_cases):
                mismatch("REPORT_SELF_TEST_CASES_MISMATCH", f"recorded {sorted(recorded_cases)}, fresh {sorted(fresh_cases)}")
            else:
                for name in sorted(fresh_cases):
                    for key in ("status", "expected_error"):
                        if recorded_cases[name].get(key) != fresh_cases[name].get(key):
                            mismatch("REPORT_SELF_TEST_CASE_MISMATCH", f"{name} {key}: recorded {recorded_cases[name].get(key)!r}, fresh {fresh_cases[name].get(key)!r}")
            recorded_fixtures = recorded_self_tests.get("fixtures", {})
            fresh_fixtures = fresh_self_tests.get("fixtures", {})
            for key in ("status", "count", "passed"):
                if recorded_fixtures.get(key) != fresh_fixtures.get(key):
                    mismatch("REPORT_FIXTURE_TEST_SUMMARY_MISMATCH", f"{key}: recorded {recorded_fixtures.get(key)!r}, fresh {fresh_fixtures.get(key)!r}")
    if archive_errors:
        mismatch("REPORT_ARCHIVE_CONTENT_MISMATCH", "; ".join(archive_errors))
    return {
        "schema_version": 1,
        "status": "passed" if not verification_errors else "failed",
        "report_path": report_path.name,
        "archive": actual_archive,
        "filename_verification": "content_identity_only" if allow_renamed_archive else "canonical_filename_and_content",
        "statistics_compared": list(IMPORTANT_REPORT_STATISTICS),
        "self_tests_compared": verify_self_tests,
        "self_test_prerequisite": self_test_prerequisite,
        "errors": verification_errors,
        "warnings": [],
    }

def copy_repo_for_test(root: Path, *, include_generated: bool = False) -> tempfile.TemporaryDirectory[str]:
    temp = tempfile.TemporaryDirectory(prefix="dsa-validator-test-")
    target = Path(temp.name)
    profile = "live" if include_generated else "bootstrap"
    for source_path in iter_repository_files(root, profile):
        relative = source_path.relative_to(root)
        if source_path.name.endswith(".zip") or "validation" in source_path.name or source_path.name.endswith(".before-final-routing"):
            continue
        if not include_generated and relative.parts and relative.parts[0] in {"units", "projects", "solutions", "attempts"}:
            continue
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination)
    if not include_generated:
        # Bootstrap fixtures exclude installed units. Normalize only their copied
        # tracker rows, so live evidence links do not point into omitted folders.
        # The source checkout and include_generated=True copies stay untouched.
        progress = target / "PROGRESS.md"
        if progress.is_file():
            lines = progress.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                cells = split_table_row(line)
                if len(cells) == 9 and re.match(
                    r"\[DSA-[A-Z]{3}-\d{3}\]\(CURRICULUM\.md#", cells[0]
                ):
                    cells[3:] = ["Absent", "Not started", "—", "—", "—", "—"]
                    lines[index] = "| " + " | ".join(cells) + " |"
            progress.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return temp

def update_progress_artifact_state(root: Path, unit_id: str, state: str) -> None:
    path = root / "PROGRESS.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = False
    for index, line in enumerate(lines):
        if line.startswith(f"| [{unit_id}]"):
            parts = line.split(" | ")
            if len(parts) < 6:
                raise RuntimeError(f"Cannot update progress row for {unit_id}")
            parts[3] = state
            lines[index] = " | ".join(parts)
            changed = True
            break
    if not changed:
        raise RuntimeError(f"Progress row not found for {unit_id}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fixture_unit_readme(unit: Unit) -> str:
    return f'''# {unit.unit_id} — {unit.title}

## Physical Notebook Core

### Problem shape or pressure

A single pass must summarize a sequence without rescanning earlier values. The interview pressure is to keep exactly the state needed for the answer while preserving a simple invariant after every element.

### One-sentence mental model

> Process each value once, update a small summary, and make the summary correct for the prefix already consumed.

### Essential visual

```text
t0: []            sum=0  max=none
t1: [3]           sum=3  max=3
t2: [3, -2]       sum=1  max=3
t3: [3, -2, 5]    sum=6  max=5
```

#### How to read this visual

Move left to right. At each time, the prefix grows by one value and the stored summary describes exactly that prefix.

#### Key insight

No earlier element needs to be visited again because the running summary contains the information required by the next update.

#### Simplification or limitation

The trace shows sum and maximum only; a different question may require different state, but the prefix-invariant method is the same.

### Governing invariant or rules

1. Before reading index `i`, the summary is correct for `values[:i]`.
2. The update uses the old valid summary and `values[i]` exactly once.
3. Incrementing `i` strictly reduces the unprocessed suffix, so the loop terminates.

### Minimal pseudocode or Python skeleton

```python
summary = initial_state
for value in values:
    summary = update(summary, value)
return summary
```

### Complexity

- Input variables: `n = len(values)`
- Time: `O(n)` because each element is processed once
- Auxiliary space: `O(1)` for a fixed-size summary
- Output space: `O(1)` for this example
- Recursion stack: none
- Important Python cost: iteration is linear; slicing the prefix on every step would make the trace implementation quadratic

### Recognition cues and anti-cues

- Signal: the answer can be updated from a prefix summary and the next item.
- Constraint signal: `n` is large enough that repeated scans are too slow.
- Anti-signal: the update needs arbitrary historical values not represented in the summary.

### Important comparison

Linear scan versus sorting: scan when relative order is irrelevant and a fixed summary is sufficient; sort only when ordering creates useful structure worth `O(n log n)`.

### Common failure

Initializing a maximum to zero breaks all-negative input. Initialize from the first element or use an explicit empty-input policy.

### Recall prompts

1. State the prefix invariant before processing index `i`.
2. Explain why two nested-looking pointer movements can still total `O(n)`.
3. Give a minimal all-negative case that breaks zero initialization.

| Field | Value |
|---|---|
| Domain | Arrays, strings, and sequence patterns |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#{unit.anchor}) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | {unit.outcome} |
| Hard prerequisites | {', '.join(unit.prerequisites) if unit.prerequisites else 'None'} |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | {unit.difficulty} |
| Depth | {unit.depth} |
| Scope | {', '.join(unit.scopes)} |
| Size | {unit.size} |
| Evidence | {'+'.join(unit.evidence)} |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. identify when one pass and constant summary state are sufficient;
2. state and preserve a prefix invariant;
3. implement, trace, test, and explain a linear aggregation without hidden Python costs.

Required evidence:

- hand-trace a running summary on positive and negative values;
- implement the separate learner challenge without copying the example helper;
- explain correctness, complexity, edge cases, and a changed requirement.

## 3. Intuition and problem shape

A scan is useful when the next answer state can be computed from the current state and the next input. The hard part is not the loop syntax; it is choosing a summary that is sufficient and no larger than needed.

## 4. Brute force and bottleneck

### Simplest correct baseline

```python
def prefix_sums_slow(values: list[int]) -> list[int]:
    return [sum(values[:end]) for end in range(1, len(values) + 1)]
```

### Exact bottleneck

Each prefix is summed again. The total work is `1 + 2 + ... + n`, which is `Theta(n^2)`, and each slice also allocates a new list.

## 5. Derivation and invariant

The repeated information is the sum of the previous prefix. Store it once, add the next value, and append the new result. The invariant is: before iteration `i`, `running` equals `sum(values[:i])`.

## 6. Detailed visual trace

### Running prefix summary

```text
values = [2, -1, 4]

i=0  running=0   next=2   -> running=2
i=1  running=2   next=-1  -> running=1
i=2  running=1   next=4   -> running=5
```

#### How to read this visual

Read each row before and after the arrow. The left side satisfies the invariant for the consumed prefix; the right side establishes it for one more element.

#### Key insight

The previous prefix result is exactly the repeated work, so keeping it removes every rescan.

#### Simplification or limitation

The trace assumes ordinary integer addition. Other aggregations require an associative update and a suitable identity or initialization rule.

## 7. Mechanics and state variables

| State variable | Meaning | Update rule | Why it is sufficient |
|---|---|---|---|
| `i` | next unread index | increment by one | proves progress and identifies the prefix |
| `running` | sum of `values[:i]` | add `values[i]` | contains all history needed by the next sum |
| `result` | completed prefix sums | append `running` | preserves required output in order |

## 8. Correctness reasoning

- **Initialization:** before index zero, the consumed prefix is empty and its sum is zero.
- **Preservation:** adding `values[i]` changes the prefix sum from `sum(values[:i])` to `sum(values[:i + 1])`.
- **Progress and termination:** `i` increases once per element and stops after `n` updates.
- **Completeness:** every input element contributes exactly once to all later prefix states through `running`.
- **Safe exclusion:** individual earlier values need not be revisited because their total contribution is already in `running`.
- **Final-state argument:** after the last update, every requested prefix sum has been appended in order.

## 9. Complexity derivation

Let `n` be the input length. The loop performs one addition and append per element, so time is `Theta(n)`. The running state is `O(1)` auxiliary space; the returned list is `Theta(n)` output space. Python list append is amortized `O(1)`. Creating slices inside the loop would add allocation and quadratic total copying.

## 10. Implementations

### Generic pseudocode

```text
running <- identity
result <- empty sequence
for each value:
    running <- combine(running, value)
    append running to result
return result
```

### Idiomatic Python

```python
def prefix_sums(values: list[int]) -> list[int]:
    running = 0
    result: list[int] = []
    for value in values:
        running += value
        result.append(running)
    return result
```

### Python 3.11 compatibility

The implementation works unchanged on Python 3.11.

### First-principles versus standard-library choice

Writing the loop exposes the invariant. In production, `itertools.accumulate` is a clear alternative when its semantics fit and the interviewer accepts it.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Invariant risk |
|---|---|---|---|
| empty input | `[]` | return an empty result | assuming a first element exists |
| negative values | `[-3, -2]` | `[-3, -5]` | using zero as a maximum sentinel in a related scan |
| singleton | `[7]` | `[7]` | off-by-one loop bounds |
| large input | many values | one pass | accidental slicing or repeated `sum` |

## 12. Comparisons and anti-signals

| Candidate | Use when | Reject when | Evidence in the problem |
|---|---|---|---|
| linear scan | fixed state updates from next item | arbitrary old items are needed | prefix summary is sufficient |
| sorting | relative order enables easier selection | original order matters or `O(n)` is available | no ordering benefit here |
| prefix table | many later range queries need preprocessing | only one aggregate is requested | query count determines value |

## 13. Common bugs and debugging

| Failure | Symptom | Smallest counterexample | Correction |
|---|---|---|---|
| repeated slicing | time limit or high allocation | `[1, 2, 3]` with `sum(values[:i])` | carry the prior summary |
| wrong initial state | incorrect all-negative result | `[-1]` | derive initialization from the invariant |
| skipped final element | last contribution missing | `[5]` | use direct iteration or verify half-open bounds |

## 14. Practice ladder

1. trace a running sum by hand;
2. diagnose a rescan-based implementation;
3. implement a separate longest-streak scan in `starter.py`;
4. vary it to return boundaries rather than length;
5. compare scanning with sorting;
6. solve a mixed unseen single-pass problem later;
7. re-solve after the scheduled delay.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. Which constraint tells you an `O(n^2)` rescan is too slow?
2. What is the simplest brute force, and which exact operation repeats?

### Invariant and correctness questions

1. What must `running` mean before each iteration?
2. Why does updating it once consider every element and safely avoid earlier values?

### Complexity questions

1. Why is the loop `Theta(n)` rather than merely `O(n)`?
2. How would slicing inside the loop change time and allocation complexity?

### Changed-constraint follow-ups

1. How would the state change if the input arrived as a stream?
2. What changes if the method must return start and end indices of the best streak rather than only its length?

### Explanation and communication questions

1. Explain the invariant in one sentence before writing code.

### Common traps and weak-answer repairs

- Trap: saying “one loop means linear” without counting work inside the loop.
- Weak answer: “I will keep a variable” — repair it by defining exactly what the variable means before and after each update.

## 16. Explanation exercises

1. Explain the optimization without saying “prefix sum” until after deriving it.
2. Use `[2, -1, 4]` to defend the invariant step by step.
3. Explain why sorting is wasted work for a plain total.
4. Recalculate complexity when every prefix result must be returned.

## 17. Experiment decision

Decision: Not created — this unit's state transition is fully observable through the runnable deterministic micro-lab; a separate runtime experiment would duplicate that evidence.

## 19. Python Mastery references

Review Python list iteration, append complexity, slicing, and mutation through the exact references in `PYTHON_REFERENCES.md`.

## 20. Authoritative sources

Use the repository's source policy and the Python standard-library documentation for any implementation-specific claims.
'''


def fixture_practice_readme(unit: Unit) -> str:
    return f'''# Practice — {unit.unit_id} {unit.title}

| Field | Value |
|---|---|
| Unit note | [{unit.unit_id}](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#{unit.anchor}) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E / T / I / P / D / R / M |
| Attempt required before solution | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_examples.py` |
| Challenge validation command | `uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py` |
| Status | Not attempted |

## Learning questions

1. Which state is sufficient to summarize a consumed prefix without rescanning it?
2. How can an invariant expose both an off-by-one error and an incorrect initialization?

## Cycle

```text
predict → trace → implement → run → observe → explain → optimize → vary → recall
```

## File and test separation

`micro_lab.py` and `test_examples.py` are complete scaffold evidence. `starter.py` and `test_challenge.py` define an unsolved learner boundary. Challenge tests are collected but are not claimed to pass during initialization.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| `{unit.unit_id}-P01` | Trace / Debug | 2 | Find the first invalid state in a faulty running-summary trace | `micro_lab.py` | Not attempted |
| `{unit.unit_id}-P02` | Implement / Compare | 3 | Implement a longest positive streak scan and defend its state | `starter.py`, `test_challenge.py` | Not attempted |

## {unit.unit_id}-P01 — Diagnose a broken prefix trace

### Task

Run the supplied trace on `[3, -2, 5]`, but first write the expected `running` value before and after every update. Then alter the initial running value to one and identify the first row where the stated prefix invariant becomes false. Explain why the later numerical output cannot repair the earlier correctness failure.

### Constraints and expected behavior

- Input or initial state: the fixed list `[3, -2, 5]` and both initial values zero and one.
- Required observation or output: a table containing index, value, state before, state after, and invariant truth value.
- Performance target: one update per element and constant state beyond the trace output.

### Required edge cases

- Empty input must produce no transition rows and preserve the empty-prefix identity.
- A singleton negative input must update from zero to that negative value without any sentinel assumption.

### Before running

Record the expected state, invariant, first divergence, and the cost of the trace before executing the micro-lab.

### Acceptance criteria

- [ ] The trace is predicted before execution.
- [ ] Every state variable is explained.
- [ ] The invariant is checked at each transition.
- [ ] The smallest failing case is identified.
- [ ] Complexity and Python-specific costs are stated.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## {unit.unit_id}-P02 — Longest strictly positive streak

### Task

Implement `longest_positive_streak(values)` in `starter.py`. Return the length of the longest contiguous run containing only values greater than zero. Derive the constant-size state from a brute-force enumeration of all subarrays, preserve the original attempt, and explain why each non-positive value safely resets the current run.

### Constraints and expected behavior

- Input contract: a finite list of integers, including negative values, zeros, duplicates, and empty input.
- Output contract: one non-negative integer representing the longest strictly positive contiguous streak.
- Performance target: `O(n)` time and `O(1)` auxiliary space.

### Required edge cases

- `[]` and `[0]` must return zero without indexing a missing first item.
- `[1, 2, 0, 3, 4, 5, -1]` must return three and must not combine runs across a reset value.

### Before coding

Record brute force, exact bottleneck, candidate state, rejected alternatives, invariant, complexity, and one adversarial dry-run.

### Acceptance criteria

- [ ] The original attempt is preserved.
- [ ] Passing scaffold/example tests remain green.
- [ ] Challenge tests collect before implementation.
- [ ] The learner implementation satisfies the challenge after a genuine attempt.
- [ ] Correctness, complexity, and edge cases are explained.
- [ ] A variation returning the winning index range is designed.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## Review record

Record the first missing reasoning step, smallest counterexample, hint level, observed commands, remaining weakness, and next review date after Rahul attempts the exercises.
'''


def fixture_review(unit: Unit) -> str:
    return f'''# Review Record — {unit.unit_id} {unit.title}

| Field | Value |
|---|---|
| Unit note | [{unit.unit_id}](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. What problem shape allows a fixed-size running summary?
2. Draw the state changes for `[2, -1, 4]` without reading the note.
3. State the invariant before processing index `i`.
4. Derive the optimized scan from the quadratic prefix-rescan baseline.
5. Why does the update preserve the invariant?
6. What are time, auxiliary, output, and recursion-stack costs?
7. When would sorting be an anti-signal rather than a useful step?
8. How is a linear scan different from a fixed-size sliding window?

## Delayed-recall questions

### 1-day recall

1. Reconstruct the minimal trace and prefix invariant.
2. Which one-element input exposes wrong maximum initialization?

### 3-day recall

1. Explain why each earlier value can be safely ignored after updating the summary.
2. Why can slicing turn a one-loop implementation quadratic?

### 7-day recall

1. Design the state for returning the start and end of the best positive streak.
2. Explain why sorting cannot preserve a contiguous-streak requirement.

### 14-day recall

1. Adapt the scan to streaming input where values cannot be stored.
2. Explain the solution without naming the pattern before the derivation.

### 30-day recall

1. Solve an unseen running-summary problem and state the invariant before coding.
2. Teach the limitation: when is fixed-size state not sufficient?

## Interview retrieval

1. How do the constraints suggest a scan?
2. What is the brute-force baseline and exact bottleneck?
3. Which invariant proves the scan correct?
4. Why is every necessary candidate considered?
5. What are time, auxiliary, output, and stack-space costs?
6. Which Python operation could silently change the bound?
7. What tempting alternative fails on contiguous requirements?
8. What changes when the result must include indices?

## One-question-at-a-time evidence record

### Question 1

What must the running state mean immediately before index `i` is processed?

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Record only after Rahul answers.

**Smallest recovery hint:** Give only when needed.

## Evidence

| Link | Result | What it proves | Remaining limitation |
|---|---|---|---|
| — | Not attempted | No learning evidence yet | Initialization alone does not prove learning |

## Error log update

| Category | Exact failure | Corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Complete the first closed-book review | 1 day after first study |

## State decision

Recommended state: **Not started**

Reason tied to the evidence gate: the complete pack exists, but Rahul has not yet produced learning evidence.
'''


def create_complete_unit_fixture(root: Path, unit: Unit) -> Path:
    update_progress_artifact_state(root, unit.unit_id, "Draft")
    unit_dir = expected_unit_directory(root, unit)
    practice_dir = unit_dir / "practice"
    practice_dir.mkdir(parents=True, exist_ok=True)
    (unit_dir / "README.md").write_text(fixture_unit_readme(unit), encoding="utf-8")
    (unit_dir / "REVIEW.md").write_text(fixture_review(unit), encoding="utf-8")
    (practice_dir / "README.md").write_text(fixture_practice_readme(unit), encoding="utf-8")
    (practice_dir / "micro_lab.py").write_text('''from __future__ import annotations\n\n\ndef running_sum_trace(values: list[int]) -> list[tuple[int, int, int, int]]:\n    running = 0\n    trace: list[tuple[int, int, int, int]] = []\n    for index, value in enumerate(values):\n        before = running\n        running += value\n        trace.append((index, value, before, running))\n    return trace\n\n\nif __name__ == "__main__":\n    for row in running_sum_trace([3, -2, 5]):\n        print(row)\n''', encoding="utf-8")
    (practice_dir / "starter.py").write_text('''from __future__ import annotations\n\n\ndef longest_positive_streak(values: list[int]) -> int:\n    raise NotImplementedError("Derive the invariant and implement after your first attempt")\n''', encoding="utf-8")
    (practice_dir / "test_examples.py").write_text('''from micro_lab import running_sum_trace\n\n\ndef test_running_sum_trace_scaffold() -> None:\n    assert running_sum_trace([3, -2, 5]) == [(0, 3, 0, 3), (1, -2, 3, 1), (2, 5, 1, 6)]\n\n\ndef test_empty_trace_scaffold() -> None:\n    assert running_sum_trace([]) == []\n\n\nif __name__ == "__main__":\n    test_running_sum_trace_scaffold()\n    test_empty_trace_scaffold()\n''', encoding="utf-8")
    (practice_dir / "test_challenge.py").write_text('''from starter import longest_positive_streak\n\n\ndef test_longest_positive_streak_contract() -> None:\n    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1]) == 3\n\n\ndef test_empty_and_non_positive_contract() -> None:\n    assert longest_positive_streak([]) == 0\n    assert longest_positive_streak([0, -1]) == 0\n''', encoding="utf-8")
    return unit_dir


def repair_fixture_from_source(source: Path, target: Path) -> list[str]:
    actions: list[str] = []
    for source_path in sorted(path for path in source.rglob("*") if path.is_file()):
        relative = source_path.relative_to(source)
        target_path = target / relative
        if target_path.exists():
            continue
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        actions.append(relative.as_posix())
    return actions


def run_fixture_tests(root: Path) -> dict[str, object]:
    cases: list[dict[str, object]] = []
    base_report = Report(root=root.resolve(), profile="bootstrap")
    _rows, units = parse_units(base_report)
    unit = units["DSA-SEQ-010"]

    def record(name: str, expected: str, observed: str, detail: object | None = None) -> None:
        cases.append({"name": name, "status": "passed" if expected == observed else "failed", "expected_result": expected, "observed_result": observed, "detail": detail})

    live_source_temp = copy_repo_for_test(root)
    try:
        live_source = Path(live_source_temp.name)
        live_unit = create_complete_unit_fixture(live_source, unit)
        progress = live_source / "PROGRESS.md"
        lines = progress.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if line.startswith(f"| [{unit.unit_id}]"):
                cells = split_table_row(line)
                cells[4:8] = ["Practiced", "2026-08-30", "2026-08-31", "synthetic recall gap"]
                cells[8] = f"[Synthetic evidence]({live_unit.relative_to(live_source).as_posix()}/README.md)"
                lines[index] = "| " + " | ".join(cells) + " |"
        progress.write_text("\n".join(lines) + "\n", encoding="utf-8")
        source_hashes = {
            path.relative_to(live_source).as_posix(): sha256_file(path)
            for path in iter_repository_files(live_source, "live")
        }
        with copy_repo_for_test(live_source) as bootstrap_name, copy_repo_for_test(
            live_source, include_generated=True
        ) as preserved_name:
            bootstrap_root, preserved_root = Path(bootstrap_name), Path(preserved_name)
            bootstrap_report = validate_repository(bootstrap_root, run_external=False, profile="bootstrap")
            preserved_report = validate_repository(preserved_root, run_external=False, profile="live")
            preserved_hashes = {
                path.relative_to(preserved_root).as_posix(): sha256_file(path)
                for path in iter_repository_files(preserved_root, "live")
            }
            source_unchanged = all(
                sha256_file(live_source / relative) == digest
                for relative, digest in source_hashes.items()
            )
            generated_omitted = not (bootstrap_root / "units").exists()
            live_copy_preserved = preserved_hashes == source_hashes
            passed = (
                not bootstrap_report.errors and not preserved_report.errors
                and generated_omitted and source_unchanged and live_copy_preserved
            )
            record(
                "bootstrap_fixture_from_live_tracker_preserves_source",
                "passed", "passed" if passed else "failed",
                {
                    "bootstrap_errors": bootstrap_report.errors,
                    "preserved_live_errors": preserved_report.errors,
                    "generated_units_omitted": generated_omitted,
                    "source_files_unchanged": source_unchanged,
                    "live_copy_byte_preserved": live_copy_preserved,
                },
            )
    finally:
        live_source_temp.cleanup()

    fresh_temp = copy_repo_for_test(root)
    try:
        fresh_root = Path(fresh_temp.name)
        fresh_report = validate_repository(fresh_root, run_external=False, profile="bootstrap")
        record(
            "fresh_bootstrap_without_git_metadata",
            "passed",
            "passed" if not fresh_report.errors else "failed",
            {"errors": fresh_report.errors, "statistics": fresh_report.statistics},
        )
    finally:
        fresh_temp.cleanup()

    git_dir_temp = copy_repo_for_test(root)
    baseline_temp = copy_repo_for_test(root)
    try:
        git_dir_root = Path(git_dir_temp.name)
        baseline_root = Path(baseline_temp.name)
        baseline_report = validate_repository(baseline_root, run_external=False, profile="bootstrap")
        git_dir = git_dir_root / ".git"
        git_dir.mkdir()
        (git_dir / "HEAD").write_text("ref: refs/heads/setup/dsa-mastery-bootstrap\n", encoding="utf-8")
        (git_dir / "internal.md").write_text(
            "# Internal Git metadata\n\n[broken](missing.md)\n\n{{SHOULD_NOT_BE_SCANNED}}\n",
            encoding="utf-8",
        )
        (git_dir / "private.key").write_text("not-repository-content\n", encoding="utf-8")
        git_report = validate_repository(git_dir_root, run_external=False, profile="bootstrap")
        stats_unchanged = git_report.statistics == baseline_report.statistics
        observed = "passed" if not git_report.errors and stats_unchanged else "failed"
        record(
            "working_bootstrap_normal_git_directory_ignored",
            "passed",
            observed,
            {
                "errors": git_report.errors,
                "statistics_unchanged": stats_unchanged,
                "baseline_statistics": baseline_report.statistics,
                "git_statistics": git_report.statistics,
            },
        )
    finally:
        git_dir_temp.cleanup()
        baseline_temp.cleanup()

    git_file_temp = copy_repo_for_test(root)
    baseline_file_temp = copy_repo_for_test(root)
    try:
        git_file_root = Path(git_file_temp.name)
        baseline_root = Path(baseline_file_temp.name)
        baseline_report = validate_repository(baseline_root, run_external=False, profile="bootstrap")
        (git_file_root / ".git").write_text(
            "gitdir: /tmp/example/.git/worktrees/dsa-topic\n", encoding="utf-8"
        )
        git_file_report = validate_repository(git_file_root, run_external=False, profile="bootstrap")
        stats_unchanged = git_file_report.statistics == baseline_report.statistics
        observed = "passed" if not git_file_report.errors and stats_unchanged else "failed"
        record(
            "working_bootstrap_linked_worktree_git_file_ignored",
            "passed",
            observed,
            {
                "errors": git_file_report.errors,
                "statistics_unchanged": stats_unchanged,
                "baseline_statistics": baseline_report.statistics,
                "git_statistics": git_file_report.statistics,
            },
        )
    finally:
        git_file_temp.cleanup()
        baseline_file_temp.cleanup()

    complete_temp = copy_repo_for_test(root)
    try:
        complete_root = Path(complete_temp.name)
        # The fixture reuses the active packaging environment. Align only the copied
        # fixture's local version selector so uv does not attempt to provision the
        # repository's pinned 3.14.7 runtime during packaging tests.
        (complete_root / ".python-version").write_text(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n", encoding="utf-8")
        unit_dir = create_complete_unit_fixture(complete_root, unit)
        git_dir = complete_root / ".git"
        git_dir.mkdir()
        (git_dir / "HEAD").write_text("ref: refs/heads/topic/DSA-SEQ-010\n", encoding="utf-8")
        (git_dir / "internal.md").write_text("# ignored Git metadata\n\n[broken](missing.md)\n{{IGNORED}}\n", encoding="utf-8")
        baseline_report = validate_repository(complete_root, run_external=False, profile="live")

        uv = shutil.which("uv")
        environment_target = Path(sys.prefix).resolve()
        selected_python = environment_target / "bin" / "python"
        environment_cfg_exists = (environment_target / "pyvenv.cfg").is_file()
        selected_python_exists = selected_python.is_file()
        selected_python_pytest = subprocess.run(
            [str(selected_python), "-c", "import pytest, sys; print(sys.prefix)"],
            text=True,
            capture_output=True,
        ) if selected_python_exists else None
        selected_python_imports_pytest = bool(selected_python_pytest and selected_python_pytest.returncode == 0)

        command_environment = os.environ.copy()
        command_environment.pop("VIRTUAL_ENV", None)
        command_environment.pop("PYTHONPATH", None)
        command_environment["UV_PYTHON_DOWNLOADS"] = "never"
        command_environment["UV_NO_SYNC"] = "1"
        # Keep only ordinary system PATH entries. Fixture commands call uv by absolute path
        # and pytest through the environment-bound `python -m pytest`.
        command_environment["PATH"] = "/usr/bin:/bin"
        unrelated_pytest_on_path = shutil.which("pytest", path=command_environment["PATH"])
        (complete_root / ".venv").symlink_to(environment_target, target_is_directory=True)

        uv_prefix_probe = None
        if uv is not None:
            uv_prefix_probe = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-c", "from pathlib import Path; import sys; print(Path(sys.prefix).resolve())"],
                cwd=complete_root, env=command_environment, text=True, capture_output=True,
            )
        uv_expected_prefix = bool(
            uv_prefix_probe
            and uv_prefix_probe.returncode == 0
            and uv_prefix_probe.stdout.strip() == str(environment_target)
        )

        if uv is None:
            compile_proc = micro = examples = challenge_collection = None
            challenge_syntax = "skipped"
        else:
            compile_proc = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-m", "compileall", "-q", str(unit_dir.relative_to(complete_root))],
                cwd=complete_root, env=command_environment, text=True, capture_output=True,
            )
            micro = subprocess.run(
                [uv, "run", "--group", "dev", "python", "practice/micro_lab.py"],
                cwd=unit_dir, env=command_environment, text=True, capture_output=True,
            )
            examples = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-m", "pytest", "-q", "practice/test_examples.py"],
                cwd=unit_dir, env=command_environment, text=True, capture_output=True,
            )
            challenge_code = (unit_dir / "practice" / "test_challenge.py").read_text(encoding="utf-8")
            try:
                ast.parse(challenge_code)
                challenge_syntax = "passed"
            except SyntaxError:
                challenge_syntax = "failed"
            challenge_collection = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-m", "pytest", "--collect-only", "-q", "practice/test_challenge.py"],
                cwd=unit_dir, env=command_environment, text=True, capture_output=True,
            )

        ignored_payloads = {
            complete_root / ".pytest_cache" / "v" / "cache" / "nodeids": "[]\n",
            complete_root / ".mypy_cache" / "3.14" / "metadata.json": "{}\n",
            complete_root / ".ruff_cache" / "cache.bin": "local-cache\n",
            complete_root / ".hypothesis" / "examples" / "case": "local-example\n",
            complete_root / "htmlcov" / "index.html": "<html>local coverage</html>\n",
            complete_root / ".coverage": "local coverage database\n",
            complete_root / "coverage.xml": "<coverage/>\n",
            complete_root / "coverage.json": "{}\n",
            complete_root / "lcov.info": "TN:\n",
        }
        for artifact_path, payload in ignored_payloads.items():
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            artifact_path.write_text(payload, encoding="utf-8")

        after_report = validate_repository(complete_root, run_external=False, profile="live")
        statistics_unchanged = after_report.statistics == baseline_report.statistics
        scanned = {path.relative_to(complete_root).as_posix() for path in iter_repository_files(complete_root, "live")}
        ignored_not_scanned = all(
            not any(component in relative.split("/") for component in WORKING_IGNORED_ROOT_DIRECTORIES | WORKING_IGNORED_DIRECTORY_NAMES)
            and not relative.endswith((".pyc", ".pyo"))
            and Path(relative).name not in WORKING_IGNORED_FILE_NAMES
            and not Path(relative).name.startswith(".coverage.")
            for relative in scanned
        )
        venv_exists = (complete_root / ".venv" / "pyvenv.cfg").is_file()
        pycache_exists = any(path.name == "__pycache__" for path in unit_dir.rglob("__pycache__"))
        pytest_cache_exists = any(path.name == ".pytest_cache" for path in complete_root.rglob(".pytest_cache"))
        command_results = [compile_proc, micro, examples, challenge_collection]
        commands_passed = all(proc is not None and proc.returncode == 0 for proc in command_results)
        observed = (
            "passed"
            if not baseline_report.errors
            and not after_report.errors
            and environment_cfg_exists
            and selected_python_imports_pytest
            and unrelated_pytest_on_path is None
            and uv_expected_prefix
            and commands_passed
            and challenge_syntax == "passed"
            and statistics_unchanged
            and ignored_not_scanned
            and venv_exists
            and pycache_exists
            and pytest_cache_exists
            else "failed"
        )
        record(
            "working_checkout_end_to_end_development_artifacts_ignored",
            "passed", observed,
            {
                "errors_before": baseline_report.errors,
                "errors_after": after_report.errors,
                "commands": {
                    "setup": "uv sync --group dev",
                    "compileall": f"uv run --group dev python -m compileall -q {unit_dir.relative_to(complete_root)}",
                    "micro_lab": "uv run --group dev python practice/micro_lab.py",
                    "scaffold_tests": "uv run --group dev python -m pytest -q practice/test_examples.py",
                    "challenge_collection": "uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py",
                },
                "returncodes": {
                    "uv_prefix_probe": None if uv_prefix_probe is None else uv_prefix_probe.returncode,
                    "compileall": None if compile_proc is None else compile_proc.returncode,
                    "micro_lab": None if micro is None else micro.returncode,
                    "scaffold_tests": None if examples is None else examples.returncode,
                    "challenge_collection": None if challenge_collection is None else challenge_collection.returncode,
                },
                "environment_target": str(environment_target),
                "environment_pyvenv_cfg_exists": environment_cfg_exists,
                "selected_python": str(selected_python),
                "selected_python_imports_pytest": selected_python_imports_pytest,
                "uv_run_sys_prefix": "" if uv_prefix_probe is None else uv_prefix_probe.stdout.strip(),
                "uv_run_uses_expected_sys_prefix": uv_expected_prefix,
                "pytest_executable_on_sanitized_path": unrelated_pytest_on_path,
                "challenge_syntax": challenge_syntax,
                "challenge_collection_output": "" if challenge_collection is None else challenge_collection.stdout.strip(),
                "challenge_tests_executed": False,
                "project_venv_exists": venv_exists,
                "pycache_created": pycache_exists,
                "pytest_cache_created": pytest_cache_exists,
                "ignored_artifacts_not_scanned": ignored_not_scanned,
                "statistics_unchanged": statistics_unchanged,
                "baseline_statistics": baseline_report.statistics,
                "post_test_statistics": after_report.statistics,
                "uv_no_sync": True,
            },
        )
    finally:
        complete_temp.cleanup()

    # Prove conventional uv-created symlinked environments must use sys.prefix,
    # not Path(sys.executable).resolve().parent.parent.
    symlink_env_temp = copy_repo_for_test(root)
    try:
        symlink_root = Path(symlink_env_temp.name)
        (symlink_root / ".python-version").write_text(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n", encoding="utf-8")
        uv = shutil.which("uv")
        if uv is None:
            record("uv_symlinked_environment_prefix_detection", "passed", "failed", {"reason": "uv unavailable"})
        else:
            env_dir = symlink_root / ".venv"
            create_env = subprocess.run(
                [uv, "venv", "--python", sys.executable, str(env_dir)],
                cwd=symlink_root, text=True, capture_output=True,
                env={**os.environ, "UV_PYTHON_DOWNLOADS": "never"},
            )
            env_python = env_dir / "bin" / "python"
            prefix_probe = subprocess.run(
                [str(env_python), "-c", "from pathlib import Path; import sys; print(Path(sys.prefix).resolve()); print(Path(sys.executable).resolve())"],
                cwd=symlink_root, text=True, capture_output=True,
            ) if create_env.returncode == 0 else None
            expected_prefix = env_dir.resolve()
            lines = [] if prefix_probe is None else prefix_probe.stdout.strip().splitlines()
            observed_prefix = Path(lines[0]) if len(lines) >= 1 else None
            resolved_executable = Path(lines[1]) if len(lines) >= 2 else None
            legacy_target = None if resolved_executable is None else resolved_executable.parent.parent

            # Make the conventional environment import the already-installed pytest
            # without consulting PATH: a .pth file points at the current environment's
            # site-packages only for this deterministic fixture.
            purelib_probe = subprocess.run(
                [str(env_python), "-c", "import sysconfig; print(sysconfig.get_paths()['purelib'])"],
                cwd=symlink_root, text=True, capture_output=True,
            ) if create_env.returncode == 0 else None
            pytest_spec = importlib.util.find_spec("pytest")
            pytest_locations = [] if pytest_spec is None or pytest_spec.submodule_search_locations is None else list(pytest_spec.submodule_search_locations)
            current_pytest_site = None if not pytest_locations else Path(pytest_locations[0]).resolve().parent
            if purelib_probe is not None and purelib_probe.returncode == 0 and current_pytest_site is not None:
                fixture_purelib = Path(purelib_probe.stdout.strip())
                fixture_purelib.mkdir(parents=True, exist_ok=True)
                (fixture_purelib / "packaging-fixture-pytest.pth").write_text(str(current_pytest_site) + "\n", encoding="utf-8")

            sanitized_env = os.environ.copy()
            sanitized_env.pop("VIRTUAL_ENV", None)
            sanitized_env.pop("PYTHONPATH", None)
            sanitized_env["PATH"] = "/usr/bin:/bin"
            sanitized_env["UV_NO_SYNC"] = "1"
            sanitized_env["UV_PYTHON_DOWNLOADS"] = "never"
            pytest_on_path = shutil.which("pytest", path=sanitized_env["PATH"])
            pytest_import = subprocess.run(
                [str(env_python), "-c", "import pytest; print(pytest.__version__)"],
                cwd=symlink_root, text=True, capture_output=True,
            ) if create_env.returncode == 0 else None
            uv_prefix = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-c", "from pathlib import Path; import sys; print(Path(sys.prefix).resolve())"],
                cwd=symlink_root, env=sanitized_env, text=True, capture_output=True,
            ) if create_env.returncode == 0 else None
            uv_pytest = subprocess.run(
                [uv, "run", "--group", "dev", "python", "-m", "pytest", "--version"],
                cwd=symlink_root, env=sanitized_env, text=True, capture_output=True,
            ) if create_env.returncode == 0 else None
            uv_prefix_ok = bool(uv_prefix and uv_prefix.returncode == 0 and uv_prefix.stdout.strip() == str(expected_prefix))
            legacy_is_wrong = legacy_target is not None and legacy_target.resolve() != expected_prefix
            observed = "passed" if (
                create_env.returncode == 0
                and (env_dir / "pyvenv.cfg").is_file()
                and observed_prefix == expected_prefix
                and legacy_is_wrong
                and pytest_import is not None and pytest_import.returncode == 0
                and pytest_on_path is None
                and uv_prefix_ok
                and uv_pytest is not None and uv_pytest.returncode == 0
            ) else "failed"
            record(
                "uv_symlinked_environment_prefix_detection", "passed", observed,
                {
                    "create_env_returncode": create_env.returncode,
                    "expected_sys_prefix": str(expected_prefix),
                    "observed_sys_prefix": None if observed_prefix is None else str(observed_prefix),
                    "resolved_sys_executable": None if resolved_executable is None else str(resolved_executable),
                    "legacy_resolved_executable_target": None if legacy_target is None else str(legacy_target),
                    "legacy_target_detected_wrong": legacy_is_wrong,
                    "pyvenv_cfg_exists": (env_dir / "pyvenv.cfg").is_file(),
                    "selected_python_imports_pytest": bool(pytest_import and pytest_import.returncode == 0),
                    "pytest_executable_on_sanitized_path": pytest_on_path,
                    "uv_run_sys_prefix": "" if uv_prefix is None else uv_prefix.stdout.strip(),
                    "uv_run_uses_expected_sys_prefix": uv_prefix_ok,
                    "uv_python_m_pytest_returncode": None if uv_pytest is None else uv_pytest.returncode,
                },
            )
    finally:
        symlink_env_temp.cleanup()

    incomplete_temp = copy_repo_for_test(root)
    source_temp = copy_repo_for_test(root)
    try:
        incomplete_root = Path(incomplete_temp.name)
        source_root = Path(source_temp.name)
        incomplete_dir = create_complete_unit_fixture(incomplete_root, unit)
        source_dir = create_complete_unit_fixture(source_root, unit)
        sentinel = "\n## Rahul's preserved note\n\nI noticed that the invariant describes the consumed prefix, not the next item.\n"
        with (incomplete_dir / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(sentinel)
        shutil.rmtree(incomplete_dir / "practice")
        (incomplete_dir / "REVIEW.md").unlink()
        before = validate_repository(incomplete_root, run_external=False, profile="live")
        before_codes = {error.split("]", 1)[0] + "]" for error in before.errors if error.startswith("[")}
        readme_before = sha256_file(incomplete_dir / "README.md")
        actions = repair_fixture_from_source(source_dir, incomplete_dir)
        readme_after = sha256_file(incomplete_dir / "README.md")
        after = validate_repository(incomplete_root, run_external=False, profile="live")
        observed = "passed" if {"[UNIT_MISSING_PRACTICE]", "[UNIT_MISSING_REVIEW]"}.issubset(before_codes) and not after.errors and readme_before == readme_after and actions else "failed"
        record("incomplete_unit_repair", "passed", observed, {"before_codes": sorted(before_codes), "actions": actions, "after_errors": after.errors, "readme_preserved": readme_before == readme_after})
    finally:
        incomplete_temp.cleanup()
        source_temp.cleanup()

    learner_temp = copy_repo_for_test(root)
    repair_source = copy_repo_for_test(root)
    try:
        learner_root = Path(learner_temp.name)
        repair_root = Path(repair_source.name)
        learner_dir = create_complete_unit_fixture(learner_root, unit)
        source_dir = create_complete_unit_fixture(repair_root, unit)
        attempt = learner_dir / "practice" / "learner_attempt.py"
        attempt.write_text('''def longest_positive_streak(values: list[int]) -> int:\n    # Rahul's first attempt is intentionally preserved.\n    best = 0\n    current = 0\n    for value in values:\n        current = current + 1 if value > 0 else 0\n        best = max(best, current)\n    return best\n''', encoding="utf-8")
        hashes_before = {path.relative_to(learner_dir).as_posix(): sha256_file(path) for path in learner_dir.rglob("*") if path.is_file()}
        actions = repair_fixture_from_source(source_dir, learner_dir)
        hashes_after = {path.relative_to(learner_dir).as_posix(): sha256_file(path) for path in learner_dir.rglob("*") if path.is_file()}
        report = validate_repository(learner_root, run_external=False, profile="live")
        observed = "passed" if not actions and hashes_before == hashes_after and not report.errors else "failed"
        record("preserved_learner_work_and_idempotent_noop", "passed", observed, {"actions": actions, "hashes_preserved": hashes_before == hashes_after, "errors": report.errors})
    finally:
        learner_temp.cleanup()
        repair_source.cleanup()

    route = decide_initialization_route(current_branch="topic/DSA-SEQ-010", exact_branch="topic/DSA-SEQ-010", clean=True, local_exists=True, remote_exists=True, remote_ahead=0, local_ahead=1, selected_is_ancestor_of_origin_main=False)
    record("same_exact_topic_resumes_when_main_moved", "resume_exact_branch", route.action or route.error_code or "unknown")
    stale = decide_initialization_route(current_branch="", exact_branch="topic/DSA-SEQ-010", clean=True, local_exists=False, remote_exists=False, selected_is_ancestor_of_origin_main=True)
    record("clean_stale_main_worktree_recovers_from_origin_main", "create_exact_branch_from_origin_main", stale.action or stale.error_code or "unknown")

    renamed_temp = copy_repo_for_test(root)
    try:
        renamed_root = Path(renamed_temp.name)
        with tempfile.TemporaryDirectory(prefix="dsa-renamed-copy-") as work:
            work_path = Path(work)
            canonical = work_path / "dsa-mastery-bootstrap.zip"
            with zipfile.ZipFile(canonical, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in sorted(path for path in renamed_root.rglob("*") if path.is_file()):
                    zf.write(file_path, file_path.relative_to(renamed_root).as_posix())
            report = validate_repository(renamed_root, run_external=False, profile="bootstrap")
            validate_archive(report, canonical, run_external=False)
            report.self_tests = {"status": "passed", "count": 0, "passed": 0, "cases": [], "fixtures": {"status": "passed", "count": 0, "passed": 0, "cases": []}}
            report_path = work_path / "report.json"
            report_path.write_text(json.dumps(report.as_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
            renamed = work_path / "downloaded-copy-renamed.zip"
            shutil.copy2(canonical, renamed)
            verification = verify_validation_report(report_path, renamed, verify_self_tests=False, allow_renamed_archive=True)
            record("renamed_archive_content_identity", "passed", verification["status"], verification)
    finally:
        renamed_temp.cleanup()

    passed = sum(case["status"] == "passed" for case in cases)
    return {"status": "passed" if passed == len(cases) else "failed", "count": len(cases), "passed": passed, "cases": cases}

def run_negative_self_tests(root: Path) -> dict[str, object]:
    tests: list[tuple[str, str, object, str]] = []

    def add(name: str, expected_error: str, runner: object, mode: str = "bootstrap_mutation") -> None:
        tests.append((name, expected_error, runner, mode))

    def duplicate_unit(r: Path) -> None:
        path = r / "CURRICULUM.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if '`DSA-FND-010` —' in line)
        path.write_text(text + "\n" + row + "\n")
    add("duplicate_unit_id", "Duplicate curriculum IDs", duplicate_unit)

    def missing_prereq(r: Path) -> None:
        path = r / "CURRICULUM.md"
        path.write_text(path.read_text().replace("`DSA-FND-010` | `C/H/H/H/D2`", "`DSA-ZZZ-999` | `C/H/H/H/D2`", 1))
    add("missing_prerequisite", "Unknown prerequisite DSA-ZZZ-999", missing_prereq)

    def cycle(r: Path) -> None:
        path = r / "CURRICULUM.md"
        path.write_text(path.read_text().replace("| None | `C/H/H/H/D1`", "| `DSA-FND-020` | `C/H/H/H/D1`", 1))
    add("prerequisite_cycle", "Curriculum prerequisite cycle detected", cycle)

    def wrong_path(r: Path) -> None:
        path = r / "LEARNING_PATHS.md"
        path.write_text(re.sub(r'"unit_count":\d+', '"unit_count":999', path.read_text(), count=1))
    add("wrong_path_count", "Declared counts do not match links for path absolute-dsa-foundations", wrong_path)

    def wrong_timing(r: Path) -> None:
        path = r / "LEARNING_PATHS.md"
        path.write_text(re.sub(r'"rapid_total_minutes":\[\d+,\d+\]', '"rapid_total_minutes":[1,2]', path.read_text(), count=1))
    add("inconsistent_rapid_timing", "Timing mismatch for absolute-dsa-foundations rapid_total_minutes", wrong_timing)

    def duplicate_problem(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        data["problems"].append(copy.deepcopy(data["problems"][0]))
        path.write_text(json.dumps(data))
    add("duplicate_problem_ownership", "Duplicate problem number/ownership: 1", duplicate_problem)

    def bad_url(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        data["problems"][0]["url"] = "https://example.com/two-sum"
        path.write_text(json.dumps(data))
    add("malformed_leetcode_url", "Malformed canonical LeetCode URL for LC 1", bad_url)

    def premium(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        data["problems"][0]["access"] = "premium"
        data["problems"][0]["free_alternative"] = None
        path.write_text(json.dumps(data))
    add("premium_mandatory_without_alternative", "Premium-only mandatory problem lacks a free alternative: LC 1", premium)

    def path_missing_owner(r: Path) -> None:
        path = r / "LEARNING_PATHS.md"
        text = re.sub(r'^\d+\. \[DSA-SEQ-020 — .*?\n', '', path.read_text(), count=1, flags=re.MULTILINE)
        match = re.search(r'"unit_count":(\d+)', text)
        if match:
            text = text[:match.start(1)] + str(int(match.group(1)) - 1) + text[match.end(1):]
        path.write_text(text)
    add("missing_problem_owner_or_prerequisite_in_path", "without owner/prerequisite DSA-SEQ-020", path_missing_owner)

    def empty_traps(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        data["problems"][0]["trap_categories"] = []
        path.write_text(json.dumps(data))
    add("empty_problem_trap_metadata", "Empty trap metadata for teaching/mandatory LC 1", empty_traps)

    def generic_followup(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        for item in data["problems"][:5]:
            item["original_follow_up_variations"] = ["Change one constraint"]
        path.write_text(json.dumps(data))
    add("generic_repeated_followup_placeholders", "Generic or empty follow-up placeholder for LC 1", generic_followup)

    def small_reserve(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        reserve = [problem for problem in data["problems"] if problem.get("reserve_pool") == "unlabeled_easy_medium"]
        for item in reserve[19:]:
            item["reserve_pool"] = "teaching"
            item["visibility"] = "teaching"
        path.write_text(json.dumps(data))
    add("insufficient_easy_medium_reserve", "Easy/Medium unlabeled reserve must contain 24–40 problems", small_reserve)

    def semantic_mismatch(r: Path) -> None:
        path = r / "CURRICULUM.md"
        path.write_text(path.read_text().replace("Low-link DFS: bridges, articulation points, and strongly connected components", "Advanced graph components", 1))
    add("semantic_required_unit_title_outcome_mismatch", "Semantic required-unit mismatch for DSA-GRA-150", semantic_mismatch)

    def identical_projects(r: Path) -> None:
        path = r / "PROJECTS.md"
        text = path.read_text()
        sections = re.findall(r'(### Seeded defects\n\n.*?)(?=\n### )', text, re.DOTALL)
        path.write_text(text.replace(sections[1], sections[0], 1))
    add("identical_project_section", "Identical project boilerplate detected in section: Seeded defects", identical_projects)

    def wrong_remaining_count(r: Path) -> None:
        path = r / "data/problems.json"
        data = json.loads(path.read_text())
        data["metadata_policy"]["online_verification"]["remaining_count"] = 89
        path.write_text(json.dumps(data))
    add("incorrect_online_verification_remaining_count", "Online verification remaining_count mismatch", wrong_remaining_count)

    def missing_practice(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        shutil.rmtree(unit_dir / "practice")
        return validate_repository(r, run_external=False, profile="live").errors
    add("missing_practice_artifact", "[UNIT_MISSING_PRACTICE]", missing_practice, "direct_runner")

    def shallow_practice(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        practice = unit_dir / "practice" / "README.md"
        practice.write_text(f"# Practice — DSA-SEQ-010 {units['DSA-SEQ-010'].title}\n\n## DSA-SEQ-010-P01 — Name only\n", encoding="utf-8")
        return validate_repository(r, run_external=False, profile="live").errors
    add("practice_titles_without_tasks", "[UNIT_PRACTICE_TASK_SHALLOW]", shallow_practice, "direct_runner")

    def missing_review(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        (unit_dir / "REVIEW.md").unlink()
        return validate_repository(r, run_external=False, profile="live").errors
    add("missing_review_artifact", "[UNIT_MISSING_REVIEW]", missing_review, "direct_runner")

    def missing_interview(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        readme = unit_dir / "README.md"
        text = readme.read_text()
        text = re.sub(r'## 15\. Interview questions, traps, and follow-ups\n.*?(?=## 16\.)', '', text, flags=re.DOTALL)
        readme.write_text(text)
        return validate_repository(r, run_external=False, profile="live").errors
    add("missing_interview_questions", "[UNIT_INTERVIEW_COVERAGE_MISSING]", missing_interview, "direct_runner")

    def missing_lab(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        (unit_dir / "practice" / "micro_lab.py").unlink()
        return validate_repository(r, run_external=False, profile="live").errors
    add("missing_required_micro_lab", "[UNIT_MISSING_MICRO_LAB]", missing_lab, "direct_runner")

    def missing_experiment(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        create_complete_unit_fixture(r, units["DSA-FND-080"])
        return validate_repository(r, run_external=False, profile="live").errors
    add("missing_required_experiment", "[UNIT_MISSING_EXPERIMENT]", missing_experiment, "direct_runner")

    def placeholder(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        with (unit_dir / "README.md").open("a") as handle:
            handle.write("\n{{UNRESOLVED_PLACEHOLDER}}\n")
        return validate_repository(r, run_external=False, profile="live").errors
    add("unresolved_unit_placeholder", "[UNIT_TEMPLATE_PLACEHOLDER]", placeholder, "direct_runner")

    def leaked_solution(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        unit_dir = create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        with (unit_dir / "practice" / "README.md").open("a") as handle:
            handle.write("\n## Complete solution\n\nHere is the complete solution before an attempt.\n")
        return validate_repository(r, run_external=False, profile="live").errors
    add("premature_complete_practice_solution", "[UNIT_PREMATURE_SOLUTION]", leaked_solution, "direct_runner")

    def workflow_exact_main(r: Path) -> None:
        path = r / "docs/WORKFLOW.md"
        path.write_text(path.read_text() + "\nThe selected Worktree commit, local main, and origin/main must identify the same synchronized baseline.\n")
    add("same_exact_topic_incorrectly_blocked_when_main_moved", "[WORKFLOW_EXACT_BRANCH_MAIN_EQUALITY_BLOCK]", workflow_exact_main)

    def workflow_other_topic(r: Path) -> None:
        path = r / "docs/WORKFLOW.md"
        path.write_text(path.read_text().replace("If the current branch is another `topic/...` or `project/...`, stop.", "If the current branch is another topic or project, switch it to the requested branch."))
    add("different_topic_incorrectly_allowed_in_occupied_worktree", "[WORKFLOW_OCCUPIED_WORKTREE_GUARD_MISSING]", workflow_other_topic)

    def workflow_stale(r: Path) -> None:
        path = r / "docs/WORKFLOW.md"
        path.write_text(path.read_text().replace("git merge-base --is-ancestor HEAD refs/remotes/origin/main", "git rev-parse HEAD"))
    add("recoverable_stale_main_worktree_incorrectly_rejected", "[WORKFLOW_STALE_MAIN_RECOVERY_MISSING]", workflow_stale)

    def workflow_repair(r: Path) -> None:
        workflow_path = r / "docs/WORKFLOW.md"
        agents_path = r / "AGENTS.md"
        workflow_path.write_text(
            workflow_path.read_text().replace(
                "Preserve existing notes, examples, attempts, experiments, review evidence, and learner files byte-for-byte unless Rahul explicitly asks for an edit.",
                "Regenerate the existing pack from the template.",
            )
        )
        agents_path.write_text(
            agents_path.read_text().replace(
                "Preserve all existing notes, examples, attempts, experiments, review evidence, and learner files.",
                "Regenerate all existing learning files.",
            )
        )
    add("repair_rerun_overwrites_learner_work", "[WORKFLOW_REPAIR_PRESERVATION_MISSING]", workflow_repair)

    def workflow_push_boundary(r: Path) -> None:
        path = r / "docs/WORKFLOW.md"
        path.write_text(path.read_text().replace("local-only commit list equals the current-operation commit list exactly", "branch contains at least one new commit"))
    add("older_local_commits_included_in_initialization_push", "[WORKFLOW_INIT_PUSH_BOUNDARY_MISSING]", workflow_push_boundary)

    def archive_with_git_directory(r: Path) -> list[str]:
        with tempfile.TemporaryDirectory(prefix="dsa-archive-git-dir-") as temp:
            archive = Path(temp) / "bad-git-dir.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in iter_repository_files(r, "bootstrap"):
                    zf.write(file_path, file_path.relative_to(r).as_posix())
                zf.writestr(".git/HEAD", "ref: refs/heads/main\n")
            archive_report = Report(root=r.resolve(), profile="bootstrap")
            validate_archive(archive_report, archive, run_external=False)
            return archive_report.errors
    add(
        "archive_forbids_git_directory_metadata",
        "[ARCHIVE_FORBIDDEN_GIT_METADATA]",
        archive_with_git_directory,
        "direct_runner",
    )

    def archive_with_git_file(r: Path) -> list[str]:
        with tempfile.TemporaryDirectory(prefix="dsa-archive-git-file-") as temp:
            archive = Path(temp) / "bad-git-file.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in iter_repository_files(r, "bootstrap"):
                    zf.write(file_path, file_path.relative_to(r).as_posix())
                zf.writestr(".git", "gitdir: /tmp/example/.git/worktrees/dsa\n")
            archive_report = Report(root=r.resolve(), profile="bootstrap")
            validate_archive(archive_report, archive, run_external=False)
            return archive_report.errors
    add(
        "archive_forbids_root_git_file",
        "[ARCHIVE_FORBIDDEN_GIT_METADATA]",
        archive_with_git_file,
        "direct_runner",
    )

    def archive_with_local_artifact(r: Path, entry_name: str, payload: bytes | str = "local\n") -> list[str]:
        with tempfile.TemporaryDirectory(prefix="dsa-archive-local-artifact-") as temp:
            archive = Path(temp) / "bad-local-artifact.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in iter_repository_files(r, "bootstrap"):
                    zf.write(file_path, file_path.relative_to(r).as_posix())
                zf.writestr(entry_name, payload)
            archive_report = Report(root=r.resolve(), profile="bootstrap")
            validate_archive(archive_report, archive, run_external=False)
            return archive_report.errors

    add(
        "archive_forbids_project_environment",
        "[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]",
        lambda r: archive_with_local_artifact(r, ".venv/pyvenv.cfg", "home = /usr/bin\n"),
        "direct_runner",
    )
    add(
        "archive_forbids_nested_bytecode_cache",
        "[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]",
        lambda r: archive_with_local_artifact(r, "nested/__pycache__/module.cpython-314.pyc", b"\x00\x00local-bytecode"),
        "direct_runner",
    )
    add(
        "archive_forbids_pytest_cache",
        "[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]",
        lambda r: archive_with_local_artifact(r, ".pytest_cache/v/cache/nodeids", "[]\n"),
        "direct_runner",
    )
    add(
        "archive_forbids_tool_cache",
        "[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]",
        lambda r: archive_with_local_artifact(r, ".mypy_cache/3.14/metadata.json", "{}\n"),
        "direct_runner",
    )
    add(
        "archive_forbids_coverage_artifact",
        "[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]",
        lambda r: archive_with_local_artifact(r, ".coverage", "local coverage database\n"),
        "direct_runner",
    )

    def working_private_path(r: Path, relative: str, profile: str = "bootstrap") -> list[str]:
        path = r / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("synthetic private fixture only\n", encoding="utf-8")
        return validate_repository(r, run_external=False, profile=profile).errors

    add(
        "working_forbids_private_directory",
        "[PROFILE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: working_private_path(r, "private/notes.txt"),
        "direct_runner",
    )
    add(
        "working_forbids_tokens_directory",
        "[PROFILE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: working_private_path(r, "tokens/example.txt"),
        "direct_runner",
    )
    add(
        "live_forbids_private_directory",
        "[PROFILE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: working_private_path(r, "private/notes.txt", "live"),
        "direct_runner",
    )
    add(
        "live_forbids_tokens_directory",
        "[PROFILE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: working_private_path(r, "tokens/example.txt", "live"),
        "direct_runner",
    )
    add(
        "archive_forbids_private_directory",
        "[ARCHIVE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: archive_with_local_artifact(r, "private/notes.txt", "synthetic private fixture only\n"),
        "direct_runner",
    )
    add(
        "archive_forbids_tokens_directory",
        "[ARCHIVE_FORBIDDEN_PRIVATE_PATH]",
        lambda r: archive_with_local_artifact(r, "tokens/example.txt", "synthetic token fixture only\n"),
        "direct_runner",
    )

    def archive_with_units(r: Path) -> list[str]:
        report = Report(root=r.resolve(), profile="bootstrap")
        _rows, units = parse_units(report)
        create_complete_unit_fixture(r, units["DSA-SEQ-010"])
        with tempfile.TemporaryDirectory(prefix="dsa-archive-generated-") as temp:
            archive = Path(temp) / "bad.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in iter_repository_files(r, "live"):
                    zf.write(file_path, file_path.relative_to(r).as_posix())
            archive_report = Report(root=r.resolve(), profile="bootstrap")
            validate_archive(archive_report, archive, run_external=False)
            return archive_report.errors
    add("archive_incorrectly_includes_generated_units", "[ARCHIVE_FORBIDDEN_GENERATED_PATH]", archive_with_units, "direct_runner")

    def older_commits_runner(_r: Path) -> list[str]:
        decision = evaluate_initialization_push(["older", "current"], ["current"])
        return [f"[{decision.error_code}] {decision.detail}"] if decision.error_code else []
    add("older_local_only_commit_publication_guard", "[INIT_PUSH_INCLUDES_OLDER_LOCAL_COMMITS]", older_commits_runner, "direct_runner")

    results: list[dict[str, object]] = []
    for name, expected_error, runner, mode in tests:
        temp = copy_repo_for_test(root)
        try:
            test_root = Path(temp.name)
            if mode == "direct_runner":
                observed_errors = runner(test_root)  # type: ignore[misc]
            else:
                runner(test_root)  # type: ignore[misc]
                observed_errors = validate_repository(test_root, run_external=False, profile="bootstrap").errors
            matching = next((error for error in observed_errors if expected_error in error), None)
            results.append({"name": name, "status": "passed" if matching else "failed", "expected_error": expected_error, "observed_matching_error": matching, "observed_error_count": len(observed_errors), "observed_errors": observed_errors if not matching else []})
        except Exception as exc:
            results.append({"name": name, "status": "failed", "expected_error": expected_error, "observed_matching_error": None, "detail": str(exc)})
        finally:
            temp.cleanup()

    stale_expected = "REPORT_ARCHIVE_SHA256_MISMATCH"
    stale_repo = copy_repo_for_test(root)
    try:
        stale_root = Path(stale_repo.name)
        with tempfile.TemporaryDirectory(prefix="dsa-stale-report-test-") as temp_dir:
            temp_path = Path(temp_dir)
            archive = temp_path / "dsa-mastery-bootstrap.zip"
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in iter_repository_files(stale_root, "bootstrap"):
                    zf.write(file_path, file_path.relative_to(stale_root).as_posix())
            genuine_report = validate_repository(stale_root, run_external=False, profile="bootstrap")
            validate_archive(genuine_report, archive, run_external=False)
            genuine_payload = genuine_report.as_dict()
            report_file = temp_path / "genuine-report.json"
            report_file.write_text(json.dumps(genuine_payload, indent=2, sort_keys=True) + "\n")
            stale_payload = json.loads(report_file.read_text())
            stale_payload["archive"]["sha256"] = "0" * 64
            report_file.write_text(json.dumps(stale_payload, indent=2, sort_keys=True) + "\n")
            verification = verify_validation_report(report_file, archive, verify_self_tests=False)
            matching = next((error for error in verification["errors"] if stale_expected in error), None)
            results.append({"name": "stale_archive_metadata", "status": "passed" if matching else "failed", "expected_error": stale_expected, "observed_matching_error": matching, "observed_error_count": len(verification["errors"]), "observed_errors": verification["errors"] if not matching else []})
    except Exception as exc:
        results.append({"name": "stale_archive_metadata", "status": "failed", "expected_error": stale_expected, "observed_matching_error": None, "detail": str(exc)})
    finally:
        stale_repo.cleanup()

    fixtures = run_fixture_tests(root)
    passed = sum(item["status"] == "passed" for item in results)
    overall = passed == len(results) and fixtures["status"] == "passed"
    return {"status": "passed" if overall else "failed", "count": len(results), "passed": passed, "cases": results, "fixtures": fixtures}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--profile", choices=sorted(VALIDATION_PROFILES), default="auto")
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--json", type=Path, dest="json_path")
    parser.add_argument("--verify-report", type=Path, dest="verify_report_path")
    parser.add_argument("--allow-renamed-archive", action="store_true")
    parser.add_argument(
        "--skip-self-test-comparison",
        action="store_true",
        help="Verify archive content and statistics without rerunning pytest-backed fixture/self-tests.",
    )
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.skip_self_test_comparison and not args.verify_report_path:
        parser.error("--skip-self-test-comparison is valid only with --verify-report")

    if args.verify_report_path:
        if not args.archive:
            parser.error("--verify-report requires --archive")
        verification = verify_validation_report(
            args.verify_report_path,
            args.archive,
            verify_self_tests=not args.skip_self_test_comparison,
            allow_renamed_archive=args.allow_renamed_archive,
        )
        print(json.dumps(verification, indent=2, sort_keys=True))
        return 0 if verification["status"] == "passed" else 1

    report = validate_repository(args.root, profile=args.profile)
    if args.self_test:
        prerequisite_error = pytest_prerequisite_error("Validator --self-test")
        if prerequisite_error:
            report.error(prerequisite_error)
            report.mark("validator_self_tests", "skipped")
            report.self_tests = {
                "status": "skipped",
                "reason": prerequisite_error,
                "setup_command": "uv sync --group dev",
                "run_command": "uv run --group dev python scripts/validate_repo.py --self-test",
                "count": 0,
                "passed": 0,
                "cases": [],
                "fixtures": {"status": "skipped", "count": 0, "passed": 0, "cases": []},
            }
        else:
            report.self_tests = run_negative_self_tests(args.root.resolve())
            report.mark("validator_self_tests", report.self_tests["status"] == "passed")
            if report.self_tests["status"] != "passed":
                report.error("Validator negative or fixture self-tests failed")
    if args.archive:
        validate_archive(report, args.archive, run_external=False)
    payload = report.as_dict()
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "passed" else 1

if __name__=="__main__": raise SystemExit(main())
