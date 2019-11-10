from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor


class App:
    def __init__(
            self,
            cli: CLI,
            preparer: ImagePreparer,
            processor: ImageProcessor,
    ) -> None:
        self.cli = cli
        self.preparer = preparer
        self.processor = processor


def compose(
        cli: CLI,
        preparer: ImagePreparer,
        processor: ImageProcessor,
) -> App:
    return App(cli=cli, preparer=preparer, processor=processor)
