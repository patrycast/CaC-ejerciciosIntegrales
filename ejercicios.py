#1- Escribir una función que calcule el máximo común divisor entre dos números

def maximo_comun_denominador(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a
 
num1 = int(input("Ingresá el primer numero: "))
num2 = int(input("Ingresá el segundo numero: "))
 
print("El máximo común divisor de ", num1," y ", num2," es: ", maximo_comun_denominador(num1, num2))



# 2- Escribir una función que calcule el mínimo común múltiplo entre dos números

def minimo_comun_multiplo(a,b):
    c=max(a, b)
    while True:
        if (c % a ==0 ) and (c % b ==0):
            return c
        c += 1

print(minimo_comun_multiplo(2,4))     
            
  
# 3- Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).        

def contar_palabras(cadena):
    palabras = cadena.split() 
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower() 
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")



# 4- Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia


def contar_palabras(cadena):
    palabras = cadena.split()  
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.lower() 
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return (palabra_max, frecuencia_max)

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print("Frecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")

palabra_repetida, frecuencia = palabra_mas_repetida(resultado)
print(f"Tupla con palabra más repetida y su frecuencia: {palabra_repetida= }, {frecuencia= }")


# 5- Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.


def get_int():
    while True:
        try:
            valor = int(input("Ingresa un valor entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Inténtalo de nuevo.")

numero = get_int()
print(f"Valor entero ingresado: {numero}")

# recursiva
def get_int():
    try:
        valor = int(input("Ingresa un valor entero: "))
        return valor
    except ValueError:
        print("Valor no válido. Inténtalo de nuevo.")
        return get_int()

numero = get_int()
print(f"Valor entero ingresado: {numero}")


# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad= 0, dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        
    def set_nombre(self, nombre):
        self.nombre= nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        if edad>=0:
            self.edad=edad
        else:
            print("Ingrese una edad válida")    
        
    def get_edad(self):
        return self.edad  
    
    def set_dni(self, dni):
        if len(dni) ==9:
            self.dni= dni
        else:
            print("Debe ingresar 9 caracteres") 
            
    def get_dni(self):
        return self.dni          
               
               
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona = Persona()

persona.set_nombre("Elsa")
persona.set_edad(26)
persona.set_dni("118345679")

persona.mostrar()

if persona.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# 7- Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular= titular
        self.cantidad= cantidad
       
    def set_titular(self, titular):
        self.titular= titular
        
    def get_titular(self):
        return self.titular   
         
    def get_cantidad(self):
        return self.cantidad
           
    def mostrar(self):
        print("Datos del titular:")
        self.titular.mostrar()
        print(f"Cantidad: {self.cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad ingresada debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva.")


persona3 = Persona("norma", 40, "123456789")
cuenta3 = Cuenta(persona3, 1000.0)
cuenta3.mostrar()

cuenta3.ingresar(500.0)
cuenta3.mostrar()
cuenta3.retirar(200.0)
cuenta3.mostrar()


# 8- Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion= bonificacion
        
    def get_bonificacion(self): 
        return self.bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion= bonificacion
         
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25   
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")

    def mostrar(self):
        return f"Cuenta Joven\nBonificación: {self.bonificacion}%\n{super().mostrar()}"


# Ejemplo de uso
persona4 = Persona("samanta", 22, "542410395")
cuenta_joven = CuentaJoven(persona4, 500.0, 5.0)
cuenta_joven.mostrar()

if cuenta_joven.es_titular_valido():
    print("El titular es válido.")
else:
    print("El titular no es válido.")

cuenta_joven.ingresar(100.0)
cuenta_joven.mostrar()

cuenta_joven.retirar(50.0)
cuenta_joven.mostrar()





       