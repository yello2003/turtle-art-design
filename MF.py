#my functions
def square(t,d):
    for times in range(4):
        t.forward(d)
        t.right(90)
        
def triangle(t,d):
    for times in range(3):
        t.forward(d)
        t.right(120)

def polygon(t,d):
    a=360/s
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)


        
            
    
        
                      
