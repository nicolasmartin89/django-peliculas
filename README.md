## Inicio Rápido
Para correr este proyecto de manera local deberás:
1. Configurar el Entorno de desarrollo en Python 3.
2. Luego de configurado el entorno, correr los siguientes comandos:
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
3. Abrir el proyecto en el navegador, en la dirección localhost:8000/admin para acceder al administrador del sitio.
4. Proceder a realizar pruebas creando por ejemplo: Usuarios, Películas, Autores, etc...
5. Abrir en el navegador localhost:8000, para observar los cambios.
