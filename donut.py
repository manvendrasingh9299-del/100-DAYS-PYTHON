import math
import time
import os

os.system("")

A = 0
B = 0

while True:
    output = [' '] * 1760
    zbuffer = [0] * 1760

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):

            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (math.cos(i) * h * math.cos(B) - t * math.sin(B)))
            y = int(12 + 15 * D * (math.cos(i) * h * math.sin(B) + t * math.cos(B)))

            o = x + 80 * y

            N = int(8 * ((f * e - c * d * g) * math.cos(B)
                - c * d * e - f * g - math.cos(i) * d * math.sin(B)))

            if 0 <= o < 1760 and D > zbuffer[o]:
                zbuffer[o] = D
                output[o] = ".,-~:;=!*#$@"[max(0, min(11, N))]

    os.system("cls" if os.name == "nt" else "clear")

    for k in range(1760):
        print(output[k] if k % 80 else "\n" + output[k], end="")

    A += 0.04
    B += 0.02
    time.sleep(0.03)