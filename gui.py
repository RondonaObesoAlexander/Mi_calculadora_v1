from operation import sumar, restar, multiplicar, dividir
from utils import obtener_numero

def main():
    print("--- Calculadora Python ---")
    num1 = obtener_numero("Primer número: ")
    op = input("Operación (+, -, *, /): ")
    num2 = obtener_numero("Segundo número: ")
    if op == '+':
        print(f"Resultado: {sumar(num1, num2)}")
    elif op == '-':
        print(f"Resultado: {restar(num1, num2)}")
    elif op == '*':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif op == '/':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Operación no reconocida.")

if __name__ == "__main__":
    main()
