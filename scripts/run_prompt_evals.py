#!/usr/bin/env python3
"""Run deterministic prompt/eval checks for the template repository."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def main() -> int:
    runner = importlib.import_module("repo_template.prompt_eval_runner")
    run_golden_eval_suite = runner.run_golden_eval_suite
    validate_prompt_eval_links = runner.validate_prompt_eval_links

    link_errors = validate_prompt_eval_links(ROOT)
    golden_results = run_golden_eval_suite(ROOT)
    golden_failures = [result for result in golden_results if not result.matched]

    print("Prompt/eval link checks:")
    if not link_errors:
        print("  OK: all active prompt/eval links are valid and reciprocal.")
    else:
        for error in link_errors:
            print(f"  FAIL: {error}")

    print("Golden eval checks:")
    if not golden_results:
        print("  FAIL: no golden eval results produced.")
        return 1

    for result in golden_results:
        status = "OK" if result.matched else "FAIL"
        reason_suffix = ""
        if result.reasons:
            reason_suffix = f" ({', '.join(result.reasons)})"
        print(
            f"  {status}: {result.eval_id} / {result.case_name} "
            f"(expected={result.expected_pass}, actual={result.actual_pass}){reason_suffix}"
        )

    if link_errors or golden_failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
