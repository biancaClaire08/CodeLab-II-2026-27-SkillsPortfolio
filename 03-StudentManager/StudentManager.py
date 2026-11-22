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
root.iconbitmap('./03-StudentManager/icon3.ico')

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
    record_frame = Frame(main_frame) #create a frame inside the root window
    record_frame.place(relx=0.5,rely=0.65,anchor="center")
    
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


# ===== FUNCTION INVOLVING STUDENT SCORES FOR HIGHEST AND LOWEST =====
def display_record(student, score_frame):
    result_frame = Frame(score_frame)
    result_frame.pack(pady=25)
    total_coursework, exam_mark, percentage, grade = calculate_results(student)

    #exact format to display the details of the student
    Label(result_frame, text="Student No.").grid(row=1, column=0, padx=10)
    Label(result_frame, text= student["student_id"]).grid(row=1, column=1)     
    Label(result_frame, text="Student Name", width=22).grid(row=2, column=0)
    Label(result_frame, text= student["student_name"]).grid(row=2, column=1)
    Label(result_frame, text="Total Coursework Mark", width=22).grid(row=3, column=0)
    Label(result_frame, text=total_coursework).grid(row=3, column=1)
    Label(result_frame, text="Exam Mark", width=22).grid(row=4, column=0)
    Label(result_frame, text=exam_mark).grid(row=4, column=1)
    Label(result_frame, text="Overall Percentage", width=22).grid(row=5, column=0)
    Label(result_frame, text=str(percentage) + "%").grid(row=5, column=1) 
    Label(result_frame, text="Grade", width=22).grid(row=6, column=0)
    Label(result_frame, text=grade).grid(row=6, column=1)

def highest_score(scores_frame):
    highest_score = 0
    highest_student = None

    for student in data["Student Details"]:
        total_coursework, exam_mark, percentage, grade = calculate_results(student)

        #calculate the total score
        total_score = total_coursework + exam_mark
        #check if the current total score is greater than the highest score
        if total_score > highest_score:
            highest_score = total_score
            highest_student = student
    display_record(highest_student, scores_frame)

def lowest_score(scores_frame):
    lowest_score = 99999999 
    lowest_student = None

    for student in data["Student Details"]:
        total_coursework, exam_mark, percentage, grade = calculate_results(student)

        total_score = total_coursework + exam_mark
        if total_score < lowest_score:
            lowest_score = total_score
            lowest_student = student
    display_record(lowest_student, scores_frame)


# ===== TEXT FILE RELATED FUNCTION (RELATED TO ITEMS 6,7 AND 8) =====
def add_student_details(new_id, new_name, new_mark1, new_mark2, new_mark3, new_examMark, frame1):
    #append the text file without overwriting the current information in the file
    with open('./03-StudentManager/student.txt', 'a') as file:
        file.write(new_id.get() + "," + new_name.get() + "," + new_mark1.get() + "," +
                   new_mark2.get() + "," + new_mark3.get() + "," + new_examMark.get() + "\n") #new student data is added to the file (same format as the rest of the students)
    messagebox.showinfo("","Student has been successfully added")

def add_student():
    frame1 = Toplevel(root)
    frame1.title("Add a Student")
    frame1.geometry("400x450")
    frame1.resizable(0,0)

    #entry to allow user to enter the details
    Label(frame1, text="Student ID:").grid(row=1, column=0, padx=8, pady=2, sticky='e')
    new_id = Entry(frame1, width=42)
    new_id.grid(row=1, column=1, sticky='w')
    Label(frame1, text="Student Name:").grid(row=2, column=0, padx=8, pady=2, sticky='e')
    new_name = Entry(frame1, width=42)
    new_name.grid(row=2, column=1)
    Label(frame1, text="Coursework 1 Marks:").grid(row=3, column=0, padx=8, pady=2, sticky='e')
    new_mark1 = Entry(frame1, width=42)
    new_mark1.grid(row=3, column=1)
    Label(frame1, text="Coursework 2 Marks:").grid(row=4, column=0, padx=8, pady=2, sticky='e')
    new_mark2 = Entry(frame1, width=42)
    new_mark2.grid(row=4, column=1)
    Label(frame1, text="Coursework 3 Marks:").grid(row=5, column=0, padx=8, pady=2, sticky='e')
    new_mark3 = Entry(frame1, width=42)
    new_mark3.grid(row=5, column=1)
    Label(frame1, text="Examination Marks:").grid(row=6, column=0, padx=8, pady=2, sticky='e')
    new_examMark = Entry(frame1, width=42)
    new_examMark.grid(row=6, column=1)

    Button(frame1, text="Add Student", font=("bold",10), width=18, bg="#17243a", fg="white", command=lambda: add_student_details(new_id, new_name, new_mark1, new_mark2, new_mark3, new_examMark, frame1)).grid(row=7, column=0, columnspan=2, pady=8)

