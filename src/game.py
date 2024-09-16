import pyray as rl
class Car:
    def __init__(self,posX,posY,angle,speed=2):
        self.angle = 0
        self.pos   = rl.Vector2(posX,posY)
        self.speed = sp

    def draw(self):
        rl.draw_rectangle_v(self.pos, rl.Vector2(50,25), rl.VIOLET)
    
    def update(self):
        if action[0] > 0.5: #Forward
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
        if action[1] > 0.5: #Right
            self.angle -= 0.1
        if action[2] > 0.5: #Left
            self.angle += 0.1
    
            
