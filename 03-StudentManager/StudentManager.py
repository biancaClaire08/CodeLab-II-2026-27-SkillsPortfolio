# ===== IMPORTING MODULES =====
from tkinter import * #import tkinter
from PIL import ImageTk, Image #import img module
import json #import JSON module

#importing messagebox and ttk
import tkinter.messagebox
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry('995x640')
#avoid resizing the window
root.resizable(0,0)
root.title('Student Manager')
root.iconbitmap('./03-StudentManager/icon3.ico') #the icon for the image

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

number_of_students=0
average=0

#function to display student records
def view_records(students=None, display_table=True): #this function will function two ways: if no parameter is passed on or if students parameter is passed on it
    record_frame = Frame(main_frame) #create a frame inside the root window
    record_frame.place(relx=0.5,rely=0.65,anchor="center")

    global number_of_students, average
    #if no students is passed into the function
    if students is None:
        student_list = data["Student Details"]
    else:
        student_list = students

    #if the parameter passes TRUE, it will display the table
    if display_table==True:
        #headings for the table, aligned using grid
        Label(record_frame, text="Student No.", width=10, bg="#919191").grid(row=25, column=1)
        Label(record_frame, text="Student Name", width=14, bg="#919191").grid(row=25, column=2)
        Label(record_frame, text="Total Coursework Mark", width=22, bg="#919191").grid(row=25, column=3)
        Label(record_frame, text="Exam Mark", width=26, bg="#919191").grid(row=25, column=4)
        Label(record_frame, text="Overall Percentage",bg="#919191", width=15).grid(row=25, column=5)
        Label(record_frame, text="Grade", width=8, bg="#919191").grid(row=25, column=6)

    row = 26 #starting row line 
    total_percentage=0

    #loop through the entire student_list
    for student in student_list:
        student_no = student["student_id"]
        student_name = student["student_name"]
        
        total_coursework, exam_mark, percentage, grade = calculate_results(student)        
        total_percentage = total_percentage + percentage
        percentage1 = str(percentage) + "%"

        if display_table==True:
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

#function to search student using ID
def search_student(id_entry):
    student_id_entered = id_entry.get() #takes the student ID entered by the user and stores it in the variable
    student_found = False 
    student_details = None #no student details stored

    #compares the student id enterd with the available student IDs in the table
    for student in data["Student Details"]:
        if str(student["student_id"]) == student_id_entered: 
            student_found = True #set to True if the ID has been found
            student_details = student #stores the details of that student found
            break
    if student_found == False: #if not found, a message box is displayed to inform the user
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

#searching student with their name (similar concept has been used based on the function above this)
def search_student1(name_entry):
    student_name_entered = name_entry.get()
    student_found = False
    student_details = None #no student details stored

    #if no name has been entered, messagebox will display the relevant message
    if student_name_entered.strip() == "":
        messagebox.showinfo("Error", "Please enter a Name")
        return
    
    for student in data["Student Details"]:
        if (student_name_entered.strip().lower()) in student["student_name"].lower():
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


def individual_record_ID():
    global search_frame 
    #open a new separate window while keeping the main window open
    search_frame = Toplevel(root)
    search_frame.title("Searching Record")
    search_frame.geometry("500x200")
    search_frame.resizable(0,0) #prevents user from resizing the window

    #labels to display information and entry for the user to enter the ID
    id_label = Label(search_frame, text="Enter Student ID:", anchor='w').grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(search_frame, width=30)
    id_entry.grid(row=0, column=1, padx=10, pady=10)
    #search button which will trigger the function
    search_btn = Button(search_frame, text="Search Student ID", font=("bold",8), width=16, bg="#162236", fg="white", command=lambda: search_student(id_entry))
    search_btn.grid(row=0, column=2, padx=15)

def individual_record_Name():
    global search_frame 
    #open a new separate window while keeping the main window open
    search_frame = Toplevel(root)
    search_frame.title("Searching Record")
    search_frame.geometry("500x200")
    search_frame.resizable(0,0)
    
    id_label = Label(search_frame, text="Enter Student Name:", anchor='w').grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(search_frame, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=10)
    search_btn = Button(search_frame, text="Search Student Name", font=("bold",8), width=17, bg="#162236", fg="white", command=lambda: search_student1(name_entry))
    search_btn.grid(row=0, column=2, padx=15)

