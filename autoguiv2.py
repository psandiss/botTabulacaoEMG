import pyautogui
import time

from PIL import Image

#verificar tamanho barra de pesquisa, deve aparecer so pesquisar
#Emg icone 3
#Excel icone 5

def teste():
    pyautogui.moveTo(1659, 927)## Abre icone da EMG precisa ser 3º icone

teste()
pos = pyautogui.position()
print(pos)

pyautogui.moveTo(1659, 927)
#912, 618
def verCor(x,y):
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    im = pyautogui.screenshot()
    px = im.getpixel((x, y))
    #pixelColor = pyautogui.screenshot().getpixel((912, 687))
    print(px)
    return px
#verCor()

def erro():
    #clica no botao pra fechar o erro
    pyautogui.click(1496, 378)

    #abre o excel
    pyautogui.click(474, 1040)
    time.sleep(0.4)
    #avança as celulas

def executar():
    pyautogui.click(352,1047)## Abre icone da EMG precisa ser 3º icone
    pyautogui.click(479,908)## abre a aba da analise
    i=0
    while i < 8:
        i += 1        #verifica se o botao da stabilography ta clicado
        if verCor(706,617) == (0,255,0):
            pyautogui.click(1023, 605)

        pyautogui.click(769, 713)  # clica no run

        # verifica se deu erro no salto
        if verCor(1496, 378) != (25,25,25):
            print("vish")
            erro()

        else:

            pyautogui.click(1659, 927)  # cancelar 1
            time.sleep(0.7)
            pyautogui.click(1659, 927)  # cancelar 2
            time.sleep(1.5)


            pyautogui.moveTo(972, 429)  # começa a arrastar
            pyautogui.mouseDown()
            pyautogui.moveTo(1226, 676)
            pyautogui.mouseUp()  # termina de arrastar
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(1290, 316)  # fecha janelas emg
            pyautogui.click(1631, 188)  # fecha janelas emg
            time.sleep(0.5)

            pyautogui.click(474, 1040)  # abre excel. Sempre deixar no 5 icone
            time.sleep(0.8)
            pyautogui.hotkey('ctrl', 'v')  # cola. Deixar sempre na celula certa

        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        time.sleep(0.5)

        pyautogui.click(352, 1047)  ## Abre icone da EMG precisa ser 3º icone
        time.sleep(0.7)
        pyautogui.click(479, 908)  ## abre a aba daanalise
        time.sleep(0.7)
        pyautogui.click(745, 321)  # load file
        time.sleep(0.7)
        pyautogui.click(975, 345, clicks=2)  # abre diretorio
        time.sleep(0.7)
        pyautogui.click(956, 325)  # seleciona o primeiro arquivo
        pyautogui.press('delete')  # deleta o arquivo
        time.sleep(0.5)
        pyautogui.click(956, 325, clicks=2)  # abre o primeiro arquivo
        time.sleep(1)


executar()
