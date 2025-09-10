---

## 📌 Estándar propuesto (basado en **Conventional Commits** + tu esquema de versión)

### 🔖 Formato de versión

```
Mayor.Menor.Build.Hotfix
```

* **Mayor (1)** → cambios disruptivos.
* **Menor (0)** → funcionalidades nuevas que no rompen compatibilidad.
* **Build (101)** → cada release significativo que haces.
* **Hotfix (0,1,2,3...)** → correcciones rápidas sobre ese build.

Ejemplo:

* `1.0.101.0` → primera release build 101.
* `1.0.101.1` → primer hotfix del build 101.
* `1.0.102.0` → siguiente build estable.

---

### 📝 Formato de commit

```
<tipo>(build|hotfix X): descripción clara
```

#### Tipos recomendados:

- `init` → inicialización del proyecto.
- `feat` → nueva funcionalidad.
- `fix` → corrección de bug.
- `docs` → cambios en documentación.
- `refactor` → mejora de código sin cambiar funcionalidad.
- `style` → formato, estilo, comentarios.
- `chore` → tareas menores (dependencias, limpieza).

#### Ejemplos:

```bash
git commit -m "init(build 101): versión 1.0.101.0 con estructura base"
git commit -m "feat(build 102): integración con Redis para cache"
git commit -m "fix(hotfix 1): corregido error en conexión DB"
git commit -m "docs: actualizado README con estándar de commits"
```

---

### 🏷️ Formato de tags

Siempre en este formato:

```
v<versión>
```

Ejemplo:

```bash
git tag -a v1.0.101.0 -m "Versión 1.0.101.0 - Build 101 inicial"
git tag -a v1.0.101.1 -m "Hotfix 1.0.101.1 - Build 101"
git tag -a v1.0.102.0 -m "Versión 1.0.102.0 - Build 102"
```

---

## 📄 Sección en tu `README.md`

Agrega esto al final de tu `README.md`:

```markdown
---

## 📌 Convenciones de Commits y Versionado

Este proyecto sigue un esquema basado en **Conventional Commits** y control de versión extendido:

### 🔖 Formato de versión
```

Mayor.Menor.Build.Hotfix

```
- **Mayor** → cambios disruptivos.
- **Menor** → funcionalidades nuevas sin romper compatibilidad.
- **Build** → número incremental de release.
- **Hotfix** → correcciones rápidas sobre un build específico.

Ejemplo: `1.0.101.0` (Build 101 inicial), `1.0.101.1` (Hotfix), `1.0.102.0` (nuevo build).

### 📝 Convenciones de commit
```

<tipo>(build|hotfix X): descripción clara

```

Tipos aceptados:
- `init` → inicialización del proyecto
- `feat` → nueva funcionalidad
- `fix` → corrección de bug
- `docs` → cambios en documentación
- `refactor` → mejora interna de código
- `style` → estilo, formato, comentarios
- `chore` → tareas menores (dependencias, limpieza)

Ejemplos:
- `init(build 101): versión 1.0.101.0 con estructura base`
- `feat(build 102): integración con Redis para cache`
- `fix(hotfix 1): corregido error en conexión DB`

### 🏷️ Tags
Cada release importante debe tener un **tag**:
- `v1.0.101.0`
- `v1.0.101.1`
- `v1.0.102.0`
```

---
