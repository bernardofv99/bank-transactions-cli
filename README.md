# 🧾 Bank Transactions CLI

## 🧩 README del Proyecto

Este documento forma parte del reto técnico propuesto por Interbank Academy. A continuación, se presenta la documentación del proyecto incluyendo introducción, instrucciones de ejecución, enfoque técnico y estructura general.

---

## 1️⃣ Introducción

Este proyecto fue desarrollado como parte de un reto técnico de la Interbank Academy.  
El objetivo es construir una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte con:

- El **balance final** (Créditos - Débitos)
- La **transacción con el monto más alto**
- El **conteo de transacciones** por tipo (Crédito y Débito)

---

## 2️⃣ Instrucciones de Ejecución

A continuación, se detallan los pasos para instalar y ejecutar el proyecto correctamente:

### 🔧 Requisitos

- Python 3.8 o superior
- Dependencias definidas en `requirements.txt`

### 📦 Pasos de instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/codeableorg/interbank-academy-25.git
   cd interbank-academy-25
   ```

2. Crear y activar un entorno virtual (recomendado):

   - En Linux/macOS:

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. Instalar las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación principal:

   ```bash
   python main.py
   ```

   Esto procesará el archivo por defecto ubicado en `data/data.csv`.

5. (Opcional) Ejecutar la aplicación con un archivo CSV personalizado:

   ```bash
   python main.py --csvfile ruta/a/otro_archivo.csv
   ```

6. (Opcional) Ejecutar las pruebas unitarias:

   ```bash
   pytest
   ```

---

## 3️⃣ Enfoque y Solución

El proyecto fue diseñado siguiendo principios de **arquitectura limpia**, **modularidad** y **precisión financiera**. Las decisiones clave incluyen:

- **Separación de responsabilidades:**  
  Toda la lógica de negocio se encuentra en la clase `TransactionProcessor` (`app/processor.py`). El archivo `main.py` actúa como punto de entrada de la CLI.

- **Redondeo financiero correcto:**  
  Se utiliza la función `format_money()` con `Decimal("0.01")` y `ROUND_HALF_UP` para asegurar que todos los montos estén redondeados con precisión contable a dos decimales.

- **Uso de pandas:**  
  El archivo CSV se carga utilizando `pandas` para aprovechar su eficiencia, robustez y facilidad de iteración.

- **Estructura mantenible y extensible:**  
  El proyecto está listo para escalar fácilmente con funcionalidades adicionales como filtros, exportadores o soporte a múltiples monedas.

- **Pruebas automatizadas:**  
  Se incluye una carpeta `tests/` con pruebas unitarias para asegurar que los cálculos de balance, máximos y conteo funcionan correctamente.

---

## 4️⃣ Estructura del Proyecto

```
interbank-academy-25/
├── app/
│   ├── processor.py         # Clase principal para el procesamiento de transacciones
│   └── utils.py             # Funciones auxiliares (format_money() por ahora)
├── data/
│   └── data.csv             # Archivo CSV de entrada por defecto
├── tests/
│   └── test_processor.py    # Pruebas unitarias del procesador
├── main.py                  # Punto de entrada de la aplicación CLI
├── requirements.txt         # Dependencias necesarias
└── README.md                # README
```
