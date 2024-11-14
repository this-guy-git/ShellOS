import pygame
import subprocess
import os
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1017, 660
TASKBAR_HEIGHT = 30
ICON_PATH = "SYSTEM/Graphical_Shell/icons/shellos.png"
BG_IMAGE_PATH = "SYSTEM/Graphical_Shell/wallpaper.png"

# Set up the display with resizable flag
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("ShellOS 1.0le")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

# Load wallpaper image
bg_image = pygame.image.load(BG_IMAGE_PATH)

# Colors
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont(None, 24)
clock_font = pygame.font.SysFont(None, 24)  # Increased font size

# Create button rectangle and clock label
launcher_button_rect = pygame.Rect(5, 2, 80, 26)
version_label_rect = pygame.Rect(WIDTH - 250, HEIGHT - 25, 240, 20)

# Initial variables
running = True
clock = pygame.time.Clock()
fullscreen = False
current_width, current_height = WIDTH, HEIGHT

# Function to open launcher
def open_launcher():
    launcher_script = os.path.join(os.getcwd(), 'SYSTEM', 'Graphical_Shell', 'launcher.py')
    subprocess.Popen(['python', launcher_script])

# Function to toggle fullscreen
def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        pygame.display.set_mode((current_width, current_height), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)

# Function to update the clock
def get_current_time():
    try:
        now = datetime.now()
        return now.strftime("%H:%M %B %d, %Y")
    except:
        return "00:00 January 1, 2000"

# Function to update elements on resize
def resize_window(new_width, new_height):
    global current_width, current_height
    current_width, current_height = new_width, new_height
    global bg_image_scaled
    bg_image_scaled = pygame.transform.scale(bg_image, (new_width, new_height - TASKBAR_HEIGHT))

# Initial scaling of background image
resize_window(WIDTH, HEIGHT)

# Main loop
while running:
    screen.fill(GRAY)  # Fill screen for taskbar background

    # Draw the taskbar
    pygame.draw.rect(screen, GRAY, (0, 0, current_width, TASKBAR_HEIGHT))

    # Draw the launcher button
    pygame.draw.rect(screen, WHITE, launcher_button_rect)
    launcher_text = font.render("Launcher", True, GRAY)
    screen.blit(launcher_text, (launcher_button_rect.x + 5, launcher_button_rect.y + 5))

    # Draw the clock, fixed to the right side
    current_time = get_current_time()
    clock_text = clock_font.render(current_time, True, WHITE)
    clock_label_x = current_width - clock_text.get_width() - 10  # Position it near the right edge
    screen.blit(clock_text, (clock_label_x, (TASKBAR_HEIGHT - clock_text.get_height()) // 2))  # Center vertically

    # Draw the resized wallpaper
    screen.blit(bg_image_scaled, (0, TASKBAR_HEIGHT))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                toggle_fullscreen()
        elif event.type == pygame.VIDEORESIZE:
            resize_window(event.w, event.h)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if launcher_button_rect.collidepoint(event.pos):
                open_launcher()

    # Update display and set frame rate
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
