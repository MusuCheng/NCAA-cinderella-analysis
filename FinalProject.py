# === 1. Import libraries ===
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# === 2. Load dataset ===
df = pd.read_csv("cbb.csv")  # Load the NCAA basketball dataset

# === 3. Filter for postseason teams only ===
df_postseason = df.dropna(subset=["POSTSEASON", "SEED"])  # Keep only teams with postseason result and seed

# === 4. Select relevant performance features for clustering ===
features = [
    "ADJOE", "ADJDE", "EFG_O", "EFG_D", "TOR", "TORD", "ORB", "DRB",
    "FTR", "FTRD", "2P_O", "2P_D", "3P_O", "3P_D", "ADJ_T", "WAB", "SEED"
]  # These are efficiency, rebounding, pace, and shooting-related stats
X = df_postseason[features]  # Extract feature matrix

# === 5. Normalize the features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Standardize the data for clustering

# === 6. Apply KMeans clustering (5 groups) ===
kmeans = KMeans(n_clusters=5, random_state=42)
df_postseason["Cluster"] = kmeans.fit_predict(X_scaled)  # Assign each team to a cluster

# === 7. Calculate mean values of each cluster ===
cluster_features_mean = pd.DataFrame(X, columns=features).copy()
cluster_features_mean["Cluster"] = df_postseason["Cluster"].values
cluster_means = cluster_features_mean.groupby("Cluster").mean()  # Average stats for each cluster

# === 8. Define a radar chart plotting function ===
def plot_radar_chart(df, cluster_id):
    labels = df.columns  # Stat names
    stats = df.loc[cluster_id].values  # Values for a specific cluster
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats = np.concatenate((stats, [stats[0]]))  # Close the radar loop
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, stats, linewidth=2)  # Draw the outline
    ax.fill(angles, stats, alpha=0.25)  # Fill the area
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_title(f"Cluster {cluster_id} Feature Profile", size=14)
    plt.show()

# === 9. Plot radar chart for each cluster ===
for cluster_id in cluster_means.index:
    plot_radar_chart(cluster_means, cluster_id)  # Visualize each cluster's traits

# === 10. Visualize clusters using PCA (2D projection) ===
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)  # Reduce to 2 dimensions

df_postseason["PCA1"] = X_pca[:, 0]
df_postseason["PCA2"] = X_pca[:, 1]

plt.figure(figsize=(10, 7))
sns.scatterplot(data=df_postseason, x="PCA1", y="PCA2", hue="Cluster", palette="Set1", alpha=0.7)
plt.title("PCA Projection of Clusters")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.legend(title="Cluster")
plt.show()

# === 11. Identify Cinderella teams ===
# Criteria: Cluster 0 or 4, SEED >= 10, and made it to E8, F4, or CHMP
cinderella_candidates = df_postseason[
    (df_postseason["Cluster"].isin([0, 4])) &
    (df_postseason["SEED"] >= 10) &
    (df_postseason["POSTSEASON"].isin(["E8", "F4", "CHMP"]))
].copy()

# === 12. Export full feature set of Cinderella teams ===
selected_columns = [
    "TEAM", "YEAR", "SEED", "POSTSEASON", "BARTHAG", "Cluster"
] + features  # Include metadata + all performance metrics

cinderella_detailed = cinderella_candidates[selected_columns]  # Filter final dataframe
print("Cinderella Teams - Full Feature Table:")
print(cinderella_detailed)