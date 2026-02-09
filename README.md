# Taller - Sistema de Gestión de Taller

Una aplicación web moderna desarrollada en Flask para la gestión de citas y operaciones de un taller mecánico.

## 🚀 Características

- **Interfaz Moderna**: Diseño responsive con gradientes y animaciones suaves
- **Sistema de Autenticación**: Formulario de login con validación
- **Arquitectura Modular**: Organizado con Blueprints de Flask
- **Diseño Profesional**: CSS moderno con efectos hover y transiciones

## 📁 Estructura del Proyecto

```
Flask_Taller/
├── app/
│   ├── app.py                 # Aplicación principal
│   ├── config.py              # Configuración de la aplicación
│   ├── extensions.py          # Extensiones de Flask
├── main/
│   │   └── routes.py          # Rutas principales (inicio, login)
│   ├── login/
│   │   └── routes.py          # Rutas de autenticación
│   ├── templates/
│   │   ├── layout.html        # Plantilla base
│   │   ├── area.html          # Página usuario
│   │   ├── registro.html      # Página registro
│   │   ├── index.html         # Página de inicio
│   │   └── login.html         # Formulario de login
│   └── static/
│       └── css/
│           ├── index.css      # Estilos principales
│           ├── layout.css
│           └── login.css      # Estilos del login
└── requirements.txt
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Jinja2
- **Arquitectura**: Blueprints de Flask
- **Estilos**: CSS Grid, Flexbox, gradientes modernos

## 🎨 Diseño y UI

- **Paleta de Colores**: Gradiente púrpura-azul (#667eea → #764ba2)
- **Tipografía**: Arial, sans-serif
- **Responsive**: Adaptado para móviles y desktop
- **Componentes**: Tarjetas con efectos hover, botones animados

## 📋 Funcionalidades Actuales

### ✅ Implementadas
- Página de inicio con hero section
- Formulario de login estilizado
- Navegación con header fijo
- Footer con enlaces
- Diseño completamente responsive

### 🔄 En Desarrollo
- Sistema de autenticación completo
- Dashboard de usuario
- Gestión de citas
- Panel de administrador

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd Flask_Taller
```

2. Activar entorno virtual:
```bash
# Windows
.\flask-taller\Scripts\activate

# Linux/Mac
source flask-taller/bin/activate
```

3. Ejecutar la aplicación:
```bash
cd app
python app.py
```

4. Abrir en navegador: `http://localhost:5000`

## 📱 Vistas de la Aplicación

### Página Principal
- Hero section atractivo
- Sección de características
- Call-to-action buttons
- Navegación intuitiva

### Login
- Formulario centrado
- Campos de email y contraseña
- Validación HTML5
- Diseño moderno con sombras

## 🔧 Configuración

- **Debug Mode**: Activado para desarrollo
- **Host**: localhost
- **Port**: 5000 (por defecto de Flask)

## 📝 Próximos Pasos

- [✅] Implementar base de datos
- [ ] Completar sistema de login
- [ ] Crear dashboard de usuario
- [ ] Agendar gestión de citas
- [ ] Panel de administrador

## 👈 Contribución

El proyecto está en desarrollo activo. Las contribuciones son bienvenidas.

---

**Desarrollado con 💜 usando Flask**