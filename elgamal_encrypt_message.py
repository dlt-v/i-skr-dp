from operator import mod
from calcs import mod_power
# Bob chce wysłać do Alicji wiadomość której wartość liczbowa wynosi x=20.
x = 20
# Oblicz wartość tekstu zaszyfrowanego Y, wiedząc, że do zaszyfrowania wybrany został randomizer r=320.
r = 320
# Klucz publiczny k1: (1619,1454)
PUBLIC_KEY = [1619, 1454]
# Klucz prywatny k2: (1619,937)

x = mod_power(2, 320, PUBLIC_KEY[0])

y = ((20 % 1619) *
     (mod_power(PUBLIC_KEY[1], r, PUBLIC_KEY[0]))) % PUBLIC_KEY[0]
print(f'C = ({x},{y})')
