# CONSULTORIO

## Demostración
[Video](https://youtu.be/9JeWVEp5E6g)

## Distinctiveness and Complexity: 
Este proyecto es una aplicación web para una clínica médica , en donde además de poder agender tu cita, eliminarla y consultar el horario los doctores puede publicar articulos de la salud, consultar el historial de sus pacientes y ver las citas agendadas. Se utilizó Django para el Backend y Javascript puro para Front End, que es lo que piden en los requerimientos del proyecto, para comunicarse una con la otra hace uso de API'S, además se hace uso de HTML, CSS y Bootstrap.

### ¿Qué contienen las carpetas?

**BlogCitas** contiene el código principal de nuestra aplicación web.
En el archivo views.py están todas las rutas a las que el usuario puede acceder, como por ejemplo: "principal, blog, post, acerca_de, citas, nueva_cita y eliminar_cita". 
En el archivo **api.py** se encuentran todas las rutas que se usan para que el Front end obtenga información, como "registro y horarios". 

En **funciones.py** se encuentran 2 funciones que podrían haber estado incluidas en api.py y views.py, pero por motivos de organización decidí ponerlos en un archivo diferente. 

En **models.py** se encuentran los modelos necesarios para crear la base de datos, que en este caso es sqlite, pero facilmente podría ser reemplazada por MySQL. 
En la carpeta **templates** estan todos los archivos html que se utilizan, y en la carpeta **static** se encuentra el archivo css y los 3 archivos de javascript. 

**media** contiene todas las fotos que se usan en la interfaz, se usa sqlite para organizarlas y cada que publicas nuevos articulos, se van guardando en la carpeta.

**Consultorio** es el archivo que crea Django al iniciar el proyecto, modifique el archivo "settings.py" y "urls.py"

###¿Qué modulos adiconales se usan para el proyecto?
tinymce
PIL

### ¿Como ejecutar la aplicación?
Despues de instalar los módulos puestos en requeriments.txt, debe hacer las migraciones de la base de datos, con los comandos: *python manage.py makemigrations*, y posteriormente *python manage.py migrate*. Después solo basta con ejecutar *pyhton manage.py runserver* para que poder acceder a la aplicación.

También necesitará crear un entorno virtual, para poner la SECRET_KEY en una variable de entorno y que este más segura. En nombre de la variable debe ser SECRET_KEY.
