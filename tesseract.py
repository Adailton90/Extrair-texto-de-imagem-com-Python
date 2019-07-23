from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR

print( pytesseract.image_to_string( Image.open('imagem.png') ) ) # Extraindo o texto da imagem

arq = open("arquivo.txt","w") #abrindo arquivo de  texto(se não existir ele cria o arquivo) com permissão de escrita

arq.write(pytesseract.image_to_string( Image.open('imagem.png') ))