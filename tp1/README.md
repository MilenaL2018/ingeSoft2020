## Trabajo Práctico 1 - Git Básico

### 1- Objetivos de Aprendizaje
 - Utilizar herramientas de control de configuración de software
 - Familiarizarse con los comandos más utilizados
 - Configurar el repositorio principal de cada alumno para la materia
  
#### Concepto de Pull Request
 Pull Request: petición que el propietario de un fork de un repositorio hace al propietario del repositorio original para que este último incorpore los commits que están en el fork. 

Comandos usados para actividad 4: git diff, git merge, git merge --abort 

LOCAL: El archivo de una branch donde se hace merge.
BASE: El pariente comun de LOCAL y REMOTE. El punto  previo a cuando ese archivo se convirtio en dos distintos
REMOTE:  El archivo de donde se mergea. 
MERGED : el archivo donde se muestran los conflictos de un merge y se tiene que editar. El codigo entre  <<<< HEAD and ===== es el que pertenece al LOCAL y
el codigo entre  ==== and >>>> <branch>, pertenece a REMOTE. 
  - Crear un branch local y agregar cambios a dicho branch. 
  - Subir el cambio a dicho branch y crear un pull request.
  - Completar el proceso de revisión en github y mergear el PR al branch master.


