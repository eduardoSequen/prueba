#1 Muestra hola mundo
def saludo():
    print("Hola mundo")

saludo()

#2 saluda pasando un nombre
def saludo_p(name):
    print("Hola", name)

saludo_p("Anibal")

#4 calcula cantidad con iva
def obtener_total(cantidad, iva = 0.21):
    total = cantidad + (cantidad * iva)
    return total
#sale el iva predeterminado
print("El total es:", obtener_total(100))
#sale el iva que se ingresa manualmente
print("El total es:", obtener_total(100, iva = 0.12))

#5 calcular el area de un circulo
def area_circulo(radius = 10):
    area = 3.1415 * radius**2
    print(area)
    return area

"""calcula el volumen de un cilindro
#utilizando la función de area anterior"""
def volumen_cilindro(altura, area_circulo):
    volumen = altura * area_circulo
    print(volumen)

volumen_cilindro(10, area_circulo())

#6 media de numeros de una lista
def media(lista):
    media = sum(lista)/ len(lista)
    return media

nums = [1,2,3,4,5]

print(media(nums))

#7 recibe una lista de números
# y devulve otra lista con sus cuadrados
def cuadrados(lista):
    lista_cuadrados = []
    for num in lista:
        lista_cuadrados.append(num**2)
    
    return lista_cuadrados

print(cuadrados([1,2,3,4,5,6,7]))

