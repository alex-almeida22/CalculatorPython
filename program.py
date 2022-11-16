def program():
    print("\n--------------------Calculadora-----------------------\n")
    print("1. Adição\n")
    print("2. Subtração\n")
    print("3. Multiplicação\n")
    print("4. Divisão\n")
    print("5. Potência\n")
    print("6. Raiz Quadrada\n")
    print("0. Sair\n")
    selection = input("Seleciona Opção: ")
    
    selectionFunction(selection)
    

def selectionFunction(selection):
    
    match selection:
        case "1":
            num1 = input("\nMeta um número: ")
            num2 = input("\nMeta outro número: ")
            addition(num1, num2)
        case "2":
            num1 = input("\nMeta um número: ")
            num2 = input("\nMeta outro número: ")
            subtraction(num1, num2)
        case "3":
            num1 = input("\nMeta um número: ")
            num2 = input("\nMeta outro número: ")
            multiplication(num1, num2)
        case "4":
            num1 = input("\nMeta um número: ")
            num2 = input("\nMeta outro número: ")
            division(num1, num2)
        case "5":
            num1 = input("\nMeta um número: ")
            num2 = input("\nMeta outro número: ")
            powerOf(num1, num2)
        case "6":
            num = input("\nMeta um número: ")
            squareRoot(num)   
        case "0":
            print("Tenha um bom dia :)")
            exit()
        case default:
            print("Número não válido! Tente Novamente\n")
            program()
     
def addition(num1, num2):
    val = float(num1) + float(num2)
    print("Resultado: " + str(val))
    program()

def subtraction(num1, num2):
    val = float(num1) - float(num2)
    print("Resultado: " + str(val))
    program()

def multiplication(num1, num2):
    val = float(num1) * float(num2)
    print("Resultado: " + str(val))
    program()

def division(num1, num2):
    val = float(num1) / float(num2)
    print("Resultado: " + str(val))
    program()

def powerOf(num1, num2):
    val = float(num1) ** float(num2)
    print("Resultado: " + str(val))
    program()

def squareRoot(num):
    val = float(num) ** (1/2)
    print("Resultado: " + str(val))
    program()


program();