#statistics function to display the stats overall
def stats(button4, home_frame):
    button4.destroy() #button destroys after user clicks it\

    #background frame, set with a different colour
    frame_bg1=Frame(home_frame, bg="#2F3845", width=175, height=130)
    frame_bg1.place(x=400,y=70)
    frame_bg2=Frame(home_frame, bg="#2F3845", width=164, height=130)
    frame_bg2.place(x=585,y=70)

    view_records(display_table=False) #set to False to prevent the entire table from displaying
    #shows the relevant information with the help of labels
    Label(frame_bg1, text="Total Number \n of Students", font=("Arial",16,"bold"), bg="#2F3845", fg="white", justify="left").place(relx=0.06,rely=0.1)
    Label(frame_bg1, text=number_of_students, font=("Arial",12), bg="#2F3845", fg="white", justify="left").place(relx=0.1,rely=0.6)
    Label(frame_bg2, text="Average Score", font=("Arial",15,"bold"), bg="#2F3845", fg="white", justify="left").place(relx=0.06,rely=0.1)
    Label(frame_bg2, text=str(average) + "%", font=("Arial",12), bg="#2F3845", fg="white", justify="left").place(relx=0.1,rely=0.6)



# ===== FUNCTION INVOLVING STUDENT SCORES FOR HIGHEST AND LOWEST =====
def display_record(student, score_frame):
    result_frame = Frame(score_frame)
    result_frame.pack(pady=25)
    #obtains the information from the function alrady declared and stores them in the appropriate variables
    total_coursework, exam_mark, percentage, grade = calculate_results(student)

    #exact format to display the details of the student
    Label(result_frame, text="Student No.", width=24, bg="#28293D", fg="white").grid(row=1, column=0, padx=10)
    Label(result_frame, text= student["student_id"], width=19).grid(row=1, column=1)     
    Label(result_frame, text="Student Name", width=24, bg="#28293D", fg="white").grid(row=2, column=0)
    Label(result_frame, text= student["student_name"], width=19).grid(row=2, column=1)
    Label(result_frame, text="Total Coursework Mark", width=24, bg="#28293D", fg="white").grid(row=3, column=0)
    Label(result_frame, text=total_coursework, width=19).grid(row=3, column=1)
    Label(result_frame, text="Exam Mark", width=24, bg="#28293D", fg="white").grid(row=4, column=0)
    Label(result_frame, text=exam_mark, width=19).grid(row=4, column=1)
    Label(result_frame, text="Overall Percentage", width=24, bg="#28293D", fg="white").grid(row=5, column=0)
    Label(result_frame, text=str(percentage) + "%", width=19).grid(row=5, column=1) 
    Label(result_frame, text="Grade", width=24, bg="#28293D", fg="white").grid(row=6, column=0)
    Label(result_frame, text=grade, width=19).grid(row=6, column=1)

def highest_score(scores_frame):
    highest_score = 0 #initialise highest_score
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

def sort_records(reverse):
    students = []
    for student in data["Student Details"]:
        students.append(student)

    #bubble sort
    for x in range(len(students)):
        for y in range(x+1, len(students)):
            if reverse == False:
                if students[x]["student_name"] > students[y]["student_name"]:
                    students[x],students[y] = students[y], students[x] #swap the places
            else:
                if students[x]["student_name"] < students[y]["student_name"]:
                    students[x],students[y] = students[y], students[x]
    view_records(students)

def sort_records1(reverse):
    students = []
    for student in data["Student Details"]:
        students.append(student)

    #bubble sort
    for x in range(len(students)):
        for y in range(x+1, len(students)):
            if reverse == False:
                if students[x]["student_id"] > students[y]["student_id"]:
                    students[x],students[y] = students[y], students[x] #swap the places
            else:
                if students[x]["student_id"] < students[y]["student_id"]:
                    students[x],students[y] = students[y], students[x]
    view_records(students)

def filter_students():
    #removes the previous student record displayed
    for table in filter_frame1.winfo_children():
        table.destroy()

    selected_grade = filter_grades.get()
    row=30
    students=read()

    for student in students:
        student_no=student["student_id"]
        student_name=student["student_name"]
        total_coursework, exam_mark, percentage, grade = calculate_results(student)
        
        if selected_grade == grade:
            Label(filter_frame1, text=student_no, width=10).grid(row=row, column=1)
            Label(filter_frame1, text=student_name, width=14).grid(row=row, column=2)
            Label(filter_frame1, text=total_coursework, width=22).grid(row=row, column=3)
            Label(filter_frame1, text=exam_mark, width=25).grid(row=row, column=4)
            Label(filter_frame1, text=percentage, width=15).grid(row=row, column=5)
            Label(filter_frame1, text=grade, width=8).grid(row=row, column=6)
            row+=1






