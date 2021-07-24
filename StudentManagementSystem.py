# ------------------------  Command Function  --------------------------------------

def dt():
				str_date = time.strftime('%d/%m/%Y')
				str_time = time.strftime('%I:%M:%S %p')
				datetime.config(text='Date :' + ' ' + str_date + '\n' + 'Time :' + ' ' + str_time)
				datetime.after(200, dt)


def Connectdb():
				def connectMySql():
								global mydb, mycursor
								host = hostvar1.get()
								user = uservar1.get()
								password = passwordvar1.get()
								# host = 'localhost'
								# user = 'root'
								# password = 'Satya@268'
								try:
												mydb = pymysql.connect(host=host, user=user, password=password)
												messagebox.showinfo(title='Connected', message='You are connected to DataBase Successfully')
												mycursor = mydb.cursor()
								
								except:
												messagebox.showerror(title='Notification', message='Data incorrect please try again', parent=dbroot)
												return
								try:
												strr = 'create database StudentManagementSystem'
												mycursor.execute(strr)
												strr = 'use StudentManagementSystem'
												mycursor.execute(strr)
												strr = 'create table StudentData(ID int,NAME varchar(50),MOBILE varchar(12),EMAIL varchar(50),ADDRESS varchar(150),GENDER varchar(10),DOB varchar(50),DATE varchar(50),TIME varchar(50))'
												mycursor.execute(strr)
												strr = 'alter table studentdata modify column id int  not null'
												mycursor.execute(strr)
												strr = 'alter table studentdata modify column id int primary key'
												mycursor.execute(strr)
												dbroot.destroy()
								
								
								except:
												strr = 'use StudentManagementSystem'
												mycursor.execute(strr)
												
												dbroot.destroy()
				
				dbroot = Toplevel()
				dbroot.grab_set()
				dbroot.title('Connect To DataBase')
				# dbroot.iconbitmap('mana.ico')
				dbroot.config(bg='blue')
				dbroot.geometry('470x250+800+230')
				dbroot.resizable(False, False)
				# ---------------- Button of Connect DataBase   Labels -----------------------
				
				hostlable = Label(dbroot, text='Enter Host Name :', bg='gold', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				hostlable.place(x=10, y=10)
				
				userlable = Label(dbroot, text='Enter User Name :', bg='gold', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				userlable.place(x=10, y=60)
				
				passwordlable = Label(dbroot, text='Enter Password  :', bg='gold', font='arial 14 bold', width=14, anchor='w',
				                      relief=RIDGE, borderwidth=4)
				passwordlable.place(x=10, y=110)
				
				# ---------------- Button of Connect DataBase  Entry  -----------------------
				
				hostvar1 = StringVar()
				uservar1 = StringVar()
				passwordvar1 = StringVar()
				
				hostentry = Entry(dbroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=hostvar1)
				hostentry.place(x=230, y=10)
				
				userentry = Entry(dbroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=uservar1)
				userentry.place(x=230, y=60)
				
				passwordentry = Entry(dbroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=passwordvar1)
				passwordentry.place(x=230, y=110)
				
				# ---------------------- Submit to DataBase ------------------------------------------
				
				submitbutton = Button(dbroot, text='Connect', width=14, borderwidth=4, relief=GROOVE, font='arial 14 bold',
				                      bg='red', activebackground='lawn green', activeforeground='black', command=connectMySql)
				submitbutton.place(x=150, y=190)
				
				dbroot.mainloop()


#  ----------------------------  DataBase Operation Function --------------------------------


def AddStudent():
				def addstudent():
								id = idvar.get()
								name = namevar.get()
								mobile = mobilevar.get()
								email = emailvar.get()
								address = addressvar.get()
								gender = gendervar.get()
								dob = dobvar.get()
								date = time.strftime('%d/%m/%Y')
								timee = time.strftime('%I:%M %p')
								
								try:
												strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
												mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, date, timee))
												mydb.commit()
												ask = messagebox.askyesnocancel('Notification',
												                                '{} Data Has been Inserted Successfully...\n Do You want to reset the form '.format(
																                                name), parent=addroot)
												if (ask == True):
																idvar.set(' ')
																namevar.set(' ')
																mobilevar.set(' ')
																emailvar.set(' ')
																addressvar.set(' ')
																gendervar.set(' ')
																dobvar.set(' ')
								
								except:
												messagebox.showerror('Notification', 'Id Already Exist, Try another Id', parent=addroot)
								
								strr = 'select * from studentdata'
								mycursor.execute(strr)
								datas = mycursor.fetchall()
								ShowDataFrame.delete(*ShowDataFrame.get_children())
								for i in datas:
												varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
												ShowDataFrame.insert('', END, values=varr)
				
				addroot = Toplevel()
				addroot.geometry('450x410+230+210')
				addroot.resizable(False, False)
				addroot.title('Add Student')
				# addroot.iconbitmap('mana.ico')
				addroot.config(bg='blue')
				addroot.grab_set()
				
				# --------------------       Labels       ---------------------
				
				idlabel = Label(addroot, text='Enter Id  :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                relief=RIDGE, borderwidth=4)
				idlabel.place(x=10, y=10)
				
				namelabel = Label(addroot, text='Enter Name : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				namelabel.place(x=10, y=60)
				
				mobilelabel = Label(addroot, text='Enter Mobile :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				mobilelabel.place(x=10, y=110)
				
				emaillabel = Label(addroot, text='Enter Email :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                   relief=RIDGE, borderwidth=4)
				emaillabel.place(x=10, y=160)
				
				addresslabel = Label(addroot, text='Enter Address :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                     relief=RIDGE, borderwidth=4)
				addresslabel.place(x=10, y=210)
				
				genderlabel = Label(addroot, text='Enter Gender :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				genderlabel.place(x=10, y=260)
				
				doblabel = Label(addroot, text='Enter D.O.B : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                 relief=RIDGE, borderwidth=4)
				doblabel.place(x=10, y=310)
				
				# -----------------------------Entry ---------------------------------------------
				
				idvar = StringVar()
				namevar = StringVar()
				mobilevar = StringVar()
				emailvar = StringVar()
				addressvar = StringVar()
				gendervar = StringVar()
				dobvar = StringVar()
				
				identry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=idvar)
				identry.place(x=210, y=10)
				
				nameentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=namevar)
				nameentry.place(x=210, y=60)
				
				mobileentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=mobilevar)
				mobileentry.place(x=210, y=110)
				
				emailentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=emailvar)
				emailentry.place(x=210, y=160)
				
				addressentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=addressvar)
				addressentry.place(x=210, y=210)
				
				genderentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=gendervar)
				genderentry.place(x=210, y=260)
				
				dobentry = Entry(addroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=dobvar)
				dobentry.place(x=210, y=310)
				
				# -----------------------------------   Buttons  -   -------------------------------------
				
				Entrybtn = Button(addroot, text='ENTRY', width=10, font='arial 14 bold', relief=RIDGE, command=addstudent)
				Entrybtn.place(x=150, y=360)
				
				addroot.mainloop()


def SearchStudent():
				def search():
								id = idvar.get()
								name = namevar.get()
								mobile = mobilevar.get()
								email = emailvar.get()
								address = addressvar.get()
								gender = gendervar.get()
								dob = dobvar.get()
								date = datevar.get()
								
								if (id != ''):
												strr = 'select * from studentdata where id=%s'
												mycursor.execute(strr, (id))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (name != ''):
												strr = 'select * from studentdata where name=%s'
												mycursor.execute(strr, (name))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (mobile != ''):
												strr = 'select * from studentdata where mobile=%s'
												mycursor.execute(strr, (mobile))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (email != ''):
												strr = 'select * from studentdata where email=%s'
												mycursor.execute(strr, (email))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (address != ''):
												strr = 'select * from studentdata where address=%s'
												mycursor.execute(strr, (address))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (gender != ''):
												strr = 'select * from studentdata where gender=%s'
												mycursor.execute(strr, (gender))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (dob != ''):
												strr = 'select * from studentdata where dob=%s'
												mycursor.execute(strr, (dob))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
								elif (date != ''):
												strr = 'select * from studentdata where date=%s'
												mycursor.execute(strr, (date))
												datas = mycursor.fetchall()
												ShowDataFrame.delete(*ShowDataFrame.get_children())
												for i in datas:
																varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
																ShowDataFrame.insert('', END, values=varr)
				
				searchroot = Toplevel()
				searchroot.geometry('450x490+230+210')
				searchroot.resizable(False, False)
				searchroot.config(bg='blue')
				searchroot.title('Search Student')
				# searchroot.iconbitmap('mana.ico')
				searchroot.grab_set()
				
				# --------------------       Labels       ---------------------
				
				idlabel = Label(searchroot, text='Enter Id  :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                relief=RIDGE, borderwidth=4)
				idlabel.place(x=10, y=10)
				
				namelabel = Label(searchroot, text='Enter Name : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				namelabel.place(x=10, y=60)
				
				mobilelabel = Label(searchroot, text='Enter Mobile :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				mobilelabel.place(x=10, y=110)
				
				emaillabel = Label(searchroot, text='Enter Email :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                   relief=RIDGE, borderwidth=4)
				emaillabel.place(x=10, y=160)
				
				addresslabel = Label(searchroot, text='Enter Address :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                     relief=RIDGE, borderwidth=4)
				addresslabel.place(x=10, y=210)
				
				genderlabel = Label(searchroot, text='Enter Gender :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				genderlabel.place(x=10, y=260)
				
				doblabel = Label(searchroot, text='Enter D.O.B : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                 relief=RIDGE, borderwidth=4)
				doblabel.place(x=10, y=310)
				
				datelabel = Label(searchroot, text='Enter Date: ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				datelabel.place(x=10, y=360)
				
				# -----------------------------Entry ---------------------------------------------
				
				idvar = StringVar()
				namevar = StringVar()
				mobilevar = StringVar()
				emailvar = StringVar()
				addressvar = StringVar()
				gendervar = StringVar()
				dobvar = StringVar()
				datevar = StringVar()
				
				identry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=idvar)
				identry.place(x=210, y=10)
				
				nameentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=namevar)
				nameentry.place(x=210, y=60)
				
				mobileentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=mobilevar)
				mobileentry.place(x=210, y=110)
				
				emailentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=emailvar)
				emailentry.place(x=210, y=160)
				
				addressentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=addressvar)
				addressentry.place(x=210, y=210)
				
				genderentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=gendervar)
				genderentry.place(x=210, y=260)
				
				dobentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=dobvar)
				dobentry.place(x=210, y=310)
				
				dateentry = Entry(searchroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=datevar)
				dateentry.place(x=210, y=360)
				
				# -----------------------------------   Buttons  -   -------------------------------------
				
				searchbtn = Button(searchroot, text='SEARCH', width=10, font='arial 14 bold', relief=RIDGE, command=search)
				searchbtn.place(x=150, y=420)
				
				searchroot.mainloop()


def RemoveStudent():
				cc = ShowDataFrame.focus()
				content = ShowDataFrame.item(cc)
				pp = content['values'][0]
				strr = 'delete from studentdata where id=%s'
				mycursor.execute(strr, (pp))
				mydb.commit()
				messagebox.showinfo('Notification', '{} Removed Successfully...'.format(pp))
				strr = 'select * from studentdata '
				mycursor.execute(strr)
				datas = mycursor.fetchall()
				ShowDataFrame.delete(*ShowDataFrame.get_children())
				for i in datas:
								varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
								ShowDataFrame.insert('', END, values=varr)


def UpdateStudent():
				def update():
								id = idvar.get()
								name = namevar.get()
								mobile = mobilevar.get()
								email = emailvar.get()
								address = addressvar.get()
								gender = gendervar.get()
								dob = dobvar.get()
								date = datevar.get()
								time = timevar.get()
								
								strr = ' update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
								mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
								mydb.commit()
								
								strr = 'select * from studentdata '
								mycursor.execute(strr)
								datas = mycursor.fetchall()
								ShowDataFrame.delete(*ShowDataFrame.get_children())
								for i in datas:
												varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
												print(varr)
												ShowDataFrame.insert('', END, values=varr)
								messagebox.showinfo('Notification', '{} Updated Successfully..'.format(id), parent=updateroot)
				
				updateroot = Toplevel()
				updateroot.geometry('450x500+230+210')
				updateroot.resizable(False, False)
				updateroot.config(bg='blue')
				updateroot.title('update Student')
				# updateroot.iconbitmap('mana.ico')
				updateroot.grab_set()
				
				# --------------------       Labels       ---------------------
				
				idlabel = Label(updateroot, text='Enter Id  :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                relief=RIDGE, borderwidth=4)
				idlabel.place(x=10, y=10)
				
				namelabel = Label(updateroot, text='Enter Name : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				namelabel.place(x=10, y=60)
				
				mobilelabel = Label(updateroot, text='Enter Mobile :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				mobilelabel.place(x=10, y=110)
				
				emaillabel = Label(updateroot, text='Enter Email :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                   relief=RIDGE, borderwidth=4)
				emaillabel.place(x=10, y=160)
				
				addresslabel = Label(updateroot, text='Enter Address :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                     relief=RIDGE, borderwidth=4)
				addresslabel.place(x=10, y=210)
				
				genderlabel = Label(updateroot, text='Enter Gender :', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                    relief=RIDGE, borderwidth=4)
				genderlabel.place(x=10, y=260)
				
				doblabel = Label(updateroot, text='Enter D.O.B : ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                 relief=RIDGE, borderwidth=4)
				doblabel.place(x=10, y=310)
				
				datelabel = Label(updateroot, text='Enter Date: ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				datelabel.place(x=10, y=360)
				
				datelabel = Label(updateroot, text='Enter Time: ', bg='gold2', font='arial 14 bold', width=14, anchor='w',
				                  relief=RIDGE, borderwidth=4)
				datelabel.place(x=10, y=410)
				
				# -----------------------------Entry ---------------------------------------------
				
				idvar = StringVar()
				namevar = StringVar()
				mobilevar = StringVar()
				emailvar = StringVar()
				addressvar = StringVar()
				gendervar = StringVar()
				dobvar = StringVar()
				datevar = StringVar()
				timevar = StringVar()
				
				identry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=idvar)
				identry.place(x=210, y=10)
				
				nameentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=namevar)
				nameentry.place(x=210, y=60)
				
				mobileentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=mobilevar)
				mobileentry.place(x=210, y=110)
				
				emailentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=emailvar)
				emailentry.place(x=210, y=160)
				
				addressentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=addressvar)
				addressentry.place(x=210, y=210)
				
				genderentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=gendervar)
				genderentry.place(x=210, y=260)
				
				dobentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=dobvar)
				dobentry.place(x=210, y=310)
				
				dateentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=datevar)
				dateentry.place(x=210, y=360)
				
				timeentry = Entry(updateroot, font='arial 14 bold', relief=RIDGE, borderwidth=4, textvariable=timevar)
				timeentry.place(x=210, y=410)
				
				# -----------------------------------   Buttons  -   -------------------------------------
				
				updatebtn = Button(updateroot, text='Update', width=10, font='arial 14 bold', relief=RIDGE, command=update)
				updatebtn.place(x=150, y=450)
				
				cc = ShowDataFrame.focus()
				content = ShowDataFrame.item(cc)
				pp = content['values']
				if (len(pp) != 0):
								idvar.set(pp[0])
								namevar.set(pp[1])
								mobilevar.set(pp[2])
								emailvar.set(pp[3])
								addressvar.set(pp[4])
								gendervar.set(pp[5])
								dobvar.set(pp[6])
								datevar.set(pp[7])
								timevar.set(pp[8])
				
				updateroot.mainloop()


def ShowStudent():
				strr = 'select * from studentdata '
				mycursor.execute(strr)
				datas = mycursor.fetchall()
				ShowDataFrame.delete(*ShowDataFrame.get_children())
				for i in datas:
								varr = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
								ShowDataFrame.insert('', END, values=varr)


def ExportData():
				gg = filedialog.asksaveasfilename()
				ss = ShowDataFrame.get_children()
				id, name, mobile, email, address, gender, dob, date, time = [], [], [], [], [], [], [], [], []
				for i in ss:
								content = ShowDataFrame.item(i)
								pp = content['values']
								id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(
												pp[4]), gender.append(pp[5]), dob.append(pp[6]), date.append(pp[7]), time.append(pp[8])
				dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Date', 'Time']
				df = pd.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, date, time)), columns=dd)
				paths = r'{}.csv'.format(gg)
				df.to_csv(paths, index=False)
				messagebox.showinfo('Notification', 'Student-Data saved at {}'.format(paths))



