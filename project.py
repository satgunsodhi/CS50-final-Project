import tkinter as tk

def setdisp(tb,value):
    tb.insert(value, value)
    print(value)
    return value

def setoperator(ls,tb,operator):
    ls.append(tb.get())
    ls.append(operator)
    tb.delete(0,'end')
    return operator

def ans(ls,tb):
    ls.append(tb.get())
    tb.delete(0,'end')
    a = ''
    for i in ls:
        a += i
    tb.insert(0,eval(a))
    ls.append(eval(a))
    print(ls)
    ls.clear()

def cl(tb):
    tb.delete(0,'end')

def main():
    ls = []
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Calculator")

    label = tk.Label(root, text="Simple Calculator", font =('Arial',18))
    label.pack()

    tb = tk.Entry(root)
    tb.pack(padx=10,pady=30)

    btn1 = tk.Button(root, text = '1', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"1"))
    btn1.place(x = 0, y = 125)

    btn2 = tk.Button(root, text = '2', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"2"))
    btn2.place(x = 125, y = 125)

    btn3 = tk.Button(root, text = '3', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"3"))
    btn3.place(x = 250, y = 125)

    btn4 = tk.Button(root, text = '4', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"4"))
    btn4.place(x = 0, y = 250)

    btn5 = tk.Button(root, text = '5', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"5"))
    btn5.place(x = 125, y = 250)

    btn6 = tk.Button(root, text = '6', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"6"))
    btn6.place(x = 250, y = 250)

    btn7 = tk.Button(root, text = '7', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"7"))
    btn7.place(x = 0, y = 375)

    btn8 = tk.Button(root, text = '8', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"8"))
    btn8.place(x = 125, y = 375)

    btn9 = tk.Button(root, text = '9', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"9"))
    btn9.place(x = 250, y = 375)

    btn0 = tk.Button(root, text = '0', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command = lambda: setdisp(tb,"0"))
    btn0.place(x = 0, y = 500)

    btnplus = tk.Button(root, text = '+', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: setoperator(ls,tb,'+'))
    btnplus.place(x = 375, y = 125)

    btnminus = tk.Button(root, text = '-', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: setoperator(ls,tb,'-'))
    btnminus.place(x = 375, y = 250)

    btnmult = tk.Button(root, text = '*', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: setoperator(ls,tb,'*'))
    btnmult.place(x = 375, y = 375)

    btndiv = tk.Button(root, text = '/', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: setoperator(ls,tb,'/'))
    btndiv.place(x = 375, y = 500)


    btnans = tk.Button(root, text = 'Ans', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: ans(ls,tb))
    btnans.place(x = 125, y = 500)


    btnclr = tk.Button(root, text = 'Clear', font = ('arial',18), height = 2, width = 4, padx = 10, pady = 10, command= lambda: cl(tb))
    btnclr.place(x = 250, y = 500)

    root.mainloop()

if __name__ == "__main__":
    main()