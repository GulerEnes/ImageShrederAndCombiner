import cv2 as cv
import numpy as np
import os

pieces = os.listdir("./datas/")
num_pieces = len(pieces)

img = np.zeros(shape=[32940, 32940, 3], dtype=np.uint8)

i = 0
for piece in pieces:
	h = int(piece.split('h_')[1].split('_w_')[0]) * 3
	w = int(piece.split('_w_')[1].split('.tif')[0]) * 3

	p_img = cv.imread("./datas/" + piece)
	p_h, p_w, p_c = p_img.shape

	print(f"Processing piece_{i}/{num_pieces} ... h: {h}  w: {w}")

	img[h:h + p_h, w:w + p_w] = p_img[:, :]

	i += 1

cv.imwrite("combined.tif", img)
print("Done!")
