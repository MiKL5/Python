# **Qu'est-ce qu'un itérateur** <a href="../../"><img align="right" src="../../assets/Python-logo-notext.svg" alt="Python" title="Phthon" widht="auto" height="64px"></a>

Les itérateurs ont une définition technique en [Python](https://docs.python.org/3/glossary.html#term-iterator "Documentation Python à propos de l'itérateur"). C'est un terme connexe.

Un itérable est un objet capable de renvoyé ses membres 1 par 1. C'est une valeur avec laquelle il est possible d'itérer avec une boucle for, une séquence, et beaucoup d'autres possibilités. Il est aussi possible de les déstructurer et créer des collections à partir d’eux en passant la valeur à des fonctions comme `list` ou `tuple`.

Voici quelques types d’itérables :
* `strings`;
* `listes` ;
* `tuples` ;
* dictionnaires ;
* `sets` ;
* objets `range` ;
* objets `zip` ;
* objets `enumerate` ;
* objets `map` ;
* objets `filter`.  

Très largement, un itérable est un objet dont on peut extraire des valeurs une par une.

Comment obtenir ces valeurs ? Comment Python sait-il ce qu’il doit nous donner ?

Il utilise des itérateurs. Si les itérables sont les objets dont nous pouvons obtenir des valeurs, les itérateurs sont les objets qui nous renvoient ces valeurs. Ils sont le mécanisme que Python utilise pour extraire des valeurs des itérables.

Comme dans la liste d’itérables, les itérateurs susmentionnés sont également des itérables. En fait, **tous les itérateurs sont des itérables**.

Il y a une raison technique à cela qui est liée à la façon dont les itérateurs sont définis, cela a aussi un sens intuitif.

Lorsque nous voulons des valeurs d’un itérable dans le cadre d’une itération : 
1. Nous demandons l’itérateur en charge de fournir vos valeurs.
2. Nous sommes alors mis en contact avec cet itérateur, et il commence à nous fournir des valeurs, une par une.
3. Si on demande directement à un itérateur.
4. il répond, qu'il est chargé de libérer les valeurs, donc qu'il peut nous les donner.

<br>

___

Important
Tous les itérateurs ne récupèrent pas les valeurs d’un autre itérable. De nombreux itérateurs génèrent spontanément des valeurs pour nous à la place.

Cela fonctionne parce que les itérateurs sont des itérables (ce qui signifie que nous pouvons itérer sur eux pour obtenir les valeurs que l'on veut), et les itérateurs sont capables de nous fournir des valeurs sans l’aide d’un autre itérateur. Il suffit qu’un itérateur ait un moyen de générer des valeurs en interne, plutôt que de nous fournir un moyen d’accéder à des valeurs définies ailleurs.

## Propriétés importantes des itérateurs

Ils possèdent plusieurs propriétés utiles et importantes.  

Tout d’abord, la plupart des itérateurs sont de type “paresseux”, notamment ceux définis dans la bibliothèque standard. Cela signifie qu’ils ne prennent pas la peine de calculer toutes leurs valeurs à l’avance, comme les objets range.

Cela est considérablement avantageux pour la mémoire, car seule la valeur la plus récente est conservée. Une fois que nous avons fini de l’utiliser, nous pouvons la jeter, libérant ainsi potentiellement cette mémoire.

Il y a également des économies potentielles en calculs, car, il se peut que l'on est pas besoin de toutes les valeurs qu’un itérateur peut fournir. Si seules les trois premières valeurs nous intéressent, il n’est pas nécessaire de déterminer quelles sont les 200 suivantes.

Mais pour cela, il faut faire des compromis.

Tout d’abord, il est souvent impossible de déterminer la longueur d’un type paresseux, car le nombre d’éléments qu’il contient peut n’apparaître qu’après le calcul de ces valeurs. 

### Les valeurs de l’itérateur sont consommées

Il est très important de garder ceci à l’esprit, car il s’agit d’un “piège” commun dans lequel tonmbent généralemment les nouveaux développeurs Python.

### Les modifications apportées aux collections mutables peuvent affecter un itérateur

C’est un autre effet secondaire assez logique de la paresse. L'itérateur se contente de référencer celle que nous avons déjà en mémoire.