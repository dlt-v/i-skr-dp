# Alicja wylosowała dwie liczby pierwsze p=37 i q=47 oraz wartość e=1001.
print("A ========================")
p_a = int(input("liczba pierwsza p: "))
q_a = int(input("liczba pierwsza q: "))
e_a = int(input("liczba e: "))
# fi
fi_a = (p_a - 1)*(q_a - 1)
print(f'Ø = (p - 1)(q - 1) = {fi_a}')
# n
n_a = p_a * q_a
print(f'n = p * q = {n_a}')

print(f'Klucz publiczny A: ({e_a},{n_a})')
print("Klucz prywatny:")
print(f'e^(-1) mod Ø = {e_a}^(-1) mod {fi_a} = ?')


print("\nB ========================")
p_b = int(input("liczba pierwsza p: "))
q_b = int(input("liczba pierwsza q: "))
e_b = int(input("liczba e: "))
# Wyznaczyć klucze asymetryczne RSA dla Alicji.
