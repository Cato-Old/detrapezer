from unittest import TestCase

from app.settings import Settings


class SettingsTest(TestCase):
    def setUp(self):
        self.settings = Settings

    def test_can_save_state_globally(self):
        self.settings(debug_mode=True)
        actual = self.settings()
        self.assertTrue(actual.debug_mode)
