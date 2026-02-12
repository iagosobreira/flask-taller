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

## 📋 Funcionalidades Actuales

### ✅ Implementadas
- **Autenticación Completa**: Login, registro y gestión de sesiones
- **Gestión de Usuarios**: Registro con roles (admin/usuario)
- **Sistema de Citas**: Agendar citas con fecha, hora, motivo y matrícula
- **Panel de Usuario**: Vista personalizada para gestionar reservas propias
- **Panel Administrativo**: Gestión completa de todas las reservas del sistema
- **Base de Datos Relacional**: PostgreSQL con tablas de usuarios y reservas
- **Diseño Responsive**: Adaptado para móviles y desktop
- **Estados de Citas**: Sistema de estados (aceptada, denegada, pendiente)

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

5. Ejecutar script de base de datos (usar `Notas.txt`):
```sql
-- Crear tablas de usuarios y reservas
-- Ver contenido en Notas.txt
```

6. Ejecutar la aplicación:
```bash
cd app
python app.py
```

7. Abrir en navegador: `http://localhost:5000`

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

## 🔧 Configuración

- **Debug Mode**: Configurable en `config.py`
- **Base de Datos**: PostgreSQL con SQLAlchemy
- **Host**: localhost (configurable)
- **Port**: 5000 (por defecto de Flask)
- **Sesiones**: Flask session management habilitado

## 🗄️ Esquema de Base de Datos

### Tablas Principales:
- **usuarios**: id, nombre, correo, contrasena, rol
- **reservas**: id, fecha_reserva, estado, id_usuario, motivo_cita, matricula

### Estados de Reserva:
- `aceptada`
- `denegada` 
- `Pendiente`

## 🔐 Variables de Entorno

Crear archivo `app/.env` con:
```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/taller_db
SECRET_KEY=tu-secret-key-seguro-aqui
FLASK_ENV=development
FLASK_DEBUG=True
```

## 🧪 Testing

Para ejecutar tests (cuando se implementen):
```bash
python -m pytest tests/
```

## 👈 Contribución

El proyecto está en desarrollo activo. Las contribuciones son bienvenidas.

### Flujo de Contribución:
1. Fork del proyecto
2. Crear feature branch: `git checkout -b feature/nueva-funcionalidad`
3. Commit changes: `git commit -m 'Añadir nueva funcionalidad'`
4. Push to branch: `git push origin feature/nueva-funcionalidad`
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

---

**Desarrollado con 💜 usando Flask y PostgreSQL**