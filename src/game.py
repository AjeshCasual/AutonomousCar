import pyray as rl
class Car:
    def __init__(self,posX,posY,angle):
        self.angle = 0
        self.pos   = rl.Vector2(posX,posY)
        self.acc   = rl.Vector2(0,0)
        self.vel   = rl.Vector2(0,0)
        self.brake = False

    def draw(self):
        rl.draw_rectangle_v(self.pos, rl.Vector2(50,25), rl.VIOLET)
    
            
