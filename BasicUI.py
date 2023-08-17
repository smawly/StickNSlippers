import sys

import pygame
import random
import time

pygame.init()

screen_width = 1280
screen_height = 720
title = "Sticks n Slippers"
font = pygame.font.SysFont('Sans', 50)
clock = pygame.time.Clock()
icon_image = pygame.image.load("StartButton.png")
screen = pygame.display.set_mode((screen_width, screen_height))
icon = pygame.display.set_icon(icon_image)
title_game = pygame.display.set_caption(title)
Text = font.render("Input Your Name", True, (0, 0, 0))
text = ""
running = True
while running:
    screen.fill((255, 255, 255))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    screen.blit(Text, (450, 270))
    text_surf = font.render(text, True, (12, 122, 12))
    screen.blit(text_surf, text_surf.get_rect(center=screen.get_rect().center))
    pygame.display.flip()
pygame.quit()
