#importando bibliotecas 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

def DecisionTree(max_depth=None, min_samples_split=2, random_state=42):
    model = DecisionTreeClassifier(
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
    return model

def KNN(n_neighbors=5, weights='uniform'):
    model = KNeighborsClassifier(
        n_neighbors=n_neighbors,
        weights=weights
    )
    return model

def RandomForest(n_estimators=200, max_depth=None, random_state=42):
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )
    return model