from tkinter import *
import random
import time;

root = Tk()
root.geometry("1650x800+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600, height = 50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#=============================TIME===================================#

localtime = time.asctime(time.localtime(time.time()))

#=====================================================================


lblInfo = Label(Tops, font=('arial',30,'bold'), text="RESTAURANT MANAGEMENT SYSTEM", fg="Steel Blue", bd=10, anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('arial',15,'bold'), text=localtime, fg="Steel Blue", bd=10, anchor="w")
lblInfo.grid(row=1,column=0)


#=======================Calculator ==============================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(12937, 50437)
    randRef = str(x)
    rand.set(randRef)

    CoF = float(fries.get())
    CoD = float(Drinks.get())
    CoFr = float(friedrice.get())
    CoJr = float(jollofrice.get())
    CoSh = float(sharwama.get())
    CoMp = float(meatpie.get())

    CostOfFries = CoF * 100
    CostOfDrinks = CoD * 150
    CostOfFriedRice = CoFr * 1100
    CostOfJollofRice = CoJr * 1200
    CostOfSharwama = CoSh * 1100
    CostOfMeatPie = CoMp * 250

    MealCost = "N",str('%.2f' % (CostOfFries + CostOfDrinks + CostOfFriedRice + CostOfJollofRice + CostOfSharwama + CostOfMeatPie))

    Tax = (( CostOfFries + CostOfDrinks + CostOfFriedRice + CostOfJollofRice + CostOfSharwama + CostOfMeatPie) + 49.99)

    TotalCost = ( CostOfFries + CostOfDrinks + CostOfFriedRice + CostOfJollofRice + CostOfSharwama + CostOfMeatPie)

    ser_Charge = (( CostOfFries + CostOfDrinks + CostOfFriedRice + CostOfJollofRice + CostOfSharwama + CostOfMeatPie) / 99)

    Service = "N",str('%.2f' % ser_Charge)

    OverallCost = "N",str('%.2f' % (Tax + TotalCost + ser_Charge))

    PaidTax = "N",str('%.2f' % Tax)

    service.set(Service)
    cost.set(MealCost)
    state.set(PaidTax)
    subtotal.set(MealCost)
    total.set(OverallCost)




def qExit():
    root.destroy()

def Reset():
    rand.set("")
    fries.set("")
    friedrice.set("")
    jollofrice.set("")
    sharwama.set("")
    meatpie.set("")
    Drinks.set("")
    service.set("")
    cost.set("")
    state.set("")
    subtotal.set("")
    total.set("")



txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

#===========================================================================================================================================

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="powder blue", command= lambda: btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="powder blue", command= lambda: btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="powder blue", command= lambda: btnClick(9)).grid(row=2,column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="powder blue", command= lambda: btnClick("+")).grid(row=2,column=3)

#=============================================================================================================================================

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="powder blue", command= lambda: btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="powder blue", command= lambda: btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="powder blue", command= lambda: btnClick(6)).grid(row=3,column=2)
Subtraction = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="powder blue", command= lambda: btnClick("-")).grid(row=3,column=3)


#============================================================================================================================================

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="powder blue", command= lambda: btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="powder blue", command= lambda: btnClick(2)).grid(row=4,column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="powder blue", command= lambda: btnClick(3)).grid(row=4,column=2)
Multiple = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="powder blue", command= lambda: btnClick("*")).grid(row=4,column=3)

#============================================================================================================================================

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="powder blue", command= lambda: btnClick(0)).grid(row=5,column=0)
btnC = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="powder blue", command= btnClearDisplay).grid(row=5,column=1)
btnEQ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="powder blue", command= btnEqualsInput).grid(row=5,column=2)
Divide = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg="powder blue", command= lambda: btnClick("/")).grid(row=5,column=3)


#====================================================================================================================================================================
rand = StringVar()
fries = StringVar()
friedrice = StringVar()
jollofrice = StringVar()
sharwama = StringVar()
meatpie = StringVar()
Drinks = StringVar()
service = StringVar()
cost = StringVar()
state = StringVar()
subtotal = StringVar()
total = StringVar()





#  RESTAURANT INFO ONE

