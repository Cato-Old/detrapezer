from typing import List

import cv2

from app.cli import CLI
from app.input import ImagePreparer
from app.processing import ImageProcessor
from app.settings import Settings


class App:
    def __init__(
            self,
            preparer: ImagePreparer,
            processor: ImageProcessor,
            settings: Settings,
    ) -> None:
        self.preparer = preparer
        self.processor = processor
        self.settings = settings

    def run(self, args: List[str]) -> None:
        self.cli = CLI()
        self.cli.parse(args)
        self.settings.debug_mode = self.cli.args.debug
        prepared_image = self.preparer.prepare(self.cli.args.path)
        if self.settings.debug_mode:
            cv2.imwrite('debug.tif', prepared_image)
        original_image = self.preparer.image
        scale = self.preparer.scale
        processed = self.processor.process(
            prepared_image, original_image, scale
        )
        cv2.imwrite(self.cli.args.output or 'out.tif', processed)


def compose(
        preparer: ImagePreparer,
        processor: ImageProcessor,
        settings: Settings,
) -> App:
    return App(
        preparer=preparer, processor=processor, settings=settings
    )
