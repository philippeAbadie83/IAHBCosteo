---
# Changelog
Todas las modificaciones relevantes en este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).
---

# Changelog

## [1.0.128.0] - 2025-09-22

### Agregado

- Filtros dinámicos habilitados en la vista `/v_tblprov_data` para `proveedor` y `familia`.
- Se utiliza `vw_cat_filtros` como fuente limpia de datos para filtros.
- Activada relación jerárquica (`proveedor` → `familia`) para dropdowns dependientes.

### Modificado

- Llamado a `crear_tabla()` actualizado con `filtros` y `relacion_filtros` definidos en el módulo de vista.
- Separación lógica entre los datos mostrados (`vw_prov_data_latest`) y los filtros (`vw_cat_filtros`).

### Conservado

- Componente `tbl_base` sigue 100% genérico y reutilizable en otras vistas.

## [1.0.127.2] - 2025-09-22

### Changed

- Deshabilitados filtros (`filtros`, `relacion_filtros`) en `v_tblprov_data` para validación inicial.
- La tabla ahora carga **todos los registros completos** sin aplicar filtros automáticos.
- Eliminada duplicación de controles de selección (filtros arriba y dentro de la tabla).
- Flujo base validado: render de tabla + acciones sin interferencias.

### Fixed

- Problema donde la opción **"Todos"** no mostraba registros completos.
- Evitada confusión por doble set de filtros en pantalla.

### Notes

- Esta versión sirve como **prueba base**: siempre muestra todos los datos.
- Próximo paso: reactivar filtros solo dentro de la tabla (`crear_tabla`), sin duplicación desde layout.

## [1.0.127.1] - 2025-09-22

### Added

- Implementación de filtros dinámicos jerárquicos en `v_tblprov_data`:
  - El filtro **Proveedor** ahora actualiza automáticamente las opciones disponibles en el filtro **Familia**.
  - Se mantiene la opción **Todos** para mostrar registros completos.

### Changed

- Refactor de la lógica de filtros para mejorar la relación padre-hijo (`relacion_filtros`).
- Integración de `filter_elements` y función `update_familias` para regenerar las familias en tiempo real.

### Fixed

- Corrección del comportamiento inicial: cuando se selecciona **Todos** en ambos filtros, se muestran todos los registros sin aplicar restricciones.

# v1.0.127.0 (2025-09-22)

## 🚀 Mejoras

- Refactorizado `v_tblprov_data.py` para evitar variables indefinidas en Pylance.
- Movido `crear_tabla(...)` dentro de la función `content()` para que todas las variables (`df`, `columnas`, `filtros`, etc.) estén en el mismo ámbito.
- Integración clara con `layout.render(content)` manteniendo la modularidad.
- Se mantiene el soporte para:
  - Filtros padre–hijo (`familia → proveedor`).
  - Exportación a Excel.
  - Formatos especiales para columnas de porcentaje.
  - Acciones estándar: **info** y **edit** con UI dialogs.

## 🐞 Fixes

- Corregido bug de **variables no definidas** (`columnas`, `df`, `filtros`, `acciones`, etc.).
- Eliminada duplicación innecesaria de funciones anidadas que causaba confusión y exceso de líneas.

## [1.0.126.11] - 2025-09-21

### Cambios

- Habilitada la integración de acciones en `frontend/pages/v_tblprov_data.py`.
  - Activadas las acciones estándar: **Info (ℹ️)** y **Editar (✏️)**.
  - `Info`: despliega un diálogo con todos los campos del registro.
  - `Editar`: muestra un `notify` con el proveedor seleccionado (placeholder para lógica futura).
- Comentarios previos en la tabla siguen activos (truncado con tooltip).
- Ajustes para que `crear_tabla` reciba correctamente la lista de acciones definidas en la página.

## [1.0.126.10] - 2025-09-21

### Fixed

- Corregido `tbl_base.py` para compatibilidad con `add_slot` de NiceGUI.
- Se aplicó `cast(Any, ...)` en los renderizados personalizados (`comentarios` y `acciones`).
- Eliminados errores de tipado y `TypeError 500` al renderizar celdas con funciones.

## [1.0.126.8] - 2025-09-21

### Fixed

- Se corrigió el error `TypeError: Type is not JSON serializable: function` en la vista `v_tblprov_data`.
- Ahora las acciones (`info`, `edit`) pasan funciones explícitas (`func`) para su ejecución en `tbl_base.py`.

### Changed

- Actualización de `v_tblprov_data.py` para definir funciones `mostrar_info` y `editar_registro`, conectadas directamente a las acciones.
- Mejor integración con el `render_acciones` en `tbl_base.py`.

## [1.0.126.7] - 2025-09-21

### Added

- Acción Info (ℹ️): dialog con detalle completo del registro en `tbl_base.py`.
- Slot para columna "comentarios" con truncado (ellipsis) y tooltip.

### Changed

- Formateo de columnas de porcentaje: se muestran como enteros con símbolo %, p.ej. 0.11 → 11%.

### Fixed

- Alineación de render de acciones y slots después de inicializar la tabla.

## [1.0.126.5] - 2025-09-21

### Added

- Incorporación de columna de acciones (`acciones`) en la tabla genérica (`tbl_base.py`).
- Botones estándar configurados:
  - Info (ℹ️): despliega detalles (por ahora `ui.notify`).
  - Update (✏️): acción de edición (por ahora `ui.notify`).
