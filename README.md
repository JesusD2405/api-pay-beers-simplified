# Pagar Cervezas Simplificado

_Proyecto en Django Rest Framework, que contiene el desarrollo de una Api para la gestión pagos de cervezas. Implementación bajo Clean Architecture (Test Mode) personalizada.. Ref: [Clean Architecture in Django](https://medium.com/21buttons-tech/clean-architecture-in-django-d326a4ab86a9)_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas o despliegue en producción._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

1. [Docker](https://docs.docker.com/)

_Es importante tener instaladas las herramientas anteriormente mencionadas para iniciar los siguientes pasos._

## Instalación 🔧


_*** Preparando nuestras variables de entorno ***_

_Nos situamos en la raíz y hacemos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente (local)_

```
 cp docker-env.dist docker-env.local
```

_En nuestro nuevo archivo docker-env.local modificamos y adaptamos las variables de entorno del Docker_

_Finalmente, en la raíz del proyecto ejecutamos_

```
 docker compose --env-file=./docker-env.local up --build
```

_De esta manera tendríamos todos nuestros conenedores levantados._

## Probando Rutas 🧪

_Para esta implementación solo se desarrollaron 2 rutas GET, las cuales son: ._

1. Obtener Orden: GET `/api/v1/orders`.
2. Obtener Stock: GET `/api/v1/stocks`.

_¿Como probar los TESTS de la API?._
_Actualmente, estos test se ejecutan automáticamente al iniciar el contenedor, pero en caso de ejecutar el test manualmente debemos ejecutar los siguentes comandos:_

```
 docker exec -it payBeersSimplified-api bash
```
_De esta manera entrariamos al contenedor de la api y podriamos ejecutar el test con python de la siguiente manera:._
```
 ./manage.py test tests.stock.stockTest
```

## Despliegue 📦

_Nos situamos en el directorio raiz y hacemos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente a desplegar:_

1. dev (Desarrollo).
2. prod (Producción).

```
 cp docker-env.dist docker-env.ambiente
```

_En nuestro nuevo archivo docker-env.ambiente modificamos y adaptamos las variables de entorno del Docker_

_Finalmente, en la raíz del proyecto ejecutamos_

```
 docker compose --env-file=./docker-env.ambiente up --build
```

## Construido con 🛠️

_Herramientas utilizadas en el proyecto:_

- [Python V3.12](https://docs.python.org/es/3.12/) - Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo.
- [Pip V21.0.1](https://pypi.org/project/pip/) - Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.
- [Docker](https://docs.docker.com/compose/install/) - Es una tecnología de contenedorización de código abierto para crear y contener sus aplicaciones.
- [Django Rest Framework](https://www.django-rest-framework.org/) - El marco Django REST es un conjunto de herramientas potente y flexible para crear API web.

---

Desarrollado por [Jesús David Pérez](https://github.com/JesusD2405/) ❤️🚀
