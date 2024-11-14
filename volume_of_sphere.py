import numpy as np

def calculate_volume_sphere(radius):
    vol = (4/3) * np.pi * (radius**3)
    return vol

r1 = 30
vol1 = calculate_volume_sphere(r1)
print(f'Volume of a sphere with radius {r1} = {vol1}')

r2 = 40
vol2 = calculate_volume_sphere(r2)
print(f'Volume of a sphere with radius {r2} = {vol2}')