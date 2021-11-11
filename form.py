#for GUI
from tkinter import *
#for database
import sqlite3
#for msgbox
from tkinter import messagebox
#provides regular expression matching operations 
import re
#defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon
import smtplib

# clear output area
def clear():
       
        # output.delete(0.0,END)

        entry_name.delete(0,END)
        entry_contact.delete(0,END)
        entry_email.delete(0,END)
        entry_age.delete(0,END)
        entry_address.delete(0,END)
        #clear checkbox and radio
        checkbox1.set(0)
        checkbox2.set(0)
        checkbox3.set(0)
        checkbox4.set(0)
        checkbox5.set(0)
        checkbox6.set(0)
        gender.set(0)

#cheaking validation of name 
def checkname(name):
    if (name.isalpha()):
        return True
    if name == "":
    	return True	
    
    else:
        #pop up a msg box which shows a warning of invalid or not allowed 
        messagebox.showwarning("Invalid","Not allowed "+ name[-1]) 
        return False
        
def checkcontact(con):
        if con.isdigit():
            return True
        if len(str(con))== 0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
            
def checkemail(email):
        # at least 8 character is needed
        if len(email)>7:
                #expression used to find all the possible emails in a large corpus of text.
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                    return True 
                else:
                    messagebox.showwarning("Alert","Invalid E-mail enter by user")
                    return False
        else:
            messagebox.showwarning("Alert","Email length is too small")

# if some information is missing 
def validations():
    x = 0
    if name.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif contact.get() == "" or len(contact.get())!=10:
        messagebox.showinfo("Alert","Enter valid Contact ")
    elif email.get() =="":
        messagebox.showinfo("Alert","Enter Email")
    elif age.get() == "": 
        messagebox.showinfo("Alert","Enter Age")
    elif gender.get() ==0:
        messagebox.showinfo("Alert","Select Gender")
    elif address.get() == "":
        messagebox.showinfo("Alert","Enter your current address")
    elif state.get() == "" or state.get() == "Select your state":
        messagebox.showinfo("Alert","Select state")
    elif country.get() == "" or country.get() == "Select your country":
        messagebox.showinfo("Alert","Select country")
    elif checkbox1.get()==0 and checkbox2.get()==0 and checkbox3.get()==0 and  checkbox4.get()==0 and checkbox5.get()==0 and checkbox6.get()==0:
        messagebox.showinfo("Alert","Select areas acc to skill")
    elif email.get()!=None:
        x = checkemail(email.get())

    # for database    
    if (x == 1):
    	prog = []
    	name1=name.get()
    	cont1=contact.get()
    	email1=email.get()
    	age1=age.get()
    	gvar=gender.get()
    	ads=address.get()
    	st=state.get()
    	cnt = country.get()
    	prog = checkbox1.get(),checkbox2.get(),checkbox3.get(),checkbox4.get(),checkbox5.get(),checkbox6.get()
    	prog = str(prog)
        # connection to database
    	conn = sqlite3.connect('Register1.db')
    	with conn:
    		cursor=conn.cursor()
    		cursor.execute('CREATE TABLE IF NOT EXISTS  Registration(Name TEXT,Contact Text,Email TEXT,Age Text,Gender Number, Address Text, State Text, Country Text,Prog Text)')
    		cursor.execute('INSERT INTO Registration(Name,Contact,Email,Age,Gender,Address,State,Country,Prog) VALUES(?,?,?,?,?,?,?,?,?)',(name1,cont1,email1,age1,gvar,ads,st,cnt,prog))
    	conn.commit()
        #make sure the changes made to the database are consistent
    	
    	#This is for giving confirmation to user who filled the form.
        #successfully form submitted confirmation
    	#getting subject input from sender
    	gmail_user = "sagarnmali3000@gmail.com"
    	gmail_pwd = "Impulse@3000"
    	#getting subject input from sender
    	subject = "About Volunteer application"
    	TEXT = "Form fill sucessfully.\nWe will let you know about you work and timing shortly\nThank You\nThis is a system generated msg, do not reply to it."
    	receiver = []
    	receiver.append(email1)
    	#Finally sending the mails to respective mail id's
    	for ADDR in receiver:
    		message = "\r\n".join(["From:"+gmail_user, "To:"+ADDR, "Subject:"+subject,"", TEXT])
            #puts the connection to the SMTP server
    		try:
    			server = smtplib.SMTP('smtp.gmail.com', 587)
    			server.starttls()
    			server.login(gmail_user, gmail_pwd)
    			server.sendmail(gmail_user,receiver,message)
    		except:
    			print("\n Try Again"); 


