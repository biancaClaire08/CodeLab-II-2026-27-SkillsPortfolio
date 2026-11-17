#import tkinter
from tkinter import *
import random #import random module

root = Tk()
root.geometry("600x450")
root.title("Alexa Tell me a Joke")
root.config(bg="#c0c0c0")

#empty lists
setup = []
punchline = []

#function to load the jokes from the text file
def jokes():
    with open("randomJokes.txt","r") as file:
        for line in file:
            sentence = line.split('?') #retrieve each line and split it using the question mark sign

            #append the data values into the list
            setup.append(sentence[0].strip() + "?") #.strip() is added to remove unnecessary spaces. The + "?" part is to add a question mark in the end of the sentence
            punchline.append(sentence[1].strip()) 


index = 0
#function to tell the joke, display the setup
def tell_joke():
    global index
    #randomly generate an integer number
    index = random.randint(0, len(setup) -1) #List indexing, -1 is included since Python starts from 0

    #display the setup of the joke
    setup_label.config(text=setup[index]) 

setup_label = Label(root, text = "")
punchline_label = Label(root, text="")



root.mainloop()