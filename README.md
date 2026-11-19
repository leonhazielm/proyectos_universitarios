# Proyectos Universitarios 

Repositorio con prácticas y aplicaciones desarrolladas en Java y Python durante mis estudios en la Universidad ITSPR | Instituto Tecnológico Superior de Purísima del Rincón perteneciente al TECNM. El enfoque principal es la programación orientada a objetos, estructuras de datos, lógica de negocio y desarrollo de interfaces gráficas de escritorio.

## Tecnologías

- **Lenguajes:** Java (JDK 25), Python 3
- **Interfaces gráficas:** PyQt6, Qt Designer
- **Entornos de desarrollo:** IntelliJ IDEA, Visual Studio Code

## Estructura del repositorio

### Java (`codigos_universidad/JAVA_POO`)

- **`sistema_gestion_restaurante_poo`**: Aplicación de consola para administrar productos (comidas y bebidas), registrar clientes y gestionar órdenes de compra. Incluye validación de datos, cálculo de cargos por tamaño, aplicación de descuentos según el tipo de cliente y corte de ventas del día.
- **`sistema_vehiculos_herencia_poo`**: Modelo de flotilla vehicular utilizando herencia (`Vehiculo`, `Automovil`, `Motocicleta`) y sobrescritura de métodos para calcular costos de mantenimiento.
- **`catalogo_biblioteca_herencia_poo`**: Gestión de inventario bibliográfico (`Libro`, `Revista`) con filtrado dinámico por año de publicación sobre colecciones.
- **`calculo_nomina_poo`**: Cálculo de salarios base, horas extra y búsqueda del empleado con mayor percepción dentro de una lista dinámica.
- **`registro_calificaciones_alumnos`**: Captura de notas por alumno mediante arreglos de objetos, cálculo de promedios y evaluación de estatus académico.
- **`registro_clientes_sobrecarga`**: Alta de clientes implementando sobrecarga de constructores para registros personalizados y valores por defecto.
- **`registro_kilometraje_choferes`**: Control de distancias recorridas por conductor a lo largo de la semana utilizando arreglos paralelos y matrices.
- **`juego_adivinar_numero`**: Programa interactivo con generación de números aleatorios, control de intentos y registro de historial.
- **`contador_ceros_matriz`**: Captura validada de matrices numéricas de tamaño dinámico y conteo de elementos en cero.

### Python (`codigos_universidad/Python_Estructuras_y_GUI`)


- **Sistema de Algoritmos de Ordenamiento con GUI (`Proyecto 2`):** Aplicación de escritorio en PyQt6 con menú principal (`main.py`) que integra cuatro módulos independientes (`burbuja.py`, `quick.py`, `shell.py`, `radix.py`). Implementa los algoritmos desde cero sin funciones nativas de ordenamiento ni `max()`, validando entradas numéricas y conservando intacta la lista original mediante copias en memoria.
- **Suite Integrada de Estructuras Lineales y Matemáticas (`concentrado/`):** Interfaz centralizada (`main.ui`) que conecta cuatro aplicaciones:
  - **Mesa de Ayuda (`Mesa.py`):** Gestión de tickets combinando una cola FIFO para atención por orden de llegada, una pila LIFO para historial y reversión de atenciones (`deshacer`), y búsqueda recursiva por usuario.
  - **Series Matemáticas (`Facto.py`, `Finonacci.py`):** Cálculo iterativo de factorial y secuencia de Fibonacci con manejo de excepciones y validación de enteros.
  - **Calculadora (`Calculadora.py`):** Operaciones aritméticas básicas con evaluación controlada de expresiones y alertas gráficas (`QMessageBox`).
- **Sistema CRUD de Registro Estudiantil (`formulario_diccionarios/`):** Formulario de escritorio respaldado por diccionarios anidados indexados por número de control para búsquedas en tiempo constante $O(1)$, con validación de campos obligatorios y confirmación de sobrescritura.
- **Calculadora de Escritorio (`calculadora/`):** Interfaz construida con `QGridLayout` (`ventana_calculadora.ui`) y manejo de errores ante expresiones inválidas o divisiones entre cero.
- **Navegación Multi-ventana (`Apps/`):** Arquitectura modular en PyQt6 que demuestra la instanciación y comunicación entre ventanas independientes (`QMainWindow`).
- **Árbol Binario de Búsqueda (`arboles.py`):** Implementación de estructura jerárquica (`Nodo`, `ArbolBinarioBusqueda`) con inserción recursiva, búsqueda binaria y recorrido inorden para salida ordenada.
- **Tabla Hash con Mapeo ASCII (`hash.py`):** Simulación de almacenamiento en memoria indexada mediante conversión de caracteres a código ASCII y función modular (`suma % 5`).
- **Benchmarking de Complejidad Algorítmica (`big_O_factorial.py`):** Cálculo iterativo de factorial instrumentado con `time.time()` y `time.process_time()` para medir tiempo real de ejecución frente a tiempo neto de CPU.
- **Sistema de Mesa de Ayuda en Consola (`proyecto_primer_parcial.py`):** Arquitectura orientada a objetos (`Ticket`, `MesaAyuda`) que integra colas FIFO, pilas LIFO y búsqueda recursiva desde terminal.
- **Estructuras Lineales y Algoritmos de Dos Punteros (`listas_colas.py`, `polindromo.py`):** Operaciones de inserción y extracción por índice sobre listas/colas y verificación de palíndromos mediante recorrido convergente de extremos (`O(n)`).


## Ejecución
1. Entrar a la carpeta `src` del proyecto correspondiente:
   `cd codigos_universidad/JAVA_POO/sistema_gestion_restaurante_poo/src`
2. Compilar y ejecutar:
   `javac *.java`
   `java Main`

### Python
1. Instalar la librería para interfaces gráficas (si aplica):
   `pip install PyQt6`
2. Ejecutar el script:
   `python nombre_del_archivo.py`
