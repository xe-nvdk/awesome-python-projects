# Tuplas

## Caracteristicas

* Listas inmutables, no se pueden modificar después de su creación.
* Permiten extraer porciones pero el resultado es una tupla nueva. 
* S permiten comprobar si un elemento se encuentra en una tupa. 

## Ventajas

* Son mas rapidas
* menos espacio
* formatean strings
* pueden utilizarse como claves en un diccionario.

## Sintaxis

### Sintaxis basica

tupla=(elem1, elem2, elem3)

### Conversion de tupla a lista

mitupla=("juan", 13,1,1995)
milista=list(mitupla)
print(mitupla)

### Conversion de lista a tupla

milista=["juan", 1,2,3]
mitupla=tuple(milista)
print(mitupla)

### Verificar si Juan esta en la tupla

milista=["juan", 1,2,3]
mitupla=tuple(milista)
print("juan" in mitupla)

### conteo de entrada en la tupa

milista=["juan", 1,2,3]
mitupla=tuple(milista)
print(mitupla.count(13))

### Longitud

milista=["juan", 1,2,3]
mitupla=tuple(milista)
print(len(mitupla))

### Longitud de tupla

milista("juan",)
print(len(mitupla))

### empaquetado de tupla

mitupla="juan",13,1,1995
print(mitupla)

### desempaquetado de tupla

mitupla=("juan", 1, 3, 1995)
nombre, dia, mes, anio=mitupla
print(nombre)
print(dia)
print(anio)
print(mes)