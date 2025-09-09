# AIHB-Costeo

Sistema de **costeo inteligente** para Hidrobart.
Basado en **Python + NiceGUI + SQLAlchemy + Redis**.

---

## 🚀 Características

- Cálculo de costos en destino y precios proyectados.
- Integración con base de datos externa y Redis.
- Estructura modular y escalable.
- Preparado para despliegue en máquina virtual (VM) con GitHub Actions.

---

## 📂 Estructura del proyecto

- aihbcosteo/
- ├── app.py # Punto de entrada (gatillador)
- ├── config.py # Configuración global (DB, Redis, .env)
- ├── core/ # Núcleo (header, perfil, layout, db)
- ├── services/ # Integraciones externas
- ├── frontend/ # Vistas y componentes NiceGUI
- ├── models/ # Tablas y ORM (SQLAlchemy)
- ├── utils/ # Utilidades y helpers
- └── .github/workflows # CI/CD (despliegue)

---

## ⚙️ Requisitos

- Python 3.11+
- pip
- Redis

---

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/philippeAbadie83/IAHBCosteo.git
cd IAHBCosteo

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate   # En Windows
# source .venv/bin/activate   # En Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

python app.py
Abrir en el navegador: http://localhost:8080

```
