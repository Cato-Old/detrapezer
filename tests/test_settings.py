from unittest import TestCase

from app.settings import Settings


class SettingsTest(TestCase):
    def setUp(self):
        self.settings = Settings
        self.settings_val = {
            'debug_mode': True,
        }

    def test_can_save_state_globally(self):
        for k, v in self.settings_val.items():
            with self.subTest(k):
                self.settings(**{k: v})
                actual = self.settings()
                self.assertEqual(getattr(actual, k), v)
                self.tearDown()

    def test_cannot_change_initiated_value(self):
        for k, v in self.settings_val.items():
            with self.subTest(k):
                self.settings(**{k: v})
                actual = self.settings()
                with self.assertRaises(TypeError):
                    setattr(actual, k, v)
                self.tearDown()

    def tearDown(self):
        self.settings.clear()
