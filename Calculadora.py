from tkinter import*

tk=Tk()
tk.title('Calculadora')
frame=Frame(tk)
frame.grid(column=0, row=0, padx=(50,50), pady=(50,50))
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0, weight=1)

valor=""
pantalla1= Entry(frame, width=25, text=valor)
pantalla1.grid(column=1, row=0, columnspan=5)

pantalla2= Entry(frame, width=25, text=valor)
pantalla2.grid(column=1, row=1, columnspan=5)

pantalla3= Label(frame, width=15, text=valor)
pantalla3.grid(column=2, row=6, columnspan=5)

def suma ():
    x=int(pantalla1.get())
    y=int(pantalla2.get())
    valor=str(x)+" + "+str(y)+" = "+str((x+y))
    print(valor)
    pantalla3.config(text=valor)

def resta ():
    x=int(pantalla1.get())
    y=int(pantalla2.get())
    valor=str(x)+" - "+str(y)+" = "+str((x-y))
    print(valor)
    pantalla3.config(text=str(valor))
    
def multiplicacion ():
    x=int(pantalla1.get())
    y=int(pantalla2.get())
    valor=str(x)+" X "+str(y)+" = "+str((x*y))
    print(valor)
    pantalla3.config(text=valor)

def divicion ():
    x=int(pantalla1.get())
    y=int(pantalla2.get())
    valor=str(x)+" / "+str(y)+" = "+str((x/y))
    print(valor)
    pantalla3.config(text=valor)

def enviar (c):
    
    pantalla1.insert(0,str(c))
        


b7=Button(frame,text="7", width=3, command=enviar(7))
b7.grid(column=1, row=2)

b8=Button(frame,text="8", width=3, command=enviar(8))
b8.grid(column=2, row=2)

b9=Button(frame,text="9", width=3, command=enviar(9))
b9.grid(column=3, row=2)

dividir= Button(frame, text="/", width=3,command=divicion)
dividir.grid(column=4, row=2)

b4=Button(frame,text="4", width=3, command=enviar(4))
b4.grid(column=1, row=3)

b5=Button(frame,text="5", width=3, command=enviar(5))
b5.grid(column=2, row=3)

b6=Button(frame,text="6", width=3, command=enviar(6))
b6.grid(column=3, row=3)

multi=Button(frame, text="X", width=3, command=multiplicacion)
multi.grid(column=4, row=3)

b1=Button(frame,text="1", width=3, command=enviar(1))
b1.grid(column=1, row=4)

b2=Button(frame,text="2", width=3, command=enviar(2))
b2.grid(column=2, row=4)

b3=Button(frame,text="3", width=3, command=enviar(3))
b3.grid(column=3, row=4)

menos=Button(frame,text="-", width=3, command=resta)
menos.grid(column=4, row=4)

b0=Button(frame,text="0", width=8, command=enviar(0))
b0.grid(column=1, row=5,columnspan=2)


igual=Label(frame,text="=", width=3)
igual.grid(column=1, row=6)

suma=Button(frame,text="+", width=8, command=suma)
suma.grid(column=3, row=5,columnspan=2)

tk.mainloop()

