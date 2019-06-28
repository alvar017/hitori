El código queda dividido en cinco archivos pincipales.
	Dos archivos cedidos en la propuesta del problema:
		búsqueda_espacio_estado.py
		problema_espacio_estado.py
	Tres archivos de generación propia:
		hitory.py (archivo principal)
		auxiliar.py (clases auxiliares de comprobación)
		investiga.py (clase general de creación de la acción)

El código puede probarse haciendo uso del archivo hitori.exe (recordamos que tarda en ejecutar entre 30
y 50 segunda) o ejecutando el archivo hitori.py

Video muestra del archivo .exe: https://www.youtube.com/watch?v=QASOYTZuO_U

El primer paso cuando se ejecuta el código es introducir la matriz del tablero a resolver, que tiene el mismo
formato que ejemplos dados en ejemplos_reto.txt y ejemplos_prueba.txt

Una vez aceptada la matriz el usuario debe decidir que algoritmo de búsqueda usar y posteriormente indicar si
quiere que se haga el detallado o no (a excepción de la búsqueda A* que no usa detallado)

Seguidamente se le muestra la representación tanto del tablero inicial como del tablero solución.