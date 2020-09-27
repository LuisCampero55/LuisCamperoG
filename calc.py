def sumam(a,b):
    return a + b

def resta(a, b):
    return a - b

def producto(a, b):
    return a * b

def division(a, b):
    if(b <= 0):
        return "El denominador no puede ser igual o menor a 0"
    return a / b

def tsumas(a=10):
    b = "+"
    numero = 0
    result = ""
    while numero < a:
      result = result + b + "\n"
      b = b + "+"
      numero = numero + 1
    return result

