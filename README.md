          Pitufin Movie – Proyecto de testing y gestión de películas

## Descripción del proyecto

**Pitufin Movie** es un proyecto backend hecho con **Python y FastAPI** cuyo objetivo principal es **practicar testing backend** a través de un sistema sencillo de **gestión de películas** y **usuarios con distintos roles**.

La idea del proyecto no es centrarse en construir una API muy compleja, sino en comprobar que el sistema funciona correctamente mediante pruebas. Se pone especial atención en validar reglas de negocio, datos de entrada, permisos de usuario y los distintos flujos que puede seguir alguien al usar la aplicación.

Desde el principio, el desarrollo se plantea con una mentalidad de testing, escribiendo pruebas antes o al mismo tiempo que la lógica.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Objetivos del proyecto

* Practicar testing backend de forma constante.
* Gestionar un catálogo de películas usando operaciones CRUD.
* Simular distintos tipos de usuarios y permisos.
* Validar reglas de negocio y errores comunes mediante tests.
* Aprender a estructurar un proyecto backend pensando en que sea fácil de testear.
* Usar persistencia simple para facilitar las pruebas (opcional).
* Ejecutar el proyecto en un entorno controlado con Docker (opcional).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Arquitectura del proyecto

El proyecto sigue una arquitectura tipo **MVC**, adaptada a FastAPI, pensada para que el código sea fácil de mantener y de probar:

* **Model**
  Aquí se definen las entidades del sistema (películas, usuarios, favoritos, propuestas) y las validaciones de datos.

* **View**
  Son los endpoints que reciben las peticiones y devuelven respuestas. Su comportamiento se comprueba directamente con tests.

* **Controller / Services**
  Contienen la lógica de negocio: creación y gestión de películas, control de permisos, favoritos y propuestas de edición.

Separar estas capas ayuda a que los tests sean más claros y a que los cambios no rompan todo el proyecto.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tipos de usuarios

### Administrador

Este rol está más enfocado a la gestión del sistema. Sirve para testear:

* Creación, edición y eliminación de películas.
* Control completo del catálogo.
* Revisión y decisión sobre propuestas de edición.
* Acceso a toda la información.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Usuario estándar

Este rol representa a un usuario normal de la aplicación y permite testear:

* Consulta del catálogo de películas.
* Gestión de una lista de favoritos.
* Propuesta de cambios sobre películas existentes.
* Acceso solo a su propia información.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Funcionalidades principales a testear

### Gestión de películas

* Crear películas con datos correctos.
* Rechazar películas con datos inválidos.
* Consultar películas existentes.
* Actualizar información de películas.
* Eliminar películas según los permisos del usuario.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Gestión de favoritos

* Añadir películas a favoritos.
* Eliminar películas de favoritos.
* Evitar que se repitan favoritos.
* Controlar errores cuando la película no existe o el usuario no tiene permisos.

---

### Propuestas de edición

* Crear propuestas de edición sobre películas existentes.
* Evitar propuestas sobre películas que no existen.
* Aprobar o rechazar propuestas según el rol del usuario.
* Validar que solo los usuarios autorizados puedan tomar decisiones.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Autenticación y permisos (opcional)

* Simular usuarios autenticados.
* Comprobar accesos permitidos y denegados.
* Verificar las diferencias entre administrador y usuario estándar.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Enfoque principal: testing

El proyecto sigue un enfoque **orientado a pruebas**, donde los tests definen cómo debería comportarse el sistema.

Se prueban tanto los casos en los que todo funciona correctamente como los errores más comunes, por ejemplo datos mal introducidos o accesos sin permisos.

Para ello se utilizan:

* **pytest**
* **TestClient** de FastAPI

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tests a implementar

### Tests del CRUD de películas

#### Crear película

* Crear una película con datos válidos.
* Error al crear una película con:

  * Campos vacíos.
  * Duración negativa.
  * Año anterior a 1888 o superior al año actual.
* Error por falta de permisos (opcional).

En los casos de error se debe devolver un código **400 Bad Request**.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Leer películas

* Listar todas las películas.
* Obtener una película por un ID válido.
* Error al consultar una película con:

  * ID inexistente.
  * ID con formato incorrecto.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Actualizar película

* Actualizar una película existente.
* Error al actualizar una película que no existe.
* Error al actualizar sin permisos (opcional).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Eliminar película

* Eliminar una película existente.
* Error al eliminar una película que no existe.
* Error al eliminar sin permisos (opcional).

```
| Operación | Endpoint            | Qué se testea                       |
|-----------|---------------------|-------------------------------------|
| CREATE    | POST /movies        | Película válida / inválida          |
| READ      | GET /movies         | Listado                             |
| READ      | GET /movies/{id}    | Existente / no existente            |
| UPDATE    | PUT /movies/{id}    | Actualización / error               |
| DELETE    | DELETE /movies/{id} | Eliminación / error                 |
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Tests de favoritos

* Añadir una película a favoritos.
* Eliminar una película de favoritos.
* Error al eliminar una película que no está en favoritos.
* Error al añadir una película inexistente.
* Error por falta de autenticación (opcional).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Tests de propuestas de edición

* Crear una propuesta válida.
* Error al crear una propuesta sobre una película inexistente.
* Aprobar una propuesta (admin).
* Rechazar una propuesta (admin).
* Error por falta de permisos (opcional).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Tests de validación

* Falta de campos obligatorios.
* Tipos de datos incorrectos.
* Valores fuera de rango.
* Formatos inválidos.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tecnologías utilizadas

* Python
* FastAPI
* pytest
* Arquitectura MVC
* MongoDB o archivos JSON (opcional)
* Docker (opcional)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Plan de desarrollo

**Semana 1**
Estructura del proyecto, diseño del dominio y primeros tests.

**Semana 2**
Tests y desarrollo del CRUD de películas.

**Semana 3**
Gestión de favoritos y roles de usuario.

**Semana 4**
Propuestas de edición, limpieza de código y documentación.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Estado del proyecto

Proyecto en desarrollo, enfocado principalmente en aprender y practicar testing backend, validando reglas de negocio y control de permisos de forma clara y ordenada.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Si quieres, puedo adaptarlo aún más a:

* Un trabajo de clase concreto
* Un README más corto
* O dejar el texto todavía más informal
