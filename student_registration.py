from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import sqlite3
from datetime import date
from tkinter import filedialog
from tkinter import Entry
import os
import pathlib

#selection og gender 
def select():
    value=radio.get()
    if(value==1):
        gender="Male"
    else:
        gender="Female"

def exit():
     nav.destroy()

# Function to save registration number
def save_registration_number():
    registration_number = Register.get()

    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registration_numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            registration_number TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO registration_numbers (registration_number)
        VALUES (?)
    ''', (registration_number,))
    conn.commit()
    conn.close()


#define students details :
def save_student_details():
    full_name = name.get()
    date_of_birth = DOB.get()
    gender = "Male" if radio.get() == 1 else "Female"
    student_standard = standard.get()
    student_caste = caste.get()
    student_skills = skills.get()
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            date_of_birth TEXT,
            gender TEXT,
            student_standard TEXT,
            student_caste TEXT,
            student_skills TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO students (full_name, date_of_birth, gender, student_standard, student_caste, student_skills)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (full_name, date_of_birth, gender, student_standard, student_caste, student_skills))
    conn.commit()
    conn.close()


#function for storing parents details 
def save_parents_details():
    # Retrieve the values entered by the user
    father_name = F_name.get()
    father_date_of_birth = F_DOB.get()
    father_occupation = F_occupation.get()
    mother_name = M_name.get()
    mother_date_of_birth = M_DOB.get()
    mother_occupation = M_occupation.get()

    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist (you can modify the table structure if needed)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            father_name TEXT,
            father_date_of_birth TEXT,
            father_occupation TEXT,
            mother_name TEXT,
            mother_date_of_birth TEXT,
            mother_occupation TEXT
        )
    ''')

    # Insert the parents' data into the database
    cursor.execute('''
        INSERT INTO parents (father_name, father_date_of_birth, father_occupation, mother_name, mother_date_of_birth, mother_occupation)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (father_name, father_date_of_birth, father_occupation, mother_name, mother_date_of_birth, mother_occupation))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    

def save_details():
    if (
        not name.get() or
        not DOB.get() or
        not standard.get() or
        not caste.get() or
        not skills.get() or
        not F_name.get() or
        not F_DOB.get() or
        not F_occupation.get() or
        not M_name.get() or
        not M_DOB.get() or
        not M_occupation.get()
    ):
        messagebox.showwarning("Incomplete Details", "Please fill in all required details.")
    else:
        save_registration_number()
        save_student_details()
        save_parents_details()
        messagebox.showinfo("Success", "Registration done successfully!")


# for uploading file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        load_and_display_image(file_path)

def load_and_display_image(file_path):
    # Open and display the selected image
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    lab16.config(image=photo)
    lab16.image = photo

# for saving image
def save_image():
    messagebox.showinfo("Success", "Image saved successfully!")

# for clear button 
def clear_details():
    # Clear student details
    name.delete(0, END)
    DOB.delete(0, END)
    radio.set(0)  # Set radio button to 'Male'
    standard.set("Select Standard")
    caste.delete(0, END)
    skills.delete(0, END)

    # Clear parents' details
    F_name.delete(0, END)
    F_DOB.delete(0, END)
    F_occupation.delete(0, END)
    M_name.delete(0, END)
    M_DOB.delete(0, END)
    M_occupation.delete(0, END)


#main 
nav=Tk()
nav.title("STUDENT REGISTRATION SYSTEM")
nav.geometry('1250x750')
nav.config(bg='#06283d')

#label for Gmail
lab1=Label(nav,text='Email: amithrk78@gmail.com',bg='#FF7F00',width=10,height=3,compound=LEFT,font=('Times New Roman  bold',10)).pack(side=TOP,fill=X)
lab2=Label(nav,text='STUDENT REGISTRATION FORM',bg='#C36464',fg='#fff',width=10,height=2,font=('Calibri bold',15)).pack(side=TOP,fill=X)

#entry 
search=StringVar()
entry1=Entry(nav,textvariable='Search',font=('calibri',15),bd=4).place(x=800,y=65)
image1=PhotoImage(file="searchimg2.0.png")
button1=Button(nav,text='Search',compound=LEFT,font=('calibri bold',15),image=image1,width=125,height=38)
button1.place(x=1040,y=58)
image2=PhotoImage(file="image4.png")
button2=Button(nav,image=image2,bg='#FFF',width=70,height=45)
button2.place(x=90,y=55)


# registration and date 
lab3=Label(nav,text="Registration No.",bg='#06283d',fg='#FF7F00',font=('calibri bold',15)).place(x=20,y=130)
lab3=Label(nav,text="Date",bg='#06283d',fg='#FF7F00',font=('calibri bold',15)).place(x=430,y=130)
Register=StringVar()
entry2=Entry(nav,textvariable='Register',font=('calibri',15),bd=4).place(x=170,y=130)


# Create a StringVar for the Date Entry
Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
Date.set(d1)
entry3 = Entry(nav, textvariable=Date, width=15, fg='black', font=('calibri', 15), bd=4)
entry3.place(x=500, y=130)


#Students details
obj1=LabelFrame(nav,text='Student Details',font=('calibri bold',12),width=900,bd=2,height=220,relief=GROOVE,bg="#EDEDED",fg='#06283D')
obj1.place(x=30,y=220)
#left side
lab4=Label(nav,text="Full Name :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=250)
lab5=Label(nav,text="Date Of Birth :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=300)
lab6=Label(nav,text="Gender :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=350)

name=StringVar()
name=Entry(nav,textvariable=name,width=15,font=('calibri bold',15),bd=4)
name.place(x=190,y=250)

DOB=StringVar()
DOB=Entry(nav,textvariable=DOB,width=15,font=('calibri bold',15),bd=4)
DOB.place(x=190,y=300)

radio=IntVar()
radio1=Radiobutton(nav,text='Male',bg='#EDEDED',fg='#06283d',font=('calibri bold',13),variable=radio,value=1,command=select)
radio1.place(x=190,y=350)
radio2=Radiobutton(nav,text='Female',bg='#EDEDED',fg='#06283d',font=('calibri bold',13),variable=radio,value=2,command=select)
radio2.place(x=260,y=350)

#right side
lab7=Label(nav,text="Standard :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=250)
lab8=Label(nav,text="Caste :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=300)
lab9=Label(nav,text="Skills :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=350)

caste=StringVar()
caste=Entry(nav,textvariable=caste,width=15,font=('calibri bold',15),bd=4)
caste.place(x=600,y=300)
skills=StringVar()
skills=Entry(nav,textvariable=skills,width=15,font=('calibri bold',15),bd=4)
skills.place(x=600,y=350)
standard=Combobox(nav,text='choose',values=['1','2','3','4','5','6','7','8','9','10','11','12','12+'],font=('roboto',10),width=19)
standard.place(x=600,y=255)
standard.set("Select Standard")

# Parents details
obj2=LabelFrame(nav,text='Parents Details',font=('calibri bold',12),width=900,bd=2,height=220,relief=GROOVE,bg="#EDEDED",fg='#06283D')
obj2.place(x=30,y=500)

# fathers details
lab10=Label(nav,text="Fathers Name :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=550)
lab11=Label(nav,text="Date of Birth :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=600)
lab12=Label(nav,text="Occupation :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=40,y=650)
F_name=StringVar()
F_name=Entry(nav,textvariable=F_name,width=15,font=('calibri bold',15),bd=4)
F_name.place(x=190,y=550)
F_DOB=StringVar()
F_DOB=Entry(nav,textvariable=F_DOB,width=15,font=('calibri bold',15),bd=4)
F_DOB.place(x=190,y=600)
F_occupation=StringVar()
F_occupation=Entry(nav,textvariable=F_occupation,width=15,font=('calibri bold',15),bd=4)
F_occupation.place(x=190,y=650)

# mothers details 
lab13=Label(nav,text="Mothers Name :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=550)
lab14=Label(nav,text="Date of Birth :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=600)
lab15=Label(nav,text="Occupation :",bg='#EDEDED',fg='#06283d',font=('calibri bold',15)).place(x=500,y=650)
M_name=StringVar()
M_name=Entry(nav,textvariable=M_name,width=15,font=('calibri bold',15),bd=4)
M_name.place(x=650,y=550)
M_DOB=StringVar()
M_DOB=Entry(nav,textvariable=M_DOB,width=15,font=('calibri bold',15),bd=4)
M_DOB.place(x=650,y=600)
M_occupation=StringVar()
M_occupation=Entry(nav,textvariable=M_occupation,width=15,font=('calibri bold',15),bd=4)
M_occupation.place(x=650,y=650)

# photo icon 
photo=Frame(nav,bd=3,bg='black',relief=GROOVE,width=200,height=200)
photo.place(x=1000,y=150)
img=PhotoImage(file="person2.png")
lab16=Label(photo,bg='black',image=img)
lab16.place(x=0,y=0)


# down side of photo icon
button2=Button(nav,text='ADD NEW',font=('calibri bold',15),bg='#00CD00',fg='black',width=20,height=2,command=open_file)
button2.place(x=1000,y=380)
img1=PhotoImage(file="addicon.png")
lab17=Label(nav,bg='black',image=img1)
lab17.place(x=1170,y=400)

button3=Button(nav,text='SAVE',font=('calibri bold',15),bg='#FF8000',fg='black',width=20,height=2,command=save_image)
button3.place(x=1000,y=460)
img2=PhotoImage(file="saveicon2.png")
lab18=Label(nav,bg='black',image=img2)
lab18.place(x=1170,y=480)

button4=Button(nav,text='Clear',font=('calibri bold',15),bg='#009ACD',fg='black',width=20,height=2,command=clear_details)
button4.place(x=1000,y=540)
img3=PhotoImage(file="reuploasd.png")
lab19=Label(nav,bg='black',image=img3)
lab19.place(x=1170,y=560)

button5=Button(nav,text='EXIT',font=('calibri bold',15),bg='#CD0000',fg='black',width=20,height=2,command=exit)
button5.place(x=1000,y=620)
img4=PhotoImage(file="exit.png")
lab20=Label(nav,bg='black',image=img4)
lab20.place(x=1170,y=640)

#submit button 
button6=Button(nav,text='SUBMIT',font=('calibri bold',15),bg='#EDEDED',fg='#06283d',command=save_details).place(x=380,y=670)

nav.mainloop()