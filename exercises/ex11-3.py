import PyPDF2
import os
import string

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(path, 'exercises', 'Sense-and-Sensibility-by-Jane-Austen.pdf')
file_handle = open(filename, 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 

frequency_table = dict()

for x in range(page_number):

    page_object = pdfReader.pages[x]    # We just get page 0 as example 
    page_text = page_object.extract_text()   # this is the str type of full page
    page_text = page_text.translate(str.maketrans('', '', string.punctuation))
    page_text = page_text.split('\n')
    page_text = page_text[2:]

    word_list = [line.split() for line in page_text if 'CHAPTER' not in line and not any(char.isdigit() for char in line)]

    for sublist in word_list:
        for word in sublist:
            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1

print(frequency_table)