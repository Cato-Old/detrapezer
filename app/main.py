import sys

from app.settings import Settings

from app.app import compose
from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor


def main():
    parsed = CLI().parse(sys.argv[1:])
    settings = Settings(
        debug_mode=parsed.debug, path=parsed.path, output=parsed.output,
    )
    app = compose(
        preparer=ImagePreparer(),
        processor=ImageProcessor(),
        settings=settings,
    )
    app.run()
