#!/usr/bin/env python
#Settings
import os
import sys    
import time
import math
import datetime
from Tkinter import *  
ScriptName =  __file__

#Functions
def QUITfunction(window):
	print "Quit!"
	#Open are you sure? Do you want to save???
	window.quit()
def TimeStampToReadable(TimeStamp):
	return datetime.datetime.fromtimestamp(int(str(TimeStamp)[0:10])).strftime('%Y-%m-%d %H:%M:%S')
	#time
def ReadableToTimeStamp(ReadableTime):
	if len(ReadableTime) <= 10:
		ReadableTime = ReadableTime[:10] + " 00:00:00"
	return int(datetime.datetime.strptime(ReadableTime, '%Y-%m-%d %H:%M:%S').strftime("%s"))
def GetR2(Ys, Xs):
	if len(Ys)>=3:
		R2 = numpy.corrcoef(Xs, Ys)[0, 1]**2	
		#print "R2 =", R2
		return R2
	else:
		return 1
def LinReg(Ys, Xs): # Returns tuple (K, M) for trendline!
	N = len(Xs)
	if N <= 1:
		return 1, 1
	else:
		Sx = Sy = Sxx = Syy = Sxy = 0.0
		for x, y in zip(Xs, Ys):
			Sx = Sx+x
			Sy = Sy+y
			Sxx = Sxx+x*x
			Syy = Syy+y*y
			Sxy = Sxy+x*y
		det = Sxx * N - Sx * Sx
		return (Sxy * N - Sy * Sx)/det, (Sxx*Sy - Sx*Sxy)/det
def Percent(x1,x2):
	#percent
	return (float(x1)/float(x2)-1)*100
def GetTime(): #CurrentTimeClass.XXX
	global CurrentTimeClass
	class CurrentTimeClass:
		Year = time.strftime("%Y")
		Month = time.strftime("%m")
		Day = time.strftime("%d")
		Hour = time.strftime("%H")
		Minutes = time.strftime("%M")
		Seconds = time.strftime("%S")
		CurrentTime = Year+Month+Day+Hour+Minutes+Seconds
		YYMMDDString = time.strftime("%Y-%m-%d")
		WeekdayNR = datetime.datetime.today().weekday()
	return CurrentTimeClass
def CalcYfromLineAndX(K,M,X):
		Y = K*X+M
		return Y
def SetTimeStampToMidnight(TimeStamp):
	TrueTime_Readable = TimeStampToReadable(TimeStamp)
	Midnight = TrueTime_Readable[0:10]+" 00:00:00"
	return ReadableToTimeStamp(Midnight)
def RNG():
	#Returns a random nr from 0.0-100.0.
	RandomNr = ((random.random()+0.01)*100)
	return RandomNr
def RNG_InInterval(x1, x2):
	#Returns a floating nr in between x1 and x2.
	Interval_size = float(x2) - float(x1)
	RandomNr = float(RNG()/(100.0/Interval_size))
	RandomNrInInterval = x1 + RandomNr
	return RandomNrInInterval
def GetRandomFromList(List):
	#Checks list-lenght and returns a random index within the list.
	index = (int(RNG())%len(List))
	return List[index]
def QUITfunction(window):
	print "Quit!"
	#Open are you sure? Do you want to save???
	window.quit()
def ClickEffectSINK(BUTTON):
	BUTTON.config(relief=SUNKEN)
	#Makes the button sunken...
def ClickEffectRAISEandCall(BUTTON, FUNCTION, ARGS):
	BUTTON.config(relief=RAISED)
	FUNCTION(ARGS)
	#Raises the button and calls the function...
def AppendToListBox(ListBox, Name):
	TEXT = ListBoxSpace+Name
	ListBox.insert(END, TEXT)
def ChangeNameOfListBoxItem(ListBox, Name, NewName):
	Index = int(ListBox.get(0, END).index(Name))
	ListBox.delete(Index)
	ListBox.insert(Index, NewName)
def ClearListBox(ListBox):
	#Clears entire listbox
	ListBox.delete(0, END)
class EntryClass:
	def __init__(self, parent, X, Y, width, default, text, LabelPlace):
		self.E = Entry(parent, width = width)
		self.E.place(x=X, y=Y)
		self.E.insert(0, default)
		self.L = Label(parent, text = text)
		if LabelPlace == "ABOVE":
			self.L.place(x=X, y=Y-22)
		if LabelPlace == "SIDE":
			Text_Lenght = len(text)
			self.L.place(x=X-Text_Lenght*6.5+width/2-8, y=Y+1)
def BUTTON(parent, text, X, Y, width, height, function, args, color):
	button = Label(parent, width = width, height=height, relief=RAISED, bg=color, borderwidth=2, text=text)
	button.bind('<ButtonPress-1>', lambda x: ClickEffectSINK(button))
	button.bind('<ButtonRelease-1>', lambda x: ClickEffectRAISEandCall(button, function, args))
	button.place(x=X, y=Y) 
class Window:
	def __init__(self, Name, Width, Height, X, Y):
		self.Name = Name
		self.Width = Width
		self.Height = Height
		self.X = X
		self.Y = Y
		if self.Name == "MainWindow":
			self.W = Tk()
		else:
			self.W = Toplevel()
		self.W.geometry("%sx%s+%s+%s" %(self.Width, self.Height, self.X, self.Y))
		self.W.title("%s" %(self.Name))
	def MAINLOOP(self):
		self.W.mainloop()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'""
#-------------------------------- END OF PROGRAM -----------------------------
print "'"+ScriptName+"'- module has been loaded."
