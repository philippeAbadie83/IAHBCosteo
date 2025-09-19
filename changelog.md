---
# Changelog
Todas las modificaciones relevantes en este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).
---

# CHANGELOG

## [v1.0.124.5] - Build 124 - 2025-09-19

### Fixes

- Ajuste de **layout**: el header ahora se mantiene fijo de lado a lado.
- El **sidebar** inicia correctamente debajo del header.
- Corrección de superposición: las tablas y placeholders ya no quedan cubiertos por el header.
- Mantiene consistencia visual en toda la aplicación (header, sidebar, contenido y footer).

## [v1.0.124.4] - Build 124 - 2025-09-19

### Fixed

- El logo de Hidrobart en el sidebar ya no invade el header (se agregó `pt-14` al drawer).
- Header fijado con `fixed top-0 z-50` para mantenerlo siempre visible.
- Se restauró la visualización de versión y perfil en el header (lado derecho).
- Se corrigió alineación general del layout y consistencia visual.
- Los títulos de secciones en el sidebar ahora se muestran en Proper Case (`.capitalize`).

## [1.0.124.3] - Build 124 - 2025-09-19

### Added

- Placeholders iniciales para todas las rutas nuevas:
  - `/v_tblprov_all` (Proveedores Todos)
  - `/productos/listado`, `/productos/importar`, `/productos/precios-proveedor`, `/productos/carga-precios`, `/productos/costo-destino`, `/productos/lista-precios`
  - `/kit/listado`, `/kit/armado`, `/kit/costeo`
  - `/sim/clientes-especiales`, `/sim/campana`, `/sim/mejores-productos`, `/sim/mejores-margenes`
  - `/reportes`, `/graficos`, `/configuracion`, `/ayuda`, `/docs`

### Changed

- `layout.py`: Sidebar actualizado para que cada botón apunte a rutas con placeholders definidos.
- Integración de `frontend/pages/placeholders.py` en `app.py` para evitar errores 404 en navegación.

### Fixed

- Alineación de rutas en botones con páginas registradas (evita fallos de navegación).

## [1.0.124.1] - 2025-09-18

### Fix & Mejoras

- Se corrigió error en la importación desde Excel/CSV causado por valores `NaN`.
- Se implementó `fillna` para asegurar inserción segura de datos numéricos y comentarios.
- Se estableció valor fijo de auditoría `prov_createby = "Philippe Abadie"`.
- Se añadieron comentarios explicativos al código (`p_imp_provData.py`) para facilitar mantenimiento.
- Mejora de UX en el flujo de importación con notificaciones más claras.

## [1.0.124.0] - 2025-09-17

### Added

- Integración de layout unificado con sidebar, header reducido y footer.
- Nueva sección en menú lateral: **Proveedores**
  - Página `/v_tblprov_data`: muestra tabla de Proveedores Activos integrada al layout.
  - Página `/importar_proveedores`: permite carga de archivo Excel/CSV y alta masiva en BD.
- Organización del menú lateral:
  - Dashboard
  - Proveedores (Tabla + Importación)
  - Costos de Productos
  - Cálculos de Costo
  - Lista de Precios
  - Lista de Precios Simulados
  - Análisis (Reportes, Gráficos)
  - Sistema (Configuración, Ayuda, Documentación)

### Changed

- `core/layout.py`: ahora controla header + sidebar + footer + render de contenido.
- `app.py`: eliminado `home_content` embebido, las páginas usan `layout.render(content)`.

### Fixed

- Consistencia en navegación: ahora todas las rutas cargan dentro del layout y no fuera de él.

## [1.0.123.0] - 2025-09-17

### Added

- Nueva utilidad `sanitize_dataframe` en `utils/helpers.py` para convertir:
  - `Timestamp` → string `YYYY-MM-DD HH:MM:SS`.
  - `Decimal` → float.
- Integración de `sanitize_dataframe` en `v_tblprov_data.py` antes de renderizar tablas.
- Soporte para serialización segura en NiceGUI evitando errores `TypeError: not JSON serializable`.

### Changed

- `v_tblprov_data.py`: ahora importa `sanitize_dataframe` y lo aplica después de `get_proveedores_activos`.
- Estructura de imports reorganizada en `frontend/pages/v_tblprov_data.py`.

### Fixed

- Error `500 Server error` al mostrar columnas con `Timestamp` y `Decimal`.

---

## [1.0.104.4] - 2025-09-11

### Fixed

- Corrigida la ruta de `test_table.py` para usar `/test-table` (guion medio en la URL).
- Se agregó log más claro al cargar `test_table` con versión y build.

---

## [1.0.104.1] - 2025-09-10

### Added

- Archivo `core/__version__.py` para centralizar la información de la aplicación:
  - `__app__`: nombre de la app.
  - `__version__`: versión semántica.
  - `__build__`: número de build incremental.

### Changed

- `core/layout.py` ahora utiliza `__version__` y `__build__` en el footer:
  - Muestra dinámicamente: `© Hidrobart 2025 | AIHB-Costeo v.1.0.104.1 (Build 104)`.
- Eliminada la versión fija (`1.0.101.0`) en el footer.

### Notes

- A partir de ahora, solo es necesario actualizar `core/__version__.py` para reflejar cambios de versión en toda la aplicación.

---

## [1.0.103.4] - 2025-09-10

### Added

- Página de prueba `test_table.py` registrada correctamente en `app.py`.
  - Ruta accesible en `http://<IP_PUBLICA>:8080/test-table`.
  - Incluye tabla demo con 10 productos mock, filtros, exportación y acciones (`edit`, `delete`).

### Changed

- `app.py` actualizado para importar explícitamente `frontend/pages/test_table`.
- Ahora NiceGUI reconoce y carga la página `/test-table`.

### Notes

- `index_page` sigue siendo la raíz `/` mostrando el mensaje de bienvenida.
- Próximas páginas deben importarse en `app.py` o configurarse para carga automática.

---

## [1.0.103.0] - 2025-09-10

### Added

- Nuevo componente `tbl_base.py` en `frontend/components/`:

  - Soporte universal de tablas con filtros (proveedor, familia, código).
  - Exportación a Excel de datos filtrados.
  - Acciones por fila con íconos (`edit`, `delete`).
  - Congelación de columnas clave (`proveedor`, `familia`, `code_sys`).

- Nueva página de prueba `test_tabla.py` en `frontend/pages/`:
  - Demo con 10 productos mock en DataFrame de pandas.
  - Validación de filtros, exportación y acciones.
  - Integración de versión y build (`__version__`, `__build__`).

### Changed

- Se eliminó duplicidad en definición de slots (`render_acciones`).
- Corrección de warnings de Pylance con `# type: ignore[arg-type]`.

### Notes

- `app.py` sigue siendo el entrypoint. Acceso de prueba vía:

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
