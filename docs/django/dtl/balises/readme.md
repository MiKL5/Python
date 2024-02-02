# Liste des balises DTL<a href="../../"><img align="right" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg" alt="Django" title="Django" widht="auto" height="64px"></a>
<div align="center">

>## **Balises de base**
`{# this won't be rendered #}` ➜ commenter sue une seule ligne  
`{% comment %}` ➜ ajouter des commentaires sur plusieurs lignes  
`{% cycle %}` ➜ faire défiler une liste de valeurs  
`{% debug %}` ➜ afficher des informations de débogage  
`{% firstof %}` ➜ afficher la première valeur non vide d'une liste  
`{% for %}` ➜ créer des boucles  
`{% if %}` ➜ tester des conditions  
`{% else %}` ➜ définir une alternative à une condition if  
`{% elif %}` ➜ ajouter des conditions supplémentaires à une instruction if  
`{% endif %}` ➜ terminer une instruction if  
`{% include %}` ➜ inclure un autre gabarit  
`{% load %}` ➜ charger des modules de balises  
`{% now %}` ➜ afficher la date et l'heure actuelles  
`{% raw %}` ➜ empêcher l'échappement HTML  
`{% static %}` ➜ générer des URL vers des fichiers statiques  
`{% url %}` ➜ générer des URL Django  
`{% with %}` ➜ définir un contexte temporaire  

>## **Balises pour les variables**  
`{{ variable }}` ➜ afficher une variable  
`{{ variable|default:'valeur par défaut' }}` ➜ afficher une valeur par défaut si la variable est vide  
`{{ variable|filter1|filter2 }}` ➜ appliquer des filtres à une variable  

> ## **Balises pour les formulaires**  
`{% csrf_token %}` ➜ générer un jeton CSRF  
`{% form %}` ➜ démarrer un formulaire  
`{% for field in form %}` ➜ boucler sur les champs d'un formulaire  
`{% endfor %}` ➜ terminer une boucle  
`{{ field.errors }}` ➜ afficher les erreurs d'un champ  
`{{ field.value }}` ➜ afficher la valeur d'un champ  
`{% endform %}` ➜ terminer un formulaire  

> ## **Balises pour les messages**  
`{% messages %}` ➜ afficher les messages flash  

> ## **Balises pour les modèles**  
`{% get_model %}` ➜ obtenir un modèle Django  
`{% object_list %}` ➜ afficher une liste d'objets  
`{% object_detail %}` ➜  afficher un objet en détail  

> ## **Balises pour les i18n**  
`{% get_current_language %}` ➜ obtenir la langue courante  
`{% get_available_languages %}` ➜ obtenir la liste des langues disponibles  
`{% trans %}` ➜ traduire une chaîne de caractères  

> ## **Balises pour les permissions**  
`{% if has_permission %}` ➜ tester si un utilisateur a une permission  
`{% else %}` ➜ définir une alternative à une condition if  
`{% endif %}` ➜ terminer une instruction if  

> ## **Balises pour les tags**  
`{% get_tags %}` ➜ obtenir la liste des tags disponibles  
`{% for tag in tags %}` ➜ boucler sur les tags  
`{% endfor %}` ➜ terminer une boucle  
`{{ tag.name }}` ➜ afficher le nom d'un tag  
`{{ tag.description }}` ➜ afficher la description d'un tag  

> ## **Balises pour les utilisateurs**
`{% get_user %}` ➜ obtenir un utilisateur Django  
`{% if user.is_authenticated %}` ➜ tester si un utilisateur est authentifié  
`{% else %}` ➜ définir une alternative à une condition if  
`{% endif %}` ➜ terminer une instruction if  
___
<div align="left"><br>

Plus de balise à la [documentation officielle](https://docs.djangoproject.com/fr/5.0/topics/templates/ "Documentation du DTL")  
