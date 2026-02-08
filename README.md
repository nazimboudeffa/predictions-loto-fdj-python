# Prédictions Loto - Analyse Historique 🎲🇫🇷

Projet d'analyse statistique des tirages historiques de loteries françaises et européennes (Super Loto, Loto National, EuroMillions) avec génération de suggestions de tirages basées sur l'historique.

## 📊 Vue d'ensemble

Ce projet analyse des décennies de données de loteries pour :
- **Super Loto** : 100 tirages (1996-2025)
- **Loto Normal** : 7,572 tirages sur **50 ans** (1976-2026)
- **EuroMillions** : 1,918 tirages sur **22 ans** (2004-2026)

Chaque loterie dispose de :
- Scripts de fusion des fichiers CSV historiques
- Scripts de nettoyage et standardisation des données
- Notebooks Jupyter interactifs avec analyses statistiques
- 4 stratégies de génération de tirages suggérés

## 🎯 Fonctionnalités

- ✅ Fusion automatique de multiples fichiers CSV historiques
- ✅ Nettoyage et standardisation des données (dates, nombres, types)
- ✅ Analyse de fréquence des numéros et étoiles
- ✅ Visualisations graphiques (distributions, heatmaps)
- ✅ Statistiques descriptives avancées
- ✅ 4 stratégies de prédiction :
  - 🔥 Numéros "chauds" (plus fréquents)
  - ⚖️ Distribution équilibrée
  - 🎲 Pondération par fréquence historique
  - ✨ Mix intelligent (recommandé)

## 📁 Structure du projet

```
predictions-loto-fdj-python/
│
├── .venv/                          # Environnement virtuel Python
│
├── loto_super/                     # Super Loto (100 tirages)
│   ├── data/
│   │   ├── *.csv                   # Fichiers sources
│   │   ├── loto_super_all.csv      # Fichier fusionné
│   │   └── loto_super_all_clean.csv # Fichier nettoyé
│   ├── merge_csv_loto_super.py     # Script de fusion
│   ├── clean_data_loto_super.py    # Script de nettoyage
│   └── analyse_loto_super.ipynb    # Notebook d'analyse
│
├── loto_normal/                    # Loto Normal (7,572 tirages - 50 ans)
│   ├── data/
│   │   ├── *.csv
│   │   ├── loto_normal_all.csv
│   │   └── loto_normal_all_clean.csv
│   ├── merge_csv_loto_normal.py
│   ├── clean_data_loto_normal.py
│   └── analyse_loto_normal.ipynb
│
├── loto_euromillions/              # EuroMillions (1,918 tirages - 22 ans)
│   ├── data/
│   │   ├── *.csv
│   │   ├── loto_euromillions_all.csv
│   │   └── loto_euromillions_all_clean.csv
│   ├── merge_csv_loto_euromillions.py
│   ├── clean_data_loto_euromillions.py
│   └── analyse_loto_euromillions.ipynb
│
├── docs/                           # Documentation
│   └── strategies-generation-tirages.md  # Guide des stratégies
│
└── README.md                       # Ce fichier
```

## 🛠️ Prérequis

- **Python 3.13.2** ou supérieur
- **Système d'exploitation** : Windows, macOS, ou Linux
- **Espace disque** : ~50 MB pour l'environnement virtuel + données

## 📦 Installation

### Étape 1 : Cloner le projet (si depuis Git)

```bash
git clone <url-du-projet>
cd predictions-loto-fdj-python
```

### Étape 2 : Créer l'environnement virtuel

**Sur Windows (PowerShell) :**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Sur Windows (CMD) :**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Sur macOS/Linux :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Étape 3 : Installer les dépendances

Une fois l'environnement virtuel activé, installer les bibliothèques nécessaires :

```bash
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn jupyter ipykernel
```

**Liste complète des dépendances :**
- `pandas` : Manipulation de données CSV
- `numpy` : Calculs numériques
- `matplotlib` : Visualisations graphiques
- `seaborn` : Visualisations statistiques avancées
- `jupyter` : Interface pour les notebooks
- `ipykernel` : Noyau Python pour Jupyter

### Étape 4 : Enregistrer le kernel Jupyter (optionnel)

Pour utiliser l'environnement dans VS Code ou Jupyter Lab :

```bash
python -m ipykernel install --user --name=loto-predictions --display-name "Loto Predictions"
```

## 🚀 Utilisation

### Option 1 : Utiliser les fichiers nettoyés existants

Les fichiers `*_all_clean.csv` sont déjà prêts. Ouvrez directement les notebooks :

1. Ouvrir VS Code dans le dossier du projet
2. Ouvrir un notebook (ex: `loto_euromillions/analyse_loto_euromillions.ipynb`)
3. Sélectionner le kernel `.venv (Python 3.13.2)`
4. Exécuter les cellules avec `Shift + Enter`

### Option 2 : Régénérer les fichiers depuis les sources

#### A. Fusionner les fichiers sources

