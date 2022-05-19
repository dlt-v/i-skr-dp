from calcs import mod_power

# ===========================

# Niech p=1019 oraz g=2 będące generatorem Zp*.
p = int(input("p: "))
g = int(input("g: "))
# Alicja wybrała wartość prywatną a=638 oraz Bob wybrał wartość prywatną b=719.

prywatny_a = int(input("Osoba A wybrała wartość prywatną a: "))
prywatny_b = int(input("Osoba B wybrała wartość prywatną b: "))

# ===========================
# TEST
# p = 1019
# g = 2
# prywatny_a = 638
# prywatny_b = 719

# ===========================

# Oblicz uzgodniony przez Alicję i Boba klucz za pomocą algorytmu DH.
publiczny_a = mod_power(g, prywatny_a, p)
print(f'\nKlucz publiczny A: {publiczny_a}')
# publiczny A = 396

input('Naciśnij dowolny klawisz by kontynuować.')

publiczny_b = mod_power(g, prywatny_b, p)
print(f'\nKlucz publiczny B: {publiczny_b}')
# publiczny B = 486

input('Naciśnij dowolny klawisz by kontynuować.')

klucz_sesji_A = mod_power(publiczny_b, prywatny_a, p)
print(f'\nKlucz sesji A: {klucz_sesji_A}')


input('Naciśnij dowolny klawisz by kontynuować.')

klucz_sesji_B = mod_power(publiczny_a, prywatny_b, p)
print(f'\nKlucz sesji B: {klucz_sesji_B}')

if klucz_sesji_A == klucz_sesji_B:
    print(f'Klucz k: {klucz_sesji_B}')
