#!/usr/bin/env python
import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from ExcelModule import *
from Settings import *
from Functions import *

def CreateReport(FileName, MouseObject):
	Report = ExcelFile(FileName)
	
	#INFO
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 1, "Report created by MouseCalculator")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 2, "Copyright TeddyBear 2017")

	#Input
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 4, "INPUT")

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 5, "Subject ID:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 2, 5, MouseObject.ID)

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 6, "Meal Size")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 2, 6, MealSize)

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 7, "Minutes Of Rest Before Meal")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 2, 7, MinutesOfRestBeforeMeal)

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 8, "Food Within Time For Meal")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 2, 8, Meal_FoodWithinTimeRestriction)

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, 9, "Minutes Of Rest After Meal")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 2, 9, MinutesOfRestAfterMeal)

	#Output
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 5, 4, "OUTPUT")

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 5, 5, "Nr of Meals:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 6, 5, MouseObject.NrOfMeals)

	Report.AddDataToCell(Report.ListOfWorkSheets[0], 5, 6, "Nr of Snacks:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 6, 6, MouseObject.NrOfSnacks)

#meals
	x = 11
	y = 12
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y-2, "Meal Info:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y-1, "Start:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+1, y-1, "End:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+2, y-1, "Lenght:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+3, y-1, "Intake:")
	for meal in MouseObject.ListOfMeals:
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y, meal.Start)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+1, y, meal.End)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+2, y, meal.Lenght)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+3, y, meal.Intake)
		y +=1
		print meal.List

#snacks
	x = 16
	y = 12 
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y-2, "Snack Info:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y-1, "Start:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+1, y-1, "End:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+2, y-1, "Lenght:")
	Report.AddDataToCell(Report.ListOfWorkSheets[0], x+3, y-1, "Intake:")
	for snack in MouseObject.ListOfSnacks:
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x, y, snack.Start)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+1, y, snack.End)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+2, y, snack.Lenght)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], x+3, y, snack.Intake)
		y +=1
		print snack.List

	#Time
	Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, FirstY, "Time")
	for x in range(0, len(MouseObject.Intake_Raw_MinByMin)):
		minute = x+1
		CellY = x+1+(FirstY)
		Report.AddDataToCell(Report.ListOfWorkSheets[0], 1, CellY, int(minute))

	#Intake RAW
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Intake_Raw_MinByMin, "Raw Intake", 2, FirstY)

	#Intake RAW Accumulated
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Intake_Accumulated_All_MinByMin , "Acc. Raw Intake", 3, FirstY)

	#Intake Positive
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Intake_Positive_MinByMin, "Positive Intake", 4, FirstY)

	#Intake Positive Accumulated
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Intake_Accumulated_Positive_MinByMin, "Acc. Positive Intake", 5, FirstY)

	#Meals Binary
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Meals_Binary, "MEALS_Binary", 7, FirstY)

	#Snacks Binary
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.Snacks_Binary, "SNACKS_Binary", 8, FirstY)

	#15 Min Intake Calculation
	AddVerticalData(Report, Report.ListOfWorkSheets[0], MouseObject.ListOf15MinFoodIntake, "15 Min Food", 9, FirstY)

	x = 0
	for Meal_BinList in MouseObject.StandardizedMeal(0,9999):
		AddVerticalData(Report, Report.ListOfWorkSheets[0], Meal_BinList, ("MealStd" + str(x+1)), 21+x, FirstY)
		x+=1

	#END - Save file
	Report.Save(FolderPath+SaveFolderName)
	return Report