# ===== FUNCTIONS FOR FRAMES =====
def home_page():
    delete_pages()
    home_frame = Frame(main_frame, bg="white")
    heading = Label(home_frame, text="Home", font=("Arial",26, "bold"), bg="#FFFFFF", fg="black")
    heading.pack(anchor='w', padx=10) #aligns the text to the left with spacing on the x-axis
    
    button1 = Button(home_frame, text="View all student records", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=view_records)
    button1.pack(anchor='w', padx=10, pady=(15,12))
    button2 = Button(home_frame, text="View individual student record by ID", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=individual_record_ID)
    button2.pack(anchor='w', padx=10, pady=(0,12))
    button3 = Button(home_frame, text="View individual student record by Name", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=individual_record_Name)
    button3.pack(anchor='w', padx=10)
    
    frame_bg=Frame(home_frame, bg="#222A37", width=370, height=150)
    frame_bg.place(x=390,y=60)
    button4 = Button(home_frame, text="Extra Information", font=("Times", 12), bg="black", fg="#FFFFFF", padx=27, pady=5, width=20, command=lambda: stats(button4, home_frame))
    button4.place(x=455, y=115)

    home_frame.pack(anchor='w', padx=10, pady=15, fill="both", expand="Yes")

def scores_page():
    delete_pages()
    scores_frame = Frame(main_frame, bg="white")
    heading1 = Label(scores_frame, text="Student Scores", font=("Arial",26, "bold"), bg="#FFFFFF", fg="black")
    heading1.pack(anchor='w', padx=10)

    button1 = Button(scores_frame, text="Highest Scoring Student", font=("Times", 14), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=lambda: highest_score(scores_frame))
    button1.pack(anchor='w', padx=10, pady=(30,10))
    button2 = Button(scores_frame, text="Lowest Scoring Student", font=("Times", 14), bg="black", fg="#FFFFFF", padx=27, pady=5, width=30, command=lambda: lowest_score(scores_frame))
    button2.pack(anchor='w', padx=10)

    img = Image.open('03-StudentManager/img1.png')
    resized_img = img.resize((300,280))
    new_img = ImageTk.PhotoImage(resized_img)
    img_label = Label(main_frame, image = new_img, bg="white")
    img_label.image = new_img
    img_label.place(x=460,y=80)
    
    scores_frame.pack(anchor='w', padx=10, pady=15)

def sort_page():
    delete_pages()
    sort_frame = Frame(main_frame, bg="white")
    heading2 = Label(sort_frame, text="Sorting Student Records", font=("Arial",26, "bold"), bg="#FFFFFF", fg="black")
    heading2.pack(anchor='w', padx=10)

    Label(sort_frame,text="Name", font=("Times",14, "underline"), bg="#FFFFFF", fg="black").place(x=38,y=58)
    ascend = Radiobutton(sort_frame, text="Ascending", value="ascend", font=("Times", 14), fg="black", bg="white", padx=27, pady=5, command=lambda: sort_records(False))
    ascend.pack(anchor='w', padx=10, pady=(40,10))
    descend = Radiobutton(sort_frame, text="Descending", value="descend", font=("Times", 14),fg="black", bg="white", padx=27, pady=5, command=lambda: sort_records(True))
    descend.pack(anchor='w', padx=10)

    Label(sort_frame,text="ID", font=("Times",14, "underline"), bg="#FFFFFF", fg="black").place(x=300,y=58)
    ascend1 = Radiobutton(sort_frame, text="Ascending", value="ascend1", font=("Times", 14), fg="black", bg="white", padx=27, pady=5, command=lambda: sort_records1(False))
    ascend1.place(x=270,y=87)
    descend1 = Radiobutton(sort_frame, text="Descending", value="descend1", font=("Times", 14),fg="black", bg="white", padx=27, pady=5, command=lambda: sort_records1(True))
    descend1.place(x=270,y=138)
    
    sort_frame.pack(anchor='w', padx=10, pady=15)

