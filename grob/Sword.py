from tkinter import Tk, Canvas
from Weapon import Weapon

class Sword (Weapon):

    def __init__(self, c, n, d):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display (self, x, y):
        handle = canvas.create_rectangle(150, 100, 170, 300, fill="gray")

        blade = canvas.create_polygon(150, 100, 250, 200, 150, 300, fill="silver")

        root.mainloop()

from random import random

wp1 = Sword(Canvas, 'Меч тысячи истин',12)
wp2 = Sword(Canvas, 'Скалка Пирожка',9)
s1 = random. choice (students)
p1=Hero(Canvas, s1['full_name'] , 100, 500, s1['gender'])
p1. setWeapon (wp1)
p1. display ()
s1 = random. choice (students)
p2=Hero(Canvas, s1[' full_name'], 500, 500, s1['gender'])
p2. setWeapon (wp2)
p2. display()
p1. attack(p2)
root.mainloop()
