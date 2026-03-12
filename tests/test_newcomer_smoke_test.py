import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "newcomer_smoke_test.py"

spec = importlib.util.spec_from_file_location("newcomer_smoke_test", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_newcomer_smoke_checks_pass_required_items() -> None:
    checks = module.run_newcomer_smoke_checks(ROOT)
    failures = [
        check for check in checks if not check.passed and check.name != "powershell-available"
    ]
    assert not failures, "\n".join(f"{check.name}: {check.detail}" for check in failures)
