#import tkinter
from tkinter import *
import random #import random module

root = Tk()
root.geometry("550x450")
root.title("Alexa Tell me a Joke")
root.config(bg="#c0c0c0")
root.iconbitmap('./02-AlexaTellMeAJoke/icon2.ico')

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

index = 0
#function to tell the joke, display the setup
def tell_joke():
    global index
    #randomly generate an integer number
    index = random.randint(0, len(setup) -1) #List indexing, -1 is included since Python starts from 0

    #display the setup of the joke
    setup_label.config(text=setup[index])
    punchline_label.config(text="") #clears the previous punchline displayed

#function to close the window
def quit():
    root.destroy()

#displays the punchline for the joke
def show_punchline():
    global index
    punchline_label.config(text=punchline[index])

def next_joke():
    tell_joke() #calls the tell_joke function

#title displayed using label
title = Label(root,text="ALEXA'S JOKES", font=("Courier",24,"bold"), bg="#c0c0c0", fg="black")
title.pack(pady=(60,0))

#frame
frame = Frame(root, bg="#526B5D", width=700, height=150)
frame.pack(pady=30)


#label to display the joke setup
setup_label = Label(root, text = (""), font=("Roboto", 13, "bold"), bg="#526B5D", fg="black")
setup_label.place(relx=0.5, y=190, anchor="center") #relx positions the label at 50% point of the entire window's width

#label to display the joke punchline
punchline_label = Label(root, text = (""), font=("Roboto", 11), bg="#526B5D", fg="black")
punchline_label.place(relx=0.5, y=225, anchor="center")


# ===== BUTTONS =====
#button to tell a random joke 
button1 = Button(root, text="Alexa tell me a Joke", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, cursor = "hand2", command=tell_joke) #padding inside the button
button1.pack(side="left", padx=(65,10)) #placed on the left side

#button to show the punchline
button2 = Button(root, text="Show Punchline", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, cursor = "hand2", command=show_punchline) #cursor hand 2 will switch the cursor to the pointing one
button2.pack(side="left", padx=10) 

#button to display the next joke
button3 = Button(root, text="Next Joke", font=("Arial", 12), bg="#545454", fg="white", padx=5, pady=8, cursor = "hand2", command=next_joke) 
button3.pack(side="left", padx=10)

#button to close the application
close_button = Button(root, text="X", font=("Arial", 12), bg="#545454", fg="white", padx=3, pady=1, cursor = "hand2", command=quit) 
close_button.place(x=500, y=10)

root.mainloop()