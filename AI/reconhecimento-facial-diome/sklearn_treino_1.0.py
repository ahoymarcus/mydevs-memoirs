import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib


# Carregar os embeddings e os rótulos salvos
x = np.load('embeddings.npy')
y = np.load('labels.npy')


# Codificar os rótulos de texto para números (ex: 'c1' -> 0, 'c2' -> 1)# Passo necessário para a maioria dos classificadores do scikit-learn
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Dividir dados: Treinamento e Teste
# 80% para Treino, e 20% para Teste
x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

# Inicializar e Treinar o modelo SVM
print("Treinando o classificador SVM...")
model = SVC(kernel='linear', probability=True)
model.fit(x_train, y_train)
print("Treinamento concluído!")

# Avaliar o desempenho do modelo nos dados de teste
print("Avaliando o modelo...")
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy * 100:.2f}%')


# Gravar o modelo treinado para uso   
joblib.dump(model, 'face_classifier.pkl')
joblib.dump(encoder, 'label_encoder.pkl')
print("Modelo e encoder salvos como 'face_classifier.pkl' e 'label_encoder.pkl'.")


































