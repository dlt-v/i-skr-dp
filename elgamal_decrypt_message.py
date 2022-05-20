from calcs import mod_power
# Alicja otrzymała od Boba szyfrogram Y=(130, 414). Obliczyć przez Alicję wartość tekstu jawnego x.
Y = [130, 414]
# Klucz publiczny k1: (1619,1454)
PUBLIC_KEY = [1619, 1454]
# Klucz prywatny k2: (1619,937)
PRIVATE_KEY = [1619, 937]

p = Y[1] * Y[0]
potega = (PRIVATE_KEY[0] - 1 - PRIVATE_KEY[1])
# p = mod_power(p, (PRIVATE_KEY[0] - 1 - PRIVATE_KEY[1]), PRIVATE_KEY[0])
first_value = Y[1] % PUBLIC_KEY[0]
second_value = mod_power(Y[0], potega, PUBLIC_KEY[0])
print(
    f'x = ({Y[1]} mod {PUBLIC_KEY[0]}) * ({Y[0]}^({potega}) mod {PUBLIC_KEY[0]}) mod {PUBLIC_KEY[0]}')
print(f'x = {first_value} * {second_value} mod {PUBLIC_KEY[0]}')
print(f'x = {first_value * second_value % PUBLIC_KEY[0]}')
