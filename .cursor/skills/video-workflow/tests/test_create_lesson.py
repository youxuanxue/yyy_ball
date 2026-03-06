import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_lesson.py"
HELPER_PATH = Path(__file__).resolve().parents[1] / "scripts" / "lesson_num.py"


def load_create_lesson_module():
    spec = importlib.util.spec_from_file_location("video_create_lesson_script", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def load_lesson_num_module():
    spec = importlib.util.spec_from_file_location("video_lesson_num_script", HELPER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class TestCreateLessonScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_create_lesson_module()
        cls.helper = load_lesson_num_module()

    def test_zsxq_data_source_path_is_precise(self):
        cfg = self.mod.get_series_config("zsxq")
        self.assertEqual(cfg["data_source"], "assets/zsxq/jingpin_100ke_posts.json")

    def test_normalize_lesson_num_accepts_prefix(self):
        normalized = self.helper.normalize_lesson_num("lesson9", 3)
        self.assertEqual(normalized, "009")

    def test_normalize_lesson_num_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            self.helper.normalize_lesson_num("0", 2)
        with self.assertRaises(ValueError):
            self.helper.normalize_lesson_num("100", 2)


if __name__ == "__main__":
    unittest.main()
