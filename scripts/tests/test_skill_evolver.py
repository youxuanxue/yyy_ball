import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[2] / ".cursor" / "skills" / "skill-evolver" / "scripts" / "evolve.py"


def load_module():
    spec = importlib.util.spec_from_file_location("skill_evolver_script", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class TestSkillEvolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_record_observation_writes_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = self.mod.record_observation(
                series="zsxq",
                lesson="002",
                stage="render",
                status="failed",
                failure_type="icon-missing",
                affects="adapter",
                summary="missing icon",
                notes="",
                commands=["uv run manim ..."],
                files=["script.json"],
                observations_dir=Path(tmp),
            )
            self.assertTrue(output.exists())
            text = output.read_text(encoding="utf-8")
            self.assertIn('"series": "zsxq"', text)
            self.assertIn('"failure_type": "icon-missing"', text)

    def test_build_report_promotes_cross_series_failure_to_core(self):
        rows = [
            {
                "series": "zsxq",
                "lesson": "002",
                "stage": "render",
                "status": "failed",
                "failure_type": "voice-timeout",
                "affects": "unknown",
                "summary": "timeout on render",
            },
            {
                "series": "moneywise",
                "lesson": "021",
                "stage": "render",
                "status": "failed",
                "failure_type": "voice-timeout",
                "affects": "unknown",
                "summary": "timeout on render again",
            },
        ]
        report = self.mod.build_report(rows)
        self.assertIn("recommended_target: core", report)
        self.assertIn("- series:", report)
        self.assertIn("zsxq", report)
        self.assertIn("moneywise", report)


if __name__ == "__main__":
    unittest.main()
