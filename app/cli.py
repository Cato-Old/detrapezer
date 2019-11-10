from argparse import ArgumentParser
from typing import List


class CLI:
    def __init__(self) -> None:
        self.parser = ArgumentParser()
        self.parser.add_argument('path')
        self.args = None

    def parse(self, args: List[str]) -> None:
        parsed = self.parser.parse_args(args)
        self.args = parsed
