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

def decideOperation(): #random operation sign
    operation = ["+", "-"] #the options for operators
    choice = random.choice(operation) #randomly selects from the operation choices
    return choice

def selectedDifficulty(difficulty_selected):
    global difficulty, score, question_counter, number_of_attempts, question
    difficulty=difficulty_selected
    #label that outputs the difficulty (easy, moderate, advanced) along with mode, all in uppercase
    label1.config(text=difficulty.upper() + " MODE")

    #initialising the score, question counter and attempt for each question
    score=0
    question_counter = 0
    number_of_attempts=1
    question = False

    displayProblem() #calls the displayProblem function


def displayProblem(): #function triggers when user clicks on the button difficulty
    #allow the function to access these variables
    global score, question_counter, number_of_attempts, correct_answer, question
    switch_frame(frame1) #switches to frame 1 (where the quiz takes place)

    if question == False:
        #condition to check whether 10 questions have been displayed
        if question_counter >=10:
            return "done"

        number_of_attempts = 1 #resets the attempt after every new question
        question_counter+=1 #increments after one question is done
    
        #calls the functions to obtain the number and operation
        num1, num2 = randomInt(difficulty)
        operation_choice = decideOperation() 
        #it checks the operation and finds the right answer corresponding to the two numbers and operation
        if operation_choice == "+":
            correct_answer = num1+num2
        else:
            correct_answer = num1-num2

        question_label.config(text= f"{num1} {operation_choice} {num2} =") #take the numbers and operations from the random module

        answer_entry.delete(0, END) #clear the content of the entry widget
        question=True
        return
        
    #try except handle to ensure the number entered is an integer
    try:
        user_answer = int(answer_entry.get()) #gets the users answer
    except ValueError: #if the answer is not an integer or left empty, the label text will be displayed
        label2.config(text="Please enter a valid answer")
        return #stop the function if user does not enter a valid integer

    if user_answer == correct_answer: #checks the user's answer with the correct answer
        if number_of_attempts == 1: #ten points added for being correct on the first attempt
            score+=10
            label2.config(text = "Correct. +10 points added")
        else:
            score+=5 #five points added for being correct on the second attempt 
            label2.config(text = "Correct. +5 points added")
        question=False #set to False when the question has been completed (will help move on to the next question)
    else:
        if number_of_attempts == 1: #another attempt to the user if the first answer is incorrect
            number_of_attempts = 2 #second attempt
            label2.config(text="Wrong answer. Try again")
            answer_entry.delete(0, END) #clears the answer written, sets the entry widget to blank
        else:
            label2.config(text="Wrong. No tries remaining") #moves to the next question with the help of the False boolean if the second attempt is also incorrect
            question=False

    if question==False: #displays the next question when the current question is done
        displayProblem()


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
    button1 = Button(main_frame, text="Easy", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command=lambda: selectedDifficulty("Easy"))
    button1.pack(pady=5)
    button2 = Button(main_frame, text="Moderate", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command=lambda: selectedDifficulty("Moderate"))
    button2.pack(pady=5)
    button3 = Button(main_frame, text="Advanced", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command = lambda:selectedDifficulty("Advanced"))
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
questionHeading_label.place(x=58, y=75)
score_label.place(x=240, y=75)

#entry to allow the user to enter the answer for the given question
answer_entry = Entry(frame1, font= ("Roboto",16), bg="#1b2645", fg="white", width = 22, justify= "center") #when the user enters the answer into the entry widget, it will start at the center of the widget
answer_entry.place(y=250, x=195, anchor="center")

#submit button
submit_button = Button(frame1, text = "SUBMIT ANSWER", font= ("Helvetica",14, "bold"), bg="#246348", fg="white", command= displayProblem) #when clicking the button, the displayProblem function is triggered
submit_button.place(y=280, x=110)

#label for the question to be displayed
question_label = Label(frame1, text="", font=("Roboto", 20), bg="#1b2645", fg="white")
question_label.place(y=180, x=200, anchor= "center")

#message label to tell the user what to do
label2 = Label(frame1, text="", font= ("Roboto",9), bg="#1b2645", fg="white")
label2.place(y=210, x=128)


#function to switch between frames
def switch_frame(frame):
    frame.tkraise()

switch_frame(main_frame)

root.mainloop()