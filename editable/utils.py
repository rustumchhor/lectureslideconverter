import os
import img2pdf
import pdf2image
import tempfile
import datetime
import pathlib
import glob

from natsort import natsorted, ns
import cv2
import datetime
from utils import *

def divide_list(lst, n_way): 
    # looping till length list
    for i in range(0, len(lst), n_way):
        yield lst[i:i + n_way]


# print single images, return output directory
def pdf_to_images(file_path, output_directory, lecture_name):
	images_from_path = pdf2image.convert_from_path(file_path, output_folder=output_directory, fmt='jpeg', output_file=lecture_name)
	# for i, image in enumerate(images_from_path):
	#     fname = lecture_name+str(i)+'.jpg'
	#     image.save(fname)


# input: directory of single images
# loop through single images, print concat images
# return output dir
def single_jpeg_to_5_graph_overlayed(input_directory, lecture_name, output_directory, paper, x_offset=0, y_offset=0):
	images = [cv2.resize(cv2.imread(file), (1920, 1080)) for file in natsorted(glob.glob("{}/*.jpg".format(input_directory)))]
	print(input_directory,len(images))
	subList = list(divide_list(images, 5))
	for i, image in enumerate(subList):
		im_v = cv2.vconcat(subList[i])
		overlayed = paper
		overlayed[y_offset:y_offset+im_v.shape[0], x_offset:x_offset+im_v.shape[1]] = im_v
		fname = lecture_name+str(i)+'.jpg'
		if not cv2.imwrite("{}/{}".format(output_directory, fname), overlayed):
			raise Exception("Could not write image")


# input: directory of concated images
# loop through concat images
# print concatenated in single pdf output
## not needed return: output file_path?
def write_pdf(input_directory, lecture_name):
	fname = lecture_name+'_'+'output'+'.pdf'
	with open(fname, "wb") as f:
		imgs = []
		for fname in os.listdir(input_directory):
			print(fname)
			if not fname.endswith(".jpg"):
				continue
			path = os.path.join(input_directory, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
			imgs = natsorted(imgs)
		f.write(img2pdf.convert(imgs))
