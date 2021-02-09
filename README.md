# lectureslideconverter
Script to overlay pdfs and powerpoints of lecture slides into a concatenated strip on top of notebook paper for notes on iPad

Will need to install:
poppler: brew install poppler
pdf2image: pip install pdf2image
img2pdf: pip install img2pdf
cv2: pip install opencv
natsort: pip install natsort

How to run this:
python main.py -f <path_to_lecture_pdf_file>

Example:
python main.py -f /Users/rustum/Desktop/6_LM_1.pdf

Output:
6_LM_1_output.pdf
