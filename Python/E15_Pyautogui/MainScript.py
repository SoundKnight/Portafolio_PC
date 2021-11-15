# ---<=> INTEGRANTES <=>---
# Ibrahim Zavala Hernandez
# Julio Gerardo Cazarez Gonzalez
# Pedro Saldaña Vazquez

# ---<=> MODULOS <=>---
import os
import time
import pyautogui
import random

# ---<=> VARIABLES <=>---
i = 0
j = 0
k = 0
l = 0
n = 1
t = 10

# ---<=> FUNCIONES <=>---
def Limpieza():
    os.system('cls')

# ---<=> PROCESOS <=>---
if __name__ == '__main__':
    print('Iniciando Script en:')
    while t > 0:
        print(t)
        time.sleep(1)
        t -= 1 
    
    Limpieza()

    file = open('refranes.txt', 'r')
    for linea in file:
        while True:
            i = random.randrange(1, 5)
            if i != j:
                break

        if i == 1:
            pyautogui.click(x = 336, y = 440, clicks = 2)
            print(i)
        elif i == 2:
            pyautogui.click(x = 336, y = 586, clicks = 2)
            print(i)
        elif i == 3:
            pyautogui.click(x = 336, y = 524, clicks = 2)
            print(i)
        elif i == 4:
            pyautogui.click(x = 336, y = 564, clicks = 2)
            print(i)
        
        while True:
            k = random.randrange(1, 13)
            if k != l:
                break

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(linea)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.click(x = 656, y = 252, clicks = 1)

        if k == 1:
            pyautogui.click(x = 487, y = 292, clicks = 1)
            print(k)
        elif k == 2:
            pyautogui.click(x = 487, y = 328, clicks = 1)
            print(k)
        elif k == 3:
            pyautogui.click(x = 487, y = 367, clicks = 1)
            print(k)
        elif k == 4:
            pyautogui.click(x = 487, y = 407, clicks = 1)
            print(k)
        elif k == 5:
            pyautogui.click(x = 487, y = 450, clicks = 1)
            print(k)
        elif k == 6:
            pyautogui.click(x = 487, y = 484, clicks = 1)
            print(k)
        elif k == 7:
            pyautogui.click(x = 487, y = 522, clicks = 1)
            print(k)
        elif k == 8:
            pyautogui.click(x = 487, y = 564, clicks = 1)
            print(k)
        elif k == 9:
            pyautogui.click(x = 668, y = 565, clicks = 1)
            pyautogui.click(x = 487, y = 453, clicks = 1)
            print(k)
        elif k == 10:
            pyautogui.click(x = 668, y = 565, clicks = 1)
            pyautogui.click(x = 487, y = 490, clicks = 1)
            print(k)
        elif k == 11:
            pyautogui.click(x = 668, y = 565, clicks = 1)
            pyautogui.click(x = 487, y = 531, clicks = 1)
            print(k)
        elif k == 12:
            pyautogui.click(x = 668, y = 565, clicks = 1)
            pyautogui.click(x = 487, y = 566, clicks = 1)
            print(k)
        
        pyautogui.press('tab')
        pyautogui.press('tab')
        
        correo = 'Correo_Falso_' + str(n)
        pyautogui.typewrite(correo)
        pyautogui.hotkey('altright','q') #teclado Español-Mexico
        pyautogui.typewrite('falso.com')
        pyautogui.press('tab')
        
        directorio = './ss_' + str(n)
    
        if os.path.isdir('./images'):
            print('')
        else:
            os.mkdir('./images')
        os.chdir('./images')

        if os.path.isdir(directorio):
            print('')
        else:
            os.mkdir(directorio)
        os.chdir(directorio)

        im = pyautogui.screenshot()
        print(im)
        im.save(r'ss.png')

        os.chdir('../')
        os.chdir('../')

        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.click(x = 393, y = 460, clicks = 1)
        time.sleep(3)

        print('Formulario', n, 'Llenado')

        l = k
        k += 1
        j = i
        i += 1
        n += 1
    file.close()

    print('\nFORMULARIOS LLENADOS EXITOSAMENTE')
    print('\nFin del Script')
    input('Presione ENTER para Salir')

