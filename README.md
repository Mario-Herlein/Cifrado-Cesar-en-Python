Es una aplicación en Python que permite el cifrado y descifrado Cesar, con la particularidad de que puede descifrar sin contar con la clave de cifrado.
La aplicación se realizó para usar con Python 3 en adelante, tanto en Windows como en Linux
Se deberá tener instaladas las siguientes librerías:
•	doctest
•	re
•	requests
•	bs4
•	termcolor
•	unicodedata 
•	string


A continuación, detallo su funcionamiento.

Primeramente, se ingresa el mensaje a cifrar o descifrar.

Cifrado: Si se desea cifrar, se deberá ingresar la clave en la que se realizará el mismo. Una vez esto hecho, el programa pasa todos los caracteres a su forma sin diacríticos, o sea sin tildes, diéresis, etc. y lo pone en mayúsculas para normalizar el texto. Luego considerando la clave ingresada, reemplaza las letras tomando como referencia una lista que tiene el abecedario.
Realizado el cifrado procede a la impresión en pantalla del mensaje.

Descifrado: esta opción cuenta con tres alternativas posibles, que sea con clave, sin clave con texto en estilo continuo y sin clave con texto en estilo discontinuo. 

•	Con clave: Toma el texto cifrado, que pasará a mayúsculas para normalizar, además por estar cifrado, se encuentra en su forma sin diacríticos. Luego, considerando la clave y la lista que tiene como referencia, reemplaza las letras cifradas por su valor real.

•	Sin clave con texto en estilo continuo: Se considera que es un texto cifrado, sin espacio entre palabras, en este caso pasará todo el texto a mayúsculas para normalizar, además por estar cifrado, se encuentra en su forma sin diacríticos. Luego considerará las 27 claves existentes para descifrar y mostrará en pantalla el resultado posible para cada una de ellas, el las cuales el usuario elegirá el mensaje válido.

•	Sin clave con texto en estilo discontinuo: Se considera que es un texto cifrado, con espacio entre palabras, como un párrafo normal, en este caso pasará todo el texto a mayúsculas para normalizar. Posteriormente tomará la primera palabra y la irá codificando con cada una de las 27 claves, cada vez que pruebe una clave, el texto generado será buscado en un diccionario online, para comprobar de que se trate de una palabra válida en nuestro idioma, si el resultado es admitido y se trata de un mensaje de más de una palabra, se realiza la misma comprobación con la palabra siguiente, en caso de ser válida la segunda palabra se usa la clave probada para descifrar el resto del texto. La doble comprobación busca eliminar la posibilidad de falsos mensajes cuando la primera palabra del texto es monosílaba. 
