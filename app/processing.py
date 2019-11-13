class ImageProcessor:
    pass

'''
cnts, hier = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
perimeter = cv2.arcLength(cnts[0], True)
approx = cv2.approxPolyDP(cnts[0], 0.1 * perimeter, True)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
src = []
for point in approx:
    ((x, y),) = point
    src.append([x, y])
    cv2.circle(image, (x, y), 5, (0, 255, 0), 30)

src = np.array(src, dtype="float32")
x1, y1, x2, y2 = cv2.boundingRect(approx)
cv2.rectangle(image, (x1, y1), (x2 + x1, y2 + y1), (0, 0, 255), 3)
dst = np.array([[x1, y1], [x1, y1 + y2], [x1 + x2, y1 + y2], [x1 + x2, y1]],
               dtype='float32')
print(src)
M = cv2.getPerspectiveTransform(src, dst)
image = cv2.warpPerspective(image_r, M, (image.shape[1], image.shape[0]))
cv2.imwrite('a.tif', image)
'''
