import sys

from app.app import compose
from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor


def main():
    app = compose(
        cli=CLI(),
        preparer=ImagePreparer(),
        processor=ImageProcessor()
    )
    app.run(sys.argv[1:])
