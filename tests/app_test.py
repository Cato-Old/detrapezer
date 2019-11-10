from unittest import TestCase

from app.app import compose, App


class AppComposingTest(TestCase):
    def test_compose_app(self):
        app = compose()
        self.assertIsInstance(app, App)
