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
            if(num1.isnumeric()):
                num2 = input("\nMeta outro número: ")
                if(num2.isnumeric()):
                    addition(num1, num2)
                else:
                    print("Segundo Número Inválido. Tente Novamente!")
                    program()
            else:
                print("Primeiro Número Inválido. Tente Novamente!")
                program()
        case "2":
            num1 = input("\nMeta um número: ")
            if(num1.isnumeric()):
                num2 = input("\nMeta outro número: ")
                if(num2.isnumeric()):
                    subtraction(num1, num2)
                else:
                    print("Segundo Número Inválido. Tente Novamente!")
                    program()
            else:
                print("Primeiro Número Inválido. Tente Novamente!")
                program()
            
        case "3":
            num1 = input("\nMeta um número: ")
            if(num1.isnumeric()):
                num2 = input("\nMeta outro número: ")
                if(num2.isnumeric()):
                    multiplication(num1, num2)
                else:
                    print("Segundo Número Inválido. Tente Novamente!")
                    program()
            else:
                print("Primeiro Número Inválido. Tente Novamente!")
                program()
            
        case "4":
            num1 = input("\nMeta um número: ")
            if(num1.isnumeric()):
                num2 = input("\nMeta outro número: ")
                if(num2.isnumeric()):
                    division(num1, num2)
                else:
                    print("Segundo Número Inválido. Tente Novamente!")
                    program()
            else:
                print("Primeiro Número Inválido. Tente Novamente!")
                program()
            
        case "5":
            num1 = input("\nMeta um número: ")
            if(num1.isnumeric()):
                num2 = input("\nMeta outro número: ")
                if(num2.isnumeric()):
                    powerOf(num1, num2)
                else:
                    print("Segundo Número Inválido. Tente Novamente!")
                    program()
            else:
                print("Primeiro Número Inválido. Tente Novamente!")
                program()
            
        case "6":
            num = input("\nMeta um número: ")
            if(num.isnumeric()):
                squareRoot(num)   
            else:
                print("Número Inválido. Tente Novamente!")
                program()
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
    if(num2 == 0):
        print("Divisão por 0 é impossível. Tente Novamente!")
    else:
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