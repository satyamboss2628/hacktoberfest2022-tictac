from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.wm_iconbitmap('tictactoe.ico')
root.resizable(0,0)


p1_score = StringVar()
p2_score = StringVar()
ptr1 = 0
ptr2 = 0
flag = True
ctr=0


def click(event):
	global flag,ctr
	if event['text']==" " and flag==True:
		flag = False
		event['text'] = "X"
		ctr+=1
		check()
	elif event['text']==" " and flag==False:
		flag = True
		event['text'] = "O"
		ctr+=1
		check()
		flag = True
	else:
		messagebox.showinfo("tictactoe","Wrong input")


def clearButton():
	btn1["text"]=" "	
	btn2["text"]=" "
	btn3["text"]=" "
	btn4["text"]=" "
	btn5["text"]=" "
	btn6["text"]=" "
	btn7["text"]=" "
	btn8["text"]=" "
	btn9["text"]=" "


def check():
	


f = Frame(root)

btn1 = Button(f, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn1))
btn1.pack(side=LEFT)
btn2 = Button(f, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn2))
btn2.pack(side=LEFT)
btn3 = Button(f, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn3))
btn3.pack(side=LEFT)

f.pack()

f1 = Frame(root)

btn4 = Button(f1, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn4))
btn4.pack(side=LEFT)
btn5 = Button(f1, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn5))
btn5.pack(side=LEFT)
btn6 = Button(f1, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn6))
btn6.pack(side=LEFT)

f1.pack()


f2 = Frame(root)

btn7 = Button(f2, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn7))
btn7.pack(side=LEFT)
btn8 = Button(f2, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn8))
btn8.pack(side=LEFT)
btn9 = Button(f2, text=" ", fg="cyan", bg="black", font=("Ds-Digital", 34, "bold"), borderwidth=2, relief=SUNKEN, width=3, pady=10, command=lambda:click(btn9))
btn9.pack(side=LEFT)

f2.pack()

f3 = Frame(root)
player1 = Label(root,text="Player 1:", bg = "black", fg = "cyan",font=("Ds-Digital", 15, "bold"))
player1.pack(side=LEFT)

player1_entry = Entry(root,width=8,textvariable=p1_score, bg="black", fg="cyan", font=("Ds-Digital", 15))
player1_entry.pack(side=LEFT,padx=12)

f3.pack()

f4 = Frame(root,bg="grey")

player2 = Label(root,text="Player 2:", bg = "black", fg = "cyan",font=("Ds-Digital", 15, "bold"))
player2.pack(side=RIGHT, pady=10)

player2_entry = Entry(root,width=8,textvariable=p2_score, bg="black", fg="cyan", font=("Ds-Digital", 15))
player2_entry.pack(side=RIGHT,padx=12, pady=10)

f4.pack()

def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()
