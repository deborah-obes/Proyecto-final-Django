📰 Blog Informativo – Proyecto Final Django (Informatorio 2025)

Blog colaborativo desarrollado como parte del Informatorio Chaco 2025, construido con Django y Python.
El objetivo del proyecto es ofrecer un espacio dinámico donde compartir noticias, análisis y tendencias del mundo tecnológico, acercando la informática a personas de todos los niveles.

🚀 Tecnologías utilizadas

-Python 3.x

-Django 5.x

-HTML5 / CSS3

-Bootstrap

-SQLite3 (por defecto)

-Crispy Forms + Bootstrap5

-Pillow (para manejo de imágenes)


📦 Instalación

1. Clonar el repositorio:

git clone: https://github.com/deborah-obes/Proyecto-final-Django.git

2. Crear y activar el entorno virtual:

python -m venv venv
venv/Scripts/activate   # Windows

3. Instalar dependencias:

pip install -r requirements.txt


4. Aplicar migraciones:

python manage.py makemigrations
python manage.py migrate


5. Crear superusuario (opcional):

python manage.py createsuperuser

▶️ Ejecución del proyecto:  python manage.py runserver

▶️Luego abrir en el navegador:  http://127.0.0.1:8000/

🧩 Funcionalidades principales:


✔ Gestión de usuarios:

-Registro

-Inicio de sesión

-CRUD de usuarios

-Roles básicos


✔ Blog:

-Listado de artículos

-Detalle del artículo

-Creación, edición y eliminación (según permisos)


✔ Categorías:

-Administración de categorías
-Filtrado por categoría

✔ Sistema de comentarios:

-Agregar comentarios por artículo

-Gestión desde el panel administrador


✔ Páginas informativas:

-Inicio

-About / Nosotros

-Contacto


✔ Formularios personalizados:

-Uso de Django Forms y Crispy Forms

-Validaciones y mensajes


✔ Interfaz intuitiva:

-Diseño simple y tradicional, orientado a la lectura

-Navegación clara y jerarquizada


🖼️ Capturas del proyecto:

![Home del blog](./static/img/captura-home.png)

![Detalle de artículo](./static/img/captura-articulo.png)


📁 Estructura del proyecto:


Proyecto-final-Django/
│
├── blog/
│   ├── migrations/
│   ├── templates/blog/
│   └── models.py
│
├── category/
│   ├── templates/category/
│   └── models.py
│
├── comentario/
│   ├── templates/comentario/
│   └── models.py
│
├── crud_usuario/
│   ├── templates/crud_usuario/
│   └── views.py
│
├── inicio/
│   ├── templates/inicio/
│   └── views.py
│
├── pages/
│   ├── templates/pages/
│   └── views.py
│
├── usuario/
│   ├── templates/usuario/
│   └── models.py
│
├── templates/        # Plantillas globales
├── static/           # CSS, imágenes, etc.
├── requirements.txt
├── manage.py
└── db.sqlite3

🤝 Proyecto Final desarrollado por Comision#8 / Grupo#4 - Colaboradores:

- Brenda Torres
- Deborah Obes
- Marianela Cardozo
- Mathias Arguello
- Felipe Chorvalat

📜 Licencia

Este proyecto puede utilizarse con fines educativos y de práctica.
