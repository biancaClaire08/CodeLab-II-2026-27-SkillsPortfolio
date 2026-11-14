#import the modules needed
from tkinter import *
from PIL import ImageTk, Image

import random #import random module

root = Tk()
#create an instance of tkinter window
root.geometry("400x400")
root.title("Arithmetic Quiz")
root.config(bg="#1b2645") #sets the background color of the window

# ===== FUNCTIONS =====
def randomInt(difficulty): #function for the number randomiser to give random questions to the user
    if difficulty == "Easy": #if the user clicks the easy button, single digit numbers will generate only
        num1 = random.randint(1,9) #generate any number, 1 to 9
        num2 = random.randint(1,9)
    elif difficulty == "Moderate":
        num1 = random.randint(10,99) #generate any number, 10 to 99
        num2 = random.randint(10,99)
    elif difficulty == "Advanced":
        num1 = random.randint(1000,9999) #generate any number, 1000 to 9999
        num2 = random.randint(1000,9999) 
    return num1, num2


def quiz_difficulty(difficulty): #function triggers when user clicks on the button difficulty
    num1, num2 = randomInt(difficulty)
    switch_frame(frame1) #switches to frame 1 (where the quiz takes place)

    #label that outputs the difficulty (easy, moderate, advanced) along with mode, all in uppercase
    label1.config(text=difficulty.upper() + " MODE") 

    question_label.config(text= f"{num1} + {num2} =")


# ===== HEADING SECTION USING AN IMAGE AND LABEL // FRAME 1 =====
def displayMenu(): #function to display difficulty level menu
    global main_frame
    main_frame = Frame(root, bg="#1b2645")

    img = Image.open('01-MathsQuiz/title.png') #opens the image file
    resized_img = img.resize((420,120)) #reizes the image to 360 x 100
    new_img = ImageTk.PhotoImage(resized_img)

    #displays the resized image with space of 20px vertically
    img_label = Label(main_frame, image = new_img, bg="#1b2645")
    img_label.image = new_img
    img_label.pack(pady=(20,0)) #pady, 20px space above and 0px space below the image

    #displays a message to ask the user to select a difficulty
    #label with bold, yellow text and the background color
    text = Label(main_frame, text = "Please select a difficulty!", font=("Georgia", 12, "bold"), bg='#1b2645', fg="#fde68a")
    text.pack()

    #line border made using label
    line = Label(main_frame, text = "________________________________", bg="#1b2645", fg="white")
    line.pack(pady=(0,32)) #pady, 0px space above and 32px below the label text

    # ===== BUTTONS FOR EACH DIFFICULTY =====
    #three separate buttons were created with the white font and width of the button
    button1 = Button(main_frame, text="Easy", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command=lambda: quiz_difficulty("Easy"))
    button1.pack(pady=5)
    button2 = Button(main_frame, text="Moderate", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command=lambda: quiz_difficulty("Moderate"))
    button2.pack(pady=5)
    button3 = Button(main_frame, text="Advanced", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command = lambda:quiz_difficulty("Advanced"))
    button3.pack(pady=5)

    main_frame.place(x=0, y=0, width=400, height=400) #aligns the content on the screen

displayMenu() #calls the function to display the content under displayMenu

# ===== EASY DIFFICULTY FRAME =====
frame1 = Frame(root,bg="#1b2645")
frame1.place(x=0, y=0, width=400, height=400)

#label text is empty for config
label1 = Label(frame1, text = "", font=("Georgia", 21, "bold"), fg="#fde68a", bg="#1b2645")
label1.pack(pady=(15,0))
line1 = Label(frame1, text = "_______________________________________________________", bg="#1b2645", fg="white")
line1.pack()


#using labels for the heading question and score
questionHeading_label = Label(frame1, text = "QUESTION", font= ("Helvetica",10, "bold"), bg="#1b2645", fg="white")
score_label = Label(frame1, text = "SCORE: 0 / 100", font= ("Helvetica",10, "bold"), bg="#1b2645", fg="white")

#absolute positioning using place
questionHeading_label.place(x=58, y=85)
score_label.place(x=240, y=85)

#entry to allow the user to enter the answer for the given question
answer_entry = Entry(frame1, font= ("Roboto",16), bg="#1b2645", fg="white", width = 22)
answer_entry.place(y=220, x=195, anchor="center")

#submit button
submit_button = Button(frame1, text = "SUBMIT ANSWER", font= ("Helvetica",14, "bold"), bg="#246348", fg="white")
submit_button.place(y=250, x=110)

#label for the question to be displayed
question_label = Label(frame1, text="", font=("Roboto", 20), bg="#1b2645", fg="white")
question_label.place(y=160, x=200, anchor= "center")


#function to switch between frames
def switch_frame(frame):
    frame.tkraise()

switch_frame(main_frame)

root.mainloop()