from typing import List
from calcs import mod_power

# Bob otrzymał od Alicji wiadomość, z której wyznaczył skrót h = 357...
h = 100
# ...oraz jej podpis cyfrowy RSA s = 1630.
s = 255

# Klucz publiczny
k: List[int] = [89, 319]

# Zweryfikuj przez Boba otrzymany od Alicji podpis cyfrowy.
x = mod_power(s, k[0], k[1])
print(f'{s}^({k[0]}) mod {k[1]} = {x}')
print(f'h: {h} == {x}')