class Mouse: #Creates an instance of the object "Mouse"
	class Meal: 
		def __init__(self, MouseObject, StartOfMeal, EndOfMeal):
			self.Start = StartOfMeal
			self.End = EndOfMeal
			self.List = MouseObject.Intake_Positive_MinByMin[self.Start-1 : self.End]#-1 gives index instead of acutal minute number
			self.Lenght = len(self.List)
			self.Intake = sum(self.List)

	class Snack: 
		def __init__(self, MouseObject, StartOfSnack, EndOfSnack):
			self.Start = StartOfSnack
			self.End = EndOfSnack
			self.List = MouseObject.Intake_Positive_MinByMin[self.Start-1 : self.End]
			self.Lenght = len(self.List)
			self.Intake = sum(self.List)

	def __init__(self, Worksheet):
		self.Worksheet = Worksheet
		SubjectID_fulltext = GetCellValue(1, 7, self.Worksheet)
		self.ID = SubjectID_fulltext[SubjectID_fulltext.find(":")+1:] #Takes the text in the ID cell, saves only the actuall ID
		self.Intake_Raw_MinByMin = GetColumnValues_AsList(self.Worksheet, 5, FirstDataCell_Y, LastDataCell_Y) # 5 = E = Raw intake; 20 to 5700 => all

		#The indented function below below creates a list where all values = or less than 0 is zero => only positive meals = meals.
		self.Intake_Positive_MinByMin = []
		for intake in self.Intake_Raw_MinByMin:
			if intake >= 0:
				self.Intake_Positive_MinByMin.append(intake)
			else:
				self.Intake_Positive_MinByMin.append(0)

		#The indented function below below creates a list where all values in the RAW minbymin list are accumulated.
		self.Intake_Accumulated_All_MinByMin = []
		SUM = 0
		for intake in self.Intake_Raw_MinByMin:
			if intake != 0:
				SUM = SUM+intake
			self.Intake_Accumulated_All_MinByMin.append(SUM)

		#The indented function below below creates a list where all values in the POSITIVE minbymin list are accumulated. => NO NEGATIVE NUMBERS ARE ADDED TO TOTAL
		self.Intake_Accumulated_Positive_MinByMin = []
		SUM = 0
		for intake in self.Intake_Positive_MinByMin:
			if intake != 0:
				SUM = SUM+intake
			self.Intake_Accumulated_Positive_MinByMin.append(SUM)

		#MEAL CALCULATION
		self.Meals_Binary = []
		self.ListOfMeals = []
		minute_index = 0
		meal = False
		for intake in self.Intake_Positive_MinByMin:
			minute = minute_index+1
			PreviousMealState = meal
			if intake != 0:
				if sum(self.Intake_Positive_MinByMin[minute_index:(minute_index + Meal_FoodWithinTimeRestriction)]) >= MealSize and sum(self.Intake_Positive_MinByMin[(minute_index-MinutesOfRestBeforeMeal):minute_index]) == 0: #Checks if sum of intake is more than MealSize for Meal_TimeRestriction after current minute
					meal = True
			else:
				if sum(self.Intake_Positive_MinByMin[minute_index:(minute_index + MinutesOfRestAfterMeal)]) == 0: #Checks if sum of intake is 0 for MinutesOfRestAfterMeal after current minute
					meal = False
			#END
			CurrentMealState = meal
			if CurrentMealState == True and PreviousMealState == False:
				StartOfMeal = minute

			if meal == True:
				self.Meals_Binary.append(1)
			else:
				self.Meals_Binary.append(0)
				if PreviousMealState == True:
					EndOfMeal = minute-1
					self.ListOfMeals.append(Mouse.Meal(self, StartOfMeal, EndOfMeal))
			minute_index +=1 #Increases minuteNR by one => next loop is for the next minute

		#15 MIN INTAKE CALCULATION'
		self.ListOf15MinFoodIntake = []
		Increment = 52
		ModifiedIntakeList = self.Intake_Positive_MinByMin[Start_EI:]
		for x in range(0,len(ModifiedIntakeList)/Increment):
			minute_index = x*Increment
			self.ListOf15MinFoodIntake.append(sum(ModifiedIntakeList[minute_index:(minute_index + Increment)]))
		
		#SNACK CALCULATION
		self.Snacks_Binary = []
		self.ListOfSnacks = []
		minute_index = 0
		snack = False
		for intake in self.Intake_Positive_MinByMin:
			minute = minute_index+1
			PreviousSnackState = snack
			if intake != 0:
				if self.Meals_Binary[minute_index] == 0:
					if sum(self.Intake_Positive_MinByMin[minute_index:(minute_index)]) < MealSize: 
						snack = True
			else:
				if sum(self.Intake_Positive_MinByMin[minute_index:(minute_index + 1)]) == 0:
					snack = False
			#END
			CurrentSnackState = snack
			if CurrentSnackState == True and PreviousSnackState == False:
				StartOfSnack = minute

			if snack == True:
				self.Snacks_Binary.append(1)
			else:
				self.Snacks_Binary.append(0)
				if PreviousSnackState == True:
					EndOfSnack = minute-1
					self.ListOfSnacks.append(Mouse.Snack(self, StartOfSnack, EndOfSnack))

			minute_index +=1
			self.NrOfMeals = len(self.ListOfMeals)
			self.NrOfSnacks = len(self.ListOfSnacks)


	def StandardizedMeal(self, LIMIT1, LIMIT2):
		self.ListOfStandardizedMeal = []
		ReslutingListLenght = 20
		for meal in self.ListOfMeals:
			ListOfBins = []
			Lenght = meal.Lenght
			FoodPerSecond = []
			if LIMIT1 <= Lenght <= LIMIT2:
				for intake in meal.List:
					for x in range(0,60):
						FoodPerSecond.append(intake/60.0)
				Seconds = len(FoodPerSecond)
				BinSize = Seconds/ReslutingListLenght
				for x in range(0, ReslutingListLenght):
					x1 = x*BinSize
					x2 = x*BinSize+BinSize
					ListOfBins.append(sum(FoodPerSecond[(x1):(x2)]))
				self.ListOfStandardizedMeal.append(ListOfBins)
		return self.ListOfStandardizedMeal

