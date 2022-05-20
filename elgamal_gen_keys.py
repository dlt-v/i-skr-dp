from calcs import mod_power
# Alicja chce wygenerować klucze asymetryczne ElGamala. W tym celu przyjęła wartość p=1619 oraz generator g=2.
# Wyznacz klucze asymetryczne Alicji dla jej wartości prywatnej t=937.
p = 1619
g = 2
t = 937

B = mod_power(g, t, p)
# Klucz publiczny K1
print(f'Klucz publiczny k1: ({p},{B})')

# Klucz prywatny K2
print(f'Klucz prywatny k2: ({p},{t})')
