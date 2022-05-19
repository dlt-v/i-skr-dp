from typing import List
from calcs import mod_power
# Alicja otrzymała od Boba szyfrogram y=1327.
# zaszyfrowana wiadomość
y: int = 225

# Obliczyć przez Alicję wartość tekstu jawnego x.
# klucz prywatny Ali
k: List[int] = [331, 1073]
x: int = mod_power(y, k[0], k[1])
print(f'Odszyfrowana wiadomość: {x}')
