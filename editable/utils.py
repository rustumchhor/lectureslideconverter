import os
import img2pdf
import argparse
import tempfile
import datetime




def divide_list(full_list, n_way): 
    # looping till length list
    for i in range(0, len(full_list), n_way):
        yield full_list[i:i + n_way]


# print single images, return output directory
def pdf_to_single_jpeg(file_path, output_directory, lecture_name):
	images_from_path = convert_from_path(file_path, output_folder=output_directory)
	for i, image in enumerate(images_from_path):
	    fname = lecture_name+str(i)+'.jpeg'
	    image.save(fname, "JPEG")


def writeimages(num,x_offset,y_offset,paper):
	images = [cv2.resize(cv2.imread(file), (1920, 1080)) for file in natsorted(glob.glob("lectures/{}/*.jpg".format(num)))]
	subList = list(divide_list(images, 5))
	for i in range(len(subList)):
		im_v = cv2.vconcat(subList[i])
		overlayed = paper
		overlayed[y_offset:y_offset+im_v.shape[0], x_offset:x_offset+im_v.shape[1]] = im_v
		if not cv2.imwrite("concatenated_lectures/lec_{}_pt_{}.jpeg".format(num, i), overlayed):
			raise Exception("Could not write image")

# input: directory of single images
# loop through single images, print concat images
# return output dir
def single_jpeg_to_5_graph_overlayed(input_directory, lecture_name, output_directory, x_offset=0, y_offset=0, paper):
	images = [cv2.resize(cv2.imread(file), (1920, 1080)) for file in natsorted(glob.glob("{}/*.jpeg".format(input_directory)))]
	subList = list(divide_list(images, 5))
	for i, image in enumerate(subList):
		im_v = cv2.vconcat(subList[i])
		overlayed = paper
		overlayed[y_offset:y_offset+im_v.shape[0], x_offset:x_offset+im_v.shape[1]] = im_v
		fname = lecture_name+str(i)+'.jpeg'
		if not cv2.imwrite("{}/{}".format(output_directory, fname), overlayed):
			raise Exception("Could not write image")


# input: directory of concated images
# loop through concat images
# print concatenated in single pdf output
## note needed return: output file_path?
def write_pdf(input_directory, lecture_name):
	fname = lecture_name+'output'+'.pdf'
	with open(fname, "wb") as f:
		imgs = []
		for fname in os.listdir(input_directory):
			if not fname.endswith(".jpeg"):
				continue
			path = os.path.join(input_directory, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
			imgs = natsorted(imgs)
		f.write(img2pdf.convert(imgs))



def writepdf():
	# convert all files ending in .jpeg inside a directory
	dirname = "concatenated_lectures/"
	with open("2.pdf","wb") as f:
		imgs = []
		for fname in os.listdir(dirname):
			if not fname.endswith(".jpeg"):
				continue
			path = os.path.join(dirname, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
			imgs = natsorted(imgs)
		f.write(img2pdf.convert(imgs))




