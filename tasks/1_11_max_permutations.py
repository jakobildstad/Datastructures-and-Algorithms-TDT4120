#!/usr/bin/python3
# coding=utf-8
import random
from itertools import combinations

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om koden skal kjøres på større hardkodete tester.
# Disse inneholder mellom 10 og 100 studenter. Ellers har alle
# eksemplene mindre enn 10 studenter.
large_tests = False
# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall studenter i generert instans.
n_lower = 3
# Høyest mulig antall studenter i generert instans.
# NB: Om denne verdien settes høyt (>20) vil det ta lang tid å verifisere
# svarene.
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


# Example
# path = 0, 2, 1, 0
# position = 0: 1, 2: 2, 1: 3, 0: 4
#
#
#
# current:    0  1  2  3  4  5
# M[current]: 2  0  1  1  5  4 
# 
#  
# result: {0, 1, 2, 4, 5}

def max_permutations(M):
    seen_total = set()
    res = set()
    for start in range(len(M)):
        if start in seen_total:
            continue

        current = start
        path = []
        position = {}

        while current not in seen_total:
            position[current] = len(path)
            path.append(current)
            seen_total.add(current)
            current = M[current]

        if current in position:
            cycle = path[position[current]:]
            if len(cycle) >= 2:
                res.update(cycle)

    return res

        









    
    


# Hardkodete instanser på formatet: (M, løsning)
tests = [
    ([0], set()),
    ([0, 1], set()),
    ([0, 0], set()),
    ([0, 0, 0], set()),
    ([1, 0], {0, 1}),
    ([2, 0, 1, 1, 5, 4], {0, 1, 2, 4, 5}),
    ([2, 0, 1, 1, 5, 4, 6], {0, 1, 2, 4, 5}),
    ([1, 2, 3, 4, 4], set()),
    ([1, 0], {0, 1}),
    ([1, 0, 3, 2, 5, 4], {0, 1, 2, 3, 4, 5}),
    ([1, 2, 3, 0], {0, 1, 2, 3}),
    ([1, 2, 3, 4, 3], {3, 4}),
    ([1, 0, 1, 1, 2, 3], {0, 1}),
    ([2, 1, 5, 3, 4, 7, 0, 6], {0, 2, 5, 6, 7}),
    ([4, 2, 3, 4, 1], {1, 2, 3, 4}),
    ([1, 4, 1, 4, 1, 4], {1, 4}),
    ([4, 1, 4, 1, 4, 1], set()),
]