def read():
    students = []
    with open('./03-StudentManager/student.txt','r') as file:
        for line in file:
            details=line.strip().split(",") #.strip() gets rid of unwanted characters on both ends 

            #stores the read data into the corresponding variables
            student = { "student_id": details[0],
                "student_name":details[1],
                "course_marks": [
                    int(details[2]),
                    int(details[3]),
                    int(details[4])
                ],
                "examination_mark": int(details[5])}
            students.append(student) #append the data into the students array
    return students

def delete():
    frame2 = Toplevel(root)
    frame2.title("Delete a Student Record")
    frame2.geometry("250x100")
    frame2.resizable(0,0)

    Label(frame2, text="Enter Student ID:").place(x=10, y=20)
    studentID_entry = Entry(frame2)
    studentID_entry.place(x=110, y=20)
    Button(frame2, text="Delete", bg="#17243a", fg="white", font=("bold",8), command=lambda: delete_confirmation(studentID_entry, frame2)).place(x=195, y=50)

def delete_confirmation(studentID_entry, frame2):
    student_id = studentID_entry.get()
    students = read()
    student_found = False #boolean variable set to False initially
    confirm= False
    for student in students:
        if student["student_id"].strip() == student_id.strip(): #compares the entered ID with the student ID database
            student_found = True
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete " + student["student_name"] + "?")

            if confirm==True:
                students.remove(student) #delete this student from the list 
            break
    if student_found == False:
        messagebox.showinfo("", "Student not found")

    if confirm==True:
        #open file in write mode
        with open('./03-StudentManager/student.txt','w') as file:
            #loop through the updated students array after the deletion
            for student in students: #update and write student's deatils into the text file
                file.write(student["student_id"] + "," + student["student_name"] +
                           "," + str(student["course_marks"][0]) + "," + str(student["course_marks"][1]) +
                           "," + str(student["course_marks"][2]) + "," + str(student["examination_mark"]) + "\n")

        messagebox.showinfo("", "Student record has been successfuly deleted")

def search():
    frame2 = Toplevel(root)
    frame2.title("Search Student")
    frame2.geometry("250x100")
    frame2.resizable(0,0)

    Label(frame2, text="Enter Student ID:").place(x=10, y=20)
    studentID_entry1 = Entry(frame2)
    studentID_entry1.place(x=110, y=20)
    Button(frame2, text="Find Student", bg="#17243a", fg="white", font=("bold",8), command=lambda: enter_updated_records(studentID_entry1, frame2)).place(x=165, y=50)

def update(student,student_id,name,marks1,marks2,marks3,exam_marks,update_frame,frame2):
    with open('./03-StudentManager/student.txt','r') as file:
        file_content = file.read()
        new_marks1 = int(marks1.get())
        new_marks2 = int(marks2.get())
        new_marks3 = int(marks3.get())
        new_examMarks = int(exam_marks.get())
        new_name = name.get()

        old_record = f"{student["student_id"]},{student["student_name"]},{student["course_marks"][0]},{student["course_marks"][1]},{student["course_marks"][2]},{student["examination_mark"]}"
        new_record = f"{student["student_id"]},{new_name},{new_marks1},{new_marks2},{new_marks3},{new_examMarks}"

        #modifying the old data with new data using .replace
        modified_content = file_content.replace(old_record, new_record)

        with open('./03-StudentManager/student.txt','w') as file:
            file.write(modified_content)

        messagebox.showinfo("", "Student record has been successfully updated")


