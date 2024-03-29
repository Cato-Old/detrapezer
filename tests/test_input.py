from unittest import TestCase

import cv2
from numpy.testing import assert_array_equal

from app.input import ImagePreparer


class ImagePreparerTest(TestCase):
    def setUp(self):
        self.preparer = ImagePreparer()

    def test_can_read_file(self):
        expected = cv2.imread(r'./resources/prepared.tif')
        self.preparer.prepare(r'./resources/prepared.tif')
        actual = self.preparer.image
        assert_array_equal(expected, actual)

    def test_raises_exception_when_no_image_set(self):
        with self.assertRaises(AttributeError):
            _ = self.preparer.image

    def test_raises_exception_when_no_scale_set(self):
        with self.assertRaises(AttributeError):
            _ = self.preparer.scale

    def test_can_prepare_image(self):
        expected = cv2.imread(r'./resources/prepared.tif', cv2.IMREAD_UNCHANGED)
        actual = self.preparer.prepare(r'./resources/specimen.tif')
        assert_array_equal(expected, actual)
