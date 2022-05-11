# Entrega 1 Gambin

## Trabajo Final Curso Python Django: __"Chernobyl - The Zone is Waiting"__

Guia:

<p>- Asegurar que la branch se "trabajofinal1" es el terminado

<p>- Descagar los archivos del repositorio de GitHub --https://github.com/Foxirium/Entrega1-Gambin.git--</p>


<p>- Pasar los archivos a una carpeta y abrirlos con Visual Studio Code o similar</p>

<p>- En la terminal de VS, asegurandose de estar en el directorio donde se encuentra el archivo __"Manage.py"__ escribir: "python manage.py runserver" </p>

<p>- Una vez que el server este corriendo, en un navegador entrar a http://127.0.0.1:8000/appChernobyl y sera redirigido a la pagina principal de la aplicacion </p>


# En la pagina propiamente dicha

## AppChernobyl/


- La pagina principal cuenta con 5 menues de navegacion

__Homepage__ 

    - Sera dirigido a la pagina de inicio de la aplicacion /appChernobyl
    - Cuenta con unas inscripciones y un boton "JOIN" que lo redirigira a la pagina de registro /appChernobyl/stalkers

__Stalkers__ 

    - Sera dirigido una pagina donde puede registrarse como usuario o buscar algun stalker ya registrado.

    - Si busca un stalker debe ingresar una letra al menos apretar en "SEARCH STALKER" para iniciar la busqueda. En caso de no encontrarse en la base un mensaje en rojo aparecera devolviendo "No se encontraron stalkers registrados con esos parametros

    -Si no se ingresan datos sera dirigido a una pagina sin renderizado que indica "No se han enviado datos"

    -Stalkers registrados para buscar:  Father Diodor
                                        Gordon Freeman
                                        Nimble Stalker
                                        Piotr Kalugin
                                        Vasya Boar

    - Si el stalker registrado es encontrado devolvera el nombre, apellido y faccion a la que pertence.

    - Para registrar un stalker a la base de datos, el formulario pide NAME, SURNAME, FACTION, DATEOFBIRTH en formato YYYY-MM-DD                                    

__Faccions__

    - Sera dirigido a una pagina donde puede registar su faccion con los parametros
        NAME (nombre de la faccion), FOUNDER (stalker que la funda), Age(edad de la faccion)

    - Una vez registrada su faccion sera redirigido a la pagina principal

__Artifacts__

    - Sera dirigido a una pagina donde puede registrar su artefacto con los parametros 
    Name (nombre del artefacto), Power (poder del artefacto ejemplo Radiation -50%) y DateOfBirth(Cuando nacio el artefacto con formato YYYY-MM-DD)

__Levels__

    -Sera dirigido a la pagina de levels que todavia esta en construccion.

    -Dentro de la base de datos existe un nivel creado con un nombre (lName), cantidad de estructuras(lStructureAmount), cantidad de npcs(lNpcsAmount) y dificultad (difficulty).               Name: Cordon
                                lStructureAmount: 11
                                lNpcsAmount: 52
                                difficulty: Easy

                                
