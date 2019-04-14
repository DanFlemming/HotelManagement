from tkinter import *
import tkinter.messagebox

class create_account():
	
	def __init__(acct):
		
		print('in account file')

################################################################################CREATE USERNAME
	def create_username(acct):
		
		acct.UserName = tkinter.Tk()
		acct.UserName.title('Create Account') #creates title

		#Make label
		acct.label1 = tkinter.Label(acct.UserName, text ='Create Account', font=("Helvetica",24))
		acct.label1.grid(padx=100)

		#Username Label
		acct.label2 = tkinter.Label(acct.UserName, text ='Choose a Username:', font=("Helvetica",12))
		acct.label2.grid(row=1, padx=50, pady=25, sticky=W)
		
		#Username text field
		acct.username = tkinter.Entry(acct.UserName, justify=RIGHT, font=("Helvetica",12))
		acct.username.grid(row=1, padx=25, pady=25, sticky=E)
		
		#Bind the username to the enter key, then call function
		acct.username.bind('<Return>', acct.check_username)
		acct.username.focus_force()# puts blinking cursor on entry box
		
	def check_username(acct,username):
		print ("Checking for unique username")
		userName = acct.username.get()
		
		f = open('Username.txt', 'a')
		acct.usernameList = open('Username.txt', 'r').read().split('\n')
	
		if userName in acct.usernameList:
			tkinter.messagebox.showinfo(message=("Username " + userName + " already exists "))
			acct.username.delete(0,END)
			acct.UserName.lift()
			acct.username.focus_force()
			f.close()
		else:
			acct.save_username(userName)
	
	#Write username to file	
	def save_username(acct,userName):
		f = open('Username.txt', 'a')
		f.write(userName+ '\n')
		f.close()
		acct.create_password()
		print('Username Created')

####################################################################################CREATE USERNAME END	

#####################################################################################CREATE PASSWORD
	def create_password(acct):

		#Destroy previous screen
		acct.label1.destroy()
		acct.label2.destroy()
		acct.username.destroy()

		#Make new screen morph design
		acct.label1 = tkinter.Label(acct.UserName, text ='Create Password', font=("Helvetica",24))
		acct.label1.grid(padx=100)

		#Password directions
		acct.label2 = tkinter.Label(acct.UserName, text ='Create a password of at least nine (9) characters,', font=("Helvetica",12))
		acct.label2.grid(row=1, padx=50, sticky=N)

		acct.label3 = tkinter.Label(acct.UserName, text ='that contains at least one digit, one uppercase,', font=("Helvetica",12))
		acct.label3.grid (row=2, padx=50, sticky=N)

		acct.label4 = tkinter.Label(acct.UserName, text ='and one lowercase letter.', font=("Helvetica",12))
		acct.label4.grid (row=3, padx=50, sticky=N)

		#Password text
		acct.label5 = tkinter.Label(acct.UserName, text ='Password:', font=("Helvetica",12))
		acct.label5.grid(row=4, padx=50, pady=25, sticky=W)

		#Password text field
		acct.password = tkinter.Entry(acct.UserName, justify=RIGHT,  font=("Helvetica",12)) #show="*", 
		acct.password.grid(row=4, padx=25, pady=25, sticky=E)

		#Bind the username to the enter key, then call function
		acct.password.bind('<Return>', acct.password_check)
		acct.password.focus_force()# puts blinking cursor on entry box
	


	#Check if password meets requirements	
	def password_check(acct,password):	

		print('Going through password check')
		passWord = acct.password.get()

		notvalid = True
		while notvalid:
			if (len(passWord)<9):
				tkinter.messagebox.showinfo(message='Password length must be at least 9')
				acct.password.delete(0,END)
				acct.UserName.lift()
				acct.password.focus_force()
				break
			elif not re.search("[a-z]",passWord):
				tkinter.messagebox.showinfo(message='Password must have a lowercase letter')
				acct.password.delete(0,END)
				acct.UserName.lift()
				acct.password.focus_force()
				break
			elif not re.search("[0-9]",passWord):
				tkinter.messagebox.showinfo(message='Password must have a number')
				acct.password.delete(0,END)
				acct.UserName.lift()
				acct.password.focus_force()
				break
			elif not re.search("[A-Z]",passWord):
				tkinter.messagebox.showinfo(message='Password must have a capital letter')
				acct.password.delete(0,END)
				acct.UserName.lift()
				acct.password.focus_force()
				break
			elif re.search("\s",passWord):
				break
			else:
				tkinter.messagebox.showinfo(message='Account Created! Press ok, then login')
				notvalid=False
				break
		
		
		#When password is valid make the login button enabled and save password
		if notvalid == False:
			acct.save_password(passWord)

	
	#Write the password to a file 
	def save_password(acct,passWord):
		
		f = open('Password.txt', 'a')
		#f.write(passWord, userName to same file to compare if account exists)
		f.write(passWord + '\n')
		f.close()
		print('Password Created ')
		
		#Destroy window and make login available,disable create account
		acct.UserName.destroy()
		acct.CreateAccountButton['state']=DISABLED
		acct.LoginButton['state']=NORMAL
#################################################################################CREATE PASSWORD END
