from unittest import TestCase

from app.settings import Settings


class SettingsTest(TestCase):
    def setUp(self):
        self.settings = Settings

    def test_can_save_state_globally(self):
        self.settings(debug_mode=True)
        actual = self.settings()
        self.assertTrue(actual.debug_mode)

    def test_cannot_change_initiated_value(self):
        self.settings(debug_mode=True)
        actual = self.settings()
        with self.assertRaises(TypeError):
            actual.debug_mode = False

    def tearDown(self):
        self.settings.clear()
