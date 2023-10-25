# Modèle de deep learning pour la détection de problèmes pulmonaires liés au COVID sur des radiographies
La COVID-19 est un syndrome respiratoire aigu qui a été désigné comme une pandémie mondiale par l'Organisation mondiale de la santé.
Les principaux symptômes de la COVID-19 comprennent principalement une fièvre, une toux, une dyspnée et la présence d’infiltrats bilatéraux à l’imagerie. Les cas graves de la maladie peuvent entraîner un syndrome de détresse respiratoire aiguë ou une insuffisance respiratoire complète, nécessitant une assistance ventilatoire mécanique et des soins intensifs en unité de soins intensifs. Les individus immunodéprimés et âgés sont les plus susceptibles de développer des formes graves de la maladie, allant de l’insuffisance cardiaque et rénale jusqu’au choc septique.
Les radiographies pulmonaires sont plus souvent utilisées comme premier outil de dépistage car elles sont plus simples, rapides et moins coûteux que les scanners. Les stades précoces de la COVID-19 présentent des signes caractéristiques tels que des opacités bilatérales multifocales, principalement dans les lobes pulmonaires inférieurs, tandis qu'elles évoluent vers une fibrose pulmonaire à un stade tardif. Cependant, ces signes peuvent également être similaires à ceux d'une pneumonie virale et d'autres infections pulmonaires.

L'analyse des radiographies pulmonaires dans le contexte de la COVID-19 est une application importante en data science. Elle permet de développer des modèles capables de détecter et de classifier les anomalies pulmonaires liées à la COVID-19, ce qui peut contribuer à accélérer le processus de diagnostic et à aider le corps médical à prendre des décisions éclairées, en complément d'autres tests.
C'est pourquoi, à l'aide de 3 camarades, nous avons étudier un dataset de 21.000 radiographiques afin de faire une étude croisée de divers modèles sur leurs capacités à prédire l'état pathologique ou non du patient.



Ce dépôt contient un modèle de deep learning entraîné pour la détection des problèmes pulmonaires liés au COVID sur des radiographies. Le modèle est capable de reconnaître les images de radiographies pulmonaires normales ainsi que les radiographies masquées.

Ce projet est un projet d'étude lié à notre formation chez [DataScientest](https://datascientest.com/)

### Contenu:

Ce dépôt est divisé en trois parties principales :



- Partie données : Cette partie contient les données utilisées pour entraîner le modèle, y compris les images de radiographies pulmonaires normales et masquées.



- Partie Notebook : Cette partie contient les notebooks Jupyter utilisés pour préparer et entraîner le modèle.



- Partie Streamlit : Cette partie contient les codes nécessaires pour lancer l'application Streamlit qui permet de visualiser les résultats du modèle.



### Utilisation

Pour utiliser ce modèle, voici les étapes à suivre :


Clonez le dépôt sur votre machine locale.
```
git clone https://github.com/votre_nom_de_compte/nom_du_depot.git
```


Installez toutes les dépendances requises. Les dépendances sont répertoriées dans le fichier requirements.txt.
```
pip install -r requirements.txt
```


Lancez l'application Streamlit.
```
    streamlit run app.py
```


### Crédits

Ces modèles ont été développés par Benjamin Hind Joao et Nina, et sont basés sur le COVID-19_Radiography_Dataset de Université du Qatar. Si vous utilisez ces modèles dans votre travail de recherche, veuillez citer cette source.
