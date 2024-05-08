import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

# generiranje podatkovnih primjera
X = generate_data(500, 1)

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()


km = KMeans(n_clusters=3, init='random', n_init =5 , random_state =0)
km.fit(X)
labels = km.predict(X)

plt.figure()
plt.scatter(X[:,0],X[:,1], c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri K=3')
plt.show()

km = KMeans(n_clusters=6, init='random', n_init =5 , random_state =0)
km.fit(X)
labels = km.predict(X)

plt.figure()
plt.scatter(X[:,0],X[:,1], c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri K=6',)
plt.show()

km = KMeans(n_clusters=2, init='random', n_init =5 , random_state =0)
km.fit(X)
labels = km.predict(X)

plt.figure()
plt.scatter(X[:,0],X[:,1], c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri K=2')
plt.show()






iris = load_iris()
X = iris.data  # Značajke
y_true = iris.target  # Stvarne oznake klasa

# a) Pronalaženje optimalnog broja klastera K pomoću metode lakta
distortions = []
K_range = range(1, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distortions.append(kmeans.inertia_)

# b) Grafički prikaz metode lakta
plt.plot(K_range, distortions, 'bx-')
plt.xlabel('Broj klastera K')
plt.ylabel('Izobličenje')
plt.title('Metoda lakta za pronalaženje optimalnog broja klastera K')
plt.show()

# Odabir optimalnog broja klastera K (npr. na temelju vizualne inspekcije metode lakta)
optimal_K = 3

# c) Primjena algoritma K-srednjih vrijednosti
kmeans = KMeans(n_clusters=optimal_K)
kmeans.fit(X)
y_pred = kmeans.labels_  # Predviđene oznake klastera

# d) Prikaži dobivene klastere pomoću dijagrama raspršenja
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', label='Klasteri')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='o', c='red', s=200, label='Centroidi')
plt.xlabel('Duljina latice')
plt.ylabel('Širina latice')
plt.title('K-srednje vrijednosti clustering rezultat')
plt.legend()
plt.show()

# e) Usporedi dobivene klase s stvarnim vrijednostima i izračunaj točnost klasifikacije
accuracy = accuracy_score(y_true, y_pred)
print("Točnost klasifikacije:", accuracy)
