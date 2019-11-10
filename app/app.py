from app.cli import CLI


class App:
    def __init__(self, cli: CLI) -> None:
        self.cli = cli


def compose(cli: CLI) -> App:
    return App(cli=cli)
