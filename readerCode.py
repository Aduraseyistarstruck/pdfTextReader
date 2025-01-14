import pyttsx3
speaker = pyttsx3.init()

intromess1 = "Welcome!!! This is my current speaking speed. Do you want to modify it?\n"
print(intromess1)
speaker.say(intromess1)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 80)

#voices
voices = speaker.getProperty('voices')
#print(voices)
speaker.setProperty('voice', voices[1].id)
#pdf below
from PyPDF2 import PdfReader
book = PdfReader(r'C:\Users\USER\Desktop\The_Purpose_Driven_Life.pdf')
totalpages = len(book.pages)

#without runAndWait() the string will not be read. ensure you always add it.

#volume
volume = speaker.getProperty('volume')
#print(volume)

print('Now I am going to read your pdf file master.')
speaker.say('Now I am going to read your pdf file master.')
speaker.runAndWait()

for i in range(totalpages):
    readpage = book.pages[i]
    text =  readpage.extract_text()
    speaker.say(text )
    print( text)
    speaker.runAndWait()

    speaker.say('do you want to move to the next page:')
    speaker.runAndWait()
    ask = input('do you want to move to the next page:'.upper())
    
    if ask.lower() == 'no':
        quit()
