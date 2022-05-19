import math


def format(x):
    return str(x).rjust(5)


def mod_power(a: int, base: int, n: int):  # base, power, mod
    '''
    a - podstawa, base - potęga, n - wartość mod
    '''
    t = base

    x = 1
    bin_t = [int(i) for i in list('{0:0b}'.format(t))]
    bin_t.reverse()
    print(f'{format("i")}\t{format("x(i)")}\t{format("a(i)")}\t{format("t(i)")}')

    i = 0
    while i < len(bin_t):
        row: str = f'{format(i)}\t{format(x)}\t{format(a)}\t{format(bin_t[i])}'
        if i >= 1 and i < 4:
            row += f'\t({int(math.sqrt(a))})^2 mod {n} = {a} mod {n} = {a}'
        print(row)
        i += 1

        if bin_t[i - 1] == 1:
            x = (x * a) % n

        if i == len(bin_t):
            break

        a = (a * a) % n

    print(f'{format(i)}\t{format(x)}\t{format(a)}\t{"-".rjust(5)}\n')

    # print(f'Answer is: {x}')
    return x

# print("Only input integers.")
# base = int(input("base: "))
# power = int(input("power: "))
# mod = int(input("mod: "))


# mod_power(base, power, mod)  # base, power, mod
# mod_power(2, 638, 1019)  # base, power, mod, print
