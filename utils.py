import os
import pathlib
import glob
from natsort import natsorted, ns
import img2pdf
import pdf2image
import cv2
# import tempfile

def divide_list(lst, n_way): 
    # looping till length list
    for i in range(0, len(lst), n_way):
        yield lst[i:i + n_way]


# print single images, jpeg defaults to jpg
def pdf_to_images(file_path, output_directory, lecture_name):
	images_from_path = pdf2image.convert_from_path(file_path, output_folder=output_directory, fmt='jpeg', output_file=lecture_name)


# input: directory of single images
# loop through list of single images, split them into groups of 5, concatenate the groups vertically, save them ontop of graph paper image
def single_jpeg_to_5_graph_overlayed(input_directory, lecture_name, output_directory, paper, x_offset=0, y_offset=0):
	images = [cv2.resize(cv2.imread(file), (1920, 1080)) for file in natsorted(glob.glob("{}/*.jpg".format(input_directory)))]
	subList = list(divide_list(images, 5))
	for i, image in enumerate(subList):
		im_v = cv2.vconcat(subList[i])
		overlayed = paper
		overlayed[y_offset:y_offset+im_v.shape[0], x_offset:x_offset+im_v.shape[1]] = im_v
		fname = lecture_name+str(i)+'.jpg'
		if not cv2.imwrite("{}/{}".format(output_directory, fname), overlayed):
			raise Exception("Could not write image")


# input: directory of concated images
# list all images in concatenated image directory
# sort them using natural sort
# loop through concated images
# print concatenated in single pdf output
def write_pdf(input_directory, lecture_name, output_directory):
	fname = lecture_name+'_'+'output'+'.pdf'
	with open( os.path.join(output_directory,fname), "wb") as f:
		imgs = []
		for fname in os.listdir(input_directory):
			if not fname.endswith(".jpg"):
				continue
			path = os.path.join(input_directory, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
			imgs = natsorted(imgs)
		f.write(img2pdf.convert(imgs))