**Super Loto :**
```bash
cd loto_super
python merge_csv_loto_super.py
```

**Loto Normal :**
```bash
cd loto_normal
python merge_csv_loto_normal.py
```

**EuroMillions :**
```bash
cd loto_euromillions
python merge_csv_loto_euromillions.py
```

#### B. Nettoyer les données

**Super Loto :**
```bash
cd loto_super
python clean_data_loto_super.py
```

**Loto Normal :**
```bash
cd loto_normal
python clean_data_loto_normal.py
```

**EuroMillions :**
```bash
cd loto_euromillions
python clean_data_loto_euromillions.py
```

#### C. Exécuter les notebooks

**Depuis VS Code :**
1. Ouvrir le fichier `.ipynb`
2. Sélectionner le kernel Python
3. Cliquer sur "Run All" ou exécuter cellule par cellule

**Depuis Jupyter Lab/Notebook :**
```bash
jupyter notebook
# Puis naviguer vers le notebook souhaité
```

## 📈 Résultats des analyses

### Super Loto
- **100 tirages** analysés (1996-2025)
- Format : 5 numéros (1-49) + 1 numéro chance (1-10)
- Visualisations : Distributions, Top 10 numéros

### Loto Normal
- **7,572 tirages** sur **50 ANS** ! (1976-2026)
- Format : 5 numéros (1-49) + 1 numéro chance (1-10)
- **37,860 numéros** analysés au total
- Tendances historiques sur un demi-siècle

### EuroMillions
- **1,918 tirages** sur **22 ans** (2004-2026)
- Format : 5 numéros (1-50) + 2 étoiles (1-12)
- **9,590 numéros** et **3,583 étoiles** analysés
- Données trans-européennes

## 🎲 Stratégies de tirage

Chaque notebook propose 4 stratégies :

1. **🔥 Numéros chauds** : Les plus fréquents historiquement
2. **⚖️ Équilibré** : Distribution uniforme sur toutes les zones
3. **🎲 Pondéré** : Probabilité proportionnelle aux fréquences
4. **✨ Mix intelligent** : Combinaison de fréquence et variété (recommandé)

📖 **Pour une explication détaillée de chaque stratégie** (algorithmes, avantages/inconvénients, exemples de code), consultez la [documentation complète des stratégies](docs/strategies-generation-tirages.md).

## ⚠️ Disclaimer important

**L'ensemble des loteries sont des jeux de hasard pur.** Les analyses statistiques de ce projet sont :
- À but **éducatif et illustratif uniquement**
- **N'améliorent PAS** vos chances de gagner
- Chaque tirage est **totalement indépendant** des précédents
- Les probabilités restent **extrêmement faibles** :
  - Loto : ~1 sur 19 millions
  - EuroMillions : ~1 sur 140 millions
  
**Jouez de manière responsable.** Ce projet analyse le passé, il ne prédit pas l'avenir.

## 🔧 Dépannage

### Erreur : "No module named 'pandas'"
```bash
# Vérifier que l'environnement virtuel est activé
# Réinstaller les dépendances
pip install pandas numpy matplotlib seaborn
```

### Erreur : "UnicodeDecodeError"
Les scripts gèrent automatiquement l'encodage UTF-8 et latin-1. Si l'erreur persiste, vérifier l'encodage de vos fichiers CSV sources.

### Problème avec Jupyter dans VS Code
1. Installer l'extension "Jupyter" dans VS Code
2. Recharger la fenêtre (`Ctrl + Shift + P` > "Reload Window")
3. Sélectionner le kernel `.venv`

### Erreur de chemin (PathNotFound)
Toujours exécuter les scripts depuis leur dossier parent :
```bash
cd loto_super
python merge_csv_loto_super.py
```

## 📝 Notes techniques

### Nettoyage des données
- Dates unifiées au format `YYYY-MM-DD`
- Nombres avec points décimaux (pas de virgules)
- Colonnes vides supprimées automatiquement
- Types optimisés (`Int64` pour gérer les valeurs manquantes)
- Tri chronologique systématique

### Formats de fichiers
- **Séparateur** : `;` (point-virgule)
- **Encodage** : UTF-8 (avec fallback latin-1)
- **Format de sortie** : CSV standard

### Performance
- Fusion : < 5 secondes
- Nettoyage : < 10 secondes
- Notebooks : 30-60 secondes pour exécution complète

## 🤝 Contribution

Ce projet est personnel et éducatif. Pour toute suggestion ou amélioration :
1. Forker le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commiter les changements (`git commit -m 'Ajout de...'`)
4. Pousser la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est à usage éducatif. Les données de tirages proviennent de sources publiques.

## 🙏 Remerciements

- Données historiques fournies par la Française des Jeux (FDJ)
- EuroMillions pour les données européennes
- Communauté Python pour les excellentes bibliothèques open-source

---

**Bon courage avec vos analyses de loterie !** 🍀

*Rappel : Jouez de manière responsable. Ce projet n'augmente pas vos chances de gagner.*
