from tkinter import * #import tkinter
from PIL import ImageTk, Image #import img module
import json #import JSON module
import tkinter.messagebox
from tkinter import messagebox

root = Tk()
root.geometry('995x640')
#avoid resizing the window
root.resizable(0,0)
root.title('Student Manager')

# ===== FUNCTIONS INVOLVING JSON FILE AND IN THE HOME SECTION OF THE WINDOW =====
#open and reads the JSON file
with open("03-StudentManager/studentMarks.json","r") as file:
    data = json.load(file)

#calculate the total marks, percentage and grade
def calculate_results(student):
    total_coursework = student["course_marks"][0] + student["course_marks"][1] + student["course_marks"][2] #adds the marks in course_marks in the JSON file
    exam_mark = student["examination_mark"]

    percentage = ((total_coursework + exam_mark) / 160) * 100
    #grade assigned based on the percentage calculated
    if percentage >=70:
        grade = "A"
    elif percentage >=60:
        grade = "B"
    elif percentage >=50:
        grade = "C"
    elif percentage >=40:
        grade = "D"
    else:
        grade = "F"

    return total_coursework, exam_mark, percentage, grade

def view_records(): #function to display student records
    record_frame = Frame(root) #create a frame inside the root window
    record_frame.place(relx=0.6,rely=0.7,anchor="center")
    
    #headings for the table
    Label(record_frame, text="Student No.", width=10).grid(row=25, column=1)
    Label(record_frame, text="Student Name", width=14).grid(row=25, column=2)
    Label(record_frame, text="Total Coursework Mark", width=22).grid(row=25, column=3)
    Label(record_frame, text="Exam Mark", width=9).grid(row=25, column=4)
    Label(record_frame, text="Overall Percentage", width=15).grid(row=25, column=5)
    Label(record_frame, text="Grade", width=8).grid(row=25, column=6)

    total_percentage = 0
    row = 26

    for student in data["Student Details"]:
        student_no = student["student_id"]
        student_name = student["student_name"]
        
        total_coursework, exam_mark, percentage, grade = calculate_results(student)        
        total_percentage = total_percentage + percentage
        percentage1 = str(percentage) + "%"

        #inserting the student data into the table
        Label(record_frame, text=student_no, width=10).grid(row=row, column=1)
        Label(record_frame, text=student_name, width=14).grid(row=row, column=2)
        Label(record_frame, text=total_coursework, width=22).grid(row=row, column=3)
        Label(record_frame, text=exam_mark, width=25).grid(row=row, column=4)
        Label(record_frame, text=percentage1, width=15).grid(row=row, column=5)
        Label(record_frame, text=grade, width=8).grid(row=row, column=6)
        row+=1 #increments the row counter

        #counting the number of students using len 
        number_of_students = len(data["Student Details"])
        #average of percentage
        average = total_percentage / number_of_students 

    #display number of students and average percentage in the bottom of the table
    Label(record_frame, text="Number of Students: " + str(number_of_students)).grid(row=row, column=1)
    Label(record_frame, text="Average Percentage: " + str(average)).grid(row=row+1, column=1)


def search_student(id_entry):
    student_id_entered = id_entry.get()
    student_found = False
    student_details = None #no student details stored

    for student in data["Student Details"]:
        if str(student["student_id"]) == student_id_entered:
            student_found = True
            student_details = student
            break
    if student_found == False:
        messagebox.showinfo("Invalid", "Student not found")

    if student_found == True:
        total_coursework, exam_mark, percentage, grade = calculate_results(student)        

        #heading in column 1 with the student's information in column 2
        Label(search_frame, text="Student No.").grid(row=1, column=0, padx=10)
        Label(search_frame, text=student_details["student_id"]).grid(row=1, column=1)
        
        Label(search_frame, text="Student Name", width=22).grid(row=2, column=0)
        Label(search_frame, text=student_details["student_name"]).grid(row=2, column=1)
        
        Label(search_frame, text="Total Coursework Mark", width=22).grid(row=3, column=0)
        Label(search_frame, text=total_coursework).grid(row=3, column=1)

        Label(search_frame, text="Exam Mark", width=22).grid(row=4, column=0)
        Label(search_frame, text=exam_mark).grid(row=4, column=1)
        
        Label(search_frame, text="Overall Percentage", width=22).grid(row=5, column=0)
        Label(search_frame, text=str(percentage) + "%").grid(row=5, column=1)

        Label(search_frame, text="Grade", width=22).grid(row=6, column=0)
        Label(search_frame, text=grade).grid(row=6, column=1)
     

def individual_record():
    global search_frame 
    #open a new separate window while keeping the main window open
    search_frame = Toplevel(root)
    search_frame.title("Searching Record")
    search_frame.geometry("500x200")
    search_frame.resizable(0,0)
    
    id_label = Label(search_frame, text="Enter Student ID:", anchor='w').grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(search_frame, width=30)
    id_entry.grid(row=0, column=1, padx=10, pady=10)
    search_btn = Button(search_frame, text="Search Student ID", font=("bold",8), width=16, bg="#162236", fg="white", command=lambda: search_student(id_entry))
    search_btn.grid(row=0, column=2, padx=15)


# ===== FUNCTIONS FOR FRAMES =====
def home_page():
    delete_pages()
    home_frame = Frame(main_frame, bg="white")
    heading = Label(home_frame, text="Home", font=("Courier",26, "bold"), bg="#FFFFFF", fg="black")
    heading.pack(anchor='w', padx=10) #aligns the text to the left with spacing on the x-axis
    
    button1 = Button(home_frame, text="View all student records", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=view_records)
    button1.pack(anchor='w', padx=10, pady=(30,10))
    button2 = Button(home_frame, text="View individual student record", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=individual_record)
    button2.pack(anchor='w', padx=10)

    img = Image.open('03-StudentManager/student.jpg')
    resized_img = img.resize((170,170))
    new_img = ImageTk.PhotoImage(resized_img)
    img_label = Label(main_frame, image = new_img, bg="white")
    img_label.image = new_img
    img_label.place(x=550,y=20)

    home_frame.pack(anchor='w', padx=10, pady=15)

def delete_pages():
    for frame in main_frame.winfo_children(): #loop through the frames inside main_frame
        frame.destroy() #removes the frame from the window


# ===== FRAMES =====
frame = Frame(root, bg= "#162236", width=995, height=60)
frame.pack()
options_frame = Frame(root, bg= '#202f46', width=200, height=640) #side dashboard frame for the buttons
options_frame.pack(side=LEFT)

main_frame = Frame(root, bg="#FFFFFF", width=995, height=640) #frame to display the main content
main_frame.pack(side=LEFT) #positioning of main_frame will be beside the option_frame on the available space
main_frame.pack_propagate(False) #prevent the frame from automatically resizing


# ===== BUTTONS =====
home_btn = Button(options_frame, text="HOME", font=("Tahoma",11, "bold"), fg="white", bg='#202f46', bd=0, command=home_page) #bd removes the border around the button
home_btn.place(x=20, y=50)

score_btn = Button(options_frame, text="SCORE", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
score_btn.place(x=20, y=110)

sort_btn = Button(options_frame, text="SORT RECORDS", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
sort_btn.place(x=20, y=170)

modify_btn = Button(options_frame, text="MODIFY", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
modify_btn.place(x=20, y=230)

home_page()
root.mainloop()