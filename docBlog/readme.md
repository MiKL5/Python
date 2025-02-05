# **DocBlog** <a href="../"><img align="right" src="../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
Créer l'environnement virtuel.
```pwsh
python3.12 -m venv .env
```
<!-- ou venvv -->
Le sourcer<!-- en allant chercher le fichier `activate` dans `venv` ou `env`. Sourcer veut dire activer. -->.
```bash
source .env/bin/activate
# L'environnement est activé.
```
Connaître la version Python du projet.
```bash
which python
# J'ai bien le python de l'environnement virtuel, il est correctement créer.
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