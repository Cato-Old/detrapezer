from unittest import TestCase

import cv2
from numpy.testing import assert_array_equal

from app.processing import ImageProcessor


class ImageProcessorTest(TestCase):
    def setUp(self):
        self.processor = ImageProcessor()

    def test_can_process_image(self):
        image = cv2.imread('./resources/prepared.tif', cv2.IMREAD_UNCHANGED)
        original = cv2.imread('./resources/specimen.tif', cv2.IMREAD_UNCHANGED)
        actual = self.processor.process(image, original)
        expected = cv2.imread('./resources/processed.tif', cv2.IMREAD_UNCHANGED)
        assert_array_equal(expected, actual)


