import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

runner = importlib.import_module("repo_template.prompt_eval_runner")
run_golden_eval_suite = runner.run_golden_eval_suite
validate_prompt_eval_links = runner.validate_prompt_eval_links


def test_prompt_eval_links_are_consistent() -> None:
    errors = validate_prompt_eval_links(ROOT)
    assert not errors, "Prompt/eval link errors:\n- " + "\n- ".join(errors)


def test_golden_eval_cases_match_expected_outcomes() -> None:
    results = run_golden_eval_suite(ROOT)
    assert results, "Expected at least one golden eval case result."
    mismatches = [result for result in results if not result.matched]
    assert not mismatches, "Golden eval mismatches:\n- " + "\n- ".join(
        f"{result.eval_id}/{result.case_name} expected={result.expected_pass} "
        f"actual={result.actual_pass} reasons={list(result.reasons)}"
        for result in mismatches
    )
