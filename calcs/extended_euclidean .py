

def fmt(x: str) -> str:
    '''
    Dodaje 4-znakowy padding do wartosci.
    '''
    return str(x).rjust(7)
# rozszerzony algorytm euklidesa
# np. 1001(-1) mod 1656 = 761
# gdzie podstawa to 1001 i mod to 1656


def extended_euclidean(a: int, n: int):
    '''
    Rozszerzony Algorytm Euklidesa. Przyjmuje dwie nieujemne liczby całkowite a, n, gdzie a >= n.
    '''
    x: int = n
    y: int = a
    print(f'{fmt("i")}{fmt("u(i)")}{fmt("up(i)")}{fmt("v(i)")}{fmt("vp(i)")}{fmt("n(i)")}{fmt("a(i)")}{fmt("q(i)")}{fmt("r(i)")}\n')
    i: int = 0
    u: int = 0
    up: int = 1
    v: int = 1
    vp: int = 0
    while True:
        row: str = ''
        # iteration
        row += fmt(str(i))

        # u(i)
        row += fmt(str(u))

        # up(i)
        row += fmt(str(up))

        # v(i)
        row += fmt(str(v))

        # vp(i)
        row += fmt(str(vp))

        # n(i)
        row += fmt(str(n))

        # a(i)
        row += fmt(str(a))

        # q(i) - coefficient
        q = n // a
        row += fmt(str(q))

        # r(i) - remainder
        r = n % a
        row += fmt(str(r))

        i += 1

        temp_u = u
        u = up - q * temp_u
        up = temp_u

        temp_v = v
        v = vp - q * temp_v
        vp = temp_v

        n = a
        a = r

        print(row)
        if r == 0:
            break

    print(f'\na^(-1) = v3 mod n = {temp_v} mod {x} = {temp_v % x}')
    print(f'Sprawdzenie: {y} * {temp_v % x} mod {x} = {y * (temp_v % x) % x}')

    return temp_v


extended_euclidean(11, 125)
