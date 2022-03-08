from tkinter import *

from numpy import pad

import dados


def gui():
    dices = [4, 6, 8, 10, 12, 20, 100]
    width = 600
    height = 400
    root = Tk()

    root.title("DiceRoll")
    root.iconbitmap('data/favicon.ico')
    root.geometry(str(width)+"x"+str(height))
    root.resizable(False, False)

    tries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    selectedTries = IntVar(root)
    selectedTries.set(tries[0])

    inputFrame = Frame(root)

    triesLabel = Label(inputFrame, text="Nº of dices:")

    triesDropdown = OptionMenu(inputFrame, selectedTries, *tries)

    sidesFrame = LabelFrame(inputFrame, text="Size of dices:", relief=FLAT)

    diceSides = Listbox(sidesFrame, height=7, bg="#f0f0f0", relief=FLAT)

    for value in dices:
        diceSides.insert(value, "  d"+str(value))

    def roll():
        for i in diceSides.curselection():
            global result
            sides = int(diceSides.get(i).replace("d", ""))
            rolls = selectedTries.get()
            result = dados.roll(sides, rolls)
            showResults.config(text=" ".join(result["results"]))
            showTotal.config(text=result["total"])

    rollButton = Button(inputFrame, text='ROLL!', command=roll)
    frameResult = LabelFrame(root, text="Results")
    showResults = Label(frameResult, text="", font=('Arial', 12))
    showTotal = Label(frameResult, text="", font=('Arial', 40), pady=80)

    inputFrame.pack()
    inputFrame.place(x=0, height=height, width=200)
    triesLabel.pack()
    triesLabel.place(x=0, y=0, height=30)
    triesDropdown.pack()
    triesDropdown.place(x=100, y=0, height=30)
    sidesFrame.pack(pady=35)
    diceSides.pack()
    root.update()
    buttonY = 60 + sidesFrame.winfo_height()
    rollButton.pack()
    rollButton.place(x=50, y=buttonY, width=100)
    frameResult.pack()
    frameResult.place(x=200, height=height, width=width-200)

    showResults.pack()
    showTotal.pack()

    root.mainloop()


if(__name__ == "__main__"):
    gui()
