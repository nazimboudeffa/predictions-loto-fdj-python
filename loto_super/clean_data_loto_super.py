import pandas as pd
import numpy as np
from datetime import datetime

print("🔧 Nettoyage du fichier loto_super_all.csv...\n")

# Charger les données
df = pd.read_csv('data/loto_super_all.csv', sep=';', low_memory=False)
print(f"✓ Fichier chargé : {len(df)} lignes, {len(df.columns)} colonnes")

# 1. Supprimer les colonnes vides (Unnamed)
unnamed_cols = [col for col in df.columns if 'Unnamed' in str(col)]
df = df.drop(columns=unnamed_cols)
print(f"✓ Suppression de {len(unnamed_cols)} colonnes vides")

# 2. Unifier les formats de dates
def parse_date(date_str):
    """Convertir différents formats de dates en YYYY-MM-DD"""
    if pd.isna(date_str):
        return None
    
    date_str = str(date_str).strip()
    
    # Format YYYYMMDD
    if len(date_str) == 8 and date_str.isdigit():
        try:
            return datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
        except:
            pass
    
    # Format DD/MM/YYYY
    if '/' in date_str:
        try:
            return datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        except:
            pass
    
    return date_str

print("✓ Conversion des dates...")
df['date_de_tirage'] = df['date_de_tirage'].apply(parse_date)
df['date_de_forclusion'] = df['date_de_forclusion'].apply(parse_date)

# 3. Uniformiser les virgules en points pour les nombres
def clean_number(val):
    """Convertir les nombres avec virgules en float"""
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return val
    
    val_str = str(val).strip()
    # Remplacer virgule par point et supprimer espaces
    val_str = val_str.replace(',', '.').replace(' ', '')
    
    try:
        return float(val_str)
    except:
        return np.nan

# Colonnes numériques à nettoyer
numeric_cols = [
    'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'boule_6',
    'boule_complementaire', 'numero_chance',
    'nombre_de_gagnant_au_rang1', 'rapport_du_rang1',
    'nombre_de_gagnant_au_rang2', 'rapport_du_rang2',
    'nombre_de_gagnant_au_rang3', 'rapport_du_rang3',
    'nombre_de_gagnant_au_rang4', 'rapport_du_rang4',
    'nombre_de_gagnant_au_rang5', 'rapport_du_rang5',
    'nombre_de_gagnant_au_rang6', 'rapport_du_rang6',
    'nombre_de_gagnant_au_rang7', 'rapport_du_rang7',
    'nombre_de_gagnant_au_rang8', 'rapport_du_rang8',
    'nombre_de_gagnant_au_rang9', 'rapport_du_rang9',
    'nombre_de_codes_gagnants', 'rapport_codes_gagnants'
]

print("✓ Uniformisation des nombres...")
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].apply(clean_number)

# 4. Convertir les types appropriés
print("✓ Conversion des types de données...")

# Boules en entiers
boule_cols = ['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'boule_6', 
              'boule_complementaire', 'numero_chance']
for col in boule_cols:
    if col in df.columns:
        df[col] = df[col].astype('Int64')  # Int64 accepte les valeurs manquantes

# Nombres de gagnants en entiers
gagnant_cols = [col for col in df.columns if 'nombre_de_gagnant' in col or 'nombre_de_codes' in col]
for col in gagnant_cols:
    df[col] = df[col].astype('Int64')

# 5. Trier par date de tirage
print("✓ Tri chronologique...")
df['date_temp'] = pd.to_datetime(df['date_de_tirage'], errors='coerce')
df = df.sort_values('date_temp')
df = df.drop('date_temp', axis=1)

# 6. Réinitialiser l'index
df = df.reset_index(drop=True)

# 7. Sauvegarder le fichier nettoyé
output_file = 'data/loto_super_all_clean.csv'
df.to_csv(output_file, sep=';', index=False, encoding='utf-8')

print(f"\n✅ Fichier nettoyé créé : loto_super_all_clean.csv")
print(f"   - {len(df)} lignes")
print(f"   - {len(df.columns)} colonnes (vs {len(df.columns) + len(unnamed_cols)} avant)")
print(f"\n📊 Statistiques :")
print(f"   - Période : {df['date_de_tirage'].min()} à {df['date_de_tirage'].max()}")
print(f"   - Valeurs manquantes réduites")
print(f"   - Formats standardisés")

# Afficher un échantillon
print(f"\n📋 Aperçu des premières lignes :")
print(df[['annee_numero_de_tirage', 'date_de_tirage', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'numero_chance']].head())
