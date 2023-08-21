print('EJERCICIOS INTEGRADORES CLASE 7')

"""1. Escribir una función que calcule el máximo común divisor entre dos números"""

print('Resolucion ej 1')

def mcd(a, b):
  while b:
    a, b = b, a % b
  return a

print(mcd(12,18))
print(mcd(-5,20))

"""2. Escribir una función que calcule el mínimo común múltiplo entre dos números"""

print('Resolucion ej 2')

mcm = 1
a = int (input ('Ingrese el valor de A: '))
b = int (input ('Ingrese el valor de B: '))
if a<0:
    a = -a
if b<0:
    b = -b
dv = 2
while dv<=a or dv<=b:
    while (dv<=a and a%dv==0) or (dv<=b and b%dv==0):
        mcm *= dv
        if dv<=a and a%dv==0:
            a //= dv
        if dv<=b and b%dv==0:
            b //= dv
    dv += 1
print (mcm)



print('Resolucion ej 3')

"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."""

def word_frequency(text):
  
  words = text.split()

  
  frequency_dict = {}
  for word in words:
    if word in frequency_dict:
      frequency_dict[word] += 1
    else:
      frequency_dict[word] = 1
  sorted_frequency_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

  return sorted_frequency_dict

if __name__ == "__main__":
  text = input("Ingrese un texto: ")
  print(word_frequency(text))

print('Resolucion ej 4')

"""4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia."""

def cuenta_palabras(cadena):
  diccionario = {}
  for palabra in cadena.split():
    diccionario[palabra] = diccionario.get(palabra, 0) + 1
  return diccionario

def palabra_mas_repetida(diccionario):
  palabra_mas_repetida = max(diccionario, key=diccionario.get)
  frecuencia = diccionario[palabra_mas_repetida]
  return palabra_mas_repetida, frecuencia

if __name__ == "__main__":
  cadena = input("Ingresa una cadena de caracteres: ")
  diccionario = cuenta_palabras(cadena)
  tupla = palabra_mas_repetida(diccionario)
  print(tupla)

print('Resolucion ej 5')

"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva."""

def get_int_iter(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("El valor no es válido. Por favor, inténtelo de nuevo.")

get_int_iter("Ingrese un número: ")

def get_int_rec(prompt):

  try:
    return int(input(prompt))
  except ValueError:
    print("El valor ingresado no es válido. Por favor, intente nuevamente.")
    return get_int_rec(prompt)
  
get_int_rec("Ingrese un número: ")

print('Resolucion ej 6')

"""6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:
  def __init__(self, nombre='', edad=0, dni=''):
    self._nombre = nombre
    self._edad = edad
    self._dni = dni

  def get_nombre(self):
    return self._nombre

  def set_nombre(self, nombre):
    if isinstance(nombre, str):
      self._nombre = nombre
    else:
      raise ValueError("El nombre debe ser una cadena de texto")

  def get_edad(self):
    return self._edad

  def set_edad(self, edad):
    if isinstance(edad, int) and edad >= 0:
      self._edad = edad
    else:
      raise ValueError("La edad debe ser un número entero positivo")

  def get_dni(self):
    return self._dni

  def set_dni(self, dni):
    if isinstance(dni, str) and len(dni) == 8 and dni.isnumeric():
      self._dni = dni
    else:
      raise ValueError("El DNI debe ser una cadena de texto de 9 dígitos numéricos")

  def mostrar(self):
    print(f"Nombre: {self._nombre}\nEdad: {self._edad}\nDNI: {self._dni}")

  def es_mayor_de_edad(self):
    return self._edad >= 18
    
p = Persona()
p.set_nombre(input("Ingrese nombre y apellido: "))
p.set_edad(int(input("Ingrese edad: ")))
p.set_dni(input("Ingrese DNI: "))
p.mostrar()
print(f"Es mayor de edad ? {p.es_mayor_de_edad()}")

print('Resolucion ej 7')

"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

class Cuenta():
    
    def constructor(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad


    def setcantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def getcantidad(self, titular):
        self.__titular = titular

    def mostrar(self):
        return f"El titular es: {self.__titular}\nel saldo es: $ {str(self.__cantidad)}.-"

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = self.__cantidad + cantidad
            print(f"Ingresando: $ {str(cantidad)}.-")

    def retirar(self, cantidad):
        if cantidad >=0:
            self.__cantidad = self.__cantidad - cantidad
            print(f"Retirando:  $ {str(cantidad)}.-")


cuenta1 = Cuenta()
cuenta1.constructor("Walter White", 1000)
print(cuenta1.mostrar())
cuenta1.ingresar(50)
print(cuenta1.mostrar())
cuenta1.retirar(1250)
print(cuenta1.mostrar())

print('Resolucion ej 8')

"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta."""

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion, edad):
        Cuenta.constructor(self, titular, cantidad)
        self.__bonificacion = bonificacion
        self.__edad = edad
 

    def setbonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def getbonificacion(self):
        return str(self.__bonificacion)
    
    def titular_valido(self):
        if self.__edad >= 18 and self.__edad <= 25:
            return True        
        else: 
            return False

    def retirar(self, cantidad):
        if self.titular_valido():
            super().retirar(cantidad)
            print("Retiro correcto.\n")
        else: 
            print("El titular no es valido. Retiro anulado\n")

    def mostrar(self):
        if self.titular_valido() == True:
            return f"{super().mostrar()}, edad: {str(self.__edad)}, la bonificacion es: ${self.getbonificacion()}.-\n"
        else:
            return f"{super().mostrar()}, Edad: {str(self.__edad)}\nEl titular no es valido, no pertenece al segmento de la cuenta, no aplica bonficiacion\n"

cj1 = CuentaJoven("Aria Stark", 10000, 10, 19)
print(cj1.mostrar())
cj1.retirar(500)
print(cj1.mostrar())
cj2 = CuentaJoven("Berik Dondarrion", 5000, 10, 17)
print(cj2.mostrar())
cj2.retirar(500)
print(cj2.mostrar())