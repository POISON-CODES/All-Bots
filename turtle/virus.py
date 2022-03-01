from matplotlib import testing
import pyautogui as pg
import time
time.sleep(10)


for i in range(50):
        start=time.perf_counter()
        pg.write('Heya')
        pg.press('Escape')
        pg.press('Enter')
end=time.perf_counter()
pg.write(f'{(end-start)*100}seconds')
pg.press('Enter')

