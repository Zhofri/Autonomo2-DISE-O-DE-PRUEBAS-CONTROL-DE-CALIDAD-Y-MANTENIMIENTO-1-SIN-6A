# Algoritmo de Búsqueda Binaria y Pruebas Unitarias

Este repositorio contiene la implementación en Python del algoritmo de búsqueda binaria y su correspondiente batería de pruebas unitarias, cumpliendo con los requerimientos prácticos de la asignatura.

La búsqueda binaria es un algoritmo eficiente para encontrar la posición de un elemento en una lista ordenada. Su complejidad temporal en el peor de los casos es de $O(\log n)$, lo cual reduce significativamente el número de comparaciones en comparación con una búsqueda lineal tradicional.

## Estructura del Proyecto

*   `busqueda_binaria.py`: Contiene la lógica del algoritmo de búsqueda binaria implementado de manera iterativa.
*   `test_busqueda_binaria.py`: Define los casos de prueba unitaria utilizando el módulo estándar `unittest` de Python.
*   `resultado_pruebas.txt`: Archivo de texto que registra la salida oficial de la última ejecución exitosa del conjunto de pruebas.

---

## Prerrequisitos

Para ejecutar este código y sus pruebas, únicamente se requiere tener instalado **Python 3.x** en el sistema. No es necesario instalar librerías externas o dependencias de terceros, ya que todo el desarrollo se apoya en la biblioteca estándar de Python.

---

## Instrucciones de Uso

### 1. Ejecución del Algoritmo

Si deseas importar el algoritmo en tu propio script de Python, puedes hacerlo de la siguiente manera:

```python
from busqueda_binaria import busqueda_binaria

# La lista de entrada DEBE estar ordenada
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
objetivo = 23

resultado = busqueda_binaria(numeros, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("El elemento no se encuentra en la lista.")
```

### 2. Ejecución de las Pruebas Unitarias

Para verificar el correcto funcionamiento del algoritmo en todos los escenarios límite contemplados (búsquedas al inicio, al medio, al final, elementos inexistentes, listas vacías y listas con elementos duplicados), ejecuta el siguiente comando en tu terminal o consola:

```bash
python test_busqueda_binaria.py
```

La consola mostrará una salida similar a la siguiente indicando el éxito del proceso:

```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

### 3. Generación del Informe de Salida

Para redirigir y guardar los resultados del reporte de pruebas en un archivo local (`resultado_pruebas.txt`), puedes utilizar el redireccionamiento estándar en la línea de comandos de tu sistema operativo:

*   **En Windows (PowerShell / CMD):**
    ```cmd
    python test_busqueda_binaria.py > resultado_pruebas.txt 2>&1
    ```

*   **En Linux / macOS:**
    ```bash
    python test_busqueda_binaria.py > resultado_pruebas.txt 2>&1
    ```
