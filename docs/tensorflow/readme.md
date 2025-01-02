# **Qu'est-ce que Tensorflow ?** <a href="../"><img align="right" src="../../assets/Tensorflow.png" alt="Tensorflow" height="64px"></a>
C'est une bibliothèque open source de Google. Elle est dédiée au calcul numérique et au machine learning à grande échelle. Son but est de créer, déployer des modèles de ML à certaines plateformes (ordis de bureau, appareils modèles, cloud, et cætera).
## **Les principales caractéristiques**  
* La flexibilité  
    Son architecture flexible facilite le déploiement de calculs sur une variété de plateformes (CPU, GPU, TPU) et des dispositifs (ordinateurs de bureau, appareils mobiles, dispositifs en périphérie).
* La compatibilité multi-langages  
    Bien que l'API principale soit en Python, TensorFlow propose également des API pour JavaScript (TensorFlow.js) voire C++ et Java, afin que les développeurs travaillent dans le langage de leur choix. 
* L'intégration avec Keras  
    Elle intègre Keras, une API de haut niveau qui simplifie la création et l'entraînement de modèles de deep learning, rendant le processus plus intuitif pour les débutants et experts. 
* Les extensions et outils supplémentaires  
    Il y a une gamme d'extensions pour des besoins spécifiques, tels que `TensorFlow Lite` pour les appareils mobiles et embarqués, `TensorFlow Extended (TFX)` pour les pipelines de production de machine learning, et `TensorFlow.js` pour le développement en JavaScript.
## **Aspects juridiques, éthiques et environnementaux**
* Les aspects juridiques  
    Dans des projets commerciaux ou de recherche, elle nécessite une attention particulière aux licences open source et aux réglementations sur la protection des données, notamment le respect du Règlement Général sur la Protection des Données (RGPD) en Europe. 
* Les aspects éthiques  
    Lors du développement de modèles avec TensorFlow, il est crucial de considérer les implications éthiques, telles que la prévention des biais dans les modèles, la transparence des algorithmes et le respect de l'intégrité scientifique. 
* L'impact environnemental  
    L'entraînement de modèles de machine learning, particulierement de deep learning, est énergivore. En conséquence, il est important d'optimiser les modèles pour réduire leur empreinte carbone et d'utiliser des ressources informatiques de manière efficiente.
## **Quel est le positionnement des Tensorflow par rapport aux autres frameworks en ML?**
Elle se positionne en framework polyvalent et robuste pour le machine learning, adapté aussi bien aux débutants qu'experts, couvrant une large gamme d'applications (des prototypes de recherche aux solutions industrielles déployées à grande échelle).
Framework | Positionnement | Forces | Faiblesses
:-:|---|---|---
TensorFlow | Leader pour les applications industrielles et les projets complexes nécessitant une intégration de bout en bout. | ✅ Un écosystème riche (TFX, TensorFlow Lite, TensorFlow.js).<br>✅ Une compatibilité TPU.<br>✅ Une forte communauté et documentation. | ❌ Elle peut être complexe pour les débutants.<br>❌ Sa syntaxe est moins intuitive que certains frameworks comme PyTorch.
PyTorch | Est préférée dans le milieu académique et pour les recherches en machine learning grâce à sa simplicité et son dynamisme. | ✅Les graphes computationnels sont dynamiques.<br>✅ Son interface est intuitive.<br>✅ Prototypage rapide. | ❌ Elle est moins conçue pour la production et le déploiement industriel.
Scikit-learn | Est un framework généraliste pour l’apprentissage automatique classique, principalement utilisé pour des tâches simples et des prototypes. | ✅ Facile à apprendre.<br>✅ Large bibliothèque d’algorithmes traditionnels (SVM, régression, clustering). | ❌ Inadapté pour le deep learning ou les grands ensembles de données.
Keras | Est une Interface de Programmation Applicative de haut niveau (souvent intégrée à TensorFlow) conçue pour une utilisation simple et rapide dans le deep learning. | ✅ Syntaxe intuitive.<br>✅ Facilité de prototypage.<br>✅ Intégrée à TensorFlow. | ❌ Moins de contrôle sur les opérations bas niveau.
MXNet | Framework open source soutenu par AWS, souvent utilisé pour des applications cloud et le deep learning distribué. | ✅ Support natif pour plusieurs langages (Python, Julia, Scala, etc.).<br>✅ Bien adapté pour le cloud AWS. | ❌ Communauté plus petite que TensorFlow ou PyTorch.<br>❌ Documentation parfois insuffisante.
CNTK (Microsoft) | Est conçu pour l’apprentissage profond, principalement utilisé dans les environnements Microsoft. | ✅ Performant pour les réseaux neuronaux récurrents (RNNs).<br>✅ Intégrer avec d’autres outils Microsoft. | ❌ Faible adoption hors de l’écosystème Microsoft.
H2O.ai | Est un framework axé sur les solutions de machine learning pour les entreprises. | ✅ Idéal pour l'analyse prédictive.<br>✅ Interface conviviale pour les non-spécialistes. | ❌ Moins adapté pour le deep learning avancé.
Theano | Est le pionnier des frameworks de deep learning, souvent considéré comme l’ancêtre de TensorFlow et PyTorch. | ✅ Le contrôle fin des calculs.<br>✅ Bien adapté à l’expérimentation. | ❌ Son développement fût arrêté en 2017.<br>❌ Dépassé par TensorFlow et PyTorch.
JAX | Est un framework moderne de Google conçu pour le calcul numérique et le machine learning avancé. | ✅ Est performant grâce à son calcul différentiable automatisé.<br>✅ Compatible avec les TPU et GPU. | ❌ Il y a moins de modèles pré-entraînés et d’outils que TensorFlow.
## **Positionnement stratégique de TensorFlow**
* Son écosystème est complet  
    Grâce à des outils comme TensorFlow Extended (TFX), TensorFlow Lite, et `TensorBoard`, il couvre tout le cycle de vie des modèles, du développement au déploiement.
* Sa polyvalence  
    Convient aux débutants (via Keras) et aux experts (via des APIs bas niveau).
* Son optimisation pour le cloud  
    À une forte intégration avec Google Cloud Platform (GCP) et compatibilité avec d'autres clouds.
* Son support pour des matériels variés  
    Compatible avec CPU, GPU, et TPU, optimisant ainsi les performances matérielles.

_TensorFlow est un choix stratégique pour les projets nécessitant une infrastructure robuste, une flexibilité inter-langages, et un large support industriel. Néanmoins, pour des recherches exploratoires ou des besoins spécifiques._