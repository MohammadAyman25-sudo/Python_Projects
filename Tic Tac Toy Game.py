from tkinter import  *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.resizable(0, 0)
root.title('Tic Tac Toe')

ActivePlayer = 1
p1 = []
p2 = []

#Menu
menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New Game", command=lambda:BuNew())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=lambda:finish())


# Style
style = ttk.Style()
style.theme_use('xpnative')
style.configure('TButton', font=('Arial', 18, 'bold'))
style.configure('TLabel', font=('Arial', 18, 'bold'))

# Buttons
bu1 = ttk.Button(root, text='')
bu1.grid(row=0, column=0, ipadx=40, ipady=40)
bu1.config(command=lambda : BuClick(1))

bu2 = ttk.Button(root, text='')
bu2.grid(row=0, column=1, ipadx=40, ipady=40)
bu2.config(command=lambda : BuClick(2))

bu3 = ttk.Button(root, text='')
bu3.grid(row=0, column=2, ipadx=40, ipady=40)
bu3.config(command=lambda : BuClick(3))

bu4 = ttk.Button(root, text='')
bu4.grid(row=1, column=0, ipadx=40, ipady=40)
bu4.config(command=lambda : BuClick(4))

bu5 = ttk.Button(root, text='')
bu5.grid(row=1, column=1, ipadx=40, ipady=40)
bu5.config(command=lambda : BuClick(5))

bu6 = ttk.Button(root, text='')
bu6.grid(row=1, column=2, ipadx=40, ipady=40)
bu6.config(command=lambda : BuClick(6))

bu7 = ttk.Button(root, text='')
bu7.grid(row=2, column=0, ipadx=40, ipady=40)
bu7.config(command=lambda : BuClick(7))

bu8 = ttk.Button(root, text='')
bu8.grid(row=2, column=1, ipadx=40, ipady=40)
bu8.config(command=lambda : BuClick(8))

bu9 = ttk.Button(root, text='')
bu9.grid(row=2, column=2, ipadx=40, ipady=40)
bu9.config(command=lambda : BuClick(9))

#When Button Clicked
def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    if (ActivePlayer == 1):
        StayLayout(id,'X')
        ActivePlayer = 2
        p1.append(id)
        print("p1:{}".format(p1))
        CheckWinner(id)
    elif (ActivePlayer == 2):
        StayLayout(id,'O')
        ActivePlayer = 1
        p2.append(id)
        print("p2:{}".format(p2))
        CheckWinner(id)

def StayLayout(id, text):
    if id==1:
        bu1.config(text=text)
        bu1.state(['disabled'])

    elif id==2:
        bu2.config(text=text)
        bu2.state(['disabled'])

    elif id==3:
        bu3.config(text=text)
        bu3.state(['disabled'])

    elif id==4:
        bu4.config(text=text)
        bu4.state(['disabled'])

    elif id==5:
        bu5.config(text=text)
        bu5.state(['disabled'])

    elif id==6:
        bu6.config(text=text)
        bu6.state(['disabled'])

    elif id==7:
        bu7.config(text=text)
        bu7.state(['disabled'])

    elif id==8:
        bu8.config(text=text)
        bu8.state(['disabled'])

    elif id==9:
        bu9.config(text=text)
        bu9.state(['disabled'])

def CheckWinner(id):
    ## Rows
    #Row zero
    if 1 in p1 and 2 in p1 and 3 in p1:
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy','Player X Wins')

    elif 1 in p2 and 2 in p2 and 3 in p2:
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

    #Row one
    if 4 in p1 and 5 in p1 and 6 in p1:
        i = 0
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 4 in p2 and 5 in p2 and 6 in p2:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

    #Row two
    if 7 in p1 and 8 in p1 and 9 in p1:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 7 in p2 and 8 in p2 and 9 in p2:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')
    
    ##Columns
    #Column zero
    if 1 in p1 and 4 in p1 and 7 in p1:
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 1 in p2 and 4 in p2 and 7 in p2:
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

    #Column one
    if 2 in p1 and 5 in p1 and 8 in p1:
        bu1.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 2 in p2 and 5 in p2 and 8 in p2:
        bu1.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy','Player O Wins')

    #Column two
    if 3 in p1 and 6 in p1 and 9 in p1:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 3 in p2 and 6 in p2 and 9 in p2:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

    #Diagonal 1,5,9
    if 1 in p1 and 5 in p1 and 9 in p1:
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 1 in p2 and 5 in p2 and 9 in p2:
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

    #Diagonal3,5,7
    if 3 in p1 and 5 in p1 and 7 in p1:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player X Wins')

    elif 3 in p2 and 5 in p2 and 7 in p2:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu4.state(['disabled'])
        bu6.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        p1.clear()
        p2.clear()
        tkinter.messagebox.showinfo('Tic Tac Toy', 'Player O Wins')

def BuNew():
    bu1.config(text='')
    bu1.state(['!disabled'])

    bu2.config(text='')
    bu2.state(['!disabled'])
    
    bu3.config(text='')
    bu3.state(['!disabled'])
    
    bu4.config(text='')
    bu4.state(['!disabled'])
    
    bu5.config(text='')
    bu5.state(['!disabled'])
    
    bu6.config(text='')
    bu6.state(['!disabled'])
    
    bu7.config(text='')
    bu7.state(['!disabled'])
    
    bu8.config(text='')
    bu8.state(['!disabled'])
    
    bu9.config(text='')
    bu9.state(['!disabled'])

    ActivePlayer = 1

def finish():
    exit()

root.mainloop()