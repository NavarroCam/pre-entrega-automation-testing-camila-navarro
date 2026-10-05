# Pre-Entrega · Automation Testing — Camila Navarro

Proyecto de pre-entrega del curso **Automatización QA** de Talento Tech.

## Propósito del proyecto
Automatizar flujos básicos de navegación web sobre [saucedemo.com](https://www.saucedemo.com), un sitio demo diseñado para prácticas de testing. Las pruebas cubren:

1. **Login**: inicio de sesión con credenciales válidas (`standard_user` / `secret_sauce`) y validación de la redirección a `/inventory.html`.
2. **Navegación y catálogo**:
   - Título de la página de inventario ("Products").
   - Presencia de productos y nombre/precio del primero.
   - Elementos de la interfaz: menú, filtro de ordenamiento y carrito.
3. **Carrito**: agregar un producto, verificar el contador del carrito y comprobar que el producto aparece en la página del carrito.

## Tecnologías utilizadas
- **Python 3**: lenguaje principal
- **Pytest**: framework de testing
- **Selenium WebDriver**: automatización del navegador (Chrome)
- **pytest-html**: generación del reporte HTML
- **Git y GitHub**: control de versiones

## Estructura del proyecto
```
pre-entrega-automation-testing-camila-navarro/
├── tests/
│   ├── conftest.py          # Fixtures del navegador y captura automática en fallos
│   └── test_saucedemo.py    # Casos de prueba
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Funciones auxiliares: driver, login, esperas y capturas
├── reports/
│   ├── reporte.html         # Reporte HTML de la ejecución
│   ├── ejecucion.log        # Log de ejecución
│   └── capturas/            # Capturas de pantalla de tests fallidos
├── pytest.ini               # Configuración de Pytest y del log
└── README.md
```

## Instalación de dependencias
Requisitos previos: **Python 3.8+**, **Git** y **Google Chrome** instalados.

```bash
# 1. Clonar el repositorio
git clone https://github.com/NavarroCam/pre-entrega-automation-testing-camila-navarro.git
cd pre-entrega-automation-testing-camila-navarro

# 2. Crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / Mac

# 3. Instalar las dependencias
pip install selenium pytest pytest-html
```

> Selenium (versión 4.6 o superior) descarga automáticamente el ChromeDriver compatible con tu versión de Chrome.

## Cómo ejecutar las pruebas
Ejecutar todos los tests:
```bash
pytest -v
```

Ejecutar los tests y generar el reporte HTML:
```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Ver los mensajes `print` en la terminal (por ejemplo, nombre y precio del primer producto y "Test OK"):
```bash
pytest -v -s
```

## Evidencias
- **Reporte HTML**: `reports/reporte.html`. Se abre con cualquier navegador.
- **Log de ejecución**: `reports/ejecucion.log`. Registra cada paso con fecha y hora.
- **Capturas automáticas**: cuando un test falla, se guarda una captura en `reports/capturas/` y se adjunta al reporte HTML.

## Buenas prácticas aplicadas
- **Tests independientes**: cada test abre su propio navegador, así que la falla de uno no afecta a los demás.
- **Esperas explícitas** (`WebDriverWait`) en los pasos críticos: login, URL, badge del carrito.
- **Distintas estrategias de localización**: `ID`, `NAME`, `CSS_SELECTOR` y `CLASS_NAME`.
- **Código organizado** en tests y funciones auxiliares, con comentarios y nombres descriptivos.