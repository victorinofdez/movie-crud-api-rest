# 🎬 Movie CRUD API

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una **aplicación backend orientada a API REST** para la gestión de películas de cine.  
La aplicación permitirá realizar operaciones CRUD sobre películas, implementar un **sistema de autenticación y autorización**, y gestionar diferentes roles de usuario.

El objetivo principal es simular la lógica de una aplicación real, aplicando buenas prácticas de desarrollo backend, persistencia de datos y control de acceso, dejando la base preparada para una futura integración con una interfaz gráfica.

---

## 🎯 Objetivo

- Gestionar un catálogo de películas de cine.
- Permitir la interacción de distintos tipos de usuarios con diferentes permisos.
- Persistir la información en una base de datos SQL.
- Ofrecer una arquitectura preparada para evolucionar y escalar.
- Ejecutar la aplicación en entornos aislados mediante Docker.

---

## 👥 Tipos de usuarios

La aplicación contará con un sistema de autenticación con **dos roles diferenciados**:

### 🔑 Administrador (Admin / Superusuario)

Usuario con control total sobre la aplicación.

**Permisos:**
- Crear, editar y eliminar películas.
- Gestionar el contenido completo del sistema.
- Aprobar o rechazar modificaciones propuestas por usuarios.
- Acceder a toda la información sin restricciones.

### 👤 Usuario estándar (User)

Usuario autenticado con permisos limitados.

**Permisos:**
- Consultar el catálogo de películas.
- Proponer la edición de películas existentes.
- Crear y gestionar su lista de películas favoritas.
- Acceder únicamente a su información personal.

---

## ⚙️ Funcionalidades principales

### 🎞️ Gestión de películas (CRUD)

- Crear nuevas películas.
- Listar todas las películas disponibles.
- Consultar el detalle de una película.
- Editar información de películas existentes.
- Eliminar películas (solo administrador).

### 🔐 Autenticación y autorización

- Registro de usuarios.
- Inicio de sesión con credenciales.
- Sistema de roles (admin / user).
- Control de acceso según permisos.

### ⭐ Gestión de favoritos

- Añadir películas a la lista de favoritos del usuario.
- Eliminar películas de favoritos.
- Consultar la lista de favoritos del usuario autenticado.

### ✏️ Propuestas de edición

- Los usuarios pueden proponer cambios sobre películas.
- Las propuestas quedan pendientes de revisión.
- El administrador decide si aceptar o rechazar los cambios.

### 💾 Persistencia de datos

- Uso de base de datos relacional (SQL).
- Almacenamiento persistente de:
  - Usuarios
  - Películas
  - Favoritos
  - Propuestas de edición

---

## 🛠️ Tecnologías previstas

- **Backend**: API REST
- **Base de datos**: SQL
- **Persistencia**: ORM / consultas SQL
- **Autenticación**: sistema de login con roles
- **Contenedores**: Docker y Docker Compose
- **Testing**: pruebas unitarias desde fases tempranas

---

## 📦 Despliegue con Docker

La aplicación estará preparada para ejecutarse mediante contenedores Docker, facilitando:

- Configuración del entorno.
- Aislamiento de dependencias.
- Despliegue consistente en cualquier sistema.

---

## 🚧 Estado del proyecto

📍 En fase de **definición y diseño**, siguiendo un desarrollo incremental:

1. Definición del dominio y entidades.
2. Diseño funcional.
3. Implementación progresiva.
4. Testing desde el inicio.
