from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.CreateWidgets()

    def replaceText(self,text):
        self.display.delete(0, END)
        self.display.insert(0, text)
    
    def Text(self, text):
        self.display.insert(0, "=")
        self.display.insert(0, text)
    
    def calculateExcepration(self):
        self.excepration = self.display.get()
        self.result = eval(self.excepration)
        self.replaceText(self.result)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength,text)

    def clearText(self,text):
        self.display.delete(0,END)
        self.display.insert(0,text)
    
    def CreateWidgets(self):
        self.display = Entry(self,font=("Helvetica",20,"bold"),borderwidth=2,relief=RAISED,justify=LEFT)
        self.display.insert(0,"0")
        self.display.grid(row=0,column=0,columnspan=5)

        self.sevenButton = Button(self,font=("Helvetica",11,"bold"),text="7",borderwidth=2,command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1,column=0,sticky="snew")

        self.eightButton = Button(self,font=("Helvetica",11,"bold"),text="8",borderwidth=2,command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1,column=1,sticky="snew")

        self.nineButton = Button(self,font=("Helvetica",11,"bold"),text="9",borderwidth=2,command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1,column=2,sticky="snew")

        self.timesButton = Button(self,font=("Helvetica",12,"bold"),text="*",borderwidth=2,command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=1,column=3,sticky="snew")

        self.clearButton = Button(self,font=("Helvetica",11,"bold"),text="C",borderwidth=2,command=lambda:self.clearText("0"))
        self.clearButton.grid(row=1,column=4,sticky="snew")

        self.sixButton = Button(self,font=("Helvetica",11,"bold"),text="4",borderwidth=2,command=lambda: self.appendToDisplay("4"))
        self.sixButton.grid(row=2,column=0,sticky="snew")

        self.fiveButton = Button(self,font=("Helvetica",11,"bold"),text="5",borderwidth=2,command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2,column=1,sticky="snew")

        self.fourButton = Button(self,font=("Helvetica",11,"bold"),text="6",borderwidth=2,command=lambda: self.appendToDisplay("6"))
        self.fourButton.grid(row=2,column=2,sticky="snew")

        self.divideButton = Button(self,font=("Helvetica",11,"bold"),text="/",borderwidth=2,command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2,column=3,sticky="snew")

        self.percentButton = Button(self,font=("Helvetica",11,"bold"),text="%",borderwidth=2,command=lambda: self.appendToDisplay("%"))
        self.percentButton.grid(row=2,column=4,sticky="snew")
        
        self.oneButton = Button(self,font=("Helvetica",11,"bold"),text="1",borderwidth=2,command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3,column=0,sticky="snew")

        self.twoButton = Button(self,font=("Helvetica",11,"bold"),text="2",borderwidth=2,command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3,column=1,sticky="snew")

        self.threeButton = Button(self,font=("Helvetica",11,"bold"),text="3",borderwidth=2,command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3,column=2,sticky="snew")

        self.minusButton = Button(self,font=("Helvetica",11,"bold"),text="-",borderwidth=2,command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3,column=3,sticky="snew")

        self.equalsButton = Button(self,font=("Helvetica",11,"bold"),text="=",borderwidth=2,command=lambda:self.calculateExcepration())
        self.equalsButton.grid(row=3,column=4,sticky="snew",rowspan=3)

        self.zeroButton = Button(self,font=("Helvetica",11,"bold"),text="0",borderwidth=2,command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4,column=0,sticky="snew",columnspan=2)

        self.dotButton = Button(self,font=("Helvetica",11,"bold"),text=".",borderwidth=2,command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4,column=2,sticky="snew")
        
        self.plusButton = Button(self,font=("Helvetica",11,"bold"),text="+",borderwidth=2,command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4,column=3,sticky="snew")
app = Application(root).grid()
root.mainloop()
