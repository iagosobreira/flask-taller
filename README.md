# Taller - Sistema de Gestión de Taller

Una aplicación web moderna desarrollada en Flask para la gestión completa de citas y operaciones de un taller mecánico con sistema de autenticación y base de datos PostgreSQL.

## 🚀 Características

- **Interfaz Moderna**: Diseño responsive con gradientes y animaciones suaves
- **Sistema de Autenticación Completo**: Login, registro y gestión de sesiones
- **Gestión de Citas**: Sistema completo para agendar y gestionar citas de taller
- **Panel de Administrador**: Vista administrativa para gestionar todas las reservas
- **Base de Datos PostgreSQL**: Integración con SQLAlchemy para persistencia de datos
- **Arquitectura Modular**: Organizado con Blueprints de Flask
- **Diseño Profesional**: CSS moderno con efectos hover y transiciones

## 📁 Estructura del Proyecto

```
Flask_Taller/
├── app/
│   ├── app.py                 # Aplicación principal
│   ├── config.py              # Configuración de la aplicación
│   ├── extensions.py          # Extensiones de Flask (SQLAlchemy)
│   ├── .env                   # Variables de entorno
│   ├── main/
│   │   └── routes.py          # Rutas principales (inicio)
│   ├── login/
│   │   └── routes.py          # Rutas de autenticación
│   ├── area/
│   │   ├── routes.py          # Rutas de área de usuario
│   │   └── services.py        # Servicios de gestión de reservas
│   ├── admin/
│   │   └── routes.py          # Rutas del panel administrativo
│   ├── templates/
│   │   ├── layout.html        # Plantilla base
│   │   ├── admin_area.html    # Panel de administrador
│   │   ├── area.html          # Área de usuario
│   │   ├── registro.html      # Formulario de registro
│   │   ├── index.html         # Página de inicio
│   │   └── login.html         # Formulario de login
│   └── static/
│       └── css/
│           ├── index.css      # Estilos principales
│           ├── area.css       # Estilos area usuario
│           ├── layout.css     # Estilos base
│           └── login.css      # Estilos del login
├── requirements.txt           # Dependencias del proyecto
├── Notas.txt                  # Script de base de datos
└── README.md                  # Documentación
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python 3.13+)
- **Base de Datos**: PostgreSQL con SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Arquitectura**: Blueprints de Flask (modular)
- **Autenticación**: Werkzeug Security (hashing de contraseñas)
- **Estilos**: CSS Grid, Flexbox, gradientes modernos
- **Sesiones**: Flask-Session management

## 🎨 Diseño y UI

- **Paleta de Colores**: Gradiente púrpura-azul (#667eea → #764ba2)
- **Tipografía**: Arial, sans-serif
- **Responsive**: Adaptado para móviles y desktop
- **Componentes**: Tarjetas con efectos hover, botones animados

## 📋 Funcionalidades

### Autenticación
- Login con email y contraseña
- Registro de nuevos usuarios
- Hashing de contraseñas con Werkzeug
- Gestión de sesiones

### Usuario
- Dashboard personalizado
- Agendar nuevas citas (fecha, hora, motivo, matrícula)
- Ver lista de reservas propias
- Estados: Aceptada, Denegada, Pendiente

### Administrador
- Vista completa de todas las reservas
- Gestión de estados de citas
- Información de usuarios y vehículos

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd Flask_Taller
```

2. Crear y activar entorno virtual:
```bash
# Windows
python -m venv flask-taller
.\flask-taller\Scripts\activate

# Linux/Mac
python3 -m venv flask-taller
source flask-taller/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar base de datos PostgreSQL:
   - Crear base de datos en PostgreSQL
   - Configurar variables de entorno en `app/.env`:
   ```
   DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db
   SECRET_KEY=tu_secret_key_aqui
   ```

5. Ejecutar la aplicación:
```bash
cd app
python app.py
```

6. Abrir en navegador: `http://localhost:5000`

## 🗄️ Esquema de Base de Datos

### Tabla: usuarios
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Primary Key |
| nombre | VARCHAR(100) | Nombre del usuario |
| correo | VARCHAR(150) | Email único |
| contrasena | VARCHAR(255) | Contraseña hasheada |
| rol | VARCHAR(50) | 'admin' o 'usuario' |

### Tabla: reservas
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | SERIAL | Primary Key |
| fecha_reserva | TIMESTAMP | Fecha y hora de la cita |
| estado | estado_reserva | Enum: Aceptada, Denegada, Pendiente |
| id_usuario | INTEGER | Foreign Key → usuarios.id |
| motivo_cita | TEXT | Descripción del motivo |
| matricula | VARCHAR | Matrícula del vehículo |

### Enum: estado_reserva
- `Aceptada`
- `Denegada`
- `Pendiente`

## 💾 Creación de Tablas de Base de Datos

Ejecutar el siguiente script SQL en PostgreSQL para crear las tablas necesarias:

```sql
-- Crear tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('admin', 'usuario'))
);

-- Crear tipo enum para estados de reserva
CREATE TYPE estado_reserva AS ENUM (
    'Aceptada',
    'Denegada',
    'Pendiente'
);

-- Crear tabla de reservas
CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    fecha_reserva TIMESTAMP NOT NULL,
    estado estado_reserva NOT NULL DEFAULT 'Pendiente',
    id_usuario INTEGER NOT NULL,
    CONSTRAINT fk_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id)
        ON DELETE CASCADE,
    UNIQUE (fecha_reserva, id_usuario)
);

-- Agregar columnas adicionales a reservas
ALTER TABLE reservas
ADD COLUMN motivo_cita TEXT;

ALTER TABLE reservas
ADD COLUMN matricula VARCHAR(50);
```

### Notas:
- El campo `estado` por defecto es `Pendiente`
- La restricción `UNIQUE` evita que un usuario tenga dos reservas en el mismo horario
- La foreign key con `ON DELETE CASCADE` elimina las reservas si se elimina el usuario

## 🔐 Variables de Entorno

Crear archivo `app/.env` con:
```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/taller_db
SECRET_KEY=tu-secret-key-seguro-aqui
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📱 Vistas de la Aplicación

### Página Principal
- Hero section atractivo
- Sección de características
- Call-to-action buttons
- Navegación intuitiva

### Autenticación
- **Login**: Formulario centrado con email y contraseña
- **Registro**: Formulario de nuevo usuario con validación
- Validación HTML5 y hashing de contraseñas

### Área de Usuario
- Dashboard personalizado
- Formulario para agendar nuevas citas
- Lista de reservas propias
- Campos: fecha, hora, motivo cita, matrícula

### Panel Administrativo
- Vista completa de todas las reservas
- Tabla con información detallada
- Gestión de estados de citas
- Información de usuarios y vehículos

## 🧪 Testing

```bash
python -m pytest tests/
```

## 📄 Licencia

Este proyecto está bajo licencia MIT.

---

**Desarrollado con Flask y PostgreSQL**
