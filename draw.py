from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 < x0:
        tempX = x0
        tempY = y0
        x0 = x1
        y0 = y1
        x1 = tempX
        y1 = tempY

    if (x0 == x1):
        m = 2
    else:
        m = (y1 - y0)/(x1-x0)

    if (m > 0):
        if (m < 1):
            draw_o1(x0,y0,x1,y1,screen,color)
        else:
            draw_o2(x0,y0,x1,y1,screen,color)
    else:
        if (m < -1):
            draw_o7(x0,y0,x1,y1,screen,color)
        else:
            draw_o8(x0,y0,x1,y1,screen,color)

"""
    x = x0
    y = y0
    A = y1-y0
    B = x0-x1
    d = A + B

    #octant I and II
    if y1 - y0 > 0:
        #octant I
        if A < -B:
            d += A
            while x <= x1:
                plot(screen,color,x,y)
                if d>0: #point is below line
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A
        else: #octant II
            d += B
            while y <= y1:
                plot(screen,color,x,y)
                if d > 0: #point is to right of line
                    x += 1
                    d += 2*A
                y += 1
                d += 2*B
    else: #octant VII and VIII
        if A < B: #octant VIII
            d += A
            while x <= x1:
                plot(screen,color,x,y)
                if d<0: #point is below line
                    y -= 1
                    d += 2*B
                x += 1
                d += 2*A
        else: #octant VII
            d += A;
            while y <= y1:
                plot(screen,color,x,y)
                if d<0: #point is below line
                    x -= 1
                    d += 2*B
                y += 1
                d += 2*A
"""

def draw_o1(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    A = y1-y0
    B = x0-x1
    d = 2*A + B
    while (x <= x1):
        plot(screen,color,x,y)
        if (d > 0):
            y += 1
            d += 2*B
        x += 1
        d += 2*A

def draw_o2(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    A = y1-y0
    B = x0-x1
    d = A + 2*B
    while (y <= y1):
        plot(screen,color,x,y)
        if (d < 0):
            x += 1
            d += 2*A
        y += 1
        d += 2*B

def draw_o7(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    A = y1-y0
    B = x0-x1
    d = A - 2 * B
    while (y >= y1):
        plot(screen,color,x,y)
        if (d > 0):
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B

def draw_o8(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    A = y1-y0
    B = x0-x1
    d = 2 * A - B
    while (x <= x1):
        plot(screen,color,x,y)
        if (d < 0):
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A