def enter_updated_records(studentID_entry1, frame2):
    students = read()
    student_found = False
    student_id = studentID_entry1.get()

    for student in students:
        if student["student_id"].strip() == student_id:
            student_found = True
            update_frame = Toplevel(frame2)
            update_frame.title("Update Student Record")
            update_frame.geometry("350x300")

            #displays the student id and name of the student id entered by the user
            Label(update_frame, text= student["student_id"] + ", " + "Student Name:" + " " + student["student_name"], font=(10)).pack(pady=14)
            #label headings with an entry widgets to let the user update the student records
            Label(update_frame, text="Student Name:").place(x=15, y=60)
            name = Entry(update_frame, width = 30)
            name.place(x=145, y=60)
            Label(update_frame, text="Coursework 1 Marks:").place(x=15, y=90)
            marks1 = Entry(update_frame, width = 30)
            marks1.place(x=145, y=90)
            Label(update_frame, text="Coursework 2 Marks:").place(x=15, y=120)
            marks2 = Entry(update_frame, width = 30)
            marks2.place(x=145, y=120)
            Label(update_frame, text="Coursework 3 Marks:").place(x=15, y=150)
            marks3 = Entry(update_frame, width = 30)
            marks3.place(x=145, y=150)
            Label(update_frame, text="Examination Marks:").place(x=15, y=180)
            exam_marks = Entry(update_frame, width = 30)
            exam_marks.place(x=145, y=180)

            Button(update_frame, text="Save Changes", bg="#17243a", fg="white", font=("bold",10), command=lambda: update(student,student_id,name, marks1, marks2, marks3, exam_marks,update_frame, frame2)).place(relx=0.35, rely=0.72)
            break
    if student_found == False:
        messagebox.showinfo("Error", "No student found with that ID")


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

def scores_page():
    delete_pages()
    scores_frame = Frame(main_frame, bg="white")
    heading1 = Label(scores_frame, text="Student Scores", font=("Courier",26, "bold"), bg="#FFFFFF", fg="black")
    heading1.pack(anchor='w', padx=10)

    button1 = Button(scores_frame, text="Highest Scoring Student", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=lambda: highest_score(scores_frame))
    button1.pack(anchor='w', padx=10, pady=(30,10))
    button2 = Button(scores_frame, text="Lowest Scoring Student", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=lambda: lowest_score(scores_frame))
    button2.pack(anchor='w', padx=10)

    img = Image.open('03-StudentManager/img1.jpg')
    resized_img = img.resize((300,300))
    new_img = ImageTk.PhotoImage(resized_img)
    img_label = Label(main_frame, image = new_img, bg="white")
    img_label.image = new_img
    img_label.place(x=460,y=50)
    
    scores_frame.pack(anchor='w', padx=10, pady=15)

def modify():
    delete_pages()
    modify_frame = Frame(main_frame, bg="white")
    heading2 = Label(modify_frame, text="Sorting Records", font=("Courier",26, "bold"), bg="#FFFFFF", fg="black")
    heading2.pack(anchor='w', padx=10)

    add_btn = Button(modify_frame, text="Add Student Record", font=("Times", 18), bg="black", fg="#FFFFFF", padx=27, pady=5, width=80, command=add_student)
    add_btn.pack(anchor='w', padx=10, pady=(30,10))
    del_btn = Button(modify_frame, text="Delete Student Record", font=("Times", 18), bg="black", fg="#FFFFFF", padx=27, pady=5, width=80, command=delete)
    del_btn.pack(anchor='w', padx=10, pady=(0,10))
    update_btn = Button(modify_frame, text="Update Student Record", font=("Times", 18), bg="black", fg="#FFFFFF", padx=27, pady=5, width=80, command=search)
    update_btn.pack(anchor='w', padx=10, pady=(0,10))
    
    modify_frame.pack(anchor='w', padx=10, pady=15)


def delete_pages():
    for frame in main_frame.winfo_children(): #loop through the frames inside main_frame
        frame.destroy() #removes the frame from the window



# ===== FRAMES =====
frame = Frame(root, bg= "#162236", width=995, height=60)
frame.pack()
Label(root, text= "STUDENT MANAGEMENT", font=("Roboto",15, "bold"), bg= "#162236", fg="white").place(x=15, y=18)
options_frame = Frame(root, bg= '#202f46', width=200, height=640) #side dashboard frame for the buttons
options_frame.pack(side=LEFT)

main_frame = Frame(root, bg="#FFFFFF", width=995, height=640) #frame to display the main content
main_frame.pack(side=LEFT) #positioning of main_frame will be beside the option_frame on the available space
main_frame.pack_propagate(False) #prevent the frame from automatically resizing


# ===== BUTTONS =====
home_btn = Button(options_frame, text="HOME", font=("Tahoma",11, "bold"), fg="white", bg='#202f46', bd=0, command=home_page) #bd removes the border around the button
home_btn.place(x=20, y=50)

score_btn = Button(options_frame, text="SCORE", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0, command=scores_page)
score_btn.place(x=20, y=110)

sort_btn = Button(options_frame, text="SORT RECORDS", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
sort_btn.place(x=20, y=170)

modify_btn = Button(options_frame, text="MODIFY", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0, command=modify)
modify_btn.place(x=20, y=230)

home_page()
root.mainloop()