# Project Urban Routes

**Descripción del Proyecto:**
Este proyecto hace parte del Bootcamp QA y tiene como objetivo probar de manera automatizada el flujo completo de pedir un taxi, desde la configuración de la dirección hasta la asignación del conductor.

*Urban Routes* es una aplicación que permite solicitar un taxi en línea, con opciones para seleccionar diferentes tarifas y servicios adicionales.
El objetivo de estas pruebas es asegurar que el proceso de solicitud de taxi funcione correctamente, incluyendo la selección de tarifas, el ingreso de datos de contacto y pago, y la confirmación de la reserva del taxi.

# Archivos y directorios:
- data.py: Datos que se utilizan en las pruebas.
- localizadores.py: Archivo que contiene los localizadores de cada uno de los elementos de la página.
- tests_Urbanroutes.py: Contiene la lista de comprobación para las pruebas.
- Urbanroutes.py: Archivo con los métodos utilizados en las pruebas.
- helpers.py: Archivo con la clase de métodos auxiliares.

# Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **Pytest**: Entorno de pruebas utilizado para automatizar y gestionar las pruebas.
- **Selenium**: Herramienta para simular la interacción del usuario con la web de Urban Routes.
- **Devtools**: Para identificar los localizadores desde Chrome.

# Ejecución de pruebas
- Ruta de archivo: Users/stephaniepino/PycharmProjects/qa-project-Urban-Routes-es-main
- Asegúrate de tener instalados los paquetes pytest y Selenium.
- Las pruebas utilizarán el navegador Chrome, así que asegúrate de tenerlo instalado. 
- Para ejecutar las pruebas asegúrate de estar en el directorio "tests_Urbanroutes.py", donde se encuentran las pruebas. Luego, ejecuta las pruebas utilizando pytest
- Al finalizar las pruebas, pytest mostrará un resumen de los resultados en la terminal.

# Funcionalidad de las pruebas:
Las pruebas automatizadas cubren los siguientes pasos del flujo de solicitud de un taxi:

1. Configurar la dirección: Se simula la configuración de la dirección de origen y destino del viaje.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito: Se simula la interacción con el modal de "Agregar una tarjeta" y se asegura que el campo CVV (id="code" class="card-input") pierda el enfoque para habilitar el botón de enlace.
5. Escribir un mensaje para el conductor.
6. Solicitar una manta y pañuelos.
7. Pedir 2 helados.
8. Esperar la búsqueda de un taxi: Se asegura que el modal de búsqueda de conductor aparezca correctamente y que la cuenta regresiva se inicie.

---

**Autor**: Stephanie Pino para el Sprint 8
