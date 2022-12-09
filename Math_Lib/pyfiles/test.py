from trigonometry import sin
import math

pi = math.pi
print('pi:', pi)
for alpha in [0, pi, pi/2, pi/3, pi/4, pi/6]:
    print(f'For angle: {0 if alpha == 0 else "pi/"+str(int(pi/alpha))}, Sine  is ~ {sin(alpha)}')