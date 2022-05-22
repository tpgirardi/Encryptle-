import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import sys
import array
from random import randint
#creates random daily word
#x= randint(0,26)
#y= randint(0,26)
#z= randint(0,26)
#w= randint(0,26)
#creates random key words
#a= randint(1,8)
#b= randint(1,8)
#c= randint(1,8)
#d= randint(1,8)


# Define Text:
counter=0
#dw = [[x,y],
      #[z,w]]
#key matrix
#k = [[a,b],
    # [c,d]]
#encoded word
#e = [[0,0],
     #[0,0]]
#e[0][0]=(dw[0][0]*k[0][0])+(dw[0][1]*k[1][0])
#e[0][1]=(dw[0][0]*k[0][1])+(dw[0][1]*k[1][1])
#e[1][0]=(dw[1][0]*k[0][0])+(dw[1][1]*k[1][0])
#e[1][1]=(dw[1][0]*k[0][1])+(dw[1][1]*k[1][1])
dw = [[8, 1],[3, 11]]
k = [[4, 15],[7, 19]]
e = [[39, 139],[89,254]]
result='a'
result2='a'
result3='a'
result4='a'
def monkeys():
  letOne=list(finalMath1.get())
  letTwo=list(finalMath2.get())
  letThre=list(finalMath3.get())
  letFour=list(finalMath4.get())
  if letOne[0]=='h' and letTwo[0]=='a' and letThre[0]=='c' and letFour[0]=='k':
    decode.destroy()
    finale = Tk()
    finale.title("CONGRATULATIONS!!!")
    finale.geometry('300x200')
    winner=Label(finale, text="CONGRATULATIONS, YOU WON", fg="black")
    winner.pack()



def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def getTextInput():
  global counter, result2, arr1, arr2, result, arr3, result4, arr4, result3

  counter = counter+1

  arr1=list(txt2.get())
  arr2=list(txt4.get())
  arr3=list(txt3.get())
  arr4=list(inputtxt.get())

  result2=arr3[0]
  result=arr2[0]
  result4=arr4[0]
  result3=arr1[0]

  inputtxt.delete(0,END)
  txt2.delete(0,END)
  txt3.delete(0,END)
  txt4.delete(0,END)

  print(str(result))
  print(str(result2))
  print(str(result3))
  print(str(result4))

  print(counter)

  if counter==6:
    frame.destroy()
    Lose=Tk()
    Lose.geometry('200x200')
    loss=Label(Lose, text="You're Out \n Of Tries!",fg='black')
    loss.pack()

  numResult=ord(result)-96
  numResult2=ord(result2)-96
  numResult3=ord(result3)-96
  numResult4=ord(result4)-96

  if numResult==k[0][0] and numResult2==k[0][1] and numResult3==k[1][0] and numResult4==k[1][1]:
    frame.destroy()
    next = Tk()
    next.title("Decoding Step")
    next.geometry('1400x600')
    steps = Label(next, text="To decrypt the encryptle you must understand matrices. \n Matrixes are multipled by a row and column format. \n For example, if you would like to multiply a 2x2 matrices, you must multiply the left matrices row(horizontal) to the other ones colum. \n This easier understood by the rule of having to have match the starting numeral of one martix with the ending of another, \n for example 2x2 x 2x2 works, while 3x3 x 2x3 doesn't. \n You will add the neighbors of the integer in the first colum on the left matrix. \n A good trick to understanding  the final matrix is by taking the first and last letter of the multiplied  matrices. \n For example 3x3 and 3x2 is going to multiply into a 3x2. \n To encrypt a matrice we multiply one matrice with a key which is another matrice and  get a new matrice. \n To dencrypt the encryptle you will need to multiply the final matrice with the inverse of the key. An example of multiply matrices is listed below:", fg='black')
    steps.pack()


    canvas = Canvas(next, width = 1400, height = 300)
    img = PhotoImage(file="problempractice1.png")
    canvas.create_image(700,150,image=img)
    canvas.pack(side=BOTTOM, pady=20)

    bts = Button(next, bg='green', text = 'CONTINUE', command = next.destroy)
    bts.pack()

    next.mainloop()

    global decode
    decode = Tk()
    decode.title("Decoding a Matrix")
    decode.geometry('300x338')
    monkey = Label(decode, text = "Decrypt the\n daily Encryptle\n", fg="black")
    monkey.pack()
    key = Label(decode, text="Key:"+str(k[0][0])+"  "+str(k[0][1])+"\n"+str(k[1][0])+"  "+str(k[1][1]), fg = "black")
    key.place(x=20, y=50)
    chimp = Label(decode, text="Encryptle\n"+str(e[0][0])+"  "+str(e[0][1])+"\n"+str(e[1][0])+"  "+str(e[1][1]), fg="black")
    chimp.place(x = 120, y=50)
    global finalMath1
    finalMath1 = tk.Entry(decode, width = 3)
    finalMath1.place(x=120, y=130)
    global finalMath2
    finalMath2 = tk.Entry(decode, width = 3)
    finalMath2.place(x=160, y=130)
    global finalMath3
    finalMath3 = tk.Entry(decode, width = 3)
    finalMath3.place(x=120, y=160)
    global finalMath4
    finalMath4 = tk.Entry(decode, width = 3)
    finalMath4.place(x=160, y=160)
    f = [[finalMath1, finalMath2], [finalMath3, finalMath4]]
    done = tk.Button(height=1, text="Submit",
    command=monkeys, bg='green')
    done.pack(side=BOTTOM, pady=50)


    decode.mainloop()






  print(numResult)
  print(numResult2)
  print(numResult3)
  print(numResult4)


  if numResult == k[0][0]:
    r1 = Label(frame, text = result, fg = "green")
    r1.place(x = 480, y=80)
  elif numResult ==k[0][1] or numResult == k[1][0] or numResult == k[1][1]:
    r1 = Label(frame, text = result, fg = "yellow")
    r1.place(x=480, y=80)

  else:
    r1 = Label(frame, text = result, fg = "gray")
    r1.place(x=480, y=80)

  if numResult2 == k[0][1]:
    r2 = Label(frame, text = result2, fg = "green")
    r2.place(x=500,y= 80)
  elif numResult2 == k[0][0] or numResult2 == k[1][0] or numResult2 == k[1][1]:
    r2 = Label(frame, text = result2, fg = "yellow")
    r2.place(x=500, y=80)
  else:
    r2 = Label(frame, text = result2, fg = "gray")
    r2.place(x=500, y=80)

  if numResult3 == k[1][0]:
    r3 = Label(frame, text = result3, fg = "green")
    r3.place(x=480, y=100)
  elif numResult3 ==k[0][1] or numResult3 == k[0][0] or numResult3 == k[1][1]:
    r3 = Label(frame, text = result3, fg = "yellow")
    r3.place(x=480, y=100)
  else:
    r3 = Label(frame, text = result3, fg = "gray")
    r3.place(x=480, y=100)

  if numResult4 == k[1][1]:
    r4 = Label(frame, text = result4, fg = "green")
    r4.place(x=500, y=100)
  elif numResult4 == k[0][0] or numResult4 == k[0][1] or numResult4 == k[1][0]:
    r4 = Label(frame, text = result4, fg = "yellow")
    r4.place(x=500, y=100)
  else:
    r4 = Label(frame, text = result4, fg = "gray")
    r4.place(x=500, y=100)

    # Create Object
