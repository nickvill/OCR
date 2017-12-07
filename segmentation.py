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
		current = [0,0]
		for row_ind in range(len(img)):
			# When looking at a row with no text
			if min(thresh_img[row_ind]) == 255:
				# If in a block of text, add that line and reset current
				if text:
					lines.append(current)
					current = [row_ind, row_ind]
					text = False
					white_space = True
				else:
					current[1] = row_ind
			# When looking at a row with text
			else:
				if white_space:
					space.append(current)
					current = [row_ind, row_ind]
					white_space = False
					text = True
				else:
					current[1] = row_ind
		return lines

	def segment_char(self, line):
		# Split the line into characters
		# Takes an image segment as input
		# returns an array of x start and stop indices
		char = False
		white_space = True
		chars = []
		space = []
		current = [0,0]
		for column_ind in range(len(line[0])):
			# When looking at a column with no ink
			column = line[0:len(line), column_ind:(column_ind+1)]
			if min(column.flatten()) == 255:
				# If in a block of text, add that line and reset current
				if char:
					chars.append(current)
					current = [column_ind, column_ind]
					char = False
					white_space = True
				else:
					current[1] = column_ind
			# When looking at a column with text
			else:
				if white_space:
					space.append(current)
					if current[1]-current[0] >= 30:
						chars.append(current)
					current = [column_ind, column_ind]
					white_space = False
					char = True
				else:
					current[1] = column_ind
		return chars

	def process_chars(line, chars):
		img_chars = []
		for char in chars:
			char_crop_im = line_crop_im[0:len(line_crop_im), char_crop[0]:char_crop[1]]


if __name__=="__main__":
	seg = Segmentation()
	thresh = seg.threshold(img)
	cv2.imshow('thresh', thresh)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	lines = seg.segment_line(thresh)
	line_crop = lines[0]
	line_crop_im = img[line_crop[0]:line_crop[1], 0:len(img[0])]
	cv2.imshow('line', line_crop_im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	chars = seg.segment_char(line_crop_im)
	for char in range(len(chars)):
		char_crop = chars[char]
		char_crop_im = line_crop_im[0:len(line_crop_im), char_crop[0]:char_crop[1]]
		cv2.imshow('char', char_crop_im)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

