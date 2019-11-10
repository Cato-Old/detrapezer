from unittest import TestCase
from unittest.mock import Mock

from app.app import compose, App
from app.cli import CLI


class AppComposingTest(TestCase):
    def setUp(self):
        self.cli = Mock(CLI)
        self.app = compose(cli=self.cli)

    def test_compose_app(self):
        self.assertIsInstance(self.app, App)

    def test_has_app_cli(self):
        self.assertIs(self.app.cli, self.cli)
