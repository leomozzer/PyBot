import time
import pyautogui
import random
from datetime import datetime

n = random.randint(0,10)
a = 0
log_mage = open('log_mage.txt', 'w')

premmy = input('Voçê é premmy?')
print(premmy)
magia = input('Digite a magia: ')
print('Você escolheu: ', magia)

while premmy == 'nao':
    while magia == 'exura':
        while a != n:
            if(a < n):
                time.sleep(5)
                pyautogui.typewrite('exura')
                pyautogui.press('enter')
                tempo = str(datetime.now().time())
                log_mage.write(tempo + '\n')
                log_mage.write(magia + '\n')
                log_mage = open('log_mage.txt', 'a')
                time.sleep(2)
                pyautogui.press('f12')
                time.sleep(18)
                a += 1

            elif(a > n):
                time.sleep(5)
                pyautogui.typewrite('exura')
                pyautogui.press('enter')
                tempo = str(datetime.now().time())
                log_mage.write(tempo + '\n')
                log_mage.write(magia + '\n')
                log_mage = open('log_mage.txt', 'a')
                time.sleep(2)
                pyautogui.press('f12')
                time.sleep(18)
                a -= 1
        time.sleep(2)
        pyautogui.typewrite('utevo lux')
        pyautogui.press('enter')
        tempo = str(datetime.now().time())
        log_mage.write(tempo + '\n')
        log_mage.write("Utevo lux" + '\n')
        log_mage = open('log_mage.txt', 'a')
        time.sleep(23)
        n = random.randint(0,10)
        a = 0


'''
    while magia == 'utevo lux':
        time.sleep(5)
        pyautogui.hotkey('u','t','e','v','o', 'space', 'l', 'u','x')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('f12')
        time.sleep(15)
'''

#parte premmy ainda não está ok
#precisa saber quanto tempo leva a regineração
'''
while premmy == 'sim':
    while magia == 'exura':
        while a != n:
            if(a < n):
                time.sleep(5)
                pyautogui.hotkey('e','x','u','r','a')
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('f12')
                time.sleep(18)
                a += 1

            elif(a > n):
                time.sleep(5)
                pyautogui.hotkey('e','x','u','r','a')
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('f12')
                time.sleep(18)
                a -= 1
        time.sleep(2)
        pyautogui.hotkey('u','t','e','v','o', 'space', 'l', 'u','x')
        pyautogui.press('enter')
        time.sleep(23)
        n = random.randint(0,10)
        a = 0
    


    while magia == 'utevo lux':
        time.sleep(5)
        pyautogui.hotkey('u','t','e','v','o', 'space', 'l', 'u','x')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('f12')
        time.sleep(15)
'''


