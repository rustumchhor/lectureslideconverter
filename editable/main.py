import os
import img2pdf
import argparse
import pathlib
import glob

from natsort import natsorted, ns
import cv2
import datetime
from utils import *

class input_file:
	inputRegistry = []
	def __init__(self, file_path):
		self.filePath = file_path
		self.lectureName = pathlib.Path(file_path).stem
		self.fileExt = pathlib.Path(file_path).suffix
		self.si_dirPath = ''
		self.con_dirPath = ''
		# input_file._inputRegistry.append(self)


def clear_directory(mydir, ext):
	filelist = glob.glob(os.path.join(mydir, "*.{}".format(ext)))
	for f in filelist:
		os.remove(f)


def main():
	new_input = input_file(params.get('f'))

	# now = datetime.datetime.now()
	# datetime.datetime.strftime(now, '%m/%d/%Y')

	new_input.si_dirPath = 'temp/single_images'
	pathlib.Path(new_input.si_dirPath).mkdir(parents=True, exist_ok=True)
	pdf_to_images(file_path=new_input.filePath, output_directory=new_input.si_dirPath, lecture_name=new_input.lectureName)

	graph = cv2.imread("templates/graph_paper/graph1.png")
	graph_resized = cv2.resize(graph, (1815, 2754))
	graph_vert = cv2.vconcat([graph_resized,graph_resized])
	graph_hor = cv2.hconcat([graph_vert,graph_vert])

	new_input.con_dirPath = 'temp/concat_images'
	pathlib.Path(new_input.con_dirPath).mkdir(parents=True, exist_ok=True)
	single_jpeg_to_5_graph_overlayed(input_directory=new_input.si_dirPath, lecture_name=new_input.lectureName, output_directory=new_input.con_dirPath, x_offset=0, y_offset=0, paper=graph_hor)

	write_pdf(input_directory=new_input.con_dirPath, lecture_name=new_input.lectureName)

	clear_directory(new_input.si_dirPath, 'jpg')
	clear_directory(new_input.con_dirPath, 'jpg')




if __name__ == "__main__":
	parser =  argparse.ArgumentParser(description = "tool name")
	parser.add_argument('-f', metavar = '-file', type=str, help='')
	params = vars(parser.parse_args())
	print(params)
	main()