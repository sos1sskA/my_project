import math
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_size()
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 40)
big_font = pygame.font.SysFont('consolas', 90, bold=True)

CENTER = pygame.Vector2(W / 2, H / 2)

TANK_SIZE = (150, 150)
TOWER_SIZE = (250, 250)
BULLET_SIZE = (200,200)
MUZZLE_DIST = 48            # расстояние от центра до конца ствола
ANIM_DELAY = 0.2            # через сколько секунд переключается кадр танка
SHOT_COOLDOWN = 0.15        # секунд между выстрелами
BULLET_SPEED = 900
shot_timer = 0.0


def load_image(name, size=None):
    img = pygame.image.load(name).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img


tower_img = load_image("tower.png", TOWER_SIZE)
bullet_img = load_image("bullet.png", BULLET_SIZE)

# кадры анимации для каждого цвета
TANK_COLORS = ["red", "blue", "green", "yellow"]
tank_frames = {
    color: [load_image(f"{color}_tank1.png", TANK_SIZE),
            load_image(f"{color}_tank2.png", TANK_SIZE)]
    for color in TANK_COLORS
