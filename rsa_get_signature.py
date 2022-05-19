from typing import List
from calcs import mod_power
# Alicja chce wysłać do Boba wiadomość, której skrót wynosi h = 357. Wygenerować przez Alicję podpis cyfrowa RSA dla tej wiadomości.

# skrót wiadomości
h: int = 357

# klucz prywatny
k: List[int] = [761, 1739]
print(
    f'Podpis cyfrowy s = {h}^({k[0]}) mod {k[1]} = {mod_power(h, k[0], k[1])}')
