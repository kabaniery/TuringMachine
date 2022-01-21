from tkinter import *
from tkinter import messagebox as messagebox

currentCommand = "000"
currentIndex = 0
defaultCommand = currentCommand
defaultIndex = currentIndex

window = Tk()
window.title("Turing Machine")
window.geometry("750x900")


#Поле входа
inputFrame = Frame(window, background="#cfcfcf", width=700, height=400)
inputFrame.place(x=25, y=10, width=700, height=150)

entryText = Label(inputFrame, text="Input", width=600, anchor="w", background="#cfcfcf")
entryText.grid(row=0, column=0, pady=5)

inputString = StringVar()
inputText = Entry(inputFrame, textvariable=inputString, width=115)
inputText.grid(row=1, column=0, sticky="w", pady=10)

stringDefaultCommand = StringVar()
stringDefaultCommand.set("000")
inputDefaultCommand = Entry(inputFrame, textvariable=stringDefaultCommand, width=15)
inputDefaultCommand.place(x=502, y=90)

stringDefaultIndex = StringVar()
stringDefaultIndex.set("1")
inputDefaultIndex = Entry(inputFrame, textvariable=stringDefaultIndex, width=10)
inputDefaultIndex.place(x=600, y=90)

defaultText = Label(inputFrame, text="Start command | Start char", font="Arial 10", background="#cfcfcf")
defaultText.place(x=500, y=70)


#Поле выхода
commandFrame = Frame(window, background="#cfcfcf")
commandFrame.place(x=25, y=150, width=700, height=600)

commandLabel = Label(commandFrame, text="Enter command", width=80, background="#cfcfcf")
commandLabel.grid(row=0,column=0)

commandsEntry = Text(commandFrame, height=35)
commandsEntry.grid(row=1,column=0, sticky='w', padx=10)

scroll = Scrollbar(command=Text.yview)
scroll.pack(side='right', fill='y')

commandsEntry.config(yscrollcommand=scroll.set)


def startWork():
	errText = ""
	global defaultCommand
	global defaultIndex
	global inputString
	arrayOfInput = list(str(inputString.get()))
	if len(arrayOfInput) == 0:
		errText = "Пустая входная строка"
	commandString = str(commandsEntry.get("1.0", "end"))
	arrayOfRow = commandString.split("\n")
	arrayOfRow.pop()
	arrayOfCommands = list()
	rowCommand = list()
	for row in arrayOfRow:
		for command in row.split(";"):
			rowCommand.append(command)
		if (len(rowCommand) != 4):
			errText = "Нарушено правило оформления строки"
		arrayOfCommands.append(rowCommand)
		rowCommand = list()
	inputText.config(state='disabled')
	print("work is start")
	#Тут будет проверка

	#Начинаем работать
	if errText == "":
		global currentCommand
		global currentIndex
		print(currentCommand, currentIndex)
		err = 0
		while True:
			err = 1
			for command in arrayOfCommands:
				print(command[0], command[1], currentCommand, arrayOfInput[currentIndex])
				if command[0] == currentCommand and command[1] == arrayOfInput[currentIndex]:
					print("yes")
					err = 0
					if command[2] == ">":
						currentIndex += 1
						if currentIndex > len(arrayOfInput)-1:
							arrayOfInput.append(" ")
						print(currentIndex)
						currentCommand = command[3]
					elif command[2] == "<":
						currentIndex -= 1
						currentCommand = command[3]
						if currentIndex < 0:
							arrayOfInput.insert(0, " ")
					elif command[2] == ".":
						err = 2
						currentCommand = command[3]
					else:
						arrayOfInput[currentIndex] = command[2]
						currentCommand = command[3]
						inputString.set(''.join(e for e in arrayOfInput))
						break
			if err == 2:
				break
			elif err == 1:
				errText = "Нет команды"
				break
		currentCommand = defaultCommand
		currentIndex = defaultIndex	
		if errText != "":
			messagebox.showerror("Ошибка", errText)
	else:
		messagebox.showerror("Ошибка", errText)
	inputText.config(state='normal')

def shagWork():
	global currentCommand
	global currentIndex
	global inputString
	global defaultCommand
	global defaultIndex
	errText = ""
	global inputString
	arrayOfInput = list(str(inputString.get()))
	if len(arrayOfInput) == 0:
		errText = "Пустая входная строка"
		messagebox.showerror("Ошибка", errText)
		return 0
	commandString = str(commandsEntry.get("1.0", "end"))
	arrayOfRow = commandString.split("\n")
	arrayOfRow.pop()
	arrayOfCommands = list()
	rowCommand = list()
	for row in arrayOfRow:
		for command in row.split(";"):
			rowCommand.append(command)
		if (len(rowCommand) != 4):
			errText = "Нарушено правило оформления строки"
		arrayOfCommands.append(rowCommand)
		rowCommand = list()
	err = 1
	for command in arrayOfCommands:
			if command[0] == currentCommand and command[1] == arrayOfInput[currentIndex]:
				err = 0
				if command[2] == ">":
					currentIndex += 1
					currentCommand = command[3]
					if currentIndex > len(arrayOfInput)-1:
						arrayOfInput.append(" ")
				elif command[2] == "<":
					currentIndex -= 1
					currentCommand = command[3]
					if currentIndex < 0:
						arrayOfInput.insert(0, " ")
				elif command[2] == ".":
					err = 2
					currentCommand = defaultCommand
					currentIndex = defaultIndex
				else:
					arrayOfInput[currentIndex] = command[2]
					currentCommand = command[3]
					inputString.set(''.join(e for e in arrayOfInput))
					break
	if err == 1:
		messagebox.showerror("Ошибка", "Не существует команды")
		currentCommand = defaultCommand
		currentIndex = defaultIndex

def stopWork():
	global currentCommand
	currentCommand = defaultCommand
	global currentIndex
	currentIndex = defaultIndex

def setDefault():
	global stringDefaultCommand
	global stringDefaultIndex
	global defaultCommand
	global defaultIndex
	defaultCommand = str(stringDefaultCommand.get())
	defaultIndex = int(stringDefaultIndex.get())-1

startButton = Button(inputFrame, text="Выполнить работу", command=startWork)
startButton.grid(row=3, column=0, sticky="nw")

shagButton = Button(inputFrame, text="Выполнить", command=shagWork)
shagButton.place(x=125, y=70)

stopButton = Button(inputFrame, text="Остановить работу", command=startWork)
stopButton.place(x=215, y=70)

defaultButton = Button(inputFrame, text="Применить", command=setDefault, font = "Arial 8")
defaultButton.place(x=570, y=120)


window.mainloop()
