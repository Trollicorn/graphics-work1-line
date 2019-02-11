from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

for i in range(500):
    for j in range(500):
        if (i % 6 == 1):
            draw_line(i,j,i*10%500,j*10%250,s,[20+i%220,10+j%240,40+i*j%200])


#display(screen)
save_extension(s, 'img.png')
save_ppm(s,'img.ppm')
