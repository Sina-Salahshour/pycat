from cat import cat
import turtle
win = turtle.Screen()
win.setup(500,500)
cat1 = cat()
cat2 = cat()
cat1.cat.pensize(10)
cat2.cat.pensize(10)
cat1.cat.lt(90)
cat2.cat.lt(90)
cat1.operation = [('circle',360,2),('circle',360,-2),('circle',360,2),('sleep',300,),'cls',('circle',360,-2),('circle',360,2),('circle',360,-2),('sleep',300,),'cls','end']
cat2.operation = [('circle',360,2,'white'),('circle',360,-2,'white'),('circle',360,2,'white'),('sleep',300,),'cls',('circle',360,-2,'white'),('circle',360,2,'white'),('circle',360,-2,'white'),('sleep',300),'cls','end']
cat2.current_operation=['sleep',300]


cat3 = cat()
cat4 = cat()
cat3.cat.pensize(10)
cat4.cat.pensize(10)
cat3.cat.lt(270)
cat4.cat.lt(270)
cat3.operation = [('circle',360,2),('circle',360,-2),('circle',360,2),('sleep',300,),'cls',('circle',360,-2),('circle',360,2),('circle',360,-2),('sleep',300,),'cls','end']
cat4.operation = [('circle',360,2,'white'),('circle',360,-2,'white'),('circle',360,2,'white'),('sleep',300,),'cls',('circle',360,-2,'white'),('circle',360,2,'white'),('circle',360,-2,'white'),('sleep',300),'cls','end']
cat4.current_operation=['sleep',300]
# cat3.goto(0,100)
# cat4.goto(0,100)

while True:
    cat1.operate()
    cat2.operate()
    # for i in range(2):
    cat3.operate()
    cat4.operate()