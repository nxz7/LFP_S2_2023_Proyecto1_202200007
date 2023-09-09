# Lenguajes formales y de Programación
# Segundo semestre 2023
# proyecto 1
---
# Universidad San Carlos de Guatemala
## _Programador: Natalia Mariel Calderón Echeverría_
## _Carnet: 202200007_
-----
## Descprincion del proyecto
El proyecto consiste en crear un programa que tenga una intefaz grafica amigable con el usuario que permita analizar lexicamente el contenido de un archivo json, dicho analisis lexico debe realizarse tomando en cuenta la posible existencia de errores y manteniendo un control sobre ellos. El programa debe mostrar al usuario los elementos analizados lexicamente asi tambien como los errores, posteriormente se procede a realizar las debidas operacion a traves de un analisis de las misma.
## Objetivos
* Objetivo General
    * Desarrollar una herramienta capaz de actuar como analizador lexico, que reconozca el lenguaje y cumpla con las reglas establecidad y mantenga un control de los errores, esto a traves del manejo y lectura de archivos
* Objetivos Específicos
    * Desarrollar un analizador lexico a traves del uso de estados.
    * Manejo de caracteres en python.
    * Crear diagramas a traves de la informacion analizada a traves del uso de la libreria Graphviz.

## Requerimientos 
Programado en:
● Python 3.10.2
● Visual Studio Code
● Sistema operativo de 64 bits

---
## Codigo principal

## _Descripcion_
En el archivo gui.py es donde se encuentra todo el codigo relacionado con la intefaz grafica: botones, combobox, textbox, la ventana etc. Es por esas mismas razones que es aqui en donde la clase AFD.py y matematicas.py se usen y son utilizadas para poder brindarle al usuario la informacion que desea de una forma amigable, legible y sobre todo facil tanto de comprender como de usar.

Al unicio del programa se despliega una ventana en la que es posible, cargar un archivo de formato json, guardar el contenido que se encuentra en la textbox, guardar el contenido que se encuentra en la textbox bajo un nombre distinto o simplemente salir del programa. A su izquierda se encuentran tres botones que nos permite analizar el archivo, los errores y generar el reporte grafico. Al momento de presionar el boton analizar hacemos una llamada a nuestra clase AFD y procememos a analizar lexicamente el archivo json que fue cargado, asi tambien como sus errores. 
![ObtenerLink](https://i.ibb.co/wWRKttc/analizar.png)
El boton "errores" genera en forma de un archivo json una lista de los errores encontrados, asi tambien como la fila y columna en donde fueron encontrados, estos errores se encuentran a traves del codigo de la clase AFD, que como se menciona anteriormente mantiene un control de los errores. 
![ObtenerLink](https://i.ibb.co/5xm31wH/errores.png)
El boton reporte hace un llamado a la clase "matematicas.py" que a su vez se apoya en la clase AFD.py para hacer un analisis sintacticto del archivo analizado y procede a la realizacion de las operacion respectivas y a su vez a la creacion del grafico que representara a las mismas. 
![ObtenerLink](https://i.ibb.co/q94Hkfg/reporte.png)

  # _punto de vista del usuario y grafico del reporte_
  ![ObtenerLink](https://i.ibb.co/yfqwwFR/vista-usuario.png)


