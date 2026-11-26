# ===== IMPORTING MODULES =====
#import tkinter
from tkinter import *
import random #import random module
from PIL import ImageTk, Image #import PIL for images
#import messagebox
import tkinter.messagebox
from tkinter import messagebox

root = Tk()
root.geometry("550x450")
root.title("Alexa Tell me a Joke")
root.config(bg="#c0c0c0")
root.iconbitmap('./02-AlexaTellMeAJoke/icon2.ico') #icon for window

#empty lists
setup = []
punchline = []

#function to load the jokes from the text file
def jokes():
    with open("./02-AlexaTellMeAJoke/randomJokes.txt","r") as file:
        for line in file:
            sentence = line.split('?') #retrieve each line and split it using the question mark sign

            #append the data values into the list
            setup.append(sentence[0].strip() + "?") #.strip() is added to remove unnecessary spaces. The + "?" part is to add a question mark in the end of the sentence
            punchline.append(sentence[1].strip()) 

jokes() #calls the function to read the text file

#typing effect for setup_label
def typingEffect(text, index=0):
    if index<len(text): #checks if there is any characters left to be displayed
        current_text = text[:index+3] #displays up to 3 characters
        setup_label.config(text=current_text) #configurate the label
        
        #wait 80ms before displaying the next 3 characters
        root.after(80, typingEffect, text, index+3)

index = 0
#function to tell the joke, display the setup
def tell_joke():
    global index
    #randomly generate an integer number
    index = random.randint(0, len(setup) -1) #List indexing, -1 is included since Python starts from 0

    #display the setup of the joke
    setup_label.config(text="")
    typingEffect(setup[index]) 
    punchline_label.config(text="") #clears the previous punchline displayed

#function to close the window
def quit():
    choice = messagebox.askyesno("Quit", "Are you sure you want to close the window?")
    if choice==True: #if user clicks yes, the window closes
        root.destroy()

#displays the punchline for the joke
def show_punchline():
    global index
    punchline_label.config(text=punchline[index]) #punchline displays based on the current index number

def next_joke():
    tell_joke() #calls the tell_joke function

def alexa_tellAJoke():
    tell_joke() #calls the joke function
    button1.destroy() #deletes the button, user will only be able to click this button once


#image set as a background
img = Image.open("02-AlexaTellMeAJoke/bg.png")
resized_img = img.resize((550,450))
bg_img = ImageTk.PhotoImage(resized_img)
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0)

#title displayed using label
title = Label(root,text="ALEXA'S JOKES", font=("Courier",24,"bold"), bg="#ece4d9", fg="black")
title.pack(pady=(60,0))

frame = Frame(root, bg="#424242", width=700, height=150)
frame.pack(pady=30)

#label to display the joke setup
setup_label = Label(root, text = (""), font=("Roboto", 13, "bold"), bg="#424242", fg="white")
setup_label.place(relx=0.5, y=190, anchor="center") #relx positions the label at 50% point of the entire window's width

#label to display the joke punchline
punchline_label = Label(root, text = (""), font=("Roboto", 11), bg="#424242", fg="white")
punchline_label.place(relx=0.5, y=225, anchor="center")


# ===== BUTTONS =====
#button to tell a random joke at the start 
button1 = Button(root, text="Alexa tell me a Joke", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, cursor = "hand2", command=alexa_tellAJoke) #padding inside the button
button1.pack(side="top",fill=X, padx=20) 

#button to show the punchline
button2 = Button(root, text="Show Punchline", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, width=25, cursor = "hand2", command=show_punchline) #cursor hand 2 will switch the cursor to the pointing one
button2.pack(side="left", padx=(20,15)) 

#button to display the next joke
button3 = Button(root, text="Next Joke", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, width=25, cursor = "hand2", command=next_joke) 
button3.pack(side="left", padx=(15,20))

#button to close the application
close_button = Button(root, text="X", font=("Arial", 12), bg="#545454", fg="white", padx=3, pady=1, cursor = "hand2", command=quit) 
close_button.place(x=500, y=10)

root.mainloop()