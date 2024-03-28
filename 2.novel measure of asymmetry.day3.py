import numpy as np
from scipy.stats import skew, kurtosis

def asymmetry_measure(data):
    skewness = skew(data)
    kurt = kurtosis(data)
    tail_behavior = np.percentile(data, 90) - np.percentile(data, 10)
    w_skewness = 0.5
    w_kurtosis = 0.3
    w_tail_behavior = 0.2
    asymmetry = w_skewness * skewness + w_kurtosis * kurt + w_tail_behavior * tail_behavior
    return asymmetry
gene_expression_data = np.random.normal(loc=0, scale=1, size=1000)
asymmetry = asymmetry_measure(gene_expression_data)
print("Asymmetry measure:", asymmetry)

# 2
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from scipy.stats import zscore
np.random.seed(0)
num_genes = 1000
num_samples = 100
genes = [f'Gene_{i}' for i in range(num_genes)]
tissues = ['Tissue_A', 'Tissue_B', 'Tissue_C']
data = pd.DataFrame(np.random.randn(num_samples, num_genes), columns=genes)
data['Tissue'] = np.random.choice(tissues, num_samples)
kmeans = KMeans(n_clusters=3, random_state=0)
clusters_original = kmeans.fit_predict(data.iloc[:, :-1])
silhouette_original = silhouette_score(data.iloc[:, :-1], clusters_original)
print("Silhouette Score (Original Data):", silhouette_original)
data_transformed = data.iloc[:, :-1].apply(zscore)
clusters_transformed = kmeans.fit_predict(data_transformed)
silhouette_transformed = silhouette_score(data_transformed, clusters_transformed)
print("Silhouette Score (Transformed Data - Z-score Normalization):", silhouette_transformed)
pca_original = PCA(n_components=2)
pca_transformed = PCA(n_components=2)
pca_original.fit(data.iloc[:, :-1])
pca_transformed.fit(data_transformed)
pca_original_result = pca_original.transform(data.iloc[:, :-1])
pca_transformed_result = pca_transformed.transform(data_transformed)
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(pca_original_result[:, 0], pca_original_result[:, 1], c=clusters_original, cmap='viridis')
plt.title('PCA on Original Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.subplot(1, 2, 2)
plt.scatter(pca_transformed_result[:, 0], pca_transformed_result[:, 1], c=clusters_transformed, cmap='viridis')
plt.title('PCA on Transformed Data (Z-score Normalization)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.tight_layout()
plt.show()
