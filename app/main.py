import sys

from app.settings import Settings

from app.app import compose
from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor


def main():
    app = compose(
        cli=CLI(),
        preparer=ImagePreparer(),
        processor=ImageProcessor(),
        settings=Settings(),
    )
    app.run(sys.argv[1:])
