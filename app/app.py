from typing import List

import cv2

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

    def run(self, args: List[str]) -> None:
        self.cli.parse(args)
        prepared_image = self.preparer.prepare(self.cli.args.path)
        original_image = self.preparer.image
        scale = self.preparer.scale
        processed = self.processor.process(
            prepared_image, original_image, scale
        )
        cv2.imwrite(self.cli.args.output or 'out.tif', processed)


def compose(
        cli: CLI,
        preparer: ImagePreparer,
        processor: ImageProcessor,
) -> App:
    return App(cli=cli, preparer=preparer, processor=processor)
