import cv2
from numpy.core.multiarray import ndarray


class ImagePreparer:
    def __init__(self):
        self._image = None

    @property
    def image(self):
        if self._image is not None:
            return self._image
        else:
            raise ValueError('No image read in preparer')

    def prepare(self, path: str) -> ndarray:
        image = self._read_image(path)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        image = cv2.erode(image, kernel, iterations=150)
        image = cv2.dilate(image, kernel, iterations=150)
        return cv2.bitwise_not(image)

    def _read_image(self, path: str) -> ndarray:
        self._image = cv2.imread(path)
        return cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