def MainWindowInterface(main_window):
	#---------------------------------------- INTERFACE ------------------------------------------
	CalcButtonHeight = MainWindowHeight-200
	#Quit button
	BUTTON(main_window, "Quit", MainWindowWidth-100, 20, 10, 1, QUITfunction, main_window, "grey")

	#Calculate button
	BUTTON(main_window, "Calculate", MainWindowWidth/2-30, CalcButtonHeight, 10, 1, Calculate, main_window, "grey")

	#Entries
	main_window.RawDataFileName_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-170, 20, RawDataFileName, "Raw data file name: ", "SIDE")
	main_window.MealSize_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-130, 10, MealSize_Default, "Meal size (g):", "SIDE")
	main_window.MinutesOfRestBeforeMeal_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-100, 10, MinutesOfRestBeforeMeal_Default, "Rest time before meal (min):", "SIDE")
	main_window.Meal_FoodWithinTimeRestriction_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-70, 10, Meal_FoodWithinTimeRestriction_Default, "Food within time for meal (min):", "SIDE")	
	main_window.MinutesOfRestAfterMeal_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-40, 10, MinutesOfRestAfterMeal_Default, "Rest time after meal (min):", "SIDE")	
	main_window.ListOf15MinFoodIntake_Entry = EntryClass(main_window, MainWindowWidth/2-30, CalcButtonHeight-200, 10, ListOf15MinFoodIntake_Default, "Start Point:", "SIDE")

def Calculate(main_window):
	print "Calculating mouse data"
	RAW_DATA_FOLDER = FolderPath+RawDataFolderName+"/"
	DATA_FILE_NAME = str(main_window.RawDataFileName_Entry.E.get())
	#if "." in DATA_FILE_NAME:
	#	SAVE_FILE_NAME = DATA_FILE_NAME[:-1*DATA_FILE_NAME[::-1].find(".")] + "_Calc"#str(main_window.SaveFileName_Entry.E.get())
	#else:
	#	SAVE_FILE_NAME = DATA_FILE_NAME + "_Calc"
	SAVE_FILE_NAME = DATA_FILE_NAME + "_Calc"

	global MealSize, MinutesOfRestBeforeMeal, Meal_FoodWithinTimeRestriction, MinutesOfRestAfterMeal, Start_EI
	MealSize 						= float(main_window.MealSize_Entry.E.get())
	MinutesOfRestBeforeMeal 		= int(main_window.MinutesOfRestBeforeMeal_Entry.E.get())
	Meal_FoodWithinTimeRestriction  = int(main_window.Meal_FoodWithinTimeRestriction_Entry.E.get())
	MinutesOfRestAfterMeal 			= int(main_window.MinutesOfRestAfterMeal_Entry.E.get())
	Start_EI						= int(main_window.ListOf15MinFoodIntake_Entry.E.get())

	ws = GetWorksheet(RAW_DATA_FOLDER, DATA_FILE_NAME, 0)
	MouseObject = Mouse(ws)
	CreateReport(SAVE_FILE_NAME, MouseObject)

def Start():
	print "Start"
	print "Copyright TeddyBear 2017"
	global Window1
	Window1 = Window("MainWindow", MainWindowWidth, MainWindowHeight, MainWindowX, MainWindowY)
	Window1.W.title(MainWindowName)
	MainWindowInterface(Window1.W)
	Window1.MAINLOOP()

#------------------------------------------ Actuall process -----------------------------------------------
Start()
