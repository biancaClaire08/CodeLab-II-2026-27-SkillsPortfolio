from tkinter import * #import tkinter

root = Tk()
root.geometry('750x510')
#avoid resizing the window
root.resizable(0,0)
root.title('Student Manager')

# ===== FRAMES =====
frame = Frame(root, bg= "#162236", width=750, height=60)
frame.pack()
options_frame = Frame(root, bg= '#202f46', width=200, height=520)
options_frame.pack(side=LEFT)

# ===== BUTTONS =====
home_btn = Button(options_frame, text="HOME", font=("Tahoma",11, "bold"), fg="white", bg='#202f46', bd=0) #bd removes the border around the button
home_btn.place(x=20, y=50)

highest_btn = Button(options_frame, text="HIGHEST SCORE", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
highest_btn.place(x=20, y=110)

lowest_btn = Button(options_frame, text="LOWEST SCORE", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
lowest_btn.place(x=20, y=170)

sort_btn = Button(options_frame, text="SORT RECORDS", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
sort_btn.place(x=20, y=230)

modify_btn = Button(options_frame, text="MODIFY", font=("Tahoma", 11, "bold"),fg="white", bg='#202f46', bd=0)
modify_btn.place(x=20, y=290)

root.mainloop()