from unittest import TestCase
from unittest.mock import Mock

from app.app import compose, App
from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor


class AppTest(TestCase):
    def setUp(self):
        self.cli = Mock(CLI, autospec=True)
        self.preparer = Mock(ImagePreparer)
        self.processor = Mock(ImageProcessor)
        self.app = compose(
            cli=self.cli,
            preparer=self.preparer,
            processor=self.processor,
        )

    def test_compose_app(self):
        self.assertIsInstance(self.app, App)

    def test_has_app_cli(self):
        self.assertIs(self.app.cli, self.cli)

    def test_has_app_preparer(self):
        self.assertIs(self.app.preparer, self.preparer)

    def test_has_app_processor(self):
        self.assertIs(self.app.processor, self.processor)

    def test_cli_parse_arguments_when_app_run(self):
        args = [r'C:\foo\bar.baz']
        self.cli.args = Mock(path=args[0])
        self.app.run(args)
        self.cli.parse.assert_called_once_with(args)

    def test_image_preparer_process_image_when_app_runs(self):
        path = '../tests/resources/specimen.tif'
        self.cli.args = Mock(path=path)
        self.app.run([path])
        self.preparer.prepare.assert_called_once_with(path)
