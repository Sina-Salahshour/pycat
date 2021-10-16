import turtle
import random
turtle.hideturtle()
turtle.colormode(255)
turtle.tracer(0,0)
class cat:
    def __init__(self):
        self.drawing_res = 1
        self.circle_radius = 20
        self.color_step = 5
        self.color = [0,0,0,False,False,False]
        self.operation = [(1,10,'sleep'),'cls','end']
        self.current_operation = [0,0]
        self.i=0
        self.cat=turtle.Turtle()
        self.cat.speed(0)
        self.cat.hideturtle()
        self.penup=False

    def chcolor(self):
        x=random.randint(0,2)
        self.color[x]-=self.color_step if self.color[x+3] else -self.color_step
        if self.color[x] > 255-self.color_step:
            self.color[x+3] = True
        elif self.color[x] < self.color_step:
            self.color[x+3] = False
        self.cat.pencolor((self.color[0], self.color[1],self.color[2]))
    
    def operate(self):
    
        while self.current_operation[1]==0:
            if self.operation[self.i]=='end':
                self.i = 0
            if self.operation[self.i]=='cls':
                self.cat.clear()
                self.i += 1
                continue
            self.current_operation = list(self.operation[self.i])
            self.i += 1
            break
        

        if 'blank' in self.current_operation:
            self.cat.penup()
            self.penup = True
        while True:

            turtle.update()
            match self.current_operation[0]:
                case 'line':
                    if self.current_operation[1]!=0:
                        self.cat.fd(5 if self.current_operation[1] > 0 else -5)
                        self.current_operation[1] -= 5 if self.current_operation[1] > 0 else -5
                        if 'white' in self.current_operation:
                            self.cat.pencolor((255,255,255))
                        else:
                            self.chcolor()
                    break
                case 'angle':
                    self.cat.lt(self.current_operation[1])
                    self.current_operation[1]=0
                    break
                case 'circle':
                    if self.current_operation[1]!=0:
                        self.cat.circle(self.current_operation[2]*self.circle_radius,5 if self.current_operation[1] > 0 else -5,self.drawing_res)
                        self.current_operation[1] -= 5 if self.current_operation[1] > 0 else -5
                        if 'white' in self.current_operation:
                            self.cat.pencolor((255,255,255))
                        else:
                            self.chcolor()
                    break
                case 'sleep':
                    self.current_operation[1] -= 5
                    break
        if self.penup:
            self.cat.pendown()
            penup=False

    def goto(self,x,y):
        self.cat.penup()
        self.cat.goto(x,y)
        self.cat.pendown()

    def turn(self,x):
        self.cat.lt(x)