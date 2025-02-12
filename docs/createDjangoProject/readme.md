# **Créer un projet avec Django** <a href="../../"><img align="right" src="../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Créer l'environnement virtuel.
```pwsh
python3.12 -m venv .env
```
<!-- ou venvv -->
Le sourcer<!-- en allant chercher le fichier `activate` dans `venv` ou `env`. Sourcer veut dire activer. -->.
```pwsh
source .env/bin/activate # L'environnement est activé.
```
Connaître la version Python du projet.
```pwsh
which python # J'ai bien le python de l'environnement virtuel, il est correctement créer.
```
Pour Installer Django il est important que `pip` soit à jour.
```pwsh
pip install --upgrade pip
```
Installer django
```pwsh
pip install django==3.1.6 # django en minuscule
```
Vérifier l'installation
```pwsh
python -m django --version # 3.1.6
```
ou
```pwsh
python
import django
```
Géler l'environnement pour garder en mémoire les bibliothèques et vesions.
```pwsh
pip freeze > requirements.txt
```
L'afficher avec `cat` ou `more`.
```pwsh
cat requirements.txt
```
Réinstaller.
```pwsh
pip install -r requirements.txt
```
Désactiver l'environnement.
```pwsh
desactivate
```
Créer un projet
```pwsh
django-admin startproject DocBlog
```
Toutes les commandes de `django-admin`
```pwsh
django-admin --help
```
## **L'architecture du projet**
`manage.py` permet d'exécuter des commandes avec Python.
`__init__.py` est vide.
`asgi.py` & `wsgi` sont utilisés lors du déploiement sur un server.
`urls.py` pour définir les chemins et vers quelles vues pointer.
`settings.py` contient toutes les préférences de l'application.  
↪ La variavle '`debug`' passera à '`false`' quand le server sera en production.  
↪ Il y a aussi les applications utilisées, middlewares, templates, la base de données (sur sqlite3 par défaut car elle est très légère, et peut être changée.), langugage_code, et cætera.
## **Utiliser le server**
Lancer le server de production
```pwsh
python manage.py runserver
```
## **Créer une application <!-- (dans le projet)-->**
```pwsh
python manage.py startapp blog
```
## **Ajouter du style**
Dans une application, il faut créer un dossier `static`.  
Hors d'une application, il faut ajouter ce qui suit à '`settings.py`'.
```py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "DocBlog/static"),
]
```
## **Automatiser `runserver` avec PyCharm**
Edit configuration > Name : Django Server > script : adresse du fichier manage.py > OK ou Run
## **Créer les migrations**
```pwsh
manage.py makemigrations 
```
ou que pour l'appli blog
```pwsh
manage.py makemigrations blog
```
## **Migration**
Aperçu du code à migrer
```pwsh
python manage.py sqlmigrate blog 0001_initial # l'app et le fichier sans l'éextension
```
Aperçu de plusieurs
```pwsh
python manage.py sqlmigrate blog 0001_initial && python manage.py sqlmigrate blog 0002_blogpost_description
```
Migrer
```pwsh
python manage.py migrate
```
ou que blog
```pwsh
python manage.py migrate blog
```