root = Tk()
root.title("Encryptle Welcome Page")

# Initialize tkinter window with dimensions 100x100

root.geometry('600x200')

#Rules

rule = Label(root, text="Welcome to Encryptle! \n A matrix is a rectangular array or table of numbers, \n symbols, or expressions, arranged in rows and columns.\n At the start of this game, you will have 6 chances to guess a letter key to cypher the Encryptle. \n Each letter is assigned a simple numerical value where a=1, b=2, c=3, etc.. \n These numerical values will allow you to cypher the code! \n Please only guess lower case letters, and press submit when ready. \n Press the start button when you are ready! Good Luck!", fg='black')
rule.pack()

#start botton

btn = Button(root, bg='green', text = 'START', command = root.destroy)

# Set the position of button on the top of window

btn.pack()

root.mainloop()

#Window

frame = tk.Tk()
frame.title("ENCRYPTLE")
frame.geometry('600x338')
frame.resizable(False,False)

#Logo

canvas = Canvas(frame, width = 700, height = 200)
img = PhotoImage(file="finallogo.png")
canvas.create_image(300,30,image=img)
canvas.pack()

#Button


button = tk.Button(text="Quit", bg='red',   activeforeground='black', activebackground='pink', command = restart_program)
button.pack()
button.place(x=400,y=295)

#Button2

button2 = tk.Button(height=1, text="Submit",
command=getTextInput, bg='green')
button2.pack()
button2.place(x=100,y=295)

#Textbox:

global inputtxt
inputtxt = tk.Entry(frame, width = 3)
inputtxt.place(x=300,y=175)

#Textbox2:

global txt2
txt2 = tk.Entry(frame, width = 3)
txt2.place(x = 250, y = 175)

#Textbox3:

global txt3
txt3 = tk.Entry(frame, width = 3)
txt3.place(x=300, y=150)


#Textbox4:

global txt4
txt4 = tk.Entry(frame, width = 3)
txt4.place(x=250, y=150)


#displays encrypted word

matrix = Label(frame, text="Encryptle\n"+str(e[0][0])+"  "+str(e[0][1])+"\n"+str(e[1][0])+"  "+str(e[1][1]), fg="black")
matrix.place(x = 80, y=80)

input("Hit Enter to End")
