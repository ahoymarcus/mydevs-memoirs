from PIL import Image
import numpy as np

image_path = 'Lena_512x512_24bit_RGB.png'


try:
    img = Image.open(image_path)
    print(f"Imagem carregada com sucesso! \nImagem: {image_path}, \nFormato: {img.format}, Modo: {img.mode}, Tamanho: {img.size}")
except FileNotFoundError:
    print(f"Erro: Imagem '{image_path}' não encontrada. Verifique o caminho!")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao carregar a imagem: {e}")


# Converter o valor numérico da img para o padrão array Numpy
img_np = np.array(img) 

img_gray_np = np.array(0.2989 * img_np[:, :, 0] +
                       0.5870 * img_np[:, :, 1] +
                       0.1140 * img_np[:, :, 2]).astype(np.uint8)

img_gray_manual = Image.fromarray(img_gray_np, mode='L') # 'L' é o modo para escala de cinza
img_gray_manual.save('lena_512x512_24bit_gray-manual.jpg')
print("Imagem convertida para tons de cinza (manual) e salva como: 'lena_512x512_24bit_gray-manual.png'.")

#Opcional: Exibir a imagem
img_gray_manual.show()


# Definir um Limiar (Threshold) para teste
threshold = 128

img_bw = img_gray_manual.point(lambda x:0 if x < threshold else 255, '1')

img_bw.save('lena_bw.jpg')
print(f"Imagem convertida para preto e branco (limiar={threshold} e salva como 'lena_bw.jpg'.")

# Opcional: Exibir a imagem
img_bw.show()


# Fazer a binarização de forma manual com NumPy
threshold_m = 128

img_bw_np = (img_gray_np > threshold_m).astype(np.uint8) * 255 # Converter para True/False (1 ou 0) e multiplicar por 255
img_bw_manual = Image.fromarray(img_bw_np, mode='L') # Modo '1' para imagens binárias
img_bw_manual.save('lena_512x512_24bit_bw-manual.jpg')
print("Imagem convertida para preto e branco (manual) e salva como 'lena_512x512_24bit_bw-manual.jpg'.")

# Opcional: Exibir a imagem
img_bw_manual.show()