- Declaración de acciones extra como comentarios de referencia en `tbl_base.py`.

### Fixed

- Error de serialización JSON en acciones de la tabla (causado por incluir funciones en `acciones`).
- Reestructuración para que los botones se construyan en `render_acciones` después de crear la tabla.

### Changed

- Ajustes en `v_tblprov_data.py` para pasar `acciones` como lista de icon + name en lugar de funciones.
- Tabla genérica soporta **paginación** con opciones `10, 25, 50, 75, 100` y valor por defecto en 25.

## [1.0.126.4] - 2025-09-21

### Added

- Integración de acciones estándar en la tabla genérica (`tbl_base.py`): Info (ℹ️) y Update (✏️).
- Nueva estructura en `v_tblprov_data.py` que pasa explícitamente las acciones a la tabla.
- Paginación configurable: 10, 25, 50, 75, 100 (default 25).

### Fixed

- Corrección de advertencia "table is unbound" en `tbl_base.py` reordenando la definición de `table` y los slots de acciones.

## [1.0.126.3] - 2025-09-21

### Fixed

- Corregido error `500 - TypeError: Type is not JSON serializable: Timestamp` en la página `/importar_proveedores`.
- En `get_proveedores_por_fecha`, las columnas `prov_createdate` y `prov_updatedate` ahora se convierten explícitamente a `str` para ser serializables en JSON.
- Esto asegura que la tabla de proveedores importados/actualizados se renderice correctamente sin romper la UI.

## [1.0.126.2] - 2025-09-21

### Changed

- Limpieza en `db_services.py`:
  - Eliminados imports duplicados (`engine` desde `services.database`).
  - Eliminadas definiciones duplicadas de `insertar_proveedor`.
  - Consolidada en una única versión con `session` y soporte de UPSERT (`ON DUPLICATE KEY UPDATE`).
- Código reducido de ~146 a ~126 líneas sin pérdida de funcionalidad.
- Mejora en mantenibilidad y legibilidad del módulo de servicios de proveedores.

## [1.0.126.1] - 2025-09-21

### Fixed

- Se corrigió `insertar_proveedor` en `db_services.py` para usar UPSERT (`ON DUPLICATE KEY UPDATE`) con `session`.
- Ahora si `(prov_name, prov_famil)` ya existe se actualiza en lugar de fallar con error de duplicado.
- El trigger `trg_tbl_prov_data_before_update` sigue manejando histórico, versionado y vigencias automáticamente.
- Eliminadas definiciones duplicadas de `insertar_proveedor` y limpieza de imports innecesarios.

---

## [1.0.126.0] - 2025-09-21

### Added

- Integración de vista en `p_imp_provData.py` para mostrar registros importados en el mismo flujo.
- Se agregó tabla debajo de la importación usando `crear_tabla` de `tbl_base`.
- Visualización automática de registros importados en la fecha actual (`prov_createdate = hoy`).

### Changed

- Se ajustó flujo de importación: después de insertar los proveedores en BD, la interfaz refresca y muestra lo subido en el día.
- Se eliminó el uso de filtros y acciones en esta tabla; solo visualización simple de los datos.

### Fixed

- Manejo de columnas extra en Excel (ejemplo: `Total gastos`) para que no interrumpa la importación.

---

## [1.0.124.6] - 2025-09-19

### Fixes

- Se corrigió el solapamiento del **sidebar** sobre el header.
- Se eliminó el recuadro azul con icono de casa en el sidebar (ya no aparece).
- Se restauró el botón **Perfil** en el header.
- Se aplicó `pt-16` en el sidebar y en el contenido principal para asegurar que queden **debajo del header fijo**.
- Ajuste general de layout para mantener consistencia entre header, sidebar y contenido.

---

## [v1.0.124.5] - Build 124 - 2025-09-19

### Fixes

- Ajuste de **layout**: el header ahora se mantiene fijo de lado a lado.
- El **sidebar** inicia correctamente debajo del header.
- Corrección de superposición: las tablas y placeholders ya no quedan cubiertos por el header.
- Mantiene consistencia visual en toda la aplicación (header, sidebar, contenido y footer).

---

## [v1.0.124.4] - Build 124 - 2025-09-19

### Fixed

- El logo de Hidrobart en el sidebar ya no invade el header (se agregó `pt-14` al drawer).
- Header fijado con `fixed top-0 z-50` para mantenerlo siempre visible.
- Se restauró la visualización de versión y perfil en el header (lado derecho).
- Se corrigió alineación general del layout y consistencia visual.
- Los títulos de secciones en el sidebar ahora se muestran en Proper Case (`.capitalize`).

---

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

---

## [1.0.124.1] - 2025-09-18

### Fix & Mejoras

- Se corrigió error en la importación desde Excel/CSV causado por valores `NaN`.
- Se implementó `fillna` para asegurar inserción segura de datos numéricos y comentarios.
- Se estableció valor fijo de auditoría `prov_createby = "Philippe Abadie"`.
- Se añadieron comentarios explicativos al código (`p_imp_provData.py`) para facilitar mantenimiento.
- Mejora de UX en el flujo de importación con notificaciones más claras.

---

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

---

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
