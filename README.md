# Recorriendo objetos de hasta 3 anidaciones.
En este ejemplo se recorre un objeto de hasta 3 niveles de anidación, se le pasa alguna de las claves (Los objetos se construyen con una clave que siempre se encierra entre comillas dobles, y un valor que dependiendo del tipo de dato puede o no ir encerrado entre comillas ejemplo: ``` {"name": "Raúl"} ```) del objeto
y si la encuentra te regresa el valor de esa CLAVE en el objeto.

## Como funciona.
Para el primer nivel se hace un simple ```.get(CLAVE)``` pasandole la clave que buscamos y si no encuentra nada regresa un None y se va a buscar al siguiente nivel.

Para los siguientes 2 niveles lo que hace es buscar si cada CLAVE contiene otro objeto con más CLAVES (por que pueden existir objetos vacios) esto con ayuda de ```.keys()```; con un ciclo for ```for object_1 in json_object.keys()``` recorremos cada CLAVE buscando si alguna tiene un objeto con más CLAVES.
Después a nuestro objeto principal le pasamos el objeto actual encontrado ``` json_object.get(object_1, None) ``` y buscamos la clave dentro de ese objeto ``` json_object.get(object_1, None).get(field, None) ```

Si no llega a encontrar la CLAVE que estamos buscando regresará un error.

## Correr el proyecto
Para correr el proyecto:
1. Descargar el repo en tu directorio de preferencia.

2. Ejecutar el siguiente comando:
``` python recorrer_objects.py CLAVE object.json ```
Donde clave es alguna de nuestras claves del objeto por ejemplo ``` name ``` y object.json es un archivo .json que contiene un objeto creado previamente.

EL JSON PUEDE MODIFICARSE AL GUSTO DE  CADA QUIÉN PERO CON ESTE EJEMPLO SOLO PODRÁ TENER HASTA 3 NIVELES DE ANIDAMIENTO.


