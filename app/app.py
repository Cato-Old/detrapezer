from typing import List

import cv2

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

    def run(self) -> None:
        prepared_image = self.preparer.prepare(self.settings.path)
        if self.settings.debug_mode:
            cv2.imwrite('debug.tif', prepared_image)
        original_image = self.preparer.image
        scale = self.preparer.scale
        processed = self.processor.process(
            prepared_image, original_image, scale
        )
        cv2.imwrite(self.settings.output or 'out.tif', processed)


def compose(
        preparer: ImagePreparer,
        processor: ImageProcessor,
        settings: Settings,
) -> App:
    return App(
        preparer=preparer, processor=processor, settings=settings
    )