def exit():
				ask = messagebox.askyesno('Notification','Do you want to exit....')
				if(ask==True):
								root.destroy()

# ------------------  Import  ----------------------------------
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox, Toplevel, filedialog
import pymysql
import time
import pandas as pd

root = Tk()

# ------------------------------Window Sizing------------------------------- #

root.title('Student Management System')
# root.iconbitmap('')
root.config(bg='gold2')
root.geometry('1174x700+200+70')
root.resizable(False, False)

# --------------------------Creating Frames----------------------------------#

mainFrame = Frame(root, bg='gold2', borderwidth=5, relief=GROOVE)
mainFrame.place(x=20, y=100, width=480, height=560)

dataFrame = Frame(root, bg='gold2', borderwidth=5, relief=GROOVE)
dataFrame.place(x=550, y=100, width=600, height=560)

# ------------------------- MainFrame Command ------------------------------------

dataLabel = Label(mainFrame, text='--------------Welcome------------', bg='gold2', font='arial 16 bold')
dataLabel.pack(side=TOP, expand=True)

addbtn = Button(mainFrame, text='Add Student', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                bg='skyblue', activebackground='lawn green', activeforeground='black', command=AddStudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(mainFrame, text='Search Student', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                   bg='skyblue', activebackground='lawn green', activeforeground='black', command=SearchStudent)
searchbtn.pack(side=TOP, expand=True)

removebtn = Button(mainFrame, text='Remove Student', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                   bg='skyblue', activebackground='lawn green', activeforeground='black', command=RemoveStudent)
removebtn.pack(side=TOP, expand=True)

updatebtn = Button(mainFrame, text='Update Student', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                   bg='skyblue', activebackground='lawn green', activeforeground='black', command=UpdateStudent)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(mainFrame, text='Show All Student', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                    bg='skyblue', activebackground='lawn green', activeforeground='black', command=ShowStudent)
showallbtn.pack(side=TOP, expand=True)

exportbtn = Button(mainFrame, text='Export Data', font='times 14 bold', width=20, relief=RIDGE, borderwidth=4,
                   bg='skyblue', activebackground='lawn green', activeforeground='black', command=ExportData)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(mainFrame, text='Exit', borderwidth=4, relief=RIDGE, bg='skyblue', command=exit, font='times 14 bold',
                 width=20, activebackground='lawn green', activeforeground='black')
exitbtn.pack(side=TOP, expand=True)

# -------------------------------- Data Frame --------------------------------

style = ttk.Style()
style.configure('Treeview.Heading', font='Times 16 bold', foreground='red', background='green')
style.configure('Treeview', font='dosis  12 bold')

scroll_x = Scrollbar(dataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(dataFrame, orient=VERTICAL)

ShowDataFrame = Treeview(dataFrame,
                         columns=('Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Date', 'Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=ShowDataFrame.xview)
scroll_y.config(command=ShowDataFrame.yview)

ShowDataFrame.heading('Id', text='Id')
ShowDataFrame.heading('Name', text='Name')
ShowDataFrame.heading('Mobile', text='Mobile')
ShowDataFrame.heading('Email', text='Email')
ShowDataFrame.heading('Address', text='Address')
ShowDataFrame.heading('Gender', text='Gender')
ShowDataFrame.heading('D.O.B', text='D.O.B')
ShowDataFrame.heading('Date', text='Date')
ShowDataFrame.heading('Time', text='Time')

ShowDataFrame['show'] = 'headings'

ShowDataFrame.column('Id', width=150)
ShowDataFrame.column('Name', width=300)
ShowDataFrame.column('Mobile', width=150)
ShowDataFrame.column('Email', width=300)
ShowDataFrame.column('Address', width=300)
ShowDataFrame.column('Gender', width=150)
ShowDataFrame.column('D.O.B', width=150)
ShowDataFrame.column('Date', width=150)
ShowDataFrame.column('Time', width=150)

ShowDataFrame.pack(fill=BOTH, expand=1)

# --------------------------------- Heading --------------------------------------

heading1 = Label(root, text='Welcome to Student Management System', font='arial 16 bold', bg='cyan', borderwidth=4,
                 relief=GROOVE)
heading1.place(x=350, y=10, width=450, height=40)

heading2 = Label(root, text='Trident Academy Of Technology , Bhubaneswar', font='arial 10 bold', bg='gold2')
heading2.place(x=350, y=50, width=450, height=40)

heading3 = Label(root, text='Design and Developed by Mr. Satyabrata Ojha', font='arial 8 ', bg='gold2')
heading3.place(x=350, y=660, width=450, height=50)

# ---------------------------------  Date and Time ------------------------------------

datetime = Label(root, font='times 14 bold', relief=RIDGE, borderwidth=4, bg='lawn green')
datetime.place(x=20, y=10)
dt()

# -----------------------------   Buttons        ----------------------------------------

ConnectButton = Button(root, text='Connect To Database', bg='lawn green', font='times 16 bold', relief=RIDGE,
                       borderwidth=4, command=Connectdb)

ConnectButton.place(x=935, y=10)

root.mainloop()