def filter_page():
    delete_pages()
    global filter_grades, filter_frame, filter_frame1
    filter_frame = Frame(main_frame, bg="white")
    heading3 = Label(filter_frame, text="Filter Records", font=("Arial",26, "bold"), bg="#FFFFFF", fg="black")
    heading3.pack(anchor='w', padx=10)

    filter_frame1 = Frame(main_frame, bg="white")
    filter_frame2= Frame(main_frame, bg="black")

    Label(filter_frame, text="Filter by Grade:", font=("Arial",12), bg="white").pack(side="left", padx=12, pady=20)
    grades=["All Grades","A","B","C","D","F"]
    
    #Combobox
    filter_grades= ttk.Combobox(filter_frame, values=grades, state="readonly") #readonly state will prevent user from typing into the combo box
    filter_grades.set("All Grades") #option set as default selected option 
    filter_grades.pack(side="left", padx=5)

    Button(filter_frame, text="Filter", bg="#202f46", fg="white", width=7, padx=2, pady=2, command=filter_students).pack(side="right", padx=20)

    img1 = Image.open('03-StudentManager/img3.jpg')
    resized_img1 = img1.resize((900,500))
    new_img1 = ImageTk.PhotoImage(resized_img1)
    img_label1 = Label(filter_frame2, image = new_img1)
    img_label1.image = new_img1
    img_label1.pack()

    filter_frame.pack(anchor='w', padx=10, pady=15)
    filter_frame1.place(x=40,y=130, width=900, height=600)
    filter_frame2.place(x=0, y=340, width=900, height=200)


def delete_pages():
    for frame in main_frame.winfo_children(): #loop through the frames inside main_frame
        frame.destroy() #removes the frame from the window



# ===== FRAMES =====
frame = Frame(root, bg= "#162236", width=995, height=60)
frame.pack()
Label(root, text= "STUDENT MANAGEMENT", font=("Roboto",15, "bold"), bg= "#162236", fg="white").place(x=50, y=18)
small_image = Image.open('03-StudentManager/usb.png')
image_resized = small_image.resize((20,20))
new_image = ImageTk.PhotoImage(image_resized)
img_label2 = Label(root, image = new_image)
img_label2.image = new_image
img_label2.place(x=15, y=20)

options_frame = Frame(root, bg= '#202f46', width=200, height=640) #side dashboard frame for the buttons
options_frame.pack(side=LEFT)

main_frame = Frame(root, bg="#FFFFFF", width=995, height=640) #frame to display the main content
main_frame.pack(side=LEFT) #positioning of main_frame will be beside the option_frame on the available space
main_frame.pack_propagate(False) #prevent the frame from automatically resizing


# ===== BUTTONS =====
home_btn = Button(options_frame, text="HOME", font=("Tahoma",14, "bold"), fg="white", bg='#202f46', bd=0, command=home_page) #bd removes the border around the button
home_btn.place(x=20, y=20)

score_btn = Button(options_frame, text="SCORE", font=("Tahoma", 14, "bold"),fg="white", bg='#202f46', bd=0, command=scores_page)
score_btn.place(x=20, y=75)

sort_btn = Button(options_frame, text="SORT", font=("Tahoma", 14, "bold"),fg="white", bg='#202f46', bd=0, command=sort_page)
sort_btn.place(x=20, y=130)

filter_btn = Button(options_frame, text="FILTER", font=("Tahoma", 14, "bold"),fg="white", bg='#202f46', bd=0, command=filter_page)
filter_btn.place(x=20, y=185)

Label(options_frame, text="QUICK ACTIONS", font=("Tahoma", 13, "bold", "underline"),fg="white", bg='#202f46').place(x=20, y=260)

addRecord_btn = Button(options_frame, text="ADD RECORD", font=("Tahoma", 13, "bold"),fg="white", bg='#202f46', bd=0, command=add_student)
addRecord_btn.place(x=20, y=305)

delRecord_btn = Button(options_frame, text="DEL RECORD", font=("Tahoma", 13, "bold"),fg="white", bg='#202f46', bd=0, command=delete)
delRecord_btn.place(x=20, y=350)

updateRecord_btn = Button(options_frame, text="UPDATE RECORD", font=("Tahoma", 13, "bold"),fg="white", bg='#202f46', bd=0, command=search)
updateRecord_btn.place(x=20, y=395)

img1 = Image.open('03-StudentManager/img2.png')
resized_img1 = img1.resize((180,150))
new_img1 = ImageTk.PhotoImage(resized_img1)
img_label1 = Label(options_frame, image = new_img1, bg="white")
img_label1.image = new_img1
img_label1.place(x=7.5,y=450)


home_page()
root.mainloop()