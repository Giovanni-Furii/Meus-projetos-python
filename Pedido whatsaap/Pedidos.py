import pyautogui as pg
import time 
import pyperclip as pp


pg.PAUSE=1

#abrir o google 
pg.press('winleft')
pg.write('Google Crhome')
pg.press('enter')
pg.click(x=946, y=374)
time.sleep(0.5)
#abrir wpp
pp.copy('https://web.whatsapp.com/')
time.sleep(1)
pg.hotkey('ctrl' , 'v')
time.sleep(1)
pg.press('enter')
#abrir pedido do bloco de notas
pg.press('winleft')
pg.write('Bloco de notas')
time.sleep(1)
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.hotkey('ctrl' , 'o')
pg.write('Pedido novo')
pg.press('enter')
#copiar produtos do pedido 
pg.hotkey('ctrl' , 'a')
pg.hotkey('ctrl' , 'c')
pg.hotkey('Alt' , 'F4')
time.sleep(1)
#procurar o fornecedor e enviar o pedido
pg.click(x=257, y=187)
pg.write('Marcio fornecedor')
pg.click(x=207, y=317)
pg.hotkey('ctrl', 'v')
pg.press('enter')
