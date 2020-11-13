# Video 7. Sintaxis basicas V. Las listas

Listas. Arrays. Pueden guardar diferentes tipos de valores. Se pueden expandir dinamicamente anadiendo nuevos elementos.

```
lista=[elemento1, elemento2, elemento3]
```

Indice, primer elemento del array es 0, sigue 1 y asi sucesivamente.

```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[0])
```
```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[:])
```

Indice negativo, Python empieza a contar desde el final. Empieza a contar desde uno

```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[-2])
```
```
marta
```

Acceder a porcion de la lista. Rango

```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[0:3])
```
```
['juan', 'maria', 'pepe']
```

Forma de escribir abreviada para listas

```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[:3])
```

```
lista=["juan", "maria", "pepe", "marta", "antonio"]

print(lista[1:])
```

Agregar elemento al final de la lista

```
lista = ["juan", "maria", "pepe", "marta", "antonio"]

lista.append("sandra")

print(lista[:])
```

Esto fue ocurrencia mia y funciona: Agregar elemento a la lista desde un input.

```
lista = ["juan", "maria", "pepe", "marta", "antonio"]

add_name = str(input("inserte su nombre: "))

lista.append(add_name)

print(lista[:])
```

Si lo queremos agregar a un espacio determinado de la lista...

```
lista = ["juan", "maria", "pepe", "marta", "antonio"]
lista.insert(2,"nacho")
print(lista[:])
```

Si queremos agregar varios elementos al array

```
lista = ["juan", "maria", "pepe", "marta", "antonio"]

lista.extend(["nacho", "sandra", "diego"])

print(lista[:])
```

Traer el indice del elemento de la lista

```
lista = ["juan", "maria", "pepe", "marta", "antonio"]

lista.extend(["nacho", "sandra", "diego"])

print(lista.index("nacho"))
```

