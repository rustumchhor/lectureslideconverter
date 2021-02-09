#goal:
#take powerpoint as input
#output the slides as images concatenated, overlayed on the notepaper

#handling errors:
# poerpoint not exportable
# images not concatenated
# graph paper not concatenated

#classes?
#for the file we need
# powerpoint file name
# path to the folder of pictures
# path to the folder of concatenated pictures
# 

#goal: allow the user to say how many slides get concatenated in one page
# math needed to figure out:
# we need to make sure that the size of the concatenated images is smaller than the vertical size of the paper image
# --so we can concatenate the paper image with itself until its large enough
# 

import glob
from natsort import natsorted, ns
import cv2
import os
import img2pdf
import argparse

# class directory():
# 	self

def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):
        yield l[i:i + n]

# cv2.resize(cv2.imread(file), (1920, 1080))

def main():
	# directory = params.get('dir')

	# num refers to lecture number
	def writeimages(folder, x_offset, y_offset, paper):
		images = [cv2.resize(cv2.imread(file), (1920, 1080)) for file in natsorted(glob.glob("lectures/{}/*.jpg".format(folder)))]
		subList = list(divide_chunks(images, 5))
		print('here')
		for i in range(len(subList)):
			im_v = cv2.vconcat(subList[i])
			overlayed = paper
			overlayed[y_offset:y_offset+im_v.shape[0], x_offset:x_offset+im_v.shape[1]] = im_v
			if not cv2.imwrite("concatenated_lectures/lec_{}_pt_{}.jpeg".format(folder, i), overlayed):
				raise Exception("Could not write image")

	def writepdf():
			# convert all files ending in .jpg inside a directory
		dirname = "concatenated_lectures/"
		with open("2.pdf", "wb") as f:
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


	graph = cv2.imread("graph1.png")
	graph_resized = cv2.resize(graph, (1815, 2754))
	graph_vert = cv2.vconcat([graph_resized,graph_resized])
	graph_hor = cv2.hconcat([graph_vert,graph_vert])

	x_offset=0
	y_offset=0

	writeimages("2_truth_ethics", x_offset, y_offset, graph_hor)

# if __name__ == "__main__":
# 	parser =  argparse.ArgumentParser(description = "tool name")
# 	# parser.add_argument('-dir', metavar = '-dir', type=str, help='')
# 	# params = vars(parser.parse_args())
# 	# print(params)
main()






# after the pictures are made, convert to pdfs and put them together


### WAYS TO MAKE THE LIST SPLITTER NOT PAD
# from itertools import islice, chain, repeat

# def chunk_pad(it, size, padval=None):
#     it = chain(iter(it), repeat(padval))
#     return iter(lambda: tuple(islice(it, size)), (padval,) * size)

# OR THIS WAY

# _no_padding = object()
# def chunk(it, size, padval=_no_padding):
#     if padval == _no_padding:
#         it = iter(it)
#         sentinel = ()
#     else:
#         it = chain(iter(it), repeat(padval))
#         sentinel = (padval,) * size
#     return iter(lambda: tuple(islice(it, size)), sentinel)





# have it accept arguments from command line
# name of slides folder should be sys.argv


# import argparse
# parser = argparse.ArgumentParser()

# #-db DATABSE -u USERNAME -p PASSWORD -size 20
# parser.add_argument("-db", "--hostname", help="Database name")
# parser.add_argument("-u", "--username", help="User name")
# parser.add_argument("-p", "--password", help="Password")
# parser.add_argument("-size", "--size", help="Size", type=int)

# args = parser.parse_args()

# print( "Hostname {} User {} Password {} size {} ".format(
#         args.hostname,
#         args.username,
#         args.password,
#         args.size
#         ))




# # convert all files ending in .jpg inside a directory
# dirname = "/path/to/images"
# with open("name.pdf","wb") as f:
# 	imgs = []
# 	for fname in os.listdir(dirname):
# 		if not fname.endswith(".jpg"):
# 			continue
# 		path = os.path.join(dirname, fname)
# 		if os.path.isdir(path):
# 			continue
# 		imgs.append(path)
# 	f.write(img2pdf.convert(imgs))