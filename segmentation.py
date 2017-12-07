import cv2 

im = '/home/racecar/OCR/HelloWorld.png'
img = cv2.imread(im, 0)

# white = 0
# black = 0
# print len(img)
# for i in img:
# 	if white == 0:
# 		print len(i)
# 	for j in i:
# 		if j == 255:
# 			white += 1
# 		elif j == 0:
# 			black += 1

# print white
# print black

cv2.imshow('test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

class Segmentation:

	# def __init__(self):

	def threshold(self, cv_img):
		# Threshold the to be either black or white
		# Could be improved w/ adaptive thresh
		ret, thresh = cv2.threshold(img, 255./2, 255, cv2.THRESH_BINARY)
		return thresh

	def segment_line(self, thresh_img):
		# Split the image into lines of text
		text = False
		white_space = True
		lines = []
		space = []
		current = []
		for row in thresh_img:
			# When looking at a row with no text
			if min(row) == 255:
				# If in a block of text, add that line and reset current
				if text:
					lines.append(current)
					current = []
					current.append(row)
					text = False
					white_space = True
				else:
					current.append(row)
			# When looking at a row with text
			else:
				if white_space:
					space.append(current)
					current = []
					current.append(row)
					white_space = False
					text = True
				else:
					current.append(row)
		return lines


if __name__=="__main__":
	seg = Segmentation()
	thresh = seg.threshold(img)
	print type(img), 'image type'
	cv2.imshow('thresh', thresh)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	lines = seg.segment_line(thresh)
	print lines
	cv2.imshow('line', lines)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

