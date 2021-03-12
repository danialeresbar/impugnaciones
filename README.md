# IMPUGNACIONES

## Documentation ##

Plataforma para la Gestión de Incidencias e Impugnaciones

### How to run the project ###

The project use docker, so just run:

```
docker-compose up
```

> If it's first time, the images will be created. Sometimes the project doesn't run at first time because
> the init of postgres, just run again `docker-compose up` and it will work.

### When there are changes in the database container ###

It may be useful to run:

```
docker-compose down --volumes
```
 
And again run:

```
docker-compose up --build
```


*IMPUGNACIONES app will run in url `localhost:8008`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```

To remove the docker containers including database (Useful sometimes when dealing with migrations):

```
docker-compose down
```

### Accessing Administration

The django admin site of the IMPUGNACIONES project can be accessed at `localhost:8000/admin`

By default the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```
