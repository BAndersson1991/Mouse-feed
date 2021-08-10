#!/usr/bin/env python
#Settings
Separator = str("\\")
print Separator
#CONSTANT
ScriptName =  __file__
print ScriptName
FolderPath = __file__[:-1*(__file__[::-1].find(Separator))]
print FolderPath
SaveFolderName = "SaveFolder"
RawDataFolderName = "RawDataFiles"

#CHANGEABLE
#Input
RawDataFileName = "WT11_M2"
FirstDataCell_Y = 20
LastDataCell_Y = 10000

#Output
SaveFileName = RawDataFileName[:RawDataFileName.find(".")] + "_Calc"
FirstY = 11
LastDataCell_Y

#DEFINITIONS/FUNCTIONS
#meal time restirction should be shorter than rest after meal?
MealSize_Default = 0.05
MinutesOfRestBeforeMeal_Default = 15
Meal_FoodWithinTimeRestriction_Default = 15
MinutesOfRestAfterMeal_Default = 15
ListOf15MinFoodIntake_Default = 0



#INTERFACE
MainWindowName = "MouseCalculator"
MainWindowWidth = 800
MainWindowHeight = 600
MainWindowX = 0
MainWindowY = 0


#-------------------------------- END OF PROGRAM -----------------------------
print "'"+ScriptName+"'- module has been loaded."



#