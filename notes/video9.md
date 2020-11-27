# Diccionarios

* Estructura de datos que permiten almacenar valores de diferentes tipos.
* Los datos se almacenan a una clave de tal forma que se crea una asociacion de tipo clave:valor para cada elemento almacenado
* Los elementos almacenados no estan ordenados.
* podemos almacenar, listas, tuplas u otros diccionarios

## Sintaxis basica

### Ejemplo 1

midiccionario={"alemania":"berlin", "francia":"paris", "reino unido":"londres", "uruguay":"montevideo"}
print(midiccionario{"francia"})

### Agregando una entrada mas al diccionario

midiccionario={"alemania":"berlin", "francia":"paris", "reino unido":"londres", "uruguay":"montevideo"}
midireccionario["italia"]="lisboa"
print(midiccionario)

### Asignar un valor nuevo a una clave

midiccionario={"alemania":"berlin", "francia":"paris", "reino unido":"londres", "uruguay":"montevideo"}
midireccionario["italia"]="lisboa"
print(midiccionario)
midireccionario["italia"]="Roma"
print(midiccionario)

### Eliminar un valor de un diccionario

midiccionario={"alemania":"berlin", "francia":"paris", "reino unido":"londres", "uruguay":"montevideo"}
midireccionario["italia"]="lisboa"
print(midiccionario)
midireccionario["italia"]="Roma"
print(midiccionario)
del midireccionario["reino unido"]
print(midiccionario)

### Alojar diferentes tipo de datos en un diccionario

midireccionario={"alemania":"berlin", 23:"jordan", "mosqueteros":3}
print(midireccionario)

### convirtiendo una lista a diccionario

milista=["espania", "francia", reino unido", "alemania"]
midiccionario={milista[0]:"madrid", milista[1]:"Paris", milista[2]:"londres", milista[2]:"berlin"}
print(midiccionario)

### Acceder a un valor

milista=["espania", "francia", reino unido", "alemania"]
midiccionario={milista[0]:"madrid", milista[1]:"Paris", milista[2]:"londres", milista[2]:"berlin"}
print(midiccionario["francia"])

### Diccionario dentro de otro diccionario

midiccionario={23:"jordan", "nombre":"Michael", "equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario)

### keys devuelve todas las claves del diccionario

midiccionario={23:"jordan", "nombre":"Michael", "equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())

### values devuelve los valores de las claves

midiccionario={23:"jordan", "nombre":"Michael", "equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())

### cantidad de valores en un diccionario

midiccionario={23:"jordan", "nombre":"Michael", "equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

