import pyautogui
import time


#pegando o tamanho da tela
larguraTela, alturaTela = pyautogui.size()

#mostrando o tamaho da tela
print(larguraTela,alturaTela)

#capturando a posição do cursor do mouse
eixoX , eixoY = pyautogui.position()

#mostrando a posição do cursor do mouse
print(eixoX, eixoY)

#movendo o mouse para as coodernadas
pyautogui.moveTo(580,745 , duration=2)

time.sleep(5)

#clicando nessas coordenadas
pyautogui.click(580,745)


time.sleep(5)

#colando o link que está entre parenteses
pyautogui.write('https://github.com/santiagoNogueira66')

time.sleep(5)

#pressionando enter para acessar o link colado 
pyautogui.press('enter')

