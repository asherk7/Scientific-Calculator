import tkinter, math
#wipe bool inside insert number
#while false, regular insert number
#while true, wipe all numbers and set operation to false, firstval = 0
#it will be set to true inside add, subtract, etc
#these functions will save textdisplay to firstval
#could perform the respective operations on firstval when saving textdisplay instead
#set operation to true after add subtract divide or multiply are pressed
#when equal is pressed, save textdisplay to secondval
#go through if statements to see which operation it is, and do it
#this can be done by using an operation variable
#when add is pressed, operation = 'add', etc for other operations
#when operation is found, do calculations and print the number
#set first and second val to 0 and set operation to true
#after equal is pressed, save textdisplay after operations to self.answer
#implement a try and except for math errors, use wipe

class Calculator:
    def __init__(self):
        self.ans = 0
        self.firstval = 0
        self.secondval = 0
        self.answer = 0
        self.wipe = False
        self.operation = None
    def insertnumber(self, value):
        if self.wipe == False:
            self.firstval = textDisplay.get() #gets value from the text
            textDisplay.delete(0, tkinter.END) #deletes from 0 index to end
            textDisplay.insert(0, self.firstval + str(value))
        else:
            pass
    def add(self):
        pass
    def subtract(self):
        pass
    def divide(self):
        pass
    def multiply(self):
        pass
    def equal(self):
        pass
    def answer(self):
        pass
        #if textdisplay isnt empty, multiply ans with whatever is on it
        #if its empty or equal to 0, paste the answer in textdisplay
        #if there's an operation, wipe textdisplay and put ans in
        #when equal is pressed, it'll do the operation
    def pi(self):
        pass
        #if textdisplay isnt empty, multiply ans with whatever is on it
        #if its empty or equal to 0, paste the answer in textdisplay
        #if there's an operation, wipe textdisplay and put ans in
        #when equal is pressed, it'll do the operation
    def squared(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.pow(self.firstval, 2))
        textDisplay.insert(0, str(self.answer))
    def sin(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.sin(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def cos(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.cos(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def tan(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.tan(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def e(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.exp(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def log(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.log10(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def ln(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.log(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def exponent(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.pow(10, self.firstval))
        textDisplay.insert(0, str(self.answer))
    def factorial(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.factorial(int(self.firstval)))
        textDisplay.insert(0, str(self.answer))
    def root(self):
        self.firstval = float(textDisplay.get())
        textDisplay.delete(0, tkinter.END)
        self.answer = rounder(math.sqrt(self.firstval))
        textDisplay.insert(0, str(self.answer))
    def clear(self):
        textDisplay.delete(0, tkinter.END)
    def remove(self):
        val = textDisplay.get() #saves the text
        textDisplay.delete(0, tkinter.END) 
        textDisplay.insert(0, val[:-1]) #inserts the text without the last value

def main():
    global textDisplay, window, calc
    calc = Calculator()
    window = tkinter.Tk() #initializing the GUI
    window.title('Scientific Calculator') #giving it a title
    window.resizable(width = False, height = False) #making it so user cant adjust size

    menu = tkinter.Menu(window) #creating a menu for the gui
    filemenu = tkinter.Menu(menu, tearoff=0) #creating sub menus within the menu
    menu.add_cascade(label='Calculator', menu=filemenu) #adding a dropdown, setting its dropdowns to filemenu
    filemenu.add_command(label="Standard", command=lambda: scientificbuttondel()) #adding options within dropdown
    filemenu.add_command(label="Scientific", command=lambda: scientificbuttonadd())
    window.config(menu=menu) #creating the menu

    textDisplay = tkinter.Entry(window, width = 25, bd = 15, justify='right') #creating the screen
    textDisplay.grid(row=0, column=0, columnspan = 5)
    buttoninitialization()

    window.mainloop() 

def buttoninitialization(): #creating each button
    button1 = tkinter.Button(window, text='1', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(1))
    button2 = tkinter.Button(window, text='2', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(2))
    button3 = tkinter.Button(window, text='3', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(3))
    button4 = tkinter.Button(window, text='4', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(4))
    button5 = tkinter.Button(window, text='5', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(5))
    button6 = tkinter.Button(window, text='6', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(6))
    button7 = tkinter.Button(window, text='7', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(7))
    button8 = tkinter.Button(window, text='8', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(8))
    button9 = tkinter.Button(window, text='9', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(9))
    button0 = tkinter.Button(window, text='0', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber(0))
    buttonperiod = tkinter.Button(window, text='.', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.insertnumber('.'))
    #initializing the buttons
    button1.grid(row=2, column=1, padx=1, pady=1)
    button2.grid(row=2, column=2, padx=1, pady=1)
    button3.grid(row=2, column=3, padx=1, pady=1)
    button4.grid(row=3, column=1, padx=1, pady=1)
    button5.grid(row=3, column=2, padx=1, pady=1)
    button6.grid(row=3, column=3, padx=1, pady=1)
    button7.grid(row=4, column=1, padx=1, pady=1)
    button8.grid(row=4, column=2, padx=1, pady=1)
    button9.grid(row=4, column=3, padx=1, pady=1)
    button0.grid(row=5, column=1, padx=1, pady=1)
    buttonperiod.grid(row=5, column=2, padx=1, pady=1)

    add = tkinter.Button(window, text='+', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.add())
    subtract = tkinter.Button(window, text='-', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.subtract())
    divide = tkinter.Button(window, text='÷', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.divide())
    multiply = tkinter.Button(window, text='x', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.multiply())
    equal = tkinter.Button(window, text='=', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.equal())
    
    add.grid(row=1, column=4, padx=1, pady=1)
    subtract.grid(row=2, column=4, padx=1, pady=1)
    divide.grid(row=3, column=4, padx=1, pady=1)
    multiply.grid(row=4, column=4, padx=1, pady=1)
    equal.grid(row=5, column=4, padx=1, pady=1)

    clear = tkinter.Button(window, text='CE', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.clear())
    backspace = tkinter.Button(window, text='⌫', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.remove())
    squared = tkinter.Button(window, text='x²', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.squared())
    answer = equal = tkinter.Button(window, text='ans', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.answer())

    clear.grid(row=1, column=2, padx=1, pady=1)
    backspace.grid(row=1, column=3, padx=1, pady=1)
    squared.grid(row=1, column=1, padx=1, pady=1)
    answer.grid(row=5, column=3, padx=1, pady=1)

def scientificbuttonadd():
    global sin, cos, tan, e, log, ln, exponent, factorial, root, pi
    sin = tkinter.Button(window, text='sin', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.sin())
    cos = tkinter.Button(window, text='cos', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.cos())
    tan = tkinter.Button(window, text='tan', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.tan())
    e = tkinter.Button(window, text='e', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.e())
    log = tkinter.Button(window, text='log', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.log())
    ln = tkinter.Button(window, text='ln', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.ln())
    exponent = tkinter.Button(window, text='E', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.exponent())
    factorial = tkinter.Button(window, text='!', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.factorial())
    root = tkinter.Button(window, text='√', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.root())
    pi = tkinter.Button(window, text='π', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.pi())
    
    sin.grid(row=1, column=5, padx=1, pady=1)
    cos.grid(row=2, column=5, padx=1, pady=1)
    tan.grid(row=3, column=5, padx=1, pady=1)
    e.grid(row=4, column=5, padx=1, pady=1)
    log.grid(row=5, column=5, padx=1, pady=1)
    ln.grid(row=1, column=6, padx=1, pady=1)
    exponent.grid(row=2, column=6, padx=1, pady=1)
    factorial.grid(row=3, column=6, padx=1, pady=1)
    root.grid(row=4, column=6, padx=1, pady=1)
    pi.grid(row=5, column=6, padx=1, pady=1)

def scientificbuttondel():
    sin.grid_forget()
    cos.grid_forget()
    tan.grid_forget()
    e.grid_forget()
    log.grid_forget()
    ln.grid_forget()
    exponent.grid_forget()
    factorial.grid_forget()
    root.grid_forget()
    pi.grid_forget()

def rounder(x):
    if float(x)-int(x) >= 0.99:
        return round(x)
    else:
        return x

main()