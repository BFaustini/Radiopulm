#https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from PIL import Image

title = 'Principes de Modélisation'
sidebar_name = 'Principes de Modélisation'

#path = "D://documents/GitHub/AVR23---BDS---Radio-Pulm/streamlit_app/assets/"
path = "C:/Users/Nina/Documents/GitHub/AVR23---BDS---Radio-Pulm/streamlit_app/assets/"
path = "C:/Users/benji/Pictures/AVR23---BDS---Radio-Pulm/"

def run():

    st.title(title)
    
    st.divider()
          
    tab_main1, tab_main2 = st.tabs(["Généralités et Modalités d'Entrainement", "Architectures de Deep Learning"])
    
        
    with tab_main1 : #Présentation des modèles et notions
        
        tab1, tab2, tab3 = st.tabs(["Les CNNs", 
               "Métriques & Callbacks", "Compilation & Entrainement des modèles"])
               
        with tab1 : #Les CNNs
            
            st.markdown(
                """
                #### Réseaux de Neurones Convolutifs
                En ce qui concerne le Deep Learning, les Réseaux de Neurones Convolutifs (CNN), du module Keras, sont les outils les plus utilisés pour l’analyse des images. Dans le milieu médical, les CNN sont des puissants outils en raison de leurs capacités à extraire des caractéristiques des images et à apprendre à les distinguer entre les différentes classes, comme des cas positifs vs. négatifs, des cas infectés vs. sains, ou comme dans le cas du projet actuel, distinguer des classes des maladies des radiographies.
            
                L’architecture d’une CNN est composée de couches convolutives (_convulation layer_) (avec ReLU ou softmax), de couches poolings (_pooling layer_) et finalement de couches entièrement connectées (_fully connected layer_). 
            
                Comme montré dans l’image ci-dessus, les images d’entrée deviennent de plus en plus petites à mesure qu’elles progressent dans le réseau, mais elles deviennent également de plus en plus profondes avec la carte des entités. 
            
                Le réseau est divisé en 2 parties : une première partie d’apprentissage des fonctionnalités (_feature learning_) et une deuxième de classification.
                """)
            image = Image.open(path + 'archi_cnn.png')
            st.image(image, caption = "Architecture d'un CNN")
              
            st.markdown(
                """
                #### Bloc de Classification
                Une fois les images passées à travers le _feature learning bloc_, nous rencontrons le bloc classificateur. Ce bloc est construit à partir de couches plus simples, toutes entièrement connectées. _Fully connected_, comme son nom l'indique, sont des couches dans lesquelles chaque neurone de l'entrée est connecté à chaque neurone de la couche de sortie.
            
                Les modèles de _TransferLearning_ (__VGG16, EfficientNetB1, ResNet152__) ont un bloc classificateur défini comme suit :        
                """)
        
            st.markdown(
                """
                - __GlobalAveragePooling2D__ : conçue pour remplacer les couches entièrement connectées. Elle prend la moyenne de chaque feature map et alimente le vecteur résultant directement dans les couches Denses.
                - __Dense ‘ReLU’__ : couche qui absorbe une certaine non-linéarité, assurée par une fonction mathématique appelée _Rectified Linear Unit (ReLU)_.
                - __Dropout__ : couche pour éviter le surapprentissage en réduisant le nombre de neurones.
                - __Dense ‘softmax’__ : couche de sortie puisqu’il s’agit d’un problème de classification multi-classes. Dans le cas analysé, cette couche aura 4 unités, représentant le nombre de catégories étudiées.
                
                #

                #

                #
                """)
            
            
            
        with tab2 : #Métriques
            st.markdown(
                """
                #### Métriques
                Les métriques classiques pour évaluation des performances des modèles de classification sont :
                - __Accuracy score__ : proportion de bonnes prédictions.
                - __Precision__ : Spécificité pour déterminer si notre modèle est performant pour détecter les cas négatifs.
                - __Recall__ : Sensibilité pour déterminer si notre modèle est performant pour détecter les cas positifs.
                - __F1-score__ : Moyenne harmonique de précision et recall.
                - __Matrice de confusion__ : tableau pour observer les Faux Positifs, Faux Négatifs, Vrais Positifs, Vrais Négatifs.
                """)
            
            st.markdown(
                """
                #### Callbacks
                Les rappels (_callbacks_) sont des outils qui permettent de personnaliser les entraînements et les évaluations. Ils permettent alors de connaître l’état interne d’un modèle, le sauvegarder, d’afficher des statistiques intéressantes et même de changer des hyperparamètres pendant les étapes de l’entraînement. Ces _callbacks_ seront définis pour pouvoir faire évoluer les métriques de compilation et pouvoir avoir une meilleure performance.
            
                Les callbacks utilisés sur tous les modèles étudiés :
                - __Checkpoint__ : _callback_ permettant de sauvegarder régulièrement un modèle pendant son entraînement, ce qui peut être utile lors d’un long apprentissage.
                - __ReduceLROnPlateau__ : _callback_ permettant de changer le taux d’apprentissage selon la métrique choisie et non pas le nombre d’epochs.
                - __EarlyStopping__ : _callback_ très utilisé permettant de contrôler l’évolution des métriques en arrêtant l’entraînement quand ces dernières ne s’améliorent pas.
                """)
                
            image = Image.open(path + 'early_stopping.png')
            st.image(image, caption = 'EarlyStopping', width = 700)

            st.markdown(
                """
                #

                #
                
                #
                """)
        
        
        with tab3 : #Compilation & Entrainement des modèles
            st.markdown(
                """
                #### Compilation des modèles 
                Pour compiler les modèles étudiés, nous avons utilisé les hyperparamètres suivants :
                - __Optimizer__ = _Adam_ : c’est l’optimiseur le plus populaire actuellement. Le learning rate par défaut est défini à 0.001.
                - __Loss__ = ‘_categorical_crossentropy_’ : il s’agit d’un problème de classification multi-classes.
                - __Metrics__ = [‘_accuracy_’] : la précision sera la métrique analysée par le compilateur.
                """)
               
            st.markdown(
                """
                #### Entrainement des modèles
                L’ensemble des modèles étudiés ont été entraînés avec les caractéristiques suivantes :
                - Nombre maximal d’epochs : __30__
                - Taille de batch : __32__
                - Portion de l’échantillon de test : __20% de l’échantillon total__
                - Portion de l’échantillon de validation : __20% du sous-ensemble restant__
                """)

            
    with tab_main2 : #Les modèles étudiés
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "LeNet","Transfer Learning","KerasTuner", "Interprétabilité"])
        
        with tab1 : #LeNet
            st.markdown(
                """
                L'architecture LeNet est considérée comme __l’architecture de base, ou la plus simple__, pour un problème d’analyse d’images.

                L’architecture LeNet CNN est composée de 7 couches. La composition des couches est définie par 3 couches convolutives, 2 couches de sous-échantillonnage et 2 couches entièrement connectées.

                La première couche est la couche d’entrée, elle n’est généralement pas considérée comme une couche du réseau car rien n’est appris dans cette couche. Cette couche d’entrée va transmettre à la couche suivante une image de taille définie __[256, 256, 1]__. 
                
                L’architecture LeNet utilisée  :

                """)
            
            image = Image.open(path + 'summary_lenet.png')
            st.image(image, caption = 'LeNet Summary', width = 800)

        
        with tab2 : #TransferLearning
            st.markdown(
                """ 
                __L’apprentissage par transfert est le phénomène par lequel un nouvel apprentissage est facilité grâce à des apprentissages antérieurs similaires__.
                
                Les modèles existants (__VGG__, __ResNet__, __EfficientNet__) sont composés de deux grandes parties :
                - __Backbone__ : ensemble de convolution permettant l’extraction des features de l’image.
                - __Classification__ : succession de couches denses (_dense layer_) qui ont pour but de classifier.

                Les données du nouveau problème doivent être assez semblables avec le jeu de données utilisé pour le pré-entraînement. Dans ce cas, la méthode de _transfer learning_ consiste à utiliser le backbone d’un modèle pré-entraîné comme extraction de _features_, puis ajouter des couches Dense pour traiter le problème de classification ou régression étudié.

                Dans notre cas d'analyse, le fine-tuning a été utilisé sur tous les modèles de transfer learning étudiés. Le _fine-tuning_ consiste à bloquer les poids de la partie pré-entraînée (_backbone_) puisqu’ils sont proches des poids optimaux.

                Le poids utilisé dans les modèles de _transfer learning_ est le ‘__ImageNet__’. Il consiste d’une grande base des données visuelles conçue pour être utilisée dans la recherche de logiciels de reconnaissance visuelle d’objets. __Il contient plus de 14 millions d’images de haute résolution, étiquetées à environ 20 000 catégories__.
                """)
            
            with st.expander("__Modèle VGG16__") :
                
                st.markdown(
                    """
                    VGG16 est un type de CNN, considéré comme l’un des __meilleurs modèles de computer vision à ce jour__. Les créateurs de ce modèle ont évalué les réseaux et augmenté la profondeur en utilisant une architecture avec de très petits filtres de convolution (3x3), ce qui a montré une amélioration significative par rapport aux configurations de l’état de l’art antérieur. __VGG peut aller en profondeur de 16 à 19 couches, ce qui fait environ 138 paramètres entraînables__.
                    """)
                
                image1 = Image.open(path + 'vgg16_archi_1.png')
                image2 = Image.open(path + 'vgg16_archi_2.png')
                st.image(image1, width = 600)
                st.image(image2, caption = 'Architecture VGG16', width = 600)
                
                st.markdown(
                    """
                    Nous remarquons qu'il y a au total __16 couches__, d'où le nom VGG16. Ces 16 couches peuvent être divisées en blocs convolutifs, séparés par des couches _pooling_. Ces couches _pooling_ réduisent la taille de l'image d'origine qui est de [224x224] pixels par 2. Ainsi, après le premier bloc convolutif, la taille de l'image est réduite à [112x112 pixels]. Vers la fin, on se retrouve avec des images de taille 7x7 uniquement. 
                    La taille du Tensor d’entrée pour le VGG16 est de __[224, 224] avec 3 canaux (RGB)__.
                    """)
            
            with st.expander("__Modèle ResNet__") :
                st.markdown(
                    """
                    ### ResNet152
                    ResNet152 est un autre modèle de CNN largement reconnu et utilisé dans le domaine de la vision par ordinateur. Il a été développé par les chercheurs de _Microsoft Research_ et est considéré comme _l'un des modèles les plus puissants et les plus profonds pour la classification et la détection d'objets__.

                    L'architecture de ResNet152 se distingue par son utilisation de blocs résiduels, d'où son nom "_ResNet_" qui signifie __"réseau résiduel"__. Ces blocs résiduels permettent d'atténuer le problème de la dégradation de la performance des réseaux profonds en facilitant l'apprentissage des représentations résiduelles (écarts entre une prédiction et une cible souhaitée). En d'autres termes, les blocs résiduels permettent d'ajouter de nouvelles couches tout en préservant les informations importantes apprises par les couches précédentes, ce qui facilite l'entraînement de réseaux plus profonds.

                    Le modèle ResNet152 est composé de __152 couches__, ce qui le rend encore plus profond que VGG16. Cette profondeur accrue permet à ResNet152 de capturer des caractéristiques complexes et d'apprendre des représentations plus riches des images. En outre, ResNet152 utilise des filtres de convolution plus grands (par exemple, 3x3, 5x5) dans certains blocs pour améliorer sa capacité à capturer des informations contextuelles à différentes échelles. La taille d'entrée du Tensor pour ResNet152 est également de __[224 x 224] avec 3 canaux (RGB)__, similaire à VGG16.

                    """)

                image = Image.open(path + 'resnet152_archi.png')
                st.image(image, caption = 'Architecture ResNet152', width = 600)

                st.markdown(
                    """
                    ### ResNet101
                    Le modèle ResNet101 est un réseau de neurones à convolution. La principale différence entre ResNet101 et ResNet152 réside dans le nombre de couches que chacun utilise. ResNet101 contient 101 couches, tandis que ResNet152 en a 152, soit 44 millions de paramètres adaptables, pour 60 millions pour le Resnet152 : cela se traduit par une augmentation de la complexité du modèle et de sa capacité à représenter des motifs plus complexes dans les images. 

                    Cependant, cette augmentation de la complexité du modèle peut également entraîner une sur-apprentissage, c'est-à-dire une diminution des performances lorsque le modèle est confronté à de nouvelles données. C'est pourquoi nous avons essayé les 2 modèles pour les comparer et trouver un juste équilibre entre la complexité du modèle et ses performances.
                    """)

                image = Image.open(path + 'resnet101_archi.png')
                st.image(image, caption = 'Architecture ResNet101', width = 600)
                
            
            with st.expander("__Modèle EfficientNetB1__") : 
                    st.markdown(
                    """
                    __L’architecture EfficientNet est réputée pour présenter d’excellentes performances dans les problèmes de classification d’images et pour utiliser peu de ressources lors des calculs__.

                    Il existe différents modèles EfficientNet, adaptés à différents niveaux de résolution d’images. Compte tenu des images que nous disposions en entrée (256 x 256 pour les images masquées), nous avons choisi de tester un modèle EfficientNet B1 et donc une résolution de __[240 x 240 ] avec 3 canaux__ après redimensionnement des images.
                    """)

                    table = pd.DataFrame({'Base Model' : ['EfficientNetB0','EfficientNetB1','EfficientNetB2','EfficientNetB3','EfficientNetB4','EfficientNetB5','EfficientNetB6','EfficientNetB7'], 'Resolution' : [224,240,260,300,380,456,528,600]})
                    st.dataframe(table)
            
            st.markdown(
                """
                #

                #
                
                #
                """)
            
        
        with tab3 : #KerasTuner
            st.markdown(
                """
                ### L’importance du réglage des hyperparamètres
                Le réglage des __hyperparamètres__ (_hyperparameter tuning_) est le processus de recherche d'un ensemble optimal d'hyperparamètres. Il est vraiment difficile de trouver manuellement cet ensemble optimal, il existe donc certains algorithmes qui facilitent notre tuning.

                ___GridSearch___ est un des algorithmes qui effectuent une recherche exhaustive, ce qui prend du temps par nature. Une alternative à cela est l'algorithme de _RandomSearch_ qui recherche de manière aléatoire l’ensemble d’hyperparamètres, mais ne garantit pas une solution globalement optimale.

                Les algorithmes les plus susceptibles de fournir des solutions globalement optimales sont _Bayesian optimization_, _Hyperband_ et _Hyperparameter optimization_ à l'aide d'algorithmes génétiques.
                
                ### La bibliothèque KerasTuner
                Le KerasTuner est une bibliothèque open-source python développée exclusivement pour réaliser de _hyperparameter tunning_ de _Artificial Neural Networks_. Le processus de sélection du bon ensemble d’hyperparamètres pour une application d’apprentissage automatique (ML) est appelé réglage d’hyperparamètres ou hyper-réglages.

                KerasTuner actuellement est disponible pour 4 types de tuners :
                - _Bayesian Optimization_
                - _Hyperband_
                - _Sklearn_
                - _Random Search_

                Les hyperparamètres sont __les variables qui régissent le processus de formation et la topologie d’un modèle ML__. Ces variables restent constantes tout au long du processus de formation et ont un impact direct sur les performances du programme ML. Les hyperparamètres sont de 2 types :

                - __Hyperparamètres de modèle__ : influencent la sélection du modèle, tels que le nombre et la largeur des couches masquées.

                - __Hyperparamètres d’algorithme__ : influencent la vitesse et la qualité de l’algorithme d’apprentissage, tels que le taux d’apprentissage pour _Stochastic Gradient Descent_ (SGD) et le nombre de voisins les plus proches pour un classificateur _KKK_.

                Pour l’étude menée dans cette analyse, nous avons choisis itérer sur un hyperparamètre d’algorithme : le __taux d’apprentissage__ (_learning rate_).

                Un tuner _RandomSearch_ a été instancié pour effectuer l’hypertuning. Ce tuner est ensuite entraîné, en utilisant la méthode _Search_, et combiné avec un callback _EarlyStopping_. Après 3 trials, le modèle converge et désigne un _Adam learning_ rate qui maximise la précision du sous-échantillon de validation. À la suite de cela, nous construisons un nouveau modèle avec cette fois-ci l’hyperparamètre optimal défini précédemment. 
                """)
            
            st.markdown(
                """
                #

                #
                
                #
                """)
            
            
        with tab4 : #Interprétabilité
            st.markdown(
                """
                ### Gradient-Weighted Class Activation Maps (___GradCAM___)
                Pour pouvoir expliquer comment notre modèle CNN réalise ses décisions, il existe ___GradCAM__ Rosebrock (2010)_ pour aider à __visualiser les régions de l’image qui ont le plus contribué au modèle à réaliser ses prédictions__. 
                Il s’agit d’une méthode d'interprétation visuelle utilisée pour localiser les régions importantes d’une image qui ont influencé la décision d’un modèle donné. 

                _GradCAM_ suivra les étapes suivantes dans son processus.
                1. Trouver la couche convolutive finale dans le réseau.
                2. Examiner le gradient qui rentre dans cette couche.
                3. Calcul d’une note d’importance basée sur les gradients et production d’une _heatmap_ qui met en évidence les régions importantes dans l’image en lui attribuant un label. Cette _heatmap_ sera superposée sur l’image d’origine afin de visualiser les régions qui ont influencé la décision du modèle.
                En synthèse, _GradCAM_ utilise des gradients comme poids (_grad-weights_) pour mettre en évidence des régions importantes dans les images et nous permet de voir ce que chaque couche du réseau regarde dans une image d’entrée spécifique. __Les régions de l'image qui ont des valeurs élevées dans la _heatmap_ seront alors considérées comme les régions les plus importantes pour la prédiction de la classe cible__. 

                Dans notre analyse nous avons utilisé le code ___VizGradCam___ de gkeechin. C’est le moyen le plus rapide de visualiser les _GradCAM_ dans de modèles Keras.

                """)