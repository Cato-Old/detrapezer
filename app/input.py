import cv2
from numpy.core.multiarray import ndarray


class ImagePreparer:
    @property
    def image(self):
        return self._image

    @property
    def scale(self):
        return self._scale

    def prepare(self, path: str) -> ndarray:
        image = self._read_image(path)
        image = self._rescale_image(image)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        image = cv2.erode(image, kernel, iterations=25)
        image = cv2.dilate(image, kernel, iterations=25)
        return cv2.bitwise_not(image)

    def _read_image(self, path: str) -> ndarray:
        self._image = cv2.imread(path)
        return cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)

    def _rescale_image(self, image: ndarray) -> ndarray:
        if image.shape[1] > 800:
            height, width = image.shape
            self._scale = 800 / width
            dim = (round(width * self._scale), round(height * self._scale))
            image = cv2.resize(image, dim)
        else:
            self._scale = 1.0
        return image
