# lectureslideconverter
Script to overlay pdfs and powerpoints of lecture slides into a concatenated strip on top of notebook paper for notes on iPad

Will need to install:
1. poppler: brew install poppler
2. pdf2image: pip install pdf2image
3. img2pdf: pip install img2pdf
4. cv2: pip install opencv
5. natsort: pip install natsort

How to run this:
python main.py -f <path_to_lecture_pdf_file> -o <path_to_output_directory>
The -o flag is optional, if the -o flag is not used, the default output directory is where the main.py file is located

Example:
1. python main.py -f /Users/rustum/Desktop/6_LM_1.pdf
a. This will output the pdf to the directory where the python file is located

2. python3 main.py -f /Users/rustum/Downloads/10_pos.pdf -o /Users/rustum/Desktop/INFO\ 159
a. This will output the pdf under the directory I specified (/Users/rustum/Desktop/INFO\ 159)

Output:
6_LM_1_output.pdf
