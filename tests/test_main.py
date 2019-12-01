from unittest import TestCase
from unittest.mock import patch, Mock

from app.main import main
from app.settings import Settings


class MainEntryPointTest(TestCase):
    def setUp(self):
        self.settings_patcher = patch(
            'app.main.Settings',
            return_value=Settings(path=r'./resources/specimen.tif'),
        )
        self.app_mock = Mock()
        compose_patcher = patch('app.main.compose', return_value=self.app_mock)
        compose_patcher.start()
        self.addCleanup(Settings.clear)
        self.addCleanup(compose_patcher.stop)

    def test_app_is_closed_when_no_required_args_provided(self):
        with self.assertRaises(SystemExit):
            main()

    def test_app_is_running_when_required_args_provided(self):
        with patch('sys.argv', ['_', r'./resources/specimen.tif']):
            main()
        self.app_mock.run.assert_called_once()

    def test_settings_are_initiated_when_app_running(self):
        mock = self.settings_patcher.start()
        with patch('sys.argv', ['_', r'./resources/specimen.tif']):
            main()
        self.settings_patcher.stop()
        mock.assert_called_once_with(
            debug_mode=False, output=None, path='./resources/specimen.tif',
        )
