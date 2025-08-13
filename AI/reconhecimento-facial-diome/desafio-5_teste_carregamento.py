from PIL import Image

try:
    img = Image.open('lloyd.jpg')
    print("Imagem carregada com sucesso!")
    img.close()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
