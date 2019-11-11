from unittest import TestCase

import cv2
import numpy as np

from app.input import ImagePreparer


class ImagePreparerTest(TestCase):
    def setUp(self):
        self.preparer = ImagePreparer()

    def test_can_read_file(self):
        expected = cv2.imread(r'./resources/prepared.tif')
        self.preparer.prepare(r'./resources/prepared.tif')
        actual = self.preparer.image
        self.assertTrue(np.array_equal(expected, actual))

    def test_raises_exception_when_no_set_image(self):
        with self.assertRaises(ValueError):
            _ = self.preparer.image

    def test_can_prepare_image(self):
        expected = cv2.imread(r'./resources/prepared.tif', cv2.IMREAD_UNCHANGED)
        actual = self.preparer.prepare(r'./resources/specimen.tif')
        self.assertTrue(np.array_equal(expected, actual))
