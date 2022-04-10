import settings as c
from game_classes import Vector2


def accelerate(obj, accel_x, accel_y, limit_x=None):
    obj.vel += Vector2(accel_x, accel_y) * c.delta_time
    if limit_x != None:
        if obj.vel.x > 0:
            obj.vel.x = clamp(obj.vel.x, 0, limit_x)
        elif obj.vel.x < 0:
            obj.vel.x = clamp(obj.vel.x, -limit_x, 0)


def clamp(x, a, b):
    return max(a, min(b, x))


def get_flipped_sprite(sprite):
    return 429 - sprite[0] - sprite[2], sprite[1], sprite[2], sprite[3]
