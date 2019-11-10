from app.cli import CLI
from app.input import ImagePreparer


class App:
    def __init__(self, cli: CLI, preparer: ImagePreparer) -> None:
        self.cli = cli
        self.preparer = preparer


def compose(cli: CLI, preparer: ImagePreparer) -> App:
    return App(cli=cli, preparer=preparer)
