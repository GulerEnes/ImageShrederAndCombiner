import cv2 as cv

img = cv.imread("./T36SVH_20210918T083619_TCI_10m.tif")

height, width, channel = img.shape  # (10980, 10980, 3)

print("img.shape: ", img.shape)

h = 0
w = 0
i = 0

while h < height:
	while w < width:
		piece = img[h:h + min(1000, height - h), w: w + min(1000, width - w)]
		piece_name = f"piece_{i}_h_{h}_w_{w}.tif"
		cv.imwrite(piece_name, piece)

		w += 1000
		i += 1
		print(f"piece {i} is written... h: {h}   w: {w}")
	h += 1000
	w = 0

print("Done...")
