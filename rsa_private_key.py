from calcs import extended_euclidean

# Alicja wylosowała dwie liczby pierwsze p=37 i q=47 oraz wartość e=1001.
print("A ========================")
# p_a = int(input("liczba pierwsza p: "))
# q_a = int(input("liczba pierwsza q: "))
# e_a = int(input("liczba e: "))
p_a = 11
q_a = 29
e_a = 89
# fi
fi_a = (p_a - 1)*(q_a - 1)
print(f'\nØ = (p - 1)(q - 1) = {fi_a}')
# n
n_a = p_a * q_a
print(f'\nn = p * q = {n_a}')

print(f'\nKlucz publiczny A: ({e_a},{n_a})')
print("\nKlucz prywatny:")
print(f'e^(-1) mod Ø = {e_a}^(-1) mod {fi_a} = ?')
x = extended_euclidean(e_a, fi_a)
print(f'\nKlucz prywatny: ({x}, {n_a})')

# print("\nB ========================")
# p_b = int(input("liczba pierwsza p: "))
# q_b = int(input("liczba pierwsza q: "))
# e_b = int(input("liczba e: "))
# Wyznaczyć klucze asymetryczne RSA dla Alicji.


# Bob chce wysłać do Alicji wiadomość, której wartość wynosi x=20 zaszyfrowaną przy użyciu algorytmu RSA. Oblicz wartość szyfrogramu y.
