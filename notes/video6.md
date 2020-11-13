# Sintaxis basica IV, funciones II

variables y operaciones dentro de una funcion.

```
def suma():
    num_one = 5
    num_two = 7
    print(num_one+num_two)

suma()
```

reutilizar la funcion:

```
def suma():
    num_one = 5
    num_two = 7
    print(num_one+num_two)

suma()
suma()
suma()
```

reutizar funciones con parametros

```
def suma(num_one, num_two):
    print(num_one+num_two)

suma(5,7)
suma(2,3)
suma(35,400)
```

funcion con return

```
def suma(num_one, num_two):
    resultado = num_one + num_two
    return resultado

print(suma(5,7))

print(suma(3,7))

print(suma(12,5))
```

Guardando resultado en una variable e imprimiendo la variable.

```
def suma(num_one, num_two):
    resultado = num_one + num_two
    return resultado

almacena_resultado=suma(5,7)

print(almacena_resultado)
```

Python siempre pasa valores por referencia. Para Python todas son referencias.