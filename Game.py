import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

start_time = pg.time.get_ticks()
current_time = pg.time.get_ticks()
elapsed_time = start_time - current_time
elapsed_time_ms = elapsed_time / 1000.0

minutes = int(elapsed_time_ms / 60)
seconds = int(elapsed_time_ms % 60)
time_string = "{:02d}:{:02d}".format(minutes, seconds)

time_text = pg.font.render(time_string, True, (255, 255, 255))
screen = pg.display.set_mode((800, 600))
scree