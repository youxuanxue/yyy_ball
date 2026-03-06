import importlib.util
import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "workflow.py"


def load_workflow_module():
    spec = importlib.util.spec_from_file_location("video_workflow_script", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class TestWorkflowScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = load_workflow_module()

    def test_supports_moneywise_series(self):
        config = self.workflow.get_series_config("moneywise")
        self.assertEqual(config["name"], "MoneyWise Global")
        self.assertEqual(config["num_digits"], 3)

    def test_lesson_dir_and_class_name_padding(self):
        lesson_dir = self.workflow.get_lesson_dir("moneywise", "1")
        class_name = self.workflow.get_class_name("moneywise", "1")
        self.assertTrue(str(lesson_dir).endswith("series/moneywise_global/lesson001"))
        self.assertEqual(class_name, "Lesson001VerticalScenes")

    def test_lesson_prefix_input_is_supported(self):
        lesson_dir = self.workflow.get_lesson_dir("moneywise", "lesson1")
        class_name = self.workflow.get_class_name("sunzi", "lesson6")
        self.assertTrue(str(lesson_dir).endswith("series/moneywise_global/lesson001"))
        self.assertEqual(class_name, "Lesson06VerticalScenes")

    def test_invalid_lesson_num_exits(self):
        with redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit):
                self.workflow.get_lesson_dir("zsxq", "abc")

    def test_resolve_media_publisher_dir_priority(self):
        with tempfile.TemporaryDirectory() as env_dir, tempfile.TemporaryDirectory() as cli_dir:
            with patch.dict(os.environ, {"MEDIA_PUBLISHER_DIR": env_dir}, clear=True):
                resolved = self.workflow.resolve_media_publisher_dir(cli_dir)
                self.assertEqual(resolved, Path(cli_dir).resolve())

    def test_resolve_media_publisher_dir_from_env(self):
        with tempfile.TemporaryDirectory() as env_dir:
            with patch.dict(os.environ, {"MEDIA_PUBLISHER_DIR": env_dir}, clear=True):
                resolved = self.workflow.resolve_media_publisher_dir(None)
                self.assertEqual(resolved, Path(env_dir).resolve())

    def test_resolve_media_publisher_dir_missing_returns_none(self):
        with patch.object(self.workflow, "DEFAULT_MEDIA_PUBLISHER_DIR", Path("/tmp/definitely_missing_media_publisher")):
            with patch.dict(os.environ, {}, clear=True):
                resolved = self.workflow.resolve_media_publisher_dir(None)
                self.assertIsNone(resolved)


if __name__ == "__main__":
    unittest.main()
