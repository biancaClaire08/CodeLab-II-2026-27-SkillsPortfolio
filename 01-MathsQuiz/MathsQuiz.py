#import the modules needed
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#create an instance of tkinter window
root.geometry("400x400")
root.title("Arithmetic Quiz")
root.config(bg="#1b2645") #sets the background color of the window

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
    button1 = Button(main_frame, text="Easy", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"), command=lambda: switch_frame(frame1))
    button1.pack(pady=5)
    button2 = Button(main_frame, text="Moderate", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"))
    button2.pack(pady=5)
    button3 = Button(main_frame, text="Advanced", bg="#131c35", fg="white", width=21, font=("Courier New", 12, "bold"))
    button3.pack(pady=5)

    main_frame.pack() #displays the main_frame

displayMenu() #calls the function to display the content under displayMenu

# ===== EASY DIFFICULTY FRAME =====
frame1 = Frame(root,bg="#1b2645")
label1 = Label(frame1, text = "EASY MODE", font=("Georgia", 28, "bold"), fg="#fde68a", bg="#1b2645")
label1.pack()

frame1.place(x=0, y=40, width=400, height=400)

#function to switch between frames
def switch_frame(frame):
    frame.tkraise()

switch_frame(main_frame)

root.mainloop()