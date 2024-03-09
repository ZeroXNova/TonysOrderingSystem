'''Tony's Ordering System
Author James Klick
3/9/24
Version 1.0'''

#imports
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


#create root window
root = tk.Tk()

#set title
root.title('Tonys Ordering System')

#set root window size
root.geometry('640x800+300+300')
root.resizable(True, True)

#widgets

#label
img = Image.open(r'C:\Users\jklic\Documents\College\Intro To SoftwareDev\Final Project\TPOS.jpg').resize((640,100))
img_tk = ImageTk.PhotoImage(img)
title = tk.Label(root, text = "", image = img_tk)

#use string var
nameVar = tk.StringVar(root)
nameLabel = tk.Label(root, text = "First and Last name")
nameInp = tk.Entry(root, textvariable = nameVar)
addressVar = tk.StringVar(root)
addressLabel = tk.Label(root, text = "Address")
addressInp = tk.Entry(root, textvariable = addressVar)
phoneVar = tk.StringVar(root)
phoneLabel = tk.Label(root, text = "Phone Number")
phoneInp = tk.Entry(root, textvariable = phoneVar)

#use boolean var/checkbox
orderLabel = tk.Label(root, text = 'Pickup or Delivery? (Select One):')
orderFrame = tk.Frame(root)
deliveryVar = tk.BooleanVar()
pickupInp = tk.Radiobutton(orderFrame, text = "Pickup", value = True, variable = deliveryVar)
deliveryInp = tk.Radiobutton(orderFrame, text = "Delivery", value = False, variable = deliveryVar)


#spinbox
numVar = tk.IntVar(value = 1)
numLabel = tk.Label(text = "How many?")
numInp = tk.Spinbox(root, textvariable = numVar, from_ = 0, to = 100, increment = 1)


#listbox
colorVar = tk.StringVar(value = "Any")
colorLabel = tk.Label(root, text = "What is the best color for bananas?")
colorChoices = ("Any", "Green", "Green/Yellow", "Yellow", "Brown Spotted", "Black")
colorInp = tk.OptionMenu(root, colorVar, *colorChoices)

#radio button
sizeLabel = tk.Label(root, text = "What size pizza would you like?")
sizeFrame = tk.Frame(root)
sizeVar = tk.IntVar(value = 0)
sizeSmall = tk.Radiobutton(sizeFrame, text = "Small - $5.99", value = 1, variable = sizeVar)
sizeMedium = tk.Radiobutton(sizeFrame, text = "Medium - $8.99", value = 2, variable = sizeVar)
sizeLarge = tk.Radiobutton(sizeFrame, text = "Large - $10.99", value = 3, variable = sizeVar)

#use boolean var/checkbox
topLabel = tk.Label(root, text = "Which toppings would you like?(Free of Charge!)")
mushVar = tk.BooleanVar()
mushInp = tk.Checkbutton(root, variable = mushVar, text = "Mushroom")
peppVar = tk.BooleanVar()
peppInp = tk.Checkbutton(root, variable = peppVar, text = "Pepperoni")
sausVar = tk.BooleanVar()
sausInp = tk.Checkbutton(root, variable = sausVar, text = "Sausage")
hamVar = tk.BooleanVar()
hamInp = tk.Checkbutton(root, variable = hamVar, text = "Ham")
onionVar = tk.BooleanVar()
onionInp = tk.Checkbutton(root, variable = onionVar, text = "Onion")


sideLabel = tk.Label(root, text = "Which sides would you like?")
wingVar = tk.BooleanVar()
wingInp = tk.Checkbutton(root, variable = wingVar, text = "12 Wings - $4.99")
knotsVar = tk.BooleanVar()
knotsInp = tk.Checkbutton(root, variable = knotsVar, text = "6 Garlic Knots - $4.99")


#submit button
subImg = Image.open(r'C:\Users\jklic\Documents\College\Intro To SoftwareDev\Final Project\submit.png').resize((200,100))
subImg_tk = ImageTk.PhotoImage(subImg)
submitBtn = tk.Button(root, text = "", image=subImg_tk)



#output line
outputVar = tk.StringVar(value = "")
outputLine = tk.Label(root, textvariable = outputVar, anchor = "w", justify = 'left')

#geometry
title.grid(row = 0, columnspan = 2)

#name label into grid
nameLabel.grid(row = 1, column = 0)

#text entry into grid
nameInp.grid(row = 1, column = 1)

#address label into grid
addressLabel.grid(row = 2, column = 0)

#text entry into grid
addressInp.grid(row = 2, column = 1)

