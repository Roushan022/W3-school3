import math
math.pi
shape = input().strip()
if shape=="rectangle":
    w=float(input())
    l=float(input())
    print(f"Area: {l*w:.2f}")
elif shape=="circle":
    r=float(input())
    print(f"Area: {math.pi*r*r:.2f}")
elif shape=="triangle":
    b=float(input())
    h=float(input())
    print(f"Area: {0.5* b *h:.f}")
