import math

import cv2
import numpy as np
from numpy.core.multiarray import ndarray


class ImageProcessor:
    def process(self, prepared_image: ndarray, original_image: ndarray):
        contours, _ = cv2.findContours(
            prepared_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,
        )
        image = self._blank_image(prepared_image)
        cv2.drawContours(image, contours, 0, 125, 5)
        image = cv2.bitwise_not(image)

        lines = cv2.HoughLines(image, 1, np.pi / 90, 400)
        image = self._blank_image(image)
        image = self._draw_hough_lines(image, lines)
        corners = cv2.goodFeaturesToTrack(image, 4, 0.1, 100)
        src = self._sort_corners(corners)
        x1, y1, x2, y2 = cv2.boundingRect(src)
        dst = np.array(
            [[x1, y1], [x1, y1 + y2], [x1 + x2, y1 + y2], [x1 + x2, y1]],
            dtype='float32')
        matrix = cv2.getPerspectiveTransform(src, dst)
        image = cv2.warpPerspective(original_image, matrix,
                                    (image.shape[1], image.shape[0]))
        return image

    @staticmethod
    def _blank_image(image: ndarray) -> ndarray:
        image = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
        image.fill(255)
        return image

    @staticmethod
    def _draw_hough_lines(image: ndarray, lines: ndarray) -> ndarray:
        for ((rho, theta),) in lines:
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(round(x0 - 1200 * b))
            y1 = int(round(y0 + 1200 * a))
            x2 = int(round(x0 + 1200 * b))
            y2 = int(round(y0 - 1200 * a))
            cv2.line(image, (x1, y1), (x2, y2), 60, 5)
        return image

    @staticmethod
    def _sort_corners(corners: ndarray) -> ndarray:
        x_sorted = corners[np.argsort(corners[:, 0][:, 0])]
        left = x_sorted[:2]
        right = x_sorted[2:]
        return np.concatenate((
                left[np.argsort(left[:, 0][:, 1])],
                right[np.argsort(right[:, 0][:, 1])[::-1]]
            ))
