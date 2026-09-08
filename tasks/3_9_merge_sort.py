#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from itertools import combinations

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det skal kjøres tester for merge
test_merge = True
# Kontrollerer om det skal kjøres tester for merge_sort
test_merge_sort = True
# Kontrollerer om det genereres tilfeldige instanser for merge.
generate_random_tests_merge = False
# Kontrollerer om det genereres tilfeldige instanser for merge_sort.
generate_random_tests_merge_sort = False
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall verdier i generert instans.
n_lower = 3
# Høyest mulig antall verdier i generert instans.
# NB: Om denne verdien settes høyt (>=50) kan testene for merge ta veldig
#     lang tid om koden din ikke produserer riktig svar..
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def merge(arr, l, middle, r):
    l_arr = arr[l:middle + 1]
    r_arr = arr[middle+1:r + 1]

    l_i = 0
    r_i = 0
    k = l

    while l_i < len(l_arr) and r_i < len(r_arr):
        l_val = l_arr[l_i]
        r_val = r_arr[r_i]

        if l_val <= r_val:
            arr[k] = l_val
            l_i += 1
        else:
            arr[k] = r_val
            r_i += 1
        k += 1

    while l_i < len(l_arr):
        arr[k] = l_arr[l_i]
        l_i += 1
        k += 1

    while r_i < len(r_arr):
        arr[k] = r_arr[r_i]
        r_i += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        middle = (l + r) // 2
        merge_sort(arr, l, middle)
        merge_sort(arr, middle + 1, r)
        merge(arr, l, middle, r)













# Hardkodete tester for merge på format (A, p, q, r)
tests_merge = [
    ([1], 0, 0, 0),
    ([1, 3, 2], 0, 0, 1),
    ([3, 1, 2], 0, 0, 1),
    ([1, 2, 1, 2], 0, 1, 3),
    ([1, 2, 1, 2], 0, 1, 2),
    ([1, 2, 1, 2], 1, 1, 3),
    ([1, 2, 1, 2], 1, 1, 2),
    ([1, 2, 1, 2], 1, 2, 3),
    ([1, 3, 1, 3, 1, 2, 4, 3], 2, 3, 6),
    ([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 0, 5),
]

if seed:
    random.seed(seed)


# Tilfeldig genererte tester for merge
def generate_merge_tests(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        p = random.randint(0, n - 2)
        q = p + random.randint(0, n - p - 2)
        r = q + random.randint(0, n - q - 1)

        yield [random.randint(0, 99) for _ in range(n)], p, q, r


# Finner en løsning for merge gjennom bruteforce
def answer_merge(A, p, q, r):
    n = r - p + 1
    for z in combinations(range(n), q - p + 1):
        S = [None] * n
        for i, x in enumerate(z):
            S[x] = A[p + i]

        ci = 1
        for i in range(n):
            if S[i] is not None:
                continue
            S[i] = A[q + ci]
            ci += 1

        X = A[:p] + S + A[r + 1:]
        if verify_merge(A, p, q, r, X):
            return X


# Verifiserer at answer er et riktig svar for merge problemet
def verify_merge(A, p, q, r, answer):
    if type(A) != type(answer) or len(A) != len(answer):
        return False
    if A[:p] != answer[:p]:
        return False
    if A[r + 1:] != answer[r + 1:]:
        return False

    def c(B, C, S):
        if len(B) == 0:
            return C == S
        if len(C) == 0:
            return B == S
        if S[0] == B[0] and B[0] <= C[0]:
            return c(B[1:], C, S[1:])
        if S[0] == C[0] and C[0] < B[0]:
            return c(B, C[1:], S[1:])
        return False

    return c(A[p:q + 1], A[q + 1:r + 1], answer[p:r + 1])


if generate_random_tests_merge:
    tests_merge.extend(generate_merge_tests(random_tests, n_lower, n_upper))

if not test_merge:
    tests_merge = []

failed = False
for A, p, q, r in tests_merge:
    student = A[:]
    merge(student, p, q, r)
    if not verify_merge(A, p, q, r, student):
        if failed:
            print("-"*50)

        failed = True
        print(f"""
merge feilet for følgende instans:
A: {A}
p: {p}
q: {q}
r: {r}

Ditt svar: {student}
Riktig svar: {answer_merge(A, p, q, r)}
""")


if not failed and test_merge:
    print("merge ga riktig svar for alle eksempeltestene")
elif test_merge:
    print("-"*50)


# Hardkodete merge_sort tester på format: (A, p, r)
tests_merge_sort = [
    ([], 0, -1),
    ([1], 0, 0),
    ([1, 3, 2], 0, 1),
    ([3, 1, 2], 0, 1),
    ([1, 2, 1, 2], 0, 3),
    ([1, 2, 1, 2], 0, 2),
    ([1, 2, 1, 2], 1, 3),
    ([1, 2, 1, 2], 1, 2),
    ([3, 1, 0, 5], 0, 3),
    ([1, 3, 1, 3, 1, 2, 4, 3], 2, 6),
    ([99, 2, 3, 4, 5, 6, 7, 8, 7], 0, 5),
    ([1, 0, 5], 7, 6),
    ([1, 0, 5], 7, 7),
    ([1, 0, 5], 1, 1),
]


# Genererer tilfeldige tester for merge_sort
def generate_merge_sort_tests(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        p = random.randint(0, n - 2)
        r = p + random.randint(0, n - p - 1)

        yield [random.randint(0, 99) for _ in range(n)], p, r


if generate_random_tests_merge_sort:
    tests_merge_sort.extend(generate_merge_sort_tests(random_tests, n_lower, n_upper))

if not test_merge_sort:
    tests_merge_sort = []

failed = False
for A, p, r in tests_merge_sort:
    student = A[:]
    merge_sort(student, p, r)
    ans = A[:p] + sorted(A[p:r + 1]) + A[r + 1:]
    if student != ans:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
merge_sort feilet for følgende instans:
A: {A}
p: {p}
r: {r}

Ditt svar: {student}
Riktig svar: {ans}
""")

if not failed and test_merge_sort:
    print("merge_sort ga riktig svar for alle eksempeltestene")