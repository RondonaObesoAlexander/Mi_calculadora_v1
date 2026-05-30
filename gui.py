import tkinter as tk
from tkinter import messagebox
from operacion import sumar, restar, multiplicar, dividir

def calcular():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        op = operacion_var.get()
        
        if op == '+': res = sumar(n1, n2)
        elif op == '-': res = restar(n1, n2)
        elif op == '*': res = multiplicar(n1, n2)
        elif op == '/': res = dividir(n1, n2)
        
        label_res.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos")

# Configuración de la ventana
root = tk.Tk()
root.title("Calculadora")

entry1 = tk.Entry(root); entry1.pack()
operacion_var = tk.StringVar(value='+')
tk.OptionMenu(root, operacion_var, '+', '-', '*', '/').pack()
entry2 = tk.Entry(root); entry2.pack()

tk.Button(root, text="Calcular", command=calcular).pack()
label_res = tk.Label(root, text="Resultado: "); label_res.pack()

root.mainloop()
