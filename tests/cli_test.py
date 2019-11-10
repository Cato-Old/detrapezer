from unittest import TestCase

from app.cli import CLI


class CLITest(TestCase):
    def setUp(self):
        self.cli = CLI()

    def test_can_parse_path_argument(self):
        args = [r'C:\foo\bar.baz']
        self.cli.parse(args)
        self.assertEqual(args[0], self.cli.args.path)

    def test_exit_app_when_no_path_argument(self):
        args = []
        with self.assertRaises(SystemExit):
            self.cli.parse(args)
