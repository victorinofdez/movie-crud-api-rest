# 🎬 Movie CRUD API

## 📌 Descripción del proyecto

**Movie CRUD API** es una aplicación backend desarrollada con **Python y FastAPI** que permite la gestión de un catálogo de películas de cine mediante una **API REST**.  
El sistema implementa operaciones CRUD, un sistema de autenticación y autorización basado en roles, y funcionalidades específicas para usuarios finales, como la gestión de favoritos y la propuesta de ediciones.

El proyecto se desarrolla siguiendo una **arquitectura MVC**, con persistencia en una base de datos relacional y un enfoque de **testing desde el inicio**, simulando el desarrollo profesional de una aplicación real.

---

## 🎯 Objetivos del proyecto

- Desarrollar una API REST funcional y escalable.
- Gestionar un catálogo de películas mediante operaciones CRUD.
- Implementar un sistema de autenticación con distintos roles de usuario.
- Aplicar reglas de negocio y control de permisos.
- Persistir la información en una base de datos SQL.
- Utilizar Docker para la ejecución del entorno.
- Aplicar testing desde las primeras fases del desarrollo.

---

## 🧱 Arquitectura

El proyecto sigue el patrón **Modelo–Vista–Controlador (MVC)**, adaptado al entorno de FastAPI:

- **Model**  
  Representa las entidades del dominio y la persistencia de datos mediante modelos SQL y esquemas de validación.

- **View**  
  Corresponde a los endpoints de la API REST que gestionan las peticiones HTTP y devuelven respuestas en formato JSON.

- **Controller**  
  Implementa la lógica de negocio y las reglas del sistema a través de servicios desacoplados de la capa de presentación.

Esta separación facilita la mantenibilidad, la escalabilidad y el testing del sistema.

---

## 👥 Tipos de usuarios

La aplicación cuenta con un sistema de autenticación con dos roles diferenciados:

### 🔑 Administrador (Admin / Superusuario)

Usuario con control total sobre el sistema.

**Permisos:**
- Crear, editar y eliminar películas.
- Gestionar todo el contenido del catálogo.
- Aprobar o rechazar propuestas de edición realizadas por usuarios.
- Acceder a toda la información del sistema.

### 👤 Usuario estándar (User)

Usuario autenticado con permisos limitados.

**Permisos:**
- Consultar el catálogo de películas.
- Proponer ediciones sobre películas existentes.
- Crear y gestionar una lista de películas favoritas.
- Acceder únicamente a su información personal.

---

## ⚙️ Funcionalidades principales

### 🎞️ Gestión de películas (CRUD)

- Crear nuevas películas.
- Listar y consultar películas.
- Editar información de películas existentes.
- Eliminar películas (solo administradores).

### 🔐 Autenticación y autorización

- Registro de usuarios.
- Inicio de sesión mediante credenciales.
- Autenticación basada en tokens.
- Control de acceso según el rol del usuario.

### ⭐ Gestión de favoritos

- Añadir películas a la lista de favoritos del usuario.
- Eliminar películas de favoritos.
- Consultar la lista de favoritos del usuario autenticado.

### ✏️ Propuestas de edición

- Los usuarios pueden proponer cambios en películas existentes.
- Las propuestas quedan pendientes de revisión.
- El administrador puede aceptar o rechazar dichas propuestas.

### 💾 Persistencia de datos

- Almacenamiento en base de datos relacional (SQL).
- Persistencia de:
  - Usuarios
  - Películas
  - Favoritos
  - Propuestas de edición

---

## 🧪 Testing desde el inicio

El proyecto sigue un enfoque de desarrollo orientado a pruebas utilizando **pytest** y las herramientas de testing proporcionadas por FastAPI.

Antes de implementar la lógica completa de cada funcionalidad, se escriben tests que definen el comportamiento esperado del sistema, incluyendo tanto casos de éxito como escenarios de error.  
Los tests actúan como guía durante el desarrollo y como red de seguridad ante cambios futuros.

Los tests cubren:
- Reglas de negocio del dominio.
- Control de permisos según el rol del usuario.
- Validación de datos de entrada.
- Respuestas y códigos HTTP de la API.

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python  
- **Framework**: FastAPI  
- **Base de datos**: SQL  
- **Arquitectura**: MVC  
- **Testing**: pytest  
- **Contenedores**: Docker y Docker Compose  

---

## 📦 Despliegue con Docker

La aplicación está preparada para ejecutarse en contenedores Docker, lo que permite:

- Aislar el entorno de desarrollo.
- Simplificar la configuración del proyecto.
- Garantizar consistencia entre distintos entornos de ejecución.

---

## 📆 Plan de desarrollo

El proyecto se desarrolla de forma incremental a lo largo de **cuatro semanas**:

1. **Semana 1**  
   Diseño del dominio, definición de entidades, estructura MVC y configuración base del proyecto.

2. **Semana 2**  
   Implementación del CRUD de películas y control de permisos por rol.

3. **Semana 3**  
   Desarrollo del sistema de autenticación y gestión de favoritos.

4. **Semana 4**  
   Implementación de propuestas de edición, refactorización final y documentación.

---

## 🚧 Estado del proyecto

📍 En desarrollo activo, siguiendo un enfoque incremental y orientado a buenas prácticas de desarrollo backend.
