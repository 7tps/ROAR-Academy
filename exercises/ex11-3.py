import PyPDF2
import os
import string

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(path, 'exercises', 'Sense-and-Sensibility-by-Jane-Austen.pdf')
file_handle = open(filename, 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 

for x in range(page_number):

    page_object = pdfReader.pages[x]    # We just get page 0 as example 
    page_text = page_object.extract_text()   # this is the str type of full page
    page_text = page_text.translate(str.maketrans('', '', string.punctuation))
    page_text = page_text.split('\n')
    page_text = page_text[2:]

    page_text = [line for line in page_text if 'CHAPTER' not in line]

    print(page_text)