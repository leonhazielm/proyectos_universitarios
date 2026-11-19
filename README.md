# Proyectos Universitarios - Ingeniería en Computación e Informática

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

- **Interfaces gráficas (`Apps/`, `calculadora/`, `concentrado/`):** Aplicaciones de escritorio construidas con PyQt6 y Qt Designer (`.ui`), incluyendo navegación entre múltiples ventanas, calculadoras y resolución visual de series matemáticas (Fibonacci y factorial).
- **Estructuras de datos y algoritmos (`arboles.py`, `hash.py`, `listas_colas.py`, `big_O_factorial.py`):** Implementación de árboles, tablas hash, listas, colas, diccionarios y ejercicios de análisis de complejidad algorítmica.

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
