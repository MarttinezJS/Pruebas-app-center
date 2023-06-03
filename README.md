# Pruebas automatizadas de app center
Se ejecutarán las pruebas basadas en datos, con pytest, datos guardados en mongo, los cuales pueden ser accedidos atra vez de mongo express en el puerto 8081
## Ejecucion del ambiente de pruebas
Lo primero es clonar este repo haciendo un 
~~~
git clone https://github.com/MarttinezJS/Pruebas-app-center.git
~~~
Luego ingresamos a la carpeta del proyecto
~~~
cd Pruebas-app-center
~~~
Y por último ejecutar las pruebas
~~~
pytest app/test/test.py -s
~~~