#phone label into grid
phoneLabel.grid(row = 3, column = 0)

#text entry into grid
phoneInp.grid(row = 3, column = 1)

#pack
pickupInp.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
deliveryInp.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
orderLabel.grid(row = 4, columnspan = 2, sticky = tk.W)
orderFrame.grid(row = 5, columnspan = 2, sticky = tk.W)

#spinbox
numLabel.grid(row = 7, sticky = tk.W)
numInp.grid(row = 7, column = 1)

#pack
sizeSmall.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
sizeMedium.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
sizeLarge.pack(side = 'left', fill = 'x', ipadx = 10, ipady = 5)
sizeLabel.grid(row = 8, columnspan = 2, sticky = tk.W)
sizeFrame.grid(row = 9, columnspan = 2, sticky = tk.W)

#checkbox
topLabel.grid(row=10,columnspan=2, sticky="w")
mushInp.grid(row = 10, columnspan=2, sticky = 'w')
peppInp.grid(row = 11, columnspan=2, sticky = 'w')
sausInp.grid(row = 12, columnspan=2, sticky = 'w')
hamInp.grid(row = 13, columnspan=2, sticky = 'w')
onionInp.grid(row = 14, columnspan=2, sticky = 'w')

sideLabel.grid(row=15,columnspan=2, sticky="w")
wingInp.grid(row = 16, columnspan=2, sticky = 'w')
knotsInp.grid(row = 17, columnspan=2, sticky = 'w')



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
        
    #Opens new window
    new_win=tk.Toplevel(root)
    new_win.title("Order Confirmation")

    #Order Confirmation
    oConfirm = tk.Label(new_win, text = "Order Confirmed!")
    oConfirm.grid(row = 1, columnspan=2)


    #Inport variables
    pickup = deliveryVar.get()
    address = addressVar.get()
    phone = phoneVar.get()
    number = str(numVar.get())
    size = sizeVar.get()
    
    mushroom = mushVar.get()
    pepperoni = peppVar.get()
    sausage = sausVar.get()
    ham = hamVar.get()
    onion = onionVar.get()

    wings = wingVar.get()
    knots = knotsVar.get()

    total = 0





    #starts message display
    message = f'Thanks for your order, {name}.\n'


    #checks for pickup/delivery, displaying an appropraite message
    if not pickup:
        message += f"Your pizza will be delivered to: " + address + "\n"
    else:
        message += f'Pickup Selected!\n'


    #checks for size/number of pizzas, displaying an appropraite message
    if number == "1":
        if size == 1:
            total = total + 599
            message += f"1 Small pizza selected\n"
        elif size == 2:
            total = total + 899
            message += f"1 Medium pizza selected\n"
        elif size == 3:
            total = total + 1099
            message += f"1 Large pizza selected\n"
        else:
            message += f"No size selected\n"
    else:
        if size == 1:
            total = total + (int(number) * 599)
            message += number + f" Small pizzas selected\n"
        elif size == 2:
            total = total + (int(number) * 899)
            message += number + f" Medium pizzas selected\n"
        elif size == 3:
         total = total + (int(number) * 1099)
         message += number + f" Large pizzas selected\n"
        else:
            message += f"No size selected\n" 
    
   
    #checks for toppings, displaying an appropraite message
    message += f"Topped with : "

    if  not mushroom:
        message += f""
    else:
        message += f"Mushroom "
    if  not pepperoni:
        message += f""
    else:
        message += f"Pepperoni "
    if  not sausage:
        message += f""
    else:
        message += f"Sausage "
    if  not ham:
        message += f""
    else:
        message += f"Ham "
    if  not onion:
        message += f""
    else:
        message += f"Onion "
        
    message +="\n"
    #checks for sides, displaying an appropraite message
    message +="With the following sides: \n"

    if  not wings:
        message += f""
    else:
        total = total + 499
        message += f"12 Wings\n"
    if  not knots:
        message += f""
    else:
        total = total + 499
        message += f"6 Garlic Knots\n "

    #calculate taxt/total
    subtotal = total/100
    tax = subtotal * .06
    total = subtotal + round(tax, 2)

    message += f"Your subtotal today is: $" + str(subtotal)
    message += f"\nYour tax today is: $" + str(round(tax, 2))
    message += f"\nYour total today is: $" + str(round(total, 2))
    message += f"\nOur staff will call you at: " + phone + " to confirm payment. If paying by card, please have the card handy."

        

    outputVar.set(message)


submitBtn.configure(command = on_submit)


root.mainloop()