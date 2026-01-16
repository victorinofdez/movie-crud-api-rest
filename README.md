# 🎬 Pitufin Movie CRUD API

## 📌 Descripción del proyecto

**Pitufin Movie CRUD API** es una aplicación backend desarrollada con **Python y FastAPI** que permite la gestión de un catálogo de películas de cine mediante una **API REST**.  
El sistema implementa operaciones CRUD, un sistema de autenticación y autorización basado en roles (opcional), y funcionalidades específicas para usuarios finales, como la gestión de favoritos y la propuesta de ediciones.

El proyecto se desarrolla siguiendo una **arquitectura MVC**, con persistencia en una base de datos no relacional y un enfoque de **testing desde el inicio**.

---

## 🎯 Objetivos del proyecto

- Desarrollar una API REST funcional y escalable.
- Gestionar un catálogo de películas mediante operaciones CRUD.
- Implementar un sistema de autenticación con distintos roles de usuario. (opcional)
- Aplicar reglas de negocio y control de permisos.
- Persistir la información en una base de datos. (opcional)
- Utilizar Docker para la ejecución del entorno. (opcional)
- Aplicar testing desde las primeras fases del desarrollo.

---

## 🧱 Arquitectura

El proyecto sigue el patrón **Modelo–Vista–Controlador (MVC)**, adaptado al entorno de FastAPI:

- **Model**  
  Representa las entidades del dominio y la persistencia de datos mediante modelos y esquemas de validación.

- **View**  
  Corresponde a los endpoints de la API REST que gestionan las peticiones HTTP y devuelven respuestas en formato JSON.

- **Controller**  
  Implementa la lógica de negocio y las reglas del sistema a través de servicios desacoplados de la capa de presentación.

Esta separación facilita la mantenibilidad, la escalabilidad y el testing del sistema.

---

## 👥 Tipos de usuarios (opcional)

### 🔑 Administrador (Admin / Superusuario)

**Permisos:**
- Crear, editar y eliminar películas.
- Gestionar todo el catálogo.
- Aprobar o rechazar propuestas de edición.
- Acceder a toda la información del sistema.

### 👤 Usuario estándar (User)

**Permisos:**
- Consultar el catálogo de películas.
- Proponer ediciones.
- Gestionar una lista de películas favoritas.
- Acceder únicamente a su información personal.

---

## ⚙️ Funcionalidades principales

### 🎞️ Gestión de películas (CRUD)

- Crear nuevas películas.
- Listar y consultar películas.
- Editar información de películas existentes.
- Eliminar películas (solo administradores).

### ⭐ Gestión de favoritos

- Añadir películas a favoritos.
- Eliminar películas de favoritos.
- Consultar la lista de favoritos del usuario autenticado.

### ✏️ Propuestas de edición

- Proponer cambios en películas existentes.
- Revisión de propuestas por el administrador.
- Aprobación o rechazo de propuestas.

### 🔐 Autenticación y autorización (Opcional)

- Registro de usuarios.
- Inicio de sesión.
- Autenticación basada en tokens.
- Control de acceso por roles.

### 💾 Persistencia de datos (Opcional)

- Base de datos (MongoDB o archivos JSON).
- Persistencia de usuarios, películas, favoritos y propuestas.

---

## 🧪 Testing desde el inicio

El proyecto sigue un enfoque de **desarrollo orientado a pruebas (TDD)** utilizando **pytest** y `TestClient` de FastAPI.

Antes de implementar la lógica de cada funcionalidad, se definen tests que describen el comportamiento esperado del sistema, cubriendo tanto escenarios exitosos como errores.

Los tests garantizan:
- Correcta aplicación de reglas de negocio.
- Control de permisos según el rol del usuario. (opcional)
- Validación de datos de entrada.
- Respuestas HTTP correctas.

---

## 🧪 Tests a implementar

### 🎞️ Tests del CRUD de películas

#### CREATE
- Crear película con datos válidos.
- Error al crear película con datos inválidos.
- Error al crear película sin permisos de administrador. (opcional)

#### READ
- Listar todas las películas.
- Obtener película por ID existente.
- Error al obtener película inexistente.

#### UPDATE
- Actualizar película con permisos de administrador.
- Error al actualizar película inexistente.
- Error al actualizar sin permisos.

#### DELETE
- Eliminar película con permisos de administrador. (opcional)
- Error al eliminar película inexistente.
- - Error al eliminar película existente.
- Error al eliminar sin permisos. (opcional)


Operaciónes	  Endpoint	            Qué testear

CREATE	      POST /movies	        Crear película válida / inválida
READ	        GET /movies	          Listar películas
READ	        GET /movies/{id}	    Película existente / no existente
UPDATE	      PUT /movies/{id}	    Actualizar existente / error
DELETE	      DELETE /movies/{id}	  Eliminar existente / no existente

---

### ⭐ Tests de favoritos

- Añadir película a favoritos.
- Eliminar película de favoritos.
- Listar favoritos del usuario autenticado. (opcional)
- Error al añadir película inexistente.
- Error al gestionar favoritos sin autenticación. (opcional)

---

### ✏️ Tests de propuestas de edición

- Crear propuesta de edición válida.
- Listar propuestas pendientes (admin). (opcional)
- Aprobar propuesta de edición.
- Rechazar propuesta de edición.
- Error al aprobar/rechazar sin permisos. (opcional)

---

### 🔐 Tests de autenticación y autorización (opcional)

- Registro de usuario válido. 
- Inicio de sesión correcto.
- Error en login con credenciales inválidas.
- Acceso denegado a endpoints protegidos.
- Validación de roles (admin vs user).

---

### 📐 Tests de validación

- Campos obligatorios faltantes.
- Tipos de datos incorrectos.
- Valores fuera de rango.
- Formato incorrecto de datos de entrada.

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python  
- **Framework**: FastAPI  
- **Base de datos**: MongoDB o archivos JSON  
- **Arquitectura**: MVC  
- **Testing**: pytest  
- **Contenedores**: Docker y Docker Compose  

---

## 📦 Despliegue con Docker

La aplicación está preparada para ejecutarse en contenedores Docker, permitiendo:

- Aislar el entorno de desarrollo.
- Simplificar la configuración.
- Garantizar consistencia entre entornos.

---

## 📆 Plan de desarrollo

1. **Semana 1**  
   Diseño del dominio, entidades, estructura MVC y configuración base.

2. **Semana 2**  
   Implementación del CRUD de películas y permisos por rol.

3. **Semana 3**  
   Autenticación y gestión de favoritos.

4. **Semana 4**  
   Propuestas de edición, refactorización y documentación.

---

## 🚧 Estado del proyecto

📍 En desarrollo activo, siguiendo buenas prácticas de backend y testing.
