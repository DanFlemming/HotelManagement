from tkinter import *
import tkinter.messagebox

class login_gui():
	
	def __init__(login):
		print('in login file')

#################################################################################LOGIN
	def login_window(login):
		
		login.login_window = tkinter.Tk()
		login.login_window.title('Login') #creates title

 		#Make label
		login.label1 = tkinter.Label(login.login_window, text ='Login', font=("Helvetica",24))
		login.label1.grid(padx=150)

		#Instructions Label
		login.label2 = tkinter.Label(login.login_window, text ='Hit <enter>', font=("Helvetica",12))
		login.label2.grid(row=3, padx=150)

		#Cancel button
		login.CanButton = tkinter.Button(login.login_window, text='Cancel',\
													width= 18, font= ("Helvetica",12),\
													command= login.login_window.destroy)
		login.CanButton.grid(row=4, padx=25, pady=50, sticky=N)

		#Username Label
		login.label2 = tkinter.Label(login.login_window, text ='Username:', font=("Helvetica",12))
		login.label2.grid(row=1, padx=50, pady=25, sticky=W)
		
		#Username text field
		login.tempUsername = tkinter.Entry(login.login_window, justify=RIGHT, font=("Helvetica",12))
		login.tempUsername.grid(row=1, padx=25, pady=25, sticky=E)
		login.tempUsername.focus_force()# puts blinking cursor on entry box

		#Password label
		login.label3 = tkinter.Label(login.login_window, text = 'Password:', font=("Helvetica",12))
		login.label3.grid(row=2, padx=50, pady=25, sticky=W)

		#Password text field
		login.tempPassword = tkinter.Entry(login.login_window, justify=RIGHT, font=("Helvetica",12))
		login.tempPassword.grid(row=2, padx=25, pady=25, sticky=E)

		#Bind the password to the enter key, then call function
		login.tempPassword.bind('<Return>', login.call_check_login)
			
	
	def check_login(login,tempUsername,tempPassword): 
			
			usernameList = open('Username.txt', 'r').read().split('\n')
			passwordList= open('Password.txt', 'r').read().split('\n')
			usernameList.remove('')
			passwordList.remove('')
		
			print (usernameList)
			print (passwordList)

			if tempUsername in usernameList:
				if tempPassword in passwordList and usernameList.index(tempUsername) == passwordList.index(tempPassword):
						f = open('Rewards.txt', 'a')
						f.write(tempUsername +':' + tempPassword + ':'  + '1' + '\n')
						f.close()
						print(tempUsername + " " + tempPassword + " logged in")
						login.get_rewards(tempUsername,tempPassword)
				else:
					tkinter.messagebox.showinfo(message='Password is not correct')
					login.login_window.lift()
			else:
				tkinter.messagebox.showinfo(message='Username does not exist')
				login.login_window.lift()


		
	#Seperate function needed to call the check_login function
	def call_check_login(login,check_login):
		#Gets the username and password entered 
		tempUsername = login.tempUsername.get()
		tempPassword = login.tempPassword.get()
		login.check_login(tempUsername,tempPassword)		
#########################################################################################LOGIN END	