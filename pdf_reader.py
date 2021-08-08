# pdf reader reads content given in the given pdffile 
import pyttsx3
import PyPDF2
b = input("enter the book-name with .pdf extension: \n")
book = open(b, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
p = int(input("enter the page number: \n"))
page = pdfReader.getPage(p)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
