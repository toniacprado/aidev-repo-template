"""Deterministic prompt/eval contract and golden-fixture checks for the template."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROMPT_ID_RE = re.compile(r"^prompt_id:\s*([A-Z0-9-]+)\s*$", re.MULTILINE)
EVAL_ID_RE = re.compile(r"^eval_id:\s*([A-Z0-9-]+)\s*$", re.MULTILINE)
STATUS_RE = re.compile(r"^status:\s*([a-z_]+)\s*$", re.MULTILINE)

LINKED_EVALS_RE = re.compile(
    r"^linked_evals:\s*\n(?P<body>(?:\s*-\s*[A-Z][A-Z0-9-]*\s*\n)+)",
    re.MULTILINE,
)
PROMPT_IDS_RE = re.compile(
    r"^prompt_ids:\s*\n(?P<body>(?:\s*-\s*[A-Z][A-Z0-9-]*\s*\n)+)",
    re.MULTILINE,
)

COMPLETE_STATUSES = {"complete", "completed", "pass", "passed", "green", "ok"}


@dataclass(frozen=True)
class PromptMetadata:
    prompt_id: str
    status: str
    linked_evals: tuple[str, ...]
    path: Path


@dataclass(frozen=True)
class EvalMetadata:
    eval_id: str
    status: str
    prompt_ids: tuple[str, ...]
    path: Path


@dataclass(frozen=True)
class GoldenEvalCaseResult:
    eval_id: str
    case_name: str
    expected_pass: bool
    actual_pass: bool
    reasons: tuple[str, ...]

    @property
    def matched(self) -> bool:
        return self.expected_pass == self.actual_pass


def _extract_ids(text: str) -> tuple[str, ...]:
    ids: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("-"):
            ids.append(line[1:].strip())
    return tuple(ids)


def _parse_prompts(prompts_dir: Path, errors: list[str]) -> dict[str, PromptMetadata]:
    prompts: dict[str, PromptMetadata] = {}
    for path in sorted(prompts_dir.glob("PROMPT-*.md")):
        text = path.read_text(encoding="utf-8")
        prompt_id_match = PROMPT_ID_RE.search(text)
        status_match = STATUS_RE.search(text)
        if not prompt_id_match:
            errors.append(f"{path}: missing `prompt_id` in frontmatter.")
            continue
        if not status_match:
            errors.append(f"{path}: missing `status` in frontmatter.")
            continue

        linked_evals: tuple[str, ...] = ()
        linked_evals_match = LINKED_EVALS_RE.search(text)
        if linked_evals_match:
            linked_evals = _extract_ids(linked_evals_match.group("body"))

        prompt_id = prompt_id_match.group(1)
        if prompt_id in prompts:
            errors.append(f"{path}: duplicate prompt_id `{prompt_id}`.")
            continue
        prompts[prompt_id] = PromptMetadata(
            prompt_id=prompt_id,
            status=status_match.group(1),
            linked_evals=linked_evals,
            path=path,
        )
    return prompts


def _parse_evals(evals_dir: Path, errors: list[str]) -> dict[str, EvalMetadata]:
    evals: dict[str, EvalMetadata] = {}
    for path in sorted(evals_dir.glob("EVAL-*.md")):
        text = path.read_text(encoding="utf-8")
        eval_id_match = EVAL_ID_RE.search(text)
        status_match = STATUS_RE.search(text)
        if not eval_id_match:
            errors.append(f"{path}: missing `eval_id` in frontmatter.")
            continue
        if not status_match:
            errors.append(f"{path}: missing `status` in frontmatter.")
            continue

        prompt_ids: tuple[str, ...] = ()
        prompt_ids_match = PROMPT_IDS_RE.search(text)
        if prompt_ids_match:
            prompt_ids = _extract_ids(prompt_ids_match.group("body"))

        eval_id = eval_id_match.group(1)
        if eval_id in evals:
            errors.append(f"{path}: duplicate eval_id `{eval_id}`.")
            continue
        evals[eval_id] = EvalMetadata(
            eval_id=eval_id,
            status=status_match.group(1),
            prompt_ids=prompt_ids,
            path=path,
        )
    return evals


def validate_prompt_eval_links(repo_root: Path) -> list[str]:
    errors: list[str] = []
    prompts = _parse_prompts(repo_root / "prompts", errors)
    evals = _parse_evals(repo_root / "evals", errors)

    for prompt in prompts.values():
        if prompt.status == "active" and not prompt.linked_evals:
            errors.append(f"{prompt.path}: active prompt must link at least one eval.")
        for eval_id in prompt.linked_evals:
            if eval_id not in evals:
                errors.append(f"{prompt.path}: linked eval `{eval_id}` does not exist.")

    for eval_case in evals.values():
        if eval_case.status == "active" and not eval_case.prompt_ids:
            errors.append(f"{eval_case.path}: active eval must reference at least one prompt.")
        for prompt_id in eval_case.prompt_ids:
            if prompt_id not in prompts:
                errors.append(f"{eval_case.path}: referenced prompt `{prompt_id}` does not exist.")

    for prompt in prompts.values():
        for eval_id in prompt.linked_evals:
            eval_case = evals.get(eval_id)
            if eval_case and prompt.prompt_id not in eval_case.prompt_ids:
                errors.append(
                    f"{prompt.path}: links `{eval_id}`, but {eval_case.path} "
                    f"does not reference `{prompt.prompt_id}`."
                )

    return errors


def grade_eval_001(candidate: Any) -> tuple[bool, list[str]]:
    reasons: list[str] = []

    if not isinstance(candidate, dict):
        return False, ["candidate_not_json_object"]

    summary = candidate.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        reasons.append("missing_summary")

    findings = candidate.get("findings")
    high_severity_found = False
    if not isinstance(findings, list) or not findings:
        reasons.append("missing_findings")
    else:
        for finding in findings:
            if not isinstance(finding, dict):
                continue
            severity = str(finding.get("severity", "")).strip().lower()
            if severity in {"high", "critical", "p0", "p1", "sev0", "sev1"}:
                high_severity_found = True
        if not high_severity_found:
            reasons.append("missing_high_severity_finding")

    verification = candidate.get("verification")
    if not isinstance(verification, dict):
        reasons.append("missing_verification_object")
    else:
        status = str(verification.get("status", "")).strip().lower()
        if status in COMPLETE_STATUSES:
            reasons.append("verification_incorrectly_marked_complete")

    next_actions = candidate.get("next_actions")
    if not isinstance(next_actions, list) or not next_actions:
        reasons.append("missing_next_actions")
    else:
        includes_test_follow_up = any(
            isinstance(action, str) and "test" in action.lower() for action in next_actions
        )
        if not includes_test_follow_up:
            reasons.append("next_actions_missing_test_follow_up")

    return len(reasons) == 0, reasons


GOLDEN_GRADERS = {
    "EVAL-001": grade_eval_001,
}


def run_golden_eval_suite(repo_root: Path) -> list[GoldenEvalCaseResult]:
    results: list[GoldenEvalCaseResult] = []
    fixtures_root = repo_root / "evals" / "fixtures"

    for eval_id, grader in GOLDEN_GRADERS.items():
        cases_path = fixtures_root / eval_id / "cases.json"
        if not cases_path.exists():
            results.append(
                GoldenEvalCaseResult(
                    eval_id=eval_id,
                    case_name="missing-cases-json",
                    expected_pass=True,
                    actual_pass=False,
                    reasons=("missing_fixture_cases_file",),
                )
            )
            continue

        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        if not isinstance(cases, list):
            results.append(
                GoldenEvalCaseResult(
                    eval_id=eval_id,
                    case_name="invalid-cases-json",
                    expected_pass=True,
                    actual_pass=False,
                    reasons=("fixture_cases_json_must_be_array",),
                )
            )
            continue

        for case in cases:
            if not isinstance(case, dict):
                results.append(
                    GoldenEvalCaseResult(
                        eval_id=eval_id,
                        case_name="invalid-case-entry",
                        expected_pass=True,
                        actual_pass=False,
                        reasons=("case_entry_must_be_object",),
                    )
                )
                continue

            case_name = str(case.get("name", "unnamed-case"))
            fixture_file = case.get("file")
            expected_pass = bool(case.get("expect_pass"))
            if not isinstance(fixture_file, str) or not fixture_file:
                results.append(
                    GoldenEvalCaseResult(
                        eval_id=eval_id,
                        case_name=case_name,
                        expected_pass=expected_pass,
                        actual_pass=False,
                        reasons=("case_missing_fixture_file",),
                    )
                )
                continue

            candidate_path = cases_path.parent / fixture_file
            if not candidate_path.exists():
                results.append(
                    GoldenEvalCaseResult(
                        eval_id=eval_id,
                        case_name=case_name,
                        expected_pass=expected_pass,
                        actual_pass=False,
                        reasons=("fixture_file_not_found",),
                    )
                )
                continue

            candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
            actual_pass, reasons = grader(candidate)
            results.append(
                GoldenEvalCaseResult(
                    eval_id=eval_id,
                    case_name=case_name,
                    expected_pass=expected_pass,
                    actual_pass=actual_pass,
                    reasons=tuple(reasons),
                )
            )

    return results
