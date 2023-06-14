from tkinter.ttk import Combobox
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from numpy import linspace, exp, sin, cos, sinh, cosh
from funciones import exponencial, exponencial_decreciente, seno, coseno, senohyp, cosenohyp, cambiar_grado

class Interfaz:

    def __init__(self) -> None:
        self.funciones = [exponencial, exponencial_decreciente, seno, coseno, senohyp, cosenohyp]
        self.funciones_originales = [exp, exp, sin, cos, sinh, cosh]
        self.nombres_funciones = ["e^x","e^(-x)","seno(x)","cos(x)","sinh(x)","cosh(x)"]
        self.raiz = Tk()
        self.raiz.title("Polinomios de Taylor y Maclaurin")
        self.raiz.resizable(0, 0)

        self.base = Frame()
        self.base.pack()

        Label(self.base, text="Grado del polinomio").grid(row=0, column=0, padx=10)
        self.campo_grado = Entry(self.base)
        self.campo_grado.config(width=10)
        self.campo_grado.grid(row=0, column=1)
        self.campo_grado.config(justify="center")

        Label(self.base, text="Límite inferior a").grid(row=0, column=2, padx=10)
        self.campo_a = Entry(self.base)
        self.campo_a.config(width=10)
        self.campo_a.grid(row=0, column=3)
        self.campo_a.config(justify="center")

        Label(self.base, text="Límite superior b").grid(row=0, column=4, padx=10)
        self.campo_b = Entry(self.base)
        self.campo_b.config(width=10)
        self.campo_b.grid(row=0, column=5)
        self.campo_b.config(justify="center")

        Label(self.base, text="Número de puntos").grid(row=0, column=6, padx=10)
        self.campo_puntos = Entry(self.base)
        self.campo_puntos.config(width=10)
        self.campo_puntos.grid(row=0, column=7)
        self.campo_puntos.config(justify="center")

        Label(self.base, text="Función").grid(row=0, column=8, padx=10)
        self.menu_funciones = Combobox(self.base)
        self.menu_funciones.config(width=5)
        self.menu_funciones['values'] = ("e^x", "e^-x", "sen(x)", "cos(x)", "senh(x)", "cosh(x)")
        self.menu_funciones.current(0)
        self.menu_funciones.grid(row=0, column=9)
        self.funcion_actual = 0

        self.marcado = IntVar()
        self.grafica_original = Checkbutton(self.base, text="Ver Gráfica Original", variable=self.marcado, onvalue=1, offvalue=0, state="disable", command=self.graficar_original)
        self.grafica_original.grid(row=0, column=11, padx=10)

        self.boton_graficar = Button(self.base, text="Graficar", command=self.graficar)
        self.boton_graficar.grid(row=0, column=12, padx=10, pady=5)
        
        self.figura = Figure(figsize=(12, 6), dpi=90)
        self.ax = self.figura.add_subplot(111)
        self.ax.grid(True)
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y(x)$')
        self.ax.set_title("Polinomios de Taylor y Maclaurin")
        self.linea = FigureCanvasTkAgg(self.figura, self.base)
        self.linea.get_tk_widget().grid(row=2, column=0, pady=10, columnspan=13)
        self.barra_navegacion = NavigationToolbar2Tk(self.linea, self.raiz)
        self.barra_navegacion.update()
        self.raiz.mainloop()

    def graficar(self):
        self.grafica_original.config(state="normal")
        grado = int(self.campo_grado.get())
        self.a = float(self.campo_a.get())
        self.b = float(self.campo_b.get())
        self.puntos = int(self.campo_puntos.get())
        self.opcion = self.menu_funciones.current()
        if self.opcion != self.funcion_actual:
            self.ax.clear()
            self.funcion_actual = self.opcion
        cambiar_grado(grado)
        self.ax.grid(True)
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y(x)$')
        self.ax.axhline(0, color="gray")
        self.ax.axvline(0, color="gray")
        self.ax.set_xlim([self.a, self.b])
        etiqueta = "$y=T_{"+self.campo_grado.get()+"}(x)$"
        x = linspace(self.a, self.b, self.puntos)
        y = self.funciones[self.opcion](x)
        self.ax.plot(x, y, label=etiqueta)
        self.ax.legend(loc=2)
        self.linea.draw()
        self.marcado.set(0)

    def graficar_original(self):
        if self.marcado.get() == 1:
            self.grafica_original.config(state="disable")
        x = linspace(self.a, self.b, self.puntos)
        y = self.funciones_originales[self.opcion](x if self.opcion != 1 else -1*x)
        self.ax.plot(x, y, label="$"+self.nombres_funciones[self.opcion]+"$")
        self.ax.legend(loc=2)
        self.linea.draw()

if __name__ == "__main__":
    ventana = Interfaz()
    