if large_tests:
    tests += [
        # 10 - 20 studenter
        (
            [9, 0, 7, 2, 10, 8, 12, 1, 4, 6, 7, 7, 8, 5],
            {0, 1, 4, 6, 7, 8, 9, 10, 12},
        ),
        (
            [14, 11, 8, 7, 6, 13, 13, 0, 12, 4, 2, 7, 12, 14, 2, 15],
            set(),
        ),
        (
            [4, 6, 11, 10, 0, 9, 8, 0, 7, 4, 6, 6, 9],
            {0, 4},
        ),
        (
            [5, 10, 9, 14, 3, 10, 3, 4, 3, 2, 7, 13, 12, 9, 3],
            {9, 2, 3, 14},
        ),
        (
            [11, 15, 0, 11, 8, 15, 8, 10, 4, 3, 3, 15, 5, 2, 5, 0],
            {0, 4, 8, 11, 15},
        ),
        # 30 - 50 studenter
        (
            [46, 43, 11, 40, 35, 44, 8, 25, 30, 6, 34, 29, 19, 46, 14, 9, 19,
             29, 41, 8, 32, 4, 10, 10, 15, 35, 29, 9, 19, 11, 8, 9, 13, 4, 41,
             13, 22, 38, 5, 13, 32, 0, 2, 8, 26, 31, 37],
            {8, 11, 29, 30},
        ),
        (
            [26, 11, 9, 23, 7, 0, 3, 26, 17, 6, 29, 25, 5, 6, 20, 1, 1, 10, 19,
             7, 3, 3, 12, 1, 4, 28, 26, 30, 14, 13, 26],
            {1, 3, 11, 14, 20, 23, 25, 28},
        ),
        (
            [18, 24, 2, 33, 20, 42, 15, 33, 35, 23, 18, 37, 9, 32, 29, 24, 6,
             23, 12, 29, 16, 10, 2, 42, 22, 37, 25, 28, 14, 40, 2, 31, 27, 5,
             11, 21, 29, 31, 33, 35, 12, 14, 16, 1, 44],
            set(),
        ),
        (
            [15, 1, 1, 41, 4, 44, 29, 44, 18, 6, 25, 8, 6, 12, 23, 37, 22, 10,
             16, 17, 27, 4, 41, 35, 26, 42, 33, 7, 15, 28, 12, 30, 37, 4, 35,
             39, 20, 34, 12, 13, 5, 29, 17, 7, 40, 27, 43],
            {34, 35, 5, 6, 37, 39, 40, 10, 42, 12, 13, 44, 15, 17, 25, 28, 29},
        ),
        (
            [25, 13, 12, 17, 25, 19, 24, 9, 20, 28, 21, 1, 32, 19, 16, 28, 5, 7,
             16, 33, 32, 29, 22, 31, 24, 29, 12, 32, 24, 27, 16, 20, 22, 2],
            set(),
        ),
        # 50 - 100 studenter
        (
            [
                4, 62, 24, 34, 55, 1, 57, 29, 22, 60, 21, 63, 8, 45, 46, 32, 70,
                43, 21, 45, 14, 54, 15, 64, 28, 63, 50, 35, 34, 36, 66, 7, 13,
                64, 67, 40, 21, 65, 63, 67, 47, 45, 37, 38, 8, 17, 33, 52, 19,
                1, 49, 43, 37, 58, 4, 24, 24, 53, 20, 26, 50, 12, 44, 26, 71,
                70, 53, 18, 23, 55, 72, 52, 3
            ],
            {1, 4, 8, 13, 15, 17, 18, 21, 22, 24, 26, 28, 32, 34, 38, 43, 44,
             45, 49, 50, 54, 55, 62, 63, 67}
        ),
        (
            [
                56, 65, 31, 39, 46, 49, 55, 16, 55, 55, 49, 52, 10, 41, 47, 54,
                3, 15, 20, 3, 42, 65, 10, 62, 17, 42, 55, 27, 9, 37, 69, 1, 50,
                24, 41, 16, 31, 69, 20, 67, 65, 39, 64, 60, 49, 52, 14, 67, 27,
                17, 53, 60, 18, 69, 49, 0, 6, 63, 68, 2, 69, 52, 24, 20, 36, 34,
                1, 57, 45, 32
            ],
            {0, 1, 6, 15, 17, 20, 31, 32, 34, 36, 39, 41, 42, 49, 50, 53, 54,
             55, 56, 57, 63, 64, 65, 67, 69},
        ),
    ]

# Bruteforce løsning. Finner svaret ved å sjekke alle mulige
# kombinasjoner av studenter. Tar 20-30 sekunder for instanser med 25
# studenter.
def solve(M):
    n = len(M)
    for k in range(n, 0, -1):
        for subset in combinations(range(n), k):
            if set(subset) == set(M[i] for i in subset):
                return set(x for x in subset if M[x] != x)
    return set()


# Genererer k tilfeldige tester, hver med et tilfeldig antall studenter
# plukket uniformt fra intervallet [nl, nu].
def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        M = [random.randint(0, n - 1) for _ in range(n)]
        yield M, solve(M)


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(random_tests, n_lower, n_upper))

failed = False
for M, answer in tests:
    student = max_permutations(M[:])
    if student != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
M: {M}

Ditt svar: {student}
Riktig svar: {answer if answer else "{}"}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")