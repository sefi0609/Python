'''
Finding a pattern in a pdf file - using 'Find_the_Phone_Number.pdf' file
'''
#importing models
import PyPDF2,re
#can change this pattern to anything
pattern = r'\d{3}\D\d{3}\D\d{4}'
#opening a pdf file - using read Binary for pdfs
f = open('Find_the_Phone_Number.pdf','rb')
#enmpty list for all phone numbers
all_phones = []
#creating a PyPDF2 object 
pdf = PyPDF2.PdfFileReader(f)
#searching for pattern in all pages
for num in range(pdf.numPages):
    page = pdf.getPage(num)
    temp = page.extractText()
    phone = re.findall(pattern,temp)
    if phone != []:
        all_phones.extend(phone)
#printing the numbers
print(all_phones)