<p align="center">
  <a href="URL">
    <img src="https://github.com/NationalSecurityAgency/fractalrabbit/blob/master/resources/Rabbit-CreativeCommonsImage..jpg" alt="" width=370 height=247>
  </a>

  <h3 align="center">FRACTALRABBIT</h3>
<p>
In modelling a sequence of adaptive choices by an intelligent agent (e.g. places visited, web sites browsed), memory-less random walks are unsuitable, because of the formation of agent habits and preferences. 
 </p>

<p>
 Often these choices are only partially observed, and report times are sporadic and bursty, in contrast to regular or exponentially spaced times in classical models. 
</p>

<p>
The FRACTALRABBIT stochastic mobility simulator creates realistic synthetic sporadic waypoint data sets. It consist of three tiers, each based on new stochastic models: </p>

  <p align="center">	
	 (1) An Agoraphobic Point Process generates a set V of space points, whose limit is a random fractal, representing sites that could be visited. </p>

  <p align="center">	(2) A Retro-preferential Process generates a trajectory X through V , with strategic homing and self-reinforcing site ﬁdelity as observed in human/animal behavior. </p>

  <p align="center">	 (3) A Sporadic Reporting Process models time points T at which the trajectory X is observed, with bursts of reports and heavy tailed inter-event times.</p>
  </p>
</p>
<p>
 FRACTALRABBIT can be used to test algorithms applicable to sporadic waypoint data, such as (1) co-travel mining, (2) anomaly detection, and (3) extraction of maximal self-consistent subsets of corrupted data.
<p>
<p>
Reference: R. W. R. Darling, "Retro-preferential Stochastic Mobility Models on Random Fractals Under Sporadic Observations", 
<a href = "https://www.researchgate.net/publication/340741639_Retro-preferential_Stochastic_Mobility_Models_on_Random_Fractals_Under_Sporadic_Observations">DOI: 10.13140/RG.2.2.15267.40489</a>, 2018
<p>

<br>

## Explication du fonctionnement (FR seulement)
# Compilation
Utiliser la commande mvn install package, puis modifier pour avoir Main-Class: fractalRabbitGenerator.MainClassFR, sinon le programme plantera pour chercher main.MainClassFR et enfin relancer avec un mvn clean package, le binaire sera prêt.

# FractalRabbit

FractalRabbit est un simulateur stochastique de mobilité qui génère des ensembles de données synthétiques réalistes de points de cheminement sporadiques.

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure des fichiers de sortie](#structure-des-fichiers-de-sortie)
- [Interprétation des données](#interprétation-des-données)
- [Relation entre les fichiers](#relation-entre-les-fichiers)
- [Utilisation des paramètres](#utilisation-des-paramètres)
- [Exploitation des résultats](#exploitation-des-résultats)

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-nom-utilisateur/fractalrabbit.git
   ```
2. Accédez au répertoire du projet :
   ```
   cd fractalrabbit
   ```

## Utilisation

Exécutez FractalRabbit avec la commande suivante :

```
java -jar target/fractalrabbit-1.0-jar-with-dependencies.jar parameters.csv output.csv
```

## Structure des fichiers de sortie

### output.csvXY.csv

Ce fichier contient les coordonnées X et Y des points de trajectoire simulés.

- **ID**: Identifiant du voyageur (simulé)
- **Days**: Temps écoulé (en jours) depuis le début de la simulation
- **x(km)**: Coordonnée X du point (en kilomètres)
- **y(km)**: Coordonnée Y du point (en kilomètres)

### output.csvPLACES.csv

Ce fichier contient l'identifiant des lieux visités par chaque voyageur.

- **Traveler ID**: Identifiant du voyageur
- **Days**: Temps écoulé (en jours)
- **Place ID**: Identifiant du lieu visité

## Interprétation des données

### output.csvXY.csv

- Chaque ligne représente un point de la trajectoire d'un voyageur à un moment donné.
- Exemple : la première ligne indique que le voyageur 0, après 80.65 jours, se trouve aux coordonnées (120.41, -24.62).
- Les coordonnées sont exprimées en kilomètres.
- La position des points de trajectoire varie avec le temps.

### output.csvPLACES.csv

- Chaque ligne représente une visite à un lieu spécifique.
- Exemple : la première ligne indique que le voyageur 0, après 80.65 jours, visite le lieu 59.
- Les lieux sont représentés par des identifiants numériques.
- La même position peut être visitée à différents jours.
- La simulation s'effectue sur 365 jours.

## Relation entre les fichiers

Les deux fichiers sont liés par les colonnes ID (dans output.csvXY.csv) et Traveler ID (dans output.csvPLACES.csv), ainsi que par la colonne Days. Ces informations permettent de reconstruire la trajectoire complète de chaque voyageur en associant les coordonnées X et Y aux lieux visités à des moments spécifiques.

## Utilisation des paramètres

Le fichier `parameters.csv` contrôle divers aspects de la simulation :

- **d = 10**: Dimension de l'espace de simulation
- **h = 0.5**: Fréquence de retour aux lieux déjà visités
- **n = 100**: Nombre total d'emplacements potentiels
- **numTravelers = 5**: Nombre de voyageurs simulés
- **numCoTravelers = 2**: Taille des groupes de voyageurs
- **days = 365.25**: Durée de la simulation (en jours)
- **countMean = 2.5**: Nombre moyen de rapports de localisation par jour

## Exploitation des résultats

### Visualisation

- Utilisez Kepler.gl pour visualiser les données de trajectoire.
- Importez les deux fichiers CSV dans Kepler.gl.
- Configurez l'affichage des points de trajectoire et des lieux visités.
- Créez des animations pour visualiser les déplacements au fil du temps.

### Analyse des trajectoires

- Calculez des statistiques : distance parcourue, vitesse moyenne, lieux les plus visités.
- Identifiez des motifs de déplacement et des regroupements de voyageurs.

### Exploration des paramètres

Modifiez les paramètres dans `parameters.csv` et relancez la simulation pour observer les changements dans les résultats.

### Exemple d'analyse concrète

1. Identifiez les lieux préférés de chaque voyageur.
2. Calculez la distance totale parcourue par voyageur.
3. Analysez la saisonnalité des déplacements sur de longues périodes.


## Table of contents

- [Status](#status)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Status
Java version runs from the command line:
<p>
	java -jar fractalrabbit.jar parameters.csv outputfilename.csv</p>
<p>	
An example of the parameters.csv file is provided in the resources folder.
Change it to suit your modelling needs. 
It permits multiple travellers to follow the same trajectory asynchronously.
</p>	

## Bugs and feature requests
- Have a bug or a feature request? Contact Github user bbux-atg

## Documentation
- See <a href="https://github.com/NationalSecurityAgency/fractalrabbit/wiki">Wiki</a>. 

## Contributing
- New implementations of the three underlying models described in the technical report are welcome.

## Creators

**R. W. R. Darling**
<a href=https://sites.google.com/view/probabilist-us/home>bio</a>
Github: probabilist-us

## Copyright and license

Apache License 2.0
