from tkinter import Tk, Canvas, ARC, W, CENTER
from human import Human


class Hero (Human) :

    def init (self, canvas, name, x, y, gen):
        super().__init__ (canvas, name, x, y, gen)
        self._health = 100
        self._wp = None
    def setWeapon (self, weapon) :
        self._wp = weapon

    def attack(self, enemy):
        damage = self. wp.hit()
        print(f'{self._name} нанес(ла) {damage} урона {enemy. name}!')

    def _drawName (self):
        name = f"{self._name.split() [0]} {self._name.split() [1] [0]}. {self._name .split () [2] [0] }."
        self.canvas.create_text(self.x+50, self.y-250,)
        
