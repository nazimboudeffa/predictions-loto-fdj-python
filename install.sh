#!/bin/bash
# Script d'installation rapide pour Linux/macOS
# Exécuter avec : bash install.sh ou ./install.sh (après chmod +x install.sh)

echo "🎲 Installation de l'environnement Loto Predictions..."

# Vérifier Python
echo ""
echo "1. Vérification de Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Python trouvé : $PYTHON_VERSION"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo "✓ Python trouvé : $PYTHON_VERSION"
    PYTHON_CMD="python"
else
    echo "✗ Python n'est pas installé"
    echo "Installez Python depuis : https://www.python.org/downloads/"
    exit 1
fi

# Créer l'environnement virtuel
echo ""
echo "2. Création de l'environnement virtuel..."
if [ -d ".venv" ]; then
    echo "✓ .venv existe déjà"
else
    $PYTHON_CMD -m venv .venv
    echo "✓ Environnement virtuel créé"
fi

# Activer l'environnement virtuel
echo ""
echo "3. Activation de l'environnement virtuel..."
source .venv/bin/activate

# Mettre à jour pip
echo ""
echo "4. Mise à jour de pip..."
pip install --upgrade pip

# Installer les dépendances
echo ""
echo "5. Installation des dépendances..."
pip install -r requirements.txt

# Vérification
echo ""
echo "6. Vérification de l'installation..."
PACKAGES=("pandas" "numpy" "matplotlib" "seaborn" "jupyter")
ALL_INSTALLED=true

for package in "${PACKAGES[@]}"; do
    if python -c "import $package" 2>/dev/null; then
        echo "✓ $package installé"
    else
        echo "✗ $package non installé"
        ALL_INSTALLED=false
    fi
done

# Message final
echo ""
echo "================================================"
if [ "$ALL_INSTALLED" = true ]; then
    echo "✅ Installation terminée avec succès !"
    echo ""
    echo "Pour démarrer :"
    echo "  1. Activez l'environnement : source .venv/bin/activate"
    echo "  2. Ouvrez un notebook : jupyter notebook"
    echo "     ou utilisez VS Code avec l'extension Jupyter"
    echo ""
    echo "Pour désactiver l'environnement : deactivate"
else
    echo "⚠️  Installation partiellement réussie"
    echo "Certains packages n'ont pas pu être installés. Vérifiez les erreurs ci-dessus."
fi
echo "================================================"
echo ""
