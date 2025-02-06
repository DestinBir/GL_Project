# Projet Python 3.12

Bienvenue dans ce projet collaboratif en **Python 3.12** ! Ce guide vous aidera à configurer votre environnement de développement et à bien démarrer.

## 📌 Prérequis

Avant de commencer, assurez-vous d’avoir installé :
- **Python 3.12** ([Télécharger ici](https://www.python.org/downloads/))
- **Git** ([Télécharger ici](https://git-scm.com/downloads))

## 🚀 Installation et Configuration

### 1️⃣ Cloner le projet
Ouvrez un terminal et exécutez :
```bash
git clone <URL_DU_REPO>
cd <NOM_DU_PROJET>
```

### 2️⃣ Créer un environnement virtuel

#### Windows :
```bash
python -m venv env
venv\Scripts\activate
```

#### macOS & Linux :
```bash
python -m venv env
source venv/bin/activate
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer le projet
Utilisez votre editeur de code, de préférence VSCode. Et après ouverture, entre dans le terminal de VSCode et activer l'environnement. 
Et exécuter le reste des commandes là bas.

## 📦 Gestion des dépendances
Si vous ajoutez de nouvelles dépendances, après installation avec `pip install`, mettez à jour le fichier `requirements.txt` :
```bash
pip freeze > requirements.txt
```

## ✅ Contribution
1. **Créer une branche** pour votre fonctionnalité :
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
2. **Faire vos modifications** et les ajouter :
   ```bash
   git add .
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
3. **Pousser votre branche** :
   ```bash
   git push origin feature/ma-fonctionnalite
   ```
4. **Créer une Pull Request (PR)** sur GitHub et demander une revue.

## 🛠 Problèmes & Support
En cas de difficulté, partagez votre problème dans le groupe de discussion.

---
📢 **Restons organisés et efficaces !** 🚀

