# **L'anatomie d'une appli** <a href="../../"><img align="right" src="../../../src/images/Python-logo-notext.svg" alt="Python" title="Python" widht="auto" height="64px"></a>

La première chose que l'on a dans une application avec interface graphique, c'est l'application. Elle peut avoir qu'une seule application, mais plusieurs fenêtres.  
Ensuite, il y a les éléments individuels. Ce sont les widgets (barre d'adresse et de recherche, un onglet, le bouton nouvel onglet, une boîte de texte, une liste, un menu déroulant, etc), c'est le plus petit élément de l'interface. Le widget d'effectuer une action.  
Ces éléments, nous les connectons ensuite à des signaux, donc créer la logique de l'application.  
Puis, il y a les layouts (dispositions) qui sont moins visibles et permettent d'organiser les widgets de différentes façons. Certains sont horizontaux (barre d'onglets), d'autres sont verticaux, ou en grille (pour une calculatrice). Ils sont très importants pour organiser les widgets.  

En résumé :
* 1 appli
* 1 ou plusieurs fenêtres
* Plusieurs widgets (des centaines)
* Les layouts (très peu)
* les signaux (il en existe plusieurs par widgets, mais ce sout souvent les mêmes widgets), pour connecter le tout