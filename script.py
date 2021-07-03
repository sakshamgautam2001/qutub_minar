
from converter import convert_pdf_to_txt
import re

#converting downloaded pdf to text
delhi_pdf = convert_pdf_to_txt('Delhi.pdf')

#Preprocessing the text
delhi_pdf = delhi_pdf.replace('\n', ' ')
delhi_pdf = delhi_pdf.replace('\x0c', ' ')
delhi_pdf = delhi_pdf.replace('\x00', ' ')
delhi_pdf = re.sub('[^a-zA-Z1-9]', ' ', delhi_pdf)
delhi_pdf = " ".join(delhi_pdf.replace(u"\xa0", " ").strip().split())
delhi_pdf = delhi_pdf.lower()

#Making array of filtered words
pdf_arr = delhi_pdf.split(' ')
count = 0
l = len(pdf_arr)

#Counting number
for i in range(0, l-1):
    if(pdf_arr[i] == 'qutub' and pdf_arr[i+1] == 'minar'):
        count = count + 1
        
print(count)
    

