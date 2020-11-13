# Video #5 - Sintaxis Básica III - Funciones I

Una funcion es una linea de codigo agrupada que funcionan como una unidad, realizando una tarea especifica. 

Pueden o no devolver valores

pueden tener parametros/argumentos

a las funciones se las denominan metodo cuando se encuentran definida dentro de una clase.

## Utilidad funcion

reutlizacion de codigo, cuando sea necesario o si es necesario.

sintaxis de una funcion.

```
def nombre_funcion():
    instrucciones
    return (opcional)
```
```
def nombre_funcion(parametros):
    instrucciones
    return
````

funciones predefinidas, son las que vienen con el lenguaje.
funciones propias, son las que definimos nosotros.

```
def mensaje():
    print("Estamos aprendiendo python")
    print("Estamos aprendiendo instrucciones basicas")
    print("poco a poco iremos avanzando")

mensaje()
```

Para llamar a la funciona cantidad de veces 'n'

```
def mensaje():
    print("Estamos aprendiendo python")
    print("Estamos aprendiendo instrucciones basicas")
    print("poco a poco iremos avanzando")

mensaje()
mensaje()
mensaje()
```

```
def mensaje():
    print("Estamos aprendiendo python")
    print("Estamos aprendiendo instrucciones basicas")
    print("poco a poco iremos avanzando")

mensaje()
mensaje()

print("ejecuando codigo fuera de funcion")

mensaje()
```