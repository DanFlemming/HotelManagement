from tkinter import *
import tkinter.messagebox
import Login
import smtplib

class tickets_gui():
	
	def __init__(tick):
		print('in BuyTickets')
		
	
	def buy_tickets(tick):
		print('buy tickets window')

		#delete the main window stuff
		tick.login_window.destroy()
		tick.label.destroy()
		tick.CreateAccountButton.destroy()
		tick.LoginButton.destroy()
		tick.CancelButton.destroy()

		#Amount of rooms avalible
		tick.roomsLeft = 48
		tick.soldOut = False
		tick.GFsoldOut = False
		tick.SFsoldOut = False
		tick.TFsoldOut = False
		
		#Ground Floor arrays
		tick.GFkingRoom = [59,59,59,59]
		tick.GFtwinRoom = [69,69]
		tick.GFdeluxeKing = [75,75,75,75]
		tick.GFcornerKing = [90,90,90,90]
		tick.GFcornerSuite = [110,110]
		tick.GFroomArray = [tick.GFkingRoom,tick.GFtwinRoom,tick.GFdeluxeKing,tick.GFcornerKing,tick.GFcornerSuite] 

		#Second Floor arrays
		tick.SFkingRoom = [59,59,59,59]
		tick.SFtwinRoom = [69,69]
		tick.SFdeluxeKing = [75,75,75,75]
		tick.SFcornerKing = [90,90,90,90]
		tick.SFcornerSuite = [110,110]
		tick.SFroomArray = [tick.SFkingRoom,tick.SFtwinRoom,tick.SFdeluxeKing,tick.SFcornerKing,tick.SFcornerSuite] 

		#Third Floor arrays
		tick.TFkingRoom = [59,59,59,59]
		tick.TFtwinRoom = [69,69]
		tick.TFdeluxeKing = [75,75,75,75]
		tick.TFcornerKing = [90,90,90,90]
		tick.TFcornerSuite = [110,110]
		tick.TFroomArray = [tick.TFkingRoom,tick.TFtwinRoom,tick.TFdeluxeKing,tick.TFcornerKing,tick.TFcornerSuite] 
		tick.roomArray = [tick.GFroomArray,tick.SFroomArray,tick.TFroomArray]
		
		#tick.get_rewards(tempUsername,tempPassword)
		tick.display_rooms()
		
	def display_rooms(tick):
		print('Rooms being displayed')
		#Create new window layout
		#Hotel Reservation System
		tick.label = tkinter.Label(tick.main_window, text ='Hotel Reservation System', fg='blue', width=25, font=("Helvetica",24))
		tick.label.grid(row=0, column=0, padx=50)
		tick.main_window.title('Hotel Reservation System') #creates title

		
		#Get the image 
		photo = PhotoImage(file = "HotelPlan.gif")
		tick.labelGIF = tkinter.Label(image = photo)
		tick.labelGIF.image = photo
		tick.labelGIF.grid(row=1, column=0,sticky= N+S+E+W, padx=25, pady=25, rowspan=12)
		
		#Label
		tick.label1 = tkinter.Label(tick.main_window, text= 'Select Floor',\
										  width= 18, font=("Helvetica",16))
		tick.label1.grid(row=2, column=3)

		
		#Menu for Ground floor
		tick.optionList=['King Room   $59.00', 'Twin Room   $69.00',\
					'Deluxe King   $75.00', 'Corner King   $90.00', 'Corner Suite   $110.00','Sold Out']
		
		tick.option_var = tkinter.StringVar()
		tick.option_var.set('Ground Floor') 
		tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
		tick.option_menu.grid(row=3, column=3, padx=25, pady=25)

		#Menu for Second floor
		tick.optionList1=['King Room   $59.00', 'Twin Room   $69.00',\
					'Deluxe King   $75.00', 'Corner King   $90.00', 'Corner Suite   $110.00','Sold Out']
		
		tick.option_var1 = tkinter.StringVar()
		tick.option_var1.set('Second Floor') 
		tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command=lambda _: tick.SFmenu_click())
		tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)

		#Menu for Third floor
		tick.optionList2=['King Room   $59.00', 'Twin Room   $69.00',\
					'Deluxe King   $75.00', 'Corner King   $90.00', 'Corner Suite   $110.00','Sold Out']
		
		tick.option_var2 = tkinter.StringVar()
		tick.option_var2.set('Third Floor') 
		tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command=lambda _: tick.TFmenu_click())
		tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)


###################################################### Check the GF rooms ##############################################################################		

	
	def check_GFrooms(tick):
		
		tick.chosenRoom = tick.option_var.get()

		if  tick.chosenRoom == 'King Room   $59.00' and len(tick.GFkingRoom)>0 and tick.GFsoldOut==False:
			print('chose the king room') 
		
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.GFkingRoom.pop()
				tick.option_var.set('Ground Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
				#tick.send_email()
			
			if 59 not in tick.GFkingRoom :
				tkinter.messagebox.showerror(message=tick.chosenRoom+' IS NOW SOLD OUT')
				tick.option_menu.destroy()
				tick.optionList.remove('King Room   $59.00')
				tick.option_var.set('Ground Floor')
				tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
				tick.option_menu.grid(row=3, column=3, padx=25, pady=25)
				tick.GF_soldOut()
			print(tick.GFkingRoom)
	

		elif tick.chosenRoom == 'Twin Room   $69.00' and 69 in tick.GFtwinRoom and tick.GFsoldOut==False:
			print("chose the twin room")

			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.GFtwinRoom.pop()
				tick.option_var.set('Ground Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 69 not in tick.GFtwinRoom:
				tkinter.messagebox.showerror(message=tick.chosenRoom+' IS NOW SOLD OUT')
				tick.optionList.remove('Twin Room   $69.00')
				tick.option_menu.destroy()
				tick.option_var.set('Ground Floor')
				tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
				tick.option_menu.grid(row=3, column=3, padx=25, pady=25)
				tick.GF_soldOut()	
			print(tick.GFtwinRoom)
				
		elif tick.chosenRoom == 'Deluxe King   $75.00' and 75 in tick.GFdeluxeKing and tick.GFsoldOut==False:
			print('chose the deluxe king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.GFdeluxeKing.pop()
				tick.option_var.set('Ground Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 75 not in tick.GFdeluxeKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom+' IS NOW SOLD OUT')
				tick.optionList.remove('Deluxe King   $75.00')
				tick.option_menu.destroy()
				tick.option_var.set('Ground Floor') 
				tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
				tick.option_menu.grid(row=3, column=3, padx=25, pady=25)
				tick.GF_soldOut()	
			print(tick.GFdeluxeKing)
			

		elif tick.chosenRoom == 'Corner King   $90.00' and 90 in tick.GFcornerKing and tick.GFsoldOut==False:
			print ('chose the corner king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.GFcornerKing.pop()
				tick.option_var.set('Ground Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 90 not in tick.GFcornerKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom+' IS NOW SOLD OUT')
				tick.optionList.remove('Corner King   $90.00')
				tick.option_menu.destroy()
				tick.option_var.set('Ground Floor') 
				tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
				tick.option_menu.grid(row=3, column=3, padx=25, pady=25)
				tick.GF_soldOut()
			print(tick.GFcornerKing)
			

		elif tick.chosenRoom == 'Corner Suite   $110.00' and 110 in tick.GFcornerSuite and tick.GFsoldOut==False:
			print('chose the corner suite room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.GFcornerSuite.pop()
				tick.option_var.set('Ground Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")

			if 110 not in tick.GFcornerSuite:
				tkinter.messagebox.showerror(message=tick.chosenRoom+' IS NOW SOLD OUT')
				tick.optionList.remove('Corner Suite   $110.00')
				tick.option_menu.destroy()
				tick.option_var.set('Ground Floor')
				tick.option_menu = tkinter.OptionMenu(tick.main_window, tick.option_var, *tick.optionList, command=lambda _: tick.GFmenu_click())
				tick.option_menu.grid(row=3, column=3, padx=25, pady=25)
				tick.GF_soldOut()	
			print(tick.GFcornerSuite)
			
		else:
			tkinter.messagebox.showerror(message='No room chosen')


################################################# Check SF Rooms ########################################################################
	
	def check_SFrooms(tick):
		tick.chosenRoom1 = tick.option_var1.get()	

		if  tick.chosenRoom1 == 'King Room   $59.00' and len(tick.SFkingRoom)>0 and tick.SFsoldOut==False:
			print('chose the king room') 
		
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.SFkingRoom.pop()
				tick.option_var1.set('Second Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
				
			if 59 not in tick.SFkingRoom :
				tkinter.messagebox.showerror(message=tick.chosenRoom1+' IS NOW SOLD OUT')
				tick.option_menu1.destroy()
				tick.optionList1.remove('King Room   $59.00')
				tick.option_var1 = tkinter.StringVar()
				tick.option_var1.set('Second Floor') 
				tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command = lambda _: tick.SFmenu_click())
				tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)
				tick.SF_soldOut()
			print(tick.SFkingRoom)
	


		elif tick.chosenRoom1 == 'Twin Room   $69.00' and 69 in tick.SFtwinRoom and tick.SFsoldOut==False:
			print("chose the twin room")

			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.SFtwinRoom.pop()
				tick.option_var1.set('Second Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 69 not in tick.SFtwinRoom:
				tkinter.messagebox.showerror(message=tick.chosenRoom1+' IS NOW SOLD OUT')
				tick.optionList1.remove('Twin Room   $69.00')
				tick.option_menu1.destroy()
				tick.option_var1 = tkinter.StringVar()
				tick.option_var1.set('Second Floor') 
				tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command = lambda _: tick.SFmenu_click())
				tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)	
				tick.SF_soldOut()
			print(tick.SFtwinRoom)
			
			
		elif tick.chosenRoom1 == 'Deluxe King   $75.00' and 75 in tick.SFdeluxeKing and tick.SFsoldOut==False:
			print('chose the deluxe king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.SFdeluxeKing.pop()
				tick.option_var1.set('Second Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 75 not in tick.SFdeluxeKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom1+' IS NOW SOLD OUT')
				tick.optionList1.remove('Deluxe King   $75.00')
				tick.option_menu1.destroy()
				tick.option_var1 = tkinter.StringVar()
				tick.option_var1.set('Second Floor') 
				tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command = lambda _: tick.SFmenu_click())
				tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)
				tick.SF_soldOut()	
			print(tick.SFdeluxeKing)
			

		elif tick.chosenRoom1 == 'Corner King   $90.00' and 90 in tick.SFcornerKing and tick.SFsoldOut==False:
			print ('chose the corner king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.SFcornerKing.pop()
				tick.option_var1.set('Second Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 90 not in tick.SFcornerKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom1+' IS NOW SOLD OUT')
				tick.optionList1.remove('Corner King   $90.00')
				tick.option_menu1.destroy()
				tick.option_var1 = tkinter.StringVar()
				tick.option_var1.set('Second Floor') 
				tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command = lambda _: tick.SFmenu_click())
				tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)
				tick.SF_soldOut()
			print(tick.SFcornerKing)
			

		elif tick.chosenRoom1 == 'Corner Suite   $110.00' and 110 in tick.SFcornerSuite and tick.SFsoldOut==False:
			print('chose the corner suite room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.SFcornerSuite.pop()
				tick.option_var1.set('Second Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")

			if 110 not in tick.SFcornerSuite:
				tkinter.messagebox.showerror(message=tick.chosenRoom1+' IS NOW SOLD OUT')
				tick.optionList1.remove('Corner Suite   $110.00')
				tick.option_menu1.destroy()
				tick.option_var1 = tkinter.StringVar()
				tick.option_var1.set('Second Floor') 
				tick.option_menu1 = tkinter.OptionMenu(tick.main_window, tick.option_var1, *tick.optionList1, command = lambda _: tick.SFmenu_click())
				tick.option_menu1.grid(row=4, column=3, padx=25, pady=25)	
				tick.SF_soldOut()
			print(tick.SFcornerSuite)

		else:
			tkinter.messagebox.showerror(message='No room chosen')



##################################################### Check TF Rooms ######################################################################################

	def check_TFrooms(tick):

		tick.chosenRoom2 = tick.option_var2.get()

		if  tick.chosenRoom2 == 'King Room   $59.00' and 59 in tick.TFkingRoom and tick.TFsoldOut==False:
			print('chose the king room') 
		
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.TFkingRoom.pop()
				tick.option_var2.set('Third Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
				
			if 59 not in tick.TFkingRoom :
				tkinter.messagebox.showerror(message=tick.chosenRoom2+' IS NOW SOLD OUT')
				tick.optionList2.remove('King Room   $59.00')
				tick.option_menu2.destroy()
				tick.option_var2 = tkinter.StringVar()
				tick.option_var2.set('Third Floor') 
				tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command = lambda _: tick.TFmenu_click())
				tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)
				tick.TF_soldOut()
			print(tick.TFkingRoom)
	


		elif tick.chosenRoom2 == 'Twin Room   $69.00' and 69 in tick.TFtwinRoom and tick.TFsoldOut==False:
			print("chose the twin room")

			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.TFtwinRoom.pop()
				tick.option_var2.set('Third Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 69 not in tick.TFtwinRoom:
				tkinter.messagebox.showerror(message=tick.chosenRoom2+' IS NOW SOLD OUT')
				tick.optionList2.remove('Twin Room   $69.00')
				tick.option_menu2.destroy()
				tick.option_var2 = tkinter.StringVar()
				tick.option_var2.set('Third Floor') 
				tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command = lambda _: tick.TFmenu_click())
				tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)
				tick.TF_soldOut()	
			print(tick.TFtwinRoom)
			
			
		elif tick.chosenRoom2 == 'Deluxe King   $75.00' and 75 in tick.TFdeluxeKing and tick.TFsoldOut==False:
			print('chose the deluxe king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.TFdeluxeKing.pop()
				tick.option_var2.set('Third Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 75 not in tick.TFdeluxeKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom2+' IS NOW SOLD OUT')
				tick.optionList2.remove('Deluxe King   $75.00')
				tick.option_menu2.destroy()
				tick.option_var2 = tkinter.StringVar()
				tick.option_var2.set('Third Floor') 
				tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command = lambda _: tick.TFmenu_click())
				tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)	
				tick.TF_soldOut()
			print(tick.TFdeluxeKing)
			

		elif tick.chosenRoom2 == 'Corner King   $90.00' and 90 in tick.TFcornerKing and tick.TFsoldOut==False:
			print ('chose the corner king room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.TFcornerKing.pop()
				tick.option_var2.set('Third Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")
			
			if 90 not in tick.TFcornerKing:
				tkinter.messagebox.showerror(message=tick.chosenRoom2+' IS NOW SOLD OUT')
				tick.optionList2.remove('Corner King   $90.00')
				tick.option_menu2.destroy()
				tick.option_var2 = tkinter.StringVar()
				tick.option_var2.set('Third Floor') 
				tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command = lambda _: tick.TFmenu_click())
				tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)
				tick.TF_soldOut()
			print(tick.TFcornerKing)
			

		elif tick.chosenRoom2 == 'Corner Suite   $110.00' and 110 in tick.TFcornerSuite and tick.TFsoldOut==False:
			print('chose the corner suite room')
			
			if tkinter.messagebox.askyesno(message='Are you sure you want this room')==True:
				tick.TFcornerSuite.pop()
				tick.option_var2.set('Third Floor')
				tkinter.messagebox.showinfo(message="You have purchased a room!")

			if 110 not in tick.TFcornerSuite:
				tkinter.messagebox.showerror(message=tick.chosenRoom2+' IS NOW SOLD OUT')
				tick.optionList2.remove('Corner Suite   $110.00')
				tick.option_menu2.destroy()
				tick.option_var2 = tkinter.StringVar()
				tick.option_var2.set('Third Floor') 
				tick.option_menu2 = tkinter.OptionMenu(tick.main_window, tick.option_var2, *tick.optionList2, command = lambda _: tick.TFmenu_click())
				tick.option_menu2.grid(row=5, column=3, padx=25, pady=25)
				tick.TF_soldOut()	
			print(tick.TFcornerSuite)
		
		else:
			tkinter.messagebox.showerror(message='No room is chosen')

	

########################################### Buttons for specific floors ##################################################################### 

	def GFmenu_click(tick):
		print('Ground Floor button clicked')
		
		tick.option_var1.set('Second Floor')
		tick.option_var2.set('Third Floor')

		#Purchase button
		tick.PurchaseButton = tkinter.Button(tick.main_window, text= 'Purchase',\
													width= 18, font=("Helvetica",12), state=NORMAL,\
													command = tick.check_GFrooms)
		tick.PurchaseButton.grid(row=6, column=3, padx=25, pady=25)

	def SFmenu_click(tick):
		print('Second floor button clicked')
		
		tick.option_var.set('Ground Floor')
		tick.option_var2.set('Third Floor')

		#Purchase button
		tick.PurchaseButton1 = tkinter.Button(tick.main_window, text= 'Purchase',\
													width= 18, font=("Helvetica",12), state=NORMAL,\
													command = tick.check_SFrooms)
		tick.PurchaseButton1.grid(row=6, column=3, padx=25, pady=25)

	def TFmenu_click(tick):
		print('Third floor button click')
		
		tick.option_var.set('Ground Floor')
		tick.option_var1.set('Second Floor')
		
		#Purchase button
		tick.PurchaseButton2 = tkinter.Button(tick.main_window, text= 'Purchase',\
													width= 18, font=("Helvetica",12), state=NORMAL,\
													command = tick.check_TFrooms)
		tick.PurchaseButton2.grid(row=6, column=3, padx=25, pady=25)

	
######################################### When Floors are sold out ############################################################# 

	def GF_soldOut(tick):

		if 59 not in tick.GFroomArray[0] and 69 not in tick.GFroomArray[1] and 75 not in tick.GFroomArray[2] and 90 not in tick.GFroomArray[3] and 110 not in tick.GFroomArray[4]: 
			tkinter.messagebox.showerror(message='Ground Floor SOLD OUT')
			tick.roomArray.pop(0)
			print('Ground Floor sold out')
			#could delete the option menu here and put sold out as a label
			print("Room Array = " + str(len(tick.roomArray)))
			tick.hotel_soldOut()

		else:
			print('Ground floor not sold out')

	def SF_soldOut(tick):

		if 59 not in tick.SFroomArray[0] and 69 not in tick.SFroomArray[1] and 75 not in tick.SFroomArray[2] and 90 not in tick.SFroomArray[3] and 110 not in tick.SFroomArray[4]: 
			tkinter.messagebox.showerror(message='Second Floor SOLD OUT')
			tick.roomArray.pop(0)
			print('Second Floor sold out')
			#could delete the option menu here and put sold out as a label
			print("Room Array = " + str(len(tick.roomArray)))
			tick.hotel_soldOut()

		else:
			print('Second floor not sold out')

	def TF_soldOut(tick):

		if 59 not in tick.TFroomArray[0] and 69 not in tick.TFroomArray[1] and 75 not in tick.TFroomArray[2] and 90 not in tick.TFroomArray[3] and 110 not in tick.TFroomArray[4]: 
			tkinter.messagebox.showerror(message='Third Floor SOLD OUT')
			tick.roomArray.pop(0)
			print('Third Floor sold out')
			#could delete the option menu here and put sold out as a label
			print("Room Array = " + str(len(tick.roomArray)))
			tick.hotel_soldOut()

		else:
			print('Third floor not sold out')
	

############################################# See if the hotel is sold out #########################################################################################
	

	def hotel_soldOut(tick):

		if len(tick.roomArray)  == 0:
			tkinter.messagebox.showerror(message='Hotel is SOLD OUT')
			tick.option_menu2.destroy()
			tick.option_menu1.destroy()
			tick.option_menu.destroy()
			tick.label1.destroy()
			tick.PurchaseButton2.destroy()
			tick.PurchaseButton1.destroy()
			tick.PurchaseButton.destroy()
			tick.label = tkinter.Label(tick.main_window, text= 'SOLD OUT',\
										  width= 18, font=("Helvetica",16))
			tick.label.grid(row=2, column=3)


		else:
			print ('Hotel not sold out')

################################# Rewards ##################################################################
	def get_rewards(tick,tempUsername,tempPassword):
		
		rewardList = open('rewards.txt', 'r').read().split('\n')
		rewardList.remove('')

		if tempUsername +':' + tempPassword + ':'  + '1' in rewardList:
			tick.reward = rewardList.count(tempUsername +':' + tempPassword + ':'  + '1')
			print ("login times = " + str(tick.reward))
			tick.cash = tick.reward*5
			print ("reward money = $" + str(tick.cash))
			tick.buy_tickets()
		else:
			print ('No Rewards')
			tick.buy_tickets()



############################## Send Email ################################################################
	def send_email(tick):
		
		sender = 'from@fromdomain.com'
		receivers = ['to@todomain.com']

		message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		A room was Purchased.
		"""

		try:
		   smtpObj = smtplib.SMTP('localhost')
		   smtpObj.sendmail(sender, receivers, message)         
		   print ("Successfully sent email")
		except SMTPException:
		   print ("Error: unable to send email")
