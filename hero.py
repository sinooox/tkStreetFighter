from tkinter import Tk, Canvas, ARC, W
from human import Human


class Hero(Human):
    def __init__(self, canvas, name, x, y, gender):
        super().__init__(canvas, name, x, y, gender)
        self.health = 100
        self._wp = None

    def setWeapon(self, weapon):
        self._wp = weapon

    def attack(self, enemy):
        damage = self._wp.hit()
        if enemy.health >= 1:
            if self.gender == 'М':
                enemy.health -= damage
                return f'{self.name} нанес {damage} урона {enemy.name}\n', enemy.health, enemy.name
            else:
                enemy.health -= damage
                return f'{self.name} нанесла {damage} урона {enemy.name}\n', enemy.health, enemy.name

    def _DrawName(self):
        super()._DrawName()
        self.canvas.create_rectangle(self.x+1.5,
                                     self.y-230,
                                     self.x+1.5+100,
                                     self.y-300+80,
                                     outline="#FFF", fill="#FFF", width=2)
        
        self.canvas.create_rectangle(self.x+1.5,
                                     self.y-230,
                                     self.x+1.5+self.health,
                                     self.y-300+80,
                                     outline="#FFF", fill="#1f1", width=2)

    def _DrawWeapon(self):
        self.canvas.create_line(self.x+80,
                                self.y-50,
                                self.x+100,
                                self.y-150,
                                fill='#F00', width=2)

    def display(self):
        super().display()
        self._DrawWeapon()
        
        
