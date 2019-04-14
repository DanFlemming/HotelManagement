from tkinter import *
import tkinter.messagebox
import AccountCreation 
import Login
import BuyTickets
import os

class my_gui():
	
	def __init__(self):		
		
		self.main_window = tkinter.Tk() #creates main window
		self.main_window.title('Hotel Management System') #creates title
		
		#Hotel Management System
		self.label = tkinter.Label(self.main_window, text ='Hotel Management System', fg='blue', width=25, font=("Helvetica",24))
		self.label.grid(padx=50)
		
		self.label4= tkinter.Label(self.main_window,)
		self.label4.grid()
		#Create the buttons
		#Create account button
		self.CreateAccountButton = tkinter.Button(self.main_window, text = "Create Account",\
												  width= 18, font= ("Helvetica",12), \
												  command = self.create_account)
		self.CreateAccountButton.grid(row=1, padx=25, pady=50, sticky=W)

		#Login button
		my_path = "Username.txt"
		if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
			
			self.LoginButton = tkinter.Button(self.main_window, text= 'Login',\
											  width= 18, font=("Helvetica",12), state=NORMAL,\
											  command = self.login_window)
			self.LoginButton.grid(row=1, pady=50, sticky=N )
		
		else:
			self.LoginButton = tkinter.Button(self.main_window, text= 'Login',\
											  width= 18, font=("Helvetica",12), state=DISABLED,\
											  command = self.login_window)
			self.LoginButton.grid(row=1, pady=50, sticky=N )

		#Cancel button
		self.CancelButton = tkinter.Button(self.main_window, text='Cancel',\
											width= 18, font= ("Helvetica",12),\
											command= self.main_window.destroy)
		self.CancelButton.grid(row=1, padx=25, pady=50, sticky=E)

		tkinter.mainloop()
			

#################################################################
#FUNCTION CALLS FROM ACCOUNTCREATION FILE
	def create_account(acct):
		AccountCreation.create_account.create_username(acct)

	def check_username(acct,usernameList):
		AccountCreation.create_account.check_username(acct,usernameList)

	def save_username(acct,userName):
		AccountCreation.create_account.save_username(acct,userName)

	def create_password(acct):
		AccountCreation.create_account.create_password(acct)

	def password_check(acct,password):
		AccountCreation.create_account.password_check(acct,password)

	def save_password(acct,passWord):
		AccountCreation.create_account.save_password(acct,passWord)

#FUNCTION CALLS FROM LOGIN FILE
	def login_window(login):
		Login.login_gui.login_window(login)
	
	def check_login(login,tempUsername,tempPassword):
		Login.login_gui.check_login(login,tempUsername,tempPassword)

	def call_check_login(login,check_login):
		Login.login_gui.call_check_login(login,check_login)

#FUNCTION CALLS FROM BUYTICKETS FILE
	def buy_tickets(tick):
		BuyTickets.tickets_gui.buy_tickets(tick)
	
	def display_rooms(tick):
		BuyTickets.tickets_gui.display_rooms(tick)

	def check_GFrooms(tick):
		BuyTickets.tickets_gui.check_GFrooms(tick)

	def check_SFrooms(tick):
		BuyTickets.tickets_gui.check_SFrooms(tick)

	def check_TFrooms(tick):
		BuyTickets.tickets_gui.check_TFrooms(tick)
	
	def GFmenu_click(tick):
		BuyTickets.tickets_gui.GFmenu_click(tick)

	def SFmenu_click(tick):
		BuyTickets.tickets_gui.SFmenu_click(tick)

	def TFmenu_click(tick):
		BuyTickets.tickets_gui.TFmenu_click(tick)
	
	def GF_soldOut(tick):
		BuyTickets.tickets_gui.GF_soldOut(tick)

	def SF_soldOut(tick):
		BuyTickets.tickets_gui.SF_soldOut(tick)

	def TF_soldOut(tick):
		BuyTickets.tickets_gui.TF_soldOut(tick)

	def hotel_soldOut(tick):
		BuyTickets.tickets_gui.hotel_soldOut(tick)

	def get_rewards(tick,tempUsername,tempPassword):
		BuyTickets.tickets_gui.get_rewards(tick,tempUsername,tempPassword)

	def send_email(tick):
		BuyTickets.tickets_gui.send_email(tick)

##################################################################	
				
			
MyGui = my_gui()

