from calcs import mod_power

klucz_prywatny: int = 1739
e = 1001
# wiadomość
x: int = 20
y = mod_power(x, e, klucz_prywatny)
print(y)
