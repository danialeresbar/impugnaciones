# IMPUGNACIONES

## Documentación

Plataforma para la gestión de Incidencias e Impugnaciones

### Correr el proyecto

Este proyecta usa Docker, por lo que solo deberás correr el comando:

```
docker-compose up
```

*La aplicación IMPUGNACIONES correrá en la URL `localhost:8008`*

Para recrear los contenedores si las dependencias del proyecto son actualizadas ejecuta el comando:

```
docker-compose up --build
```

Para remover los contenedores de Docker incluyendo la base de datos (Útil algunas veces cuando tratamos con migraciones):

```
docker-compose down --volumes
```

### Accediendo al panel de administración

El sitio de administración de Django para la aplicación IMPUGNACIONES puede ser accedido en `localhost:8000/admin`

Por defecto la configuración de desarrollo crea un super usuario con las siguientes credenciales:

```
Username: admin
Password: admin
```

### Carga de datos básicos

Para cargar la información básica en la base de datos primero debes tener una copia de los archivos CSV.
Estos archivos los puedes encontrar en: *enlance*. Una vez que hayas descargado los archivos debes colocarlos
en la carpeta **scripts** de este proyecto. En esta carpeta se encuentran los scripts que cargarán la información
contenida en los archivos que descargaste. Para proceder a cargar la información debes entrar en el contenedor
de la aplicación:

```
docker exec -it impugnaciones bash
```

Una vez que estás en la terminal del contenedor deberás ejecutar los scripts en el siguiente orden:

```
1. python scripts/start.py
2. python scripts/startvotos.py
3. python scripts/startjsonincidencias.py
4. python scripts/startjsonvotos.py
```
