import pandas as pd
import os

# Chemin vers le dossier loto_euromillions/data
data_folder = r'c:\Users\nboud\Documents\GitHub-My-Projects\predictions-loto-fdj-python\loto_euromillions\data'

# Liste des fichiers à fusionner
files = [
    'euromillions.csv',
    'euromillions_2.csv',
    'euromillions_3.csv',
    'euromillions_4.csv',
    'euromillions_201902.csv',
    'euromillions_202002.csv'
]

# Liste pour stocker tous les dataframes
all_dfs = []

# Lire chaque fichier
for file in files:
    file_path = os.path.join(data_folder, file)
    if os.path.exists(file_path):
        print(f"Lecture de {file}...")
        try:
            df = pd.read_csv(file_path, sep=';', encoding='utf-8', low_memory=False)
        except UnicodeDecodeError:
            # Essayer avec un encodage différent
            df = pd.read_csv(file_path, sep=';', encoding='latin-1', low_memory=False)
        print(f"  - {len(df)} lignes")
        all_dfs.append(df)
    else:
        print(f"Fichier non trouvé : {file}")

# Fusionner tous les dataframes
print("\nFusion des fichiers...")
merged_df = pd.concat(all_dfs, ignore_index=True, sort=False)

# Trier par date (format DD/MM/YYYY ou YYYYMMDD)
try:
    # Convertir la colonne date_de_tirage en datetime
    merged_df['date_temp'] = pd.to_datetime(merged_df['date_de_tirage'], format='%d/%m/%Y', errors='coerce')
    # Si certaines dates sont manquantes, essayer le format YYYYMMDD
    mask = merged_df['date_temp'].isna()
    if mask.any():
        merged_df.loc[mask, 'date_temp'] = pd.to_datetime(merged_df.loc[mask, 'date_de_tirage'], format='%Y%m%d', errors='coerce')
    
    # Trier par date
    merged_df = merged_df.sort_values('date_temp', ascending=True)
    # Supprimer la colonne temporaire
    merged_df = merged_df.drop('date_temp', axis=1)
    print("Tri effectué par date de tirage")
except Exception as e:
    print(f"Impossible de trier par date: {e}")

# Sauvegarder le fichier fusionné
output_file = os.path.join(data_folder, 'loto_euromillions_all.csv')
merged_df.to_csv(output_file, sep=';', index=False, encoding='utf-8')

print(f"\nFichier fusionné créé: loto_euromillions_all.csv")
print(f"Total de {len(merged_df)} lignes")
print(f"Nombre de colonnes: {len(merged_df.columns)}")
