import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# Initialize Pygame
pg.init()

# Screen setup
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Timer Example")

# Clock and font setup
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

# Timer setup
start_time = 300000

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Calculate elapsed time
    current_time = pg.time.get_ticks()
    elapsed_time = start_time - current_time
    if elapsed_time < 0:
        elapsed_time = 0  # Prevent negative time
    elapsed_time_ms = elapsed_time / 1000.0

    # Convert to minutes and seconds
    minutes = int(elapsed_time_ms / 60)
    seconds = int(elapsed_time_ms % 60)
    time_string = "{:02d}:{:02d}".format(minutes, seconds)

    # Render the timer text
    time_text = font.render(time_string, True, (255, 255, 255))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the timer text
    screen.blit(time_text, time_text.get_rect(center=(45, 30)))

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(60)

    if elapsed_time <= 0:
        # Timer has reached zero, stop the game --> show the end screen
        running = False

pg.quit()