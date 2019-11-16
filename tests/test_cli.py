from unittest import TestCase

from app.cli import CLI


class CLITest(TestCase):
    def setUp(self):
        self.cli = CLI()

    def test_can_parse_path_argument(self):
        args = [r'C:\foo\bar.baz']
        self.cli.parse(args)
        self.assertEqual(args[0], self.cli.args.path)

    def test_can_parse_output_argument(self):
        args = [r'C:\foo\bar.baz', '', r'C:\bar\baz.foo']
        for flag in ('-o', '--output'):
            with self.subTest(flag):
                args[1] = flag
                self.cli.parse(args)
                self.assertEqual(args[2], self.cli.args.output)

    def test_exit_app_when_no_path_argument(self):
        args = []
        with self.assertRaises(SystemExit):
            self.cli.parse(args)
