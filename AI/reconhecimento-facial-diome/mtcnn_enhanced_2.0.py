from mtcnn import MTCNN
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from PIL import Image
import numpy as np


# Criar instância do detector
detector = MTCNN(device="CPU:0")

# Carregar uma imagem e Converter para o padrão NumPy de MTCNN
pil_image = Image.open("lloyd.jpg")
image = np.asarray(pil_image)

result = detector.detect_faces(image)


# Criar um figura e eixos para plotar a imagem
plt.figure(figsize=(10, 10))
plt.imshow(image)
ax = plt.gca()

# Iterar sobre cada resultado de detecção de rosto
for face in result:
    # Obter dados da caixa delimitadora e dos pontos de ref.
    x, y, width, height = face['box']
    keypoints = face['keypoints']

    # Desenhar o retângulo ao redor do rosto
    rect = Rectangle((x, y), width, height, fill=False, color='red', linewidth=2)
    ax.add_patch(rect)

    # Desenhar os pontos de ref. (Olhos, nariz, boca, etc.)
    for point in keypoints:
        circle = Circle(keypoints[point], radius=5, color='green')
        ax.add_patch(circle)


# Salvar a img de resultado
plt.savefig('lloyd_com_deteccao.jpg')

plt.show()






print(result)






