# for check-button output display
def view():
        lx = [name.get(),"\n",contact.get(),"\n",email.get(),"\n",
              age.get(),"\n",gender.get(),"\n",address.get(),"\n",state.get(),"\n",country.get(),"\n",checkbox1.get(),"\n",checkbox2.get(),"\n",
              checkbox3.get(),"\n",checkbox4.get(),"\n",checkbox5.get(),"\n",checkbox6.get()]
        messagebox.showinfo("Details",lx)         
        
#GUI

#Creating an instance of Tk initializes this interpreter and creates the root window.  
win = Tk()
#window size
win.geometry("650x800")
#for title bar
photo = PhotoImage(file = "./logo.png")
win.iconphoto(False,photo)

win.title("Volunteer Registration Form")                        
win["bg"] = "sky blue"                     
        
       
#creating data selection variable on gui
name  = StringVar()
contact =StringVar()
email = StringVar()
age = StringVar()
gender = IntVar()
address = StringVar()
state = StringVar()
country = StringVar()
checkbox1 = IntVar()
checkbox2 = IntVar()
checkbox3 = IntVar()
checkbox4 = IntVar()
checkbox5 = IntVar()
checkbox6 = IntVar()
#Form Title
label_title = Label(win,text ="Volunteer Registration Form",width = 30,font = ("bold",20)).place(x=70,y=53)

#Create fields
label_name = Label(win,text = "Name",width = 30).place(x = 70,y = 130)
entry_name = Entry(win,width = 20,textvariable = name)
entry_name.place(x = 240,y = 130)
validate_name = win.register(checkname)  #validation register
entry_name.config(validate = "key",validatecommand = (validate_name,"%P")) #validation configure


label_contact = Label(win,text ="Contact",width = 20).place(x = 70,y = 180)
entry_contact = Entry(win,textvariable = contact,width = 20)
entry_contact.place(x = 240,y = 180)
validate_contact= win.register(checkcontact)  #validation register
entry_contact.config(validate = "key",validatecommand = (validate_contact,"%P"))

label_email = Label(win,text ="Email Id",width = 30).place(x = 70,y = 230)
entry_email = Entry(win,textvariable = email,width = 20)
entry_email.place(x = 240,y = 230)

label_age = Label(win,text = "Your Age",width = 20).place(x = 70,y = 280)
#A Spinbox widget allows you to select a value from a set of values.
entry_age = Spinbox(win,textvariable = age,from_ = 1,to_ = 150 )
entry_age.place(x = 240,y = 280)

label_gender = Label(win,text = "Gender",width = 20).place(x = 70,y = 330)
g_radio_male = Radiobutton(win, text="Male",padx = 5, variable=gender ,value= 1).place(x=240,y=330)
g_radio_female =  Radiobutton(win, text="Female",padx = 20, variable=gender, value= 2).place(x=300,y=330)

label_address = Label(win,text = "Permenant address",width = 20).place(x = 70,y = 380)
entry_address = Entry(win,width = 50,textvariable = address)
entry_address.place(x = 240,y = 380)

label_state = Label(win,text = "State",width = 20).place(x = 70,y = 430)
list1 = ['Maharashtra', 'Rajasthan', 'Madhyapradesh','Kerala', 'Punjab', 'Karnataka', 'Goa', 'Other'];
droplist=OptionMenu(win,state, *list1)
droplist.config(width=15)
state.set('Select your State') 
droplist.place(x=240,y=430)


label_country = Label(win,text = "Country",width = 20).place(x = 70,y = 480)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa', 'Other'];
droplist=OptionMenu(win,country, *list1)
droplist.config(width=15)
country.set('Select your country') 
droplist.place(x=240,y=480)

label_prog = Label(win,text = "Please indicate areas\n to volunteer according\n to your skills",width = 20, height = 3).place(x = 70,y = 530)
entry_check1 = Checkbutton(win, text="Hospital", variable= checkbox1).place(x=240,y=530)
entry_check2 = Checkbutton(win, text="Orphanages", variable= checkbox2).place(x=240,y=560)
entry_check3 = Checkbutton(win, text="School", variable= checkbox3).place(x=240,y=590)
entry_check4 = Checkbutton(win, text="Community Services", variable= checkbox4).place(x=240,y=620)
entry_check5 = Checkbutton(win, text="Computer Classes", variable= checkbox5).place(x=240,y=650)
entry_check6 = Checkbutton(win, text="Art and Entertainment", variable= checkbox6).place(x=240,y=680)


Button(win, text='Submit',width=10,bg='blue',fg='black',command  = validations).place(x=180,y=730)
Button(win, text='Clear Data',width=10,bg='blue',fg='black',command = clear).place(x=50,y=730)
Button(win, text='Check',width=10,bg='blue',fg='black',command = view).place(x=320,y=730)

#tells Python to run the Tkinter event loop
win.mainloop() 
