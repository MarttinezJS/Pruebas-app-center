# Pruebas automatizadas de app center
Se ejecutarán las pruebas basadas en datos, con pytest, datos guardados en mongo, los cuales pueden ser accedidos atra vez de mongo express en el puerto 8081. Lo primero es clonar este repo haciendo  
~~~
git clone https://github.com/MarttinezJS/Pruebas-app-center.git
~~~
Luego ingresamos a la carpeta del proyecto
~~~
cd Pruebas-app-center
~~~
## Creacio e importacion de las bases de datos
levantar los contenedore de mongo y mongo express
~~~
docker compose up -d
~~~
en la carpeta "schemas" estan lo Json los cuales se pueden importar desde mongo express, accediendo al *localhost:8081*, creando la base de datos test, las colecciones de *posts*, *gets*, *deletes* y luego importar los Json con los datos
## Ejecucion del ambiente de pruebas
instalar pytest
~~~
pip install -U pytest
~~~
Y por último ejecutar las pruebas
~~~
pytest app/test/test.py -s
~~~
