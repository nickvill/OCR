import cv2
import numpy as np
import os

class Create_Dataset():

	def __init__(self):
		self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
		                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		                'a','b','c','d','e','f','g','h','i','j','k','l','m',
		                'n','o','p','q','r','s','t','u','v','w','x','y','z']
		self.fonts = [cv2.FONT_HERSHEY_SIMPLEX,
		              cv2.FONT_HERSHEY_PLAIN,
		              cv2.FONT_HERSHEY_DUPLEX,
		              cv2.FONT_HERSHEY_COMPLEX,
		              cv2.FONT_HERSHEY_TRIPLEX,
		              cv2.FONT_HERSHEY_COMPLEX_SMALL,
		              cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
		              cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
		              cv2.FONT_ITALIC]
		self.thicknesses = [1,2,3]
		self.scales = np.array(range(10,21,1))/10.
		self.dir = os.path.dirname(os.path.abspath(__file__))

	def create_folders(self):
		for letter in self.letters:
			os.system('mkdir {}'.format(letter))

	def create_data(self):
		for letter in self.letters:
			for font in self.fonts:
				for fontscale in self.scales:
					for thickness in self.thicknesses:
						letter_img = self.create_letter(letter, font, fontscale, thickness)
						img_name = '{}{}{}{}.png'.format(letter, font, fontscale, thickness)
						save_to = os.path.join(self.dir+'/{}'.format(letter), img_name)
						cv2.imwrite(save_to, letter_img)

	def create_letter(self, letter, font, fontscale, thickness):
		blank_image = np.zeros((50, 50, 1), np.uint8)
		blank_image.fill(255) 
		txtsize = cv2.getTextSize(letter, font, fontscale, thickness)[0]
		botleft = ((blank_image.shape[0]-txtsize[1])/2, (blank_image.shape[1]+txtsize[0])/2)
		letter = cv2.putText(blank_image, letter, botleft, font, fontscale, (0,0,0), thickness)
		return letter

if __name__=="__main__":
	cd = Create_Dataset()
	cd.create_folders()
	cd.create_data()


