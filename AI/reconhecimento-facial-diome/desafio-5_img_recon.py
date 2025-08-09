import cv2
from mtcnn.mtcnn import MTCNN
import matpolotlib.pyplot as plt

# Path da imagem para ser detectada
imagem_original = cv2.imread('./public/<nome-da-imagem>.png')

# Converter a imagem para RGB, para uso com a biblioteca MTCNN
magem_rgb = cv2.cvtColor(imagem_original, cv2Color_BGR2RGB)

detector = MTCNN()
resultados = detector.detect_faces(imagem_rgb)

if resultados:
    print(f"Foram detectados {len(resultados)} rostos(s) na imagem.")

    # Desenhar a Bounding boxes
    x, y, largura, altura = resultados['box']

    # Recortar o rosto para o próximo módulo de ML
    rosto_recortado = imagem_original[y:y+altura, x:x+largura]

    cv2.imwrite(f"rosto_{resultados.index(resultado)}.jpg', rost_recortado)


# Apresentar o resultado
plt.imshow(cv2.cvtColor(imagem_original, cv2COLOR_BGR2RGB))
plt.tile('Detacção de Faces com MTCNN')
plt.axis('off')
plt.show()
























