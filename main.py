from tkinter import *

main = Tk()
main.title("Demmí Zepeda y Nerea Beltrán")
main.geometry("500x500")

def cuestionario ():
  pregunta_01 = Label (main, text = "¿Cómo te sientes el día de hoy? Considera que 1 es muy mal y 5 es muy bien.", bd =4)
  variable_01 = IntVar()
  rb_01= Radiobutton(main, text= "super bien", justify = RIGHT, variable= variable_01, value=5)
  rb_02= Radiobutton(main, text= "bien", justify = RIGHT, variable= variable_01, value=4)
  rb_03= Radiobutton(main, text= "puedo estar mejor", justify = RIGHT, variable= variable_01, value=3)
  rb_04=Radiobutton(main, text= "mal ", justify = RIGHT, variable= variable_01, value=2)
  rb_05=Radiobutton(main, text= "muy mal ", justify = RIGHT, variable= variable_01, value=1)
  
def pronombres ():
  pregunta_02 = Label (main, text = "Elije los pronombres con los que te identificas", bd =4)
  variable_01 = StrVar()
  variable_02 = StrVar()
  variable_03 = StrVar()
  variable_04 = StrVar()
  variable_05 = StrVar()
  variable_06 = StrVar()
  variable_07 = StrVar()
  variable_08 = StrVar()
  rb_01= Checkbutton(main, text ="he/him", variable= variable_01, onvalue= 1, offvalue= 0, padx= 5, pady=5)
  rb_02= Checkbutton(main, text = "she/her", variable=variable_02, onvalue=1, offvalue=0, padx=5, pady=5)
  rb_03= Checkbutton(main, text ="they/them", variable= variable_03, onvalue= 1, offvalue= 0, padx= 5, pady=5)
  rb_04=Checkbutton(main, text = "xe/xem (neopronombres)", variable=variable_04, onvalue=1, offvalue=0, padx=5, pady=5)
  rb_05=Checkbutton( main, text ="kie/kir (neopronombres)", variable= variable_05, onvalue= 1, offvalue= 0, padx= 5, pady=5)
  rb_06 =Checkbutton( main, text ="elle/le", variable= variable_06, onvalue= 1, offvalue= 0, padx= 5, pady=5)
  pregunta_02.pack()
  rb_01.pack()
  rb_02.pack()
  rb_03.pack()
  rb_04.pack()
  rb_05.pack()
  rb_06.pack()



welcome = Label (main, text = "¡Bienvenide a este cuestionario!", relief = GROOVE, padx = 3, pady = 12)
welcome.pack()

name = Label (main, text = "Por favor ingresa tu nombre en el recuadro de abajo:")
name.pack()

nameEntry = Entry(main, bd=5, justify = LEFT)
nameEntry.pack(side=TOP)

apellido = Label (main, text= "Por favor ingresa tu apellido en el recuadro de abajo::", bd=5, justify = LEFT)
apellido.pack()

apellidoEntry = Entry (main, bd=5, justify = LEFT)
apellidoEntry.pack(side=TOP)

button_1 = Button(main, text = "Si estás listx para proseguir con el cuestionario, ¡HAZ CLICK AQUÍ!", command = cuestionario)
button_1.pack()

button_2= Button(main, text = "¿Quieres iniciar tu presentacion? si la respuesta es sí HAZ CLICK AQUI", command = pronombres)
button_2.pack()

adjetivos = Label(main, text = "Elige los adjetivos que sientas que te describan")
adjetivos.pack()




main.mainloop()
