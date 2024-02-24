'''Tony's Ordering System
Author James Klick
2/24/24
Version 1.0'''

#imports
import tkinter as tk

#create root window
root = tk.Tk()

#set title
root.title('Tonys Ordering System')

#set root window size
root.geometry('640x480+300+300')
root.resizable(False, False)

#widgets

#label
title = tk.Label( root, image="Welcome to Tony's Pizza, Please Enter Your Order", font=('Arial 16 bold'), bg = '#FF4500', fg = '#FFFFFF')

#use string var
nameVar = tk.StringVar(root)
nameLabel = tk.Label(root, text = "Enter your First and Last name")
nameInp = tk.Entry(root, textvariable = nameVar)
addressVar = tk.StringVar(root)
addressLabel = tk.Label(root, text = "Enter your Address")
addressInp = tk.Entry(root, textvariable = addressVar)
phoneVar = tk.StringVar(root)
phoneLabel = tk.Label(root, text = "Enter your Phone Number")
phoneInp = tk.Entry(root, textvariable = phoneVar)

#use boolean var/checkbox
eaterVar = tk.BooleanVar()
eaterInp = tk.Checkbutton(root, variable = eaterVar, text = "Check this box if you eat bananas.")

#spinbox
numVar = tk.IntVar(value = 3)
numLabel = tk.Label(text = "How many bananas do you eat per day?")
numInp = tk.Spinbox(root, textvariable = numVar, from_ = 0, to = 100, increment = 1)

#listbox
colorVar = tk.StringVar(value = "Any")
colorLabel = tk.Label(root, text = "What is the best color for bananas?")
colorChoices = ("Any", "Green", "Green/Yellow", "Yellow", "Brown Spotted", "Black")
colorInp = tk.OptionMenu(root, colorVar, *colorChoices)

#radio button
plaintainLabel = tk.Label(root, text = "Do you eat plaintains?")
plaintainFrame = tk.Frame(root)
plaintainVar = tk.BooleanVar()
plaintainYesInp = tk.Radiobutton(plaintainFrame, text = "Yes", value = True, variable = plaintainVar)
plaintainNoInp = tk.Radiobutton(plaintainFrame, text = "Eww, no!", value = False, variable = plaintainVar)

#submit button
submitBtn = tk.Button(root, text = "Submit Survey")

#output line
outputVar = tk.StringVar(value = "")
outputLine = tk.Label(root, textvariable = outputVar, anchor = "w", justify = 'left')

#geometry
title.grid(row = 0, columnspan = 2)

#name label into grid
nameLabel.grid(row = 1, column = 0)

#text entry into grid
nameInp.grid(row = 1, column = 1)

#name label into grid
addressLabel.grid(row = 2, column = 0)

#text entry into grid
addressInp.grid(row = 2, column = 1)

#name label into grid
phoneLabel.grid(row = 3, column = 0)

#text entry into grid
phoneInp.grid(row = 3, column = 1)


#checkbox
eaterInp.grid(row = 4, columnspan = 2, sticky = 'we')

#spinbox
numLabel.grid(row = 5, sticky = tk.W)
numInp.grid(row = 5, column = 1, sticky = tk.W + tk.E)

#padx and pady
colorLabel.grid(row = 6, columnspan = 2, sticky = tk.W, pady = 10)
colorInp.grid(row = 7, columnspan = 2, sticky= tk.W + tk.E, padx = 25)

#pack
plaintainYesInp.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
plaintainNoInp.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
plaintainLabel.grid(row = 8, columnspan = 2, sticky = tk.W)
plaintainFrame.grid(row = 9, columnspan = 2, sticky = tk.W)

#button
submitBtn.grid(row = 99)
outputLine.grid(row = 100, columnspan = 2, sticky = "NSEW")

#columnconfigure
root.columnconfigure(1, weight = 1)

#rowconfigure
root.rowconfigure(99, weight = 1)
root.rowconfigure(100, weight = 1)


def on_submit():
    """To be run when the user submits form"""
    #Vars all use '.get()'
    name = nameVar.get()
    try:
        number = numVar.get()
    except tk.TclError:
        number = 1000
    
    color = colorVar.get()

    bananaEater = eaterVar.get()
    plaintainEater = plaintainVar.get()

    message = f'Thanks for taking the survey, {name}.\n'

    if not bananaEater:
        message += f"Sorry you don't like bananas!\n"
    else:
        message += f'Enjoy your {number} {color} bananas!\n'

    if plaintainEater:
        message += "Enjoy your plaintains!"
    else:
        message += "May you successfully avoid plaintains!"
    
    outputVar.set(message)

submitBtn.configure(command = on_submit)

root.mainloop()