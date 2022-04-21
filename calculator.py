import tkinter, math

class Calculator:
    def __init__(self):
        self.ans = 0
        self.firstval = 0
        self.secondval = 0
    def insertnumber(self, value):
        self.firstval = textDisplay.get() #gets value from the text
        textDisplay.delete(0, tkinter.END) #deletes from 0 index to end
        textDisplay.insert(0, self.firstval + str(value))
    def add(self):
        pass
        #take the first set of numbers and save to self.add, clear board 
        #set variable command to add
        #when equal is pressed, take second set of numbers, look at variable command
        #add the first and second set of numbers and display it
        #can do this for every function, equal will have a lot of if statements tho
    def subtract(self):
        pass
    def divide(self):
        pass
    def multiply(self):
        pass
    def equal(self):
        pass
    def squared(self):
        pass
        #takes the current number on screen, saves it, squares it and displays that
    def root(self):
        pass
        #same as squared but rooting the number instead
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
    filemenu.add_command(label="Standard", command=scientificbuttondel()) #adding options within dropdown
    filemenu.add_command(label="Scientific", command=scientificbuttonadd())
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
    
    add.grid(row=2, column=4, padx=1, pady=1)
    subtract.grid(row=3, column=4, padx=1, pady=1)
    divide.grid(row=4, column=4, padx=1, pady=1)
    multiply.grid(row=5, column=4, padx=1, pady=1)
    equal.grid(row=5, column=3, padx=1, pady=1)

    clear = tkinter.Button(window, text='CE', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.clear())
    backspace = tkinter.Button(window, text='⌫', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.remove())
    squared = tkinter.Button(window, text='x²', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.squared())
    root = tkinter.Button(window, text='√', width = 4, height = 3, background = 'black', foreground = 'white', command=lambda: calc.root())

    clear.grid(row=1, column=3, padx=1, pady=1)
    backspace.grid(row=1, column=4, padx=1, pady=1)
    squared.grid(row=1, column=2, padx=1, pady=1)
    root.grid(row=1, column=1, padx=1, pady=1)

def scientificbuttonadd():
    pass
    #creating buttons for sin, cos, tan, e, log, ln, exponent, factorial, modulus, pi

def scientificbuttondel():
    pass
    #removing the newly added buttons

main()