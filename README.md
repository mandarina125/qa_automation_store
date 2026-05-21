# QA Automation Store 🛒

Proyecto de automatización de pruebas para una tienda online
usando Selenium, Pytest y Page Object Model.

## 🛠️ Tecnologías
- Python 3.11
- Selenium
- Pytest
- pytest-html
- Page Object Model (POM)

## 📁 Estructura del proyecto
qa_automation_store/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
└── conftest.py

## ▶️ Cómo ejecutar
1. Instalar dependencias
pip install -r requirements.txt

2. Ejecutar los tests
python -m pytest tests/ --html=reporte.html

## ✅ Tests incluidos
- Login exitoso con credenciales válidas
- Login fallido con credenciales inválidas
