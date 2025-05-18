#importando bibliotecas 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


#Criando funcoes de modelos de classificação para serem utilizados em outros arquivos caso necessario chama-los depois.
def Decisiontree():
    model = DecisionTreeClassifier()
    return model

def KNN():
    model = KNeighborsClassifier()
    return model

def RandomForest():
    model = RandomForestClassifier()
    return model