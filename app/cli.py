from argparse import ArgumentParser, Namespace
from typing import List


class CLI:
    def __init__(self) -> None:
        self.parser = ArgumentParser()
        self.parser.add_argument('path')
        self.parser.add_argument('-o', '--output')
        self.parser.add_argument('-d', '--debug', action='store_true')

    def parse(self, args: List[str]) -> Namespace:
        return self.parser.parse_args(args)
