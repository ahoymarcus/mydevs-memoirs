import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Valores de teste para a Matriz de Confusão
y_verdadeiro = np.array([1]*50 + [0]*50) # 50 vezes que "choveu" (1) e 50 que "não choveu" (0)
y_previsoes = np.array([1]*40 + [0]*10 + [1]*15 + [0]*35) # Previsões feitas pelo modelo hipotético


# 1. Calcular a Matriz de Confusão
cm =  confusion_matrix(y_verdadeiro, y_previsoes)
print("Matriz de Confusão: \n", cm)
print("-" * 30)

# 2. Calcular as Métricas
acuracia = accuracy_score(y_verdadeiro, y_previsoes)
sensibilidade = recall_score(y_verdadeiro, y_previsoes)
especificidade = cm[0,0] / (cm[0,0] + cm[0,1]) # Cálculo manual
precisao = precision_score(y_verdadeiro, y_previsoes)
f1 = f1_score(y_verdadeiro, y_previsoes)

print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F1-Score: {f1:.2f}")
print("-" * 30)

# 3. Gerar a Curva ROC
# Para o gráfico, é necessário as probabilidades ou pontuações do modelo
# Simular as probabilidades do modelo
y_probabilidades = np.concatenate([np.random.uniform(0.6, 0.9, 40), # VP: Prob. alta para chuva
                                    np.random.uniform(0.1, 0.4, 10), # FN: Prob. baixa para chuva
                                    np.random.uniform(0.6, 0.9, 15), # FP: Prob. alta para chuva
                                    np.random.uniform(0.1, 0.4, 35)]) # VN: Prob. baixa para chuva

fpr, tpr, thresholds = roc_curve(y_verdadeiro, y_probabilidades)
roc_auc = roc_auc_score(y_verdadeiro, y_probabilidades)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (área = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falso Positivo (1 - Especificidade)')
plt.ylabel('Taxa de Verdadeiro Positivo (Sensibilidade)')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()
















