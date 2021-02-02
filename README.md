Este script en python funciona como un intérprete de la API de AEMET OpenData, con la finalidad de pasar los datos entregados en formato .JSON a formato .CSV para manejarlos como tablas en excel.

Está hecho pensando en usuarios que no conocen de programación.

Descargar los archivos en una misma carpeta.

## Qué se necesita si soy usuario de Windows 10?

Se necesita tener instalado Python 3.9 (preferiblemente), el cual puede descargarse desde la tienda oficial de Microsoft de forma gratuita.

- Python 3.9


También es necesario instalar algunas dependencias de Python, para esto tan sólo es necesario darle doble click al archivo: "instalar dependencias.bat". Si por el contrario, se desean instalar las dependencias de Python de forma manual, es necesario ejecutar las siguientes líneas de código en el prompt:

```sh
$ pip3 install requests
$ python3 -m pip install requests
$ python3 -m pip install pandas
```

## Cómo ejecuto el script de Python?
 
Para ejecutar el script, basta con darle doble click al archivo: "double click to execute.bat". Aunque si se desea ejecutar el script manualmente, hay que abrir el prompt de Windows, navegar hasta la dirección en que están contenidos los archivos, y ejecutar:

$ python3 app.py

## Usando el Script

Es necesario haber solicitado primero una API KEY en AEMET OpenData, la pueden solicitar en el siguiente link: https://opendata.aemet.es/centrodedescargas/altaUsuario?

A continuación, deben conocer el rango de fechas del cuál desean solicitar la información, y el código de la estación.

Seguir los pasos que se muestran en la app.

## Me generó el archivo de excel .CSV pero no está tabulado.

Para esto hay que elegir toda la columna donde está la información solicitada (generalmente toda la columna A), ir a la pestana de Datos> Texto a Columna.
Y elegir el delimitador, el cual probablemente es (,) si la pc está en castellano y (;) si está en inglés.

Para modificaciones, o solicitudes me pueden escribir a:
antonio_martinez88@hotmail.com