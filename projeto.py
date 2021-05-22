from itertools import product
from PIL import Image
import numpy as np
import os

class PixelImagem(object):
    def __init__(self, pixelX, pixelY):
        self.pixelX = pixelX
        self.pixelY = pixelY

def abrindoImagemEscolhida(nomeDaImagem):
    return Image.open(nomeDaImagem)

def convertendoImagemEmEscalaCinza(imagem):
    return imagem.convert('L')

def aplicarLimiarizacaoNaImagem(imagem):
    imagem = convertendoImagemEmEscalaCinza(imagem)
    matrizDePixelsDaImagem = imagem.load()

    for x in range(imagem.width):
        for y in range(imagem.height):
            if matrizDePixelsDaImagem[x, y] >= 100:
                matrizDePixelsDaImagem[x, y] = 255
            else:
                matrizDePixelsDaImagem[x, y] = 0
    return imagem

def aplicarDilatacaoNaImagem(imagem):
    listaDePixelsParaPintar = []
    matrizDePixelsDaImagemBinarizada = imagem.load()
    larguraMatrizDePixels, alturaMatrizDePixels = imagem.size

    for y, x in product(range(alturaMatrizDePixels-1), range(larguraMatrizDePixels-1)):
        if x > 0 and y > 0:
            if matrizDePixelsDaImagemBinarizada[x-1, y] == 255 or matrizDePixelsDaImagemBinarizada[x+1, y] == 255 or matrizDePixelsDaImagemBinarizada[x, y+1] == 255 or matrizDePixelsDaImagemBinarizada[x, y-1] == 255:
                listaDePixelsParaPintar.append(PixelImagem(x, y))
    for pixel in listaDePixelsParaPintar:
        matrizDePixelsDaImagemBinarizada[pixel.pixelX, pixel.pixelY] = 255
    return imagem

def aplicarErosaoNaImagem(imagem):
    listaDePixelsParaPintar = []
    matrizDePixelsDaImagemBinarizada = imagem.load()
    larguraMatrizDePixels, alturaMatrizDePixels = imagem.size

    for y, x in product(range(alturaMatrizDePixels-1), range(larguraMatrizDePixels-1)):
        if x > 0 and y > 0:
            if matrizDePixelsDaImagemBinarizada[x-1, y] == 255 and matrizDePixelsDaImagemBinarizada[x+1, y] == 255 and matrizDePixelsDaImagemBinarizada[x, y+1] == 255 and matrizDePixelsDaImagemBinarizada[x, y-1] == 255:
                listaDePixelsParaPintar.append(PixelImagem(x, y))
    for y, x in product(range(alturaMatrizDePixels), range(larguraMatrizDePixels)):
        matrizDePixelsDaImagemBinarizada[x, y] = 0
    for pixel in listaDePixelsParaPintar:
        matrizDePixelsDaImagemBinarizada[pixel.pixelX, pixel.pixelY] = 255
    return imagem

def abertura(imagem):
    imagem = aplicarErosaoNaImagem(imagem)
    imagem = aplicarDilatacaoNaImagem(imagem)
    return imagem

def fechamento(imagem):
    imagem = aplicarDilatacaoNaImagem(imagem)
    imagem = aplicarErosaoNaImagem(imagem)
    return imagem

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    nomeDaImagem = "imagens/" + input("Digite o nome da imagem (com sua extensão):\n")
    opcao = input("Escolha uma opcao:\n"
                  + "1 - Aplicar Limiarização na imagem\n"
                  + "2 - Aplicar Dilatação na imagem\n"
                  + "3 - Aplicar Erosão na imagem\n"
                  + "4 - Fazer Abertura da imagem\n"
                  + "5 - Fazer Fechamento da imagem\n")
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        imagem = abrindoImagemEscolhida(nomeDaImagem)
    except:
        input("Não existem imagem disponível com esse nome... Pressione Enter para tentar de novo!")
        menu()

    if opcao == '1':
        imagem.show()
        imagem = convertendoImagemEmEscalaCinza(imagem)
        imagem.show()
        imagem = aplicarLimiarizacaoNaImagem(imagem)
    elif opcao == '2':
        imagem.show()
        imagem = aplicarLimiarizacaoNaImagem(imagem)
        imagem.show()
        imagem = aplicarDilatacaoNaImagem(imagem)
    elif opcao == '3':
        imagem.show()
        imagem = aplicarLimiarizacaoNaImagem(imagem)
        imagem.show()
        imagem = aplicarErosaoNaImagem(imagem)
    elif opcao == '4':
        imagem.show()
        imagem = aplicarLimiarizacaoNaImagem(imagem)
        imagem.show()
        imagem = abertura(imagem)
    elif opcao == '5':
        imagem.show()
        imagem = aplicarLimiarizacaoNaImagem(imagem)
        imagem.show()
        imagem = fechamento(imagem)
    else:
        input("Opção inválida... Pressione Enter para tentar de novo!")
    imagem.show()
    menu()

menu()