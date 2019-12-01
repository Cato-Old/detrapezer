import os
from unittest import TestCase
from unittest.mock import Mock, PropertyMock

import cv2
from numpy.testing import assert_array_equal

from app.app import compose, App
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
        self.preparer = self._configure_preparer_mock()
        self.processor = self._configure_processor_mock()
        self.settings = self._configure_settings_mock()
        self.app = self._configure_app(
            self.preparer, self.processor, self.settings,
        )

    def _configure_app(
            self,
            preparer: ImagePreparer,
            processor: ImageProcessor,
            settings: Settings,
    ) -> App:
        return compose(preparer, processor, settings)

    def _configure_preparer_mock(self) -> Mock:
        preparer = Mock(ImagePreparer)
        preparer.prepare = Mock(return_value=self.res['prepared'])
        type(preparer).image = PropertyMock(return_value=self.res['specimen'])
        return preparer

    def _configure_processor_mock(self) -> Mock:
        processor = Mock(ImageProcessor)
        processor.process = Mock(return_value=self.res['processed'])
        return processor

    def _configure_settings_mock(
            self, debug_mode=False, output='',
    ) -> Mock:
        return Mock(
            debug_mode=debug_mode,
            path=self.res_paths['specimen'],
            output=output
        )

    def test_compose_app(self):
        self.assertIsInstance(self.app, App)

    def test_has_app_preparer(self):
        self.assertIs(self.app.preparer, self.preparer)

    def test_has_app_processor(self):
        self.assertIs(self.app.processor, self.processor)

    def test_has_app_settings(self):
        self.assertIs(self.app.settings, self.settings)

    def test_image_preparer_process_image_when_app_runs(self):
        self.app.run()
        self.preparer.prepare.assert_called_once_with(
            self.res_paths['specimen']
        )

    def test_image_processor_process_image_when_app_runs(self):
        self.app.run()
        self.processor.process.assert_called_once()
        mock_args = self.processor.process.call_args
        assert_array_equal(self.res['prepared'], mock_args[0][0])
        assert_array_equal(self.res['specimen'], mock_args[0][1])

    def test_app_saves_prepared_image_in_debug_mode(self):
        settings = self._configure_settings_mock(debug_mode=True)
        app = self._configure_app(self.preparer, self.processor, settings)
        app.run()
        self.assertTrue(os.path.exists('debug.tif'))

    def tearDown(self):
        for file in ('debug.tif', 'out.tif'):
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
