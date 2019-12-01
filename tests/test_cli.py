from unittest import TestCase

from app.cli import CLI


class CLITest(TestCase):
    def setUp(self):
        self.cli = CLI()

    def test_can_parse_path_argument(self):
        args = [r'C:\foo\bar.baz']
        actual = self.cli.parse(args)
        self.assertEqual(args[0], actual.path)

    def test_can_parse_output_argument(self):
        args = [r'C:\foo\bar.baz', '', r'C:\bar\baz.foo']
        for flag in ('-o', '--output'):
            with self.subTest(flag):
                args[1] = flag
                actual = self.cli.parse(args)
                self.assertEqual(args[2], actual.output)

    def test_can_parse_debug_flag(self):
        args = [r'C:\foo\bar.bas', '']
        for flag in ['-d', '--debug']:
            with self.subTest(flag):
                args[1] = flag
                actual = self.cli.parse(args)
                self.assertIsInstance(actual.debug, bool)
                self.assertTrue(actual.debug)

    def test_can_set_debug_flag_false_when_no_arg(self):
        args = [r'C:\foo\bar.bas']
        actual = self.cli.parse(args)
        self.assertFalse(actual.debug)

    def test_exit_app_when_no_path_argument(self):
        args = []
        with self.assertRaises(SystemExit):
            self.cli.parse(args)
