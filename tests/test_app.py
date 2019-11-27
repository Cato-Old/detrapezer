from unittest import TestCase
from unittest.mock import Mock, PropertyMock

import cv2
import numpy as np
from numpy.testing import assert_array_equal

from app.app import compose, App
from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor
from app.settings import Settings


class AppTest(TestCase):
    def setUp(self):
        self.res_paths = {
            k: f'../tests/resources/{k}.tif'
            for k in ('prepared', 'specimen', 'processed')
        }
        self.res = {
            k: cv2.imread(v, cv2.IMREAD_UNCHANGED)
            for k, v in self.res_paths.items()
        }
        self.cli = self._configure_cli_mock()
        self.preparer = self._configure_preparer_mock()
        self.processor = self._configure_processor_mock()
        self.settings = Mock(Settings)
        self.app = compose(
            cli=self.cli,
            preparer=self.preparer,
            processor=self.processor,
            settings=self.settings,
        )

    def _configure_preparer_mock(self) -> Mock:
        preparer = Mock(ImagePreparer)
        preparer.prepare = Mock(return_value=self.res['prepared'])
        type(preparer).image = PropertyMock(return_value=self.res['specimen'])
        return preparer

    def _configure_cli_mock(self) -> Mock:
        cli = Mock(CLI, autospec=True)
        cli.args = Mock(
            path=self.res_paths['specimen'], output=None, debug=True,
        )
        return cli

    def _configure_processor_mock(self) -> Mock:
        processor = Mock(ImageProcessor)
        processor.process = Mock(return_value=self.res['processed'])
        return processor

    def test_compose_app(self):
        self.assertIsInstance(self.app, App)

    def test_has_app_cli(self):
        self.assertIs(self.app.cli, self.cli)

    def test_has_app_preparer(self):
        self.assertIs(self.app.preparer, self.preparer)

    def test_has_app_processor(self):
        self.assertIs(self.app.processor, self.processor)

    def test_has_app_settings(self):
        self.assertIs(self.app.settings, self.settings)

    def test_cli_parse_arguments_when_app_run(self):
        args = [r'C:\foo\bar.baz']
        self.cli.args.path = args[0]
        self.app.run(args)
        self.cli.parse.assert_called_once_with(args)

    def test_image_preparer_process_image_when_app_runs(self):
        path = self.res_paths['specimen']
        self.app.run([path])
        self.preparer.prepare.assert_called_once_with(path)

    def test_image_processor_process_image_when_app_runs(self):
        self.app.run([self.res_paths['specimen']])
        self.processor.process.assert_called_once()
        mock_args = self.processor.process.call_args
        assert_array_equal(self.res['prepared'], mock_args[0][0])
        assert_array_equal(self.res['specimen'], mock_args[0][1])

    def test_settings_has_debug_mode_set_from_cli_arg(self):
        self.app.run([self.res_paths['specimen']])
        self.assertEqual(self.settings.debug_mode, self.cli.args.debug)
