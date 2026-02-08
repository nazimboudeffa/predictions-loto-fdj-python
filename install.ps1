# Script d'installation rapide pour Windows
# Exécuter avec : .\install.ps1

Write-Host "🎲 Installation de l'environnement Loto Predictions..." -ForegroundColor Cyan

# Vérifier Python
Write-Host "`n1. Vérification de Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "✓ Python trouvé : $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python n'est pas installé ou n'est pas dans le PATH" -ForegroundColor Red
    Write-Host "Téléchargez Python depuis : https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Créer l'environnement virtuel
Write-Host "`n2. Création de l'environnement virtuel..." -ForegroundColor Yellow
if (Test-Path ".venv") {
    Write-Host "✓ .venv existe déjà" -ForegroundColor Green
} else {
    python -m venv .venv
    Write-Host "✓ Environnement virtuel créé" -ForegroundColor Green
}

# Activer l'environnement virtuel
Write-Host "`n3. Activation de l'environnement virtuel..." -ForegroundColor Yellow
.venv\Scripts\Activate.ps1

# Mettre à jour pip
Write-Host "`n4. Mise à jour de pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Installer les dépendances
Write-Host "`n5. Installation des dépendances..." -ForegroundColor Yellow
pip install -r requirements.txt

# Vérification
Write-Host "`n6. Vérification de l'installation..." -ForegroundColor Yellow
$packages = @("pandas", "numpy", "matplotlib", "seaborn", "jupyter")
$allInstalled = $true

foreach ($package in $packages) {
    try {
        python -c "import $package"
        Write-Host "✓ $package installé" -ForegroundColor Green
    } catch {
        Write-Host "✗ $package non installé" -ForegroundColor Red
        $allInstalled = $false
    }
}

# Message final
Write-Host "`n================================================" -ForegroundColor Cyan
if ($allInstalled) {
    Write-Host "✅ Installation terminée avec succès !" -ForegroundColor Green
    Write-Host "`nPour démarrer :" -ForegroundColor Yellow
    Write-Host "  1. Assurez-vous que l'environnement est activé : .venv\Scripts\Activate.ps1"
    Write-Host "  2. Ouvrez un notebook : jupyter notebook"
    Write-Host "     ou utilisez VS Code avec l'extension Jupyter"
    Write-Host "`nPour désactiver l'environnement : deactivate" -ForegroundColor Gray
} else {
    Write-Host "⚠️  Installation partiellement réussie" -ForegroundColor Yellow
    Write-Host "Certains packages n'ont pas pu être installés. Vérifiez les erreurs ci-dessus." -ForegroundColor Yellow
}
Write-Host "================================================`n" -ForegroundColor Cyan
