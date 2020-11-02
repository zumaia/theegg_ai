Tarea_22

Diseñar un algoritmo que resuelva el siguiente problema.

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa. Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día. Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de leche, observando el límite de peso del camión. Python

El archivo Tarea_22.py contiene el algoritmo en Python que resuelve el problema del lechero.

El programa pide los datos al usuario (no comprueba que los datos de entrada sean "buenos"). Las características de las vacas se almacenan en una lista de colecciones tipo diccionario. Se hacen todas las combinaciones de vacas que puede haber con la librería itertools, y se compara cada combinación, filtrando las que superan el peso permitido del cambión y almacenando la combinación que mayor producción de leche da. Finalmente se muestra el resultado por consola.

Muestro el ejercicio en formato notebook y en formato ejecutable.