lblReference = Label(f1, font=('arial', 15, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0,column=0)
textReference = Entry(f1, font=('arial', 15, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify="right")
textReference.grid(row=0,column=1)

#====================================================================================================================================================================

lblFries = Label(f1, font=('arial', 15, 'bold'), text="Large Fries", bd=16, anchor="w")
lblFries.grid(row=1,column=0)
textFries = Entry(f1, font=('arial', 15, 'bold'), textvariable=fries, bd=10, insertwidth=4, bg="powder blue", justify="right")
textFries.grid(row=1,column=1)

#==================================================================================================================================================================

lblFriedRice = Label(f1, font=('arial', 15, 'bold'), text="Fried Rice", bd=16, anchor="w")
lblFriedRice.grid(row=2,column=0)
textFriedRice = Entry(f1, font=('arial', 15, 'bold'), textvariable=friedrice, bd=10, insertwidth=4, bg="powder blue", justify="right")
textFriedRice.grid(row=2,column=1)

#=============================================================================================================================================

lblJollofRice = Label(f1, font=('arial', 15, 'bold'), text="Jollof Rice", bd=16, anchor="w")
lblJollofRice.grid(row=3,column=0)
textJollofRice = Entry(f1, font=('arial', 15, 'bold'), textvariable=jollofrice, bd=10, insertwidth=4, bg="powder blue", justify="right")
textJollofRice.grid(row=3,column=1)

#=============================================================================================================================================

lblSharwama = Label(f1, font=('arial', 15, 'bold'), text="Sharwama", bd=16, anchor="w")
lblSharwama.grid(row=4,column=0)
textSharwama = Entry(f1, font=('arial', 15, 'bold'), textvariable=sharwama, bd=10, insertwidth=4, bg="powder blue", justify="right")
textSharwama.grid(row=4,column=1)

#=============================================================================================================================================

lblMeatpie = Label(f1, font=('arial', 15, 'bold'), text="  Meat Pie  ", bd=16, anchor="w")
lblMeatpie.grid(row=5,column=0)
textMeatpie = Entry(f1, font=('arial', 15, 'bold'), textvariable=meatpie, bd=10, insertwidth=4, bg="powder blue", justify="right")
textMeatpie.grid(row=5,column=1)


#  RESTAURANT INFO TWO

lblDrinks = Label(f1, font=('arial', 15, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0,column=2)
textDrinks = Entry(f1, font=('arial', 15, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="#ffffff", justify="right")
textDrinks.grid(row=0,column=3)

#====================================================================================================================================================================

lblcost = Label(f1, font=('arial', 15, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblcost.grid(row=1,column=2)
textcost = Entry(f1, font=('arial', 15, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg="#ffffff", justify="right")
textcost.grid(row=1,column=3)

#==================================================================================================================================================================

lblservice = Label(f1, font=('arial', 15, 'bold'), text="Service Charge", bd=16, anchor="w")
lblservice.grid(row=2,column=2)
textservice = Entry(f1, font=('arial', 15, 'bold'), textvariable=service, bd=10, insertwidth=4, bg="#ffffff", justify="right")
textservice.grid(row=2,column=3)

#=============================================================================================================================================

lblstate = Label(f1, font=('arial', 15, 'bold'), text="State Tax", bd=16, anchor="w")
lblstate.grid(row=3,column=2)
textstate = Entry(f1, font=('arial', 15, 'bold'), textvariable=state, bd=7, insertwidth=4, bg="#ffffff", justify="right")
textstate.grid(row=3,column=3)

#=============================================================================================================================================

lblsubtotal = Label(f1, font=('arial', 15, 'bold'), text="SubTotal", bd=16, anchor="w")
lblsubtotal.grid(row=4,column=2)
textsubtotal = Entry(f1, font=('arial', 15, 'bold'), textvariable=subtotal, bd=10, insertwidth=4, bg="#ffffff", justify="right")
textsubtotal.grid(row=4,column=3)

#=============================================================================================================================================

lbltotal = Label(f1, font=('arial', 15, 'bold'), text=" Total Cost", bd=16, anchor="w")
lbltotal.grid(row=5,column=2)
texttotal = Entry(f1, font=('arial', 15, 'bold'), textvariable=total, bd=10, insertwidth=4, bg="#ffffff", justify="right")
texttotal.grid(row=5,column=3)


#=============================================================================================================================================
btnTotal = Button(f1, padx=16, pady=8,bd=16, fg="black", width=10,text="Total",bg="powder blue", font=('arial', 15, 'bold'), command=Ref).grid(row=7,column=1)

btnReset = Button(f1, padx=16, pady=8,bd=16, fg="black", width=10,text="Reset",bg="powder blue", font=('arial', 15, 'bold'), command=Reset).grid(row=7,column=2)

btnExit = Button(f1, padx=16, pady=8,bd=16, fg="black", width=10,text="Exit",bg="powder blue", font=('arial', 15, 'bold'), command=qExit).grid(row=7,column=3)



root.mainloop()