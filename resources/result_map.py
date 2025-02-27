import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import time  # Juste pour simuler le calcul du graphique

print("[INFO] Chargement des fichiers CSV...")

# Charger les fichiers CSV contenant les données
df1 = pd.read_csv('outputPLACES.csv')  # Contient Traveler ID, Days, Place ID
df2 = pd.read_csv('outputXY.csv')      # Contient ID, Days, x(km), y(km)

print(f"[INFO] outputPLACES.csv chargé avec {df1.shape[0]} lignes et {df1.shape[1]} colonnes")
print(f"[INFO] outputXY.csv chargé avec {df2.shape[0]} lignes et {df2.shape[1]} colonnes")

# Fusionner les deux datasets basés sur 'Traveler ID' et 'ID'
print("[INFO] Fusion des datasets...")
merged_df = pd.merge(df1, df2, left_on='Traveler ID', right_on='ID')

print(f"[INFO] Fusion effectuée : {merged_df.shape[0]} lignes résultantes")

# Vérification rapide des premières lignes du dataset fusionné
print("[INFO] Aperçu des premières lignes des données fusionnées :")
print(merged_df.head())

# Plotting
print("[INFO] Génération du graphique...")

plt.figure(figsize=(10, 6))

# Création de la barre de progression
num_points = len(merged_df)
progress_bar = tqdm(total=num_points, desc="[INFO] Progression du tracé", unit="points")

# Tracé avec mise à jour de la barre de progression
for i in range(num_points):
    sns.scatterplot(x=[merged_df.loc[i, 'x(km)']], 
                    y=[merged_df.loc[i, 'y(km)']], 
                    hue=[merged_df.loc[i, 'Traveler ID']], 
                    palette='viridis', 
                    s=100)
    progress_bar.update(1)
    time.sleep(0.01)  # Simule un calcul (peut être supprimé)

progress_bar.close()

plt.title('Traveler Locations based on Days and Coordinates')
plt.xlabel('X (km)')
plt.ylabel('Y (km)')
plt.legend(title='Traveler ID')
plt.grid(True)

print("[INFO] Affichage du graphique...")
plt.show()
print("[INFO] Script terminé avec succès.")
