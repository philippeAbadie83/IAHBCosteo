---
# Changelog
Todas las modificaciones relevantes en este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).
---

## [Unreleased]

### Added

- Configuración inicial de CI/CD con GitHub Actions para despliegue en VM de Azure.
- Definición de secretos en GitHub (`SSH_HOST`, `SSH_USER`, `SSH_KEY`).
- Reglas de seguridad en Azure NSG para permitir acceso solo desde IPs de GitHub Actions.

### Changed

- Organización de llaves `.pem` en carpetas separadas (`~/.ssh/azure` y `~/.ssh/aws`).
- Ajuste de permisos de usuario `admphilippe` y grupos en la VM.

### Fixed

- Error de conexión SSH por puertos bloqueados en NSG.
- Confusión con el uso de claves privadas en `secrets`.

---

## [1.0.101.0] - 2025-09-09

### Added

- Estructura base del proyecto `IAHBCosteo` con carpetas:
  - `core/`
  - `frontend/`
  - `models/`
  - `services/`
  - `utils/`
- Archivos iniciales: `app.py`, `config.py`, `requirements.txt`.

### Changed

- Documentación inicial en `README.md`.
- Inclusión de `CONTRIBUTING.md` para guías de colaboración.

---

## [1.0.0] - 2025-09-01

### Added

- Creación del repositorio `IAHBCosteo` en GitHub.
- Configuración inicial de control de versiones.
