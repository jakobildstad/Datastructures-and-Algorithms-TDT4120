#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres
random_tests = 1000
# Lavest mulig antall verdier i generert instans.
n_lower = 1
# Høyest mulig antall verdier i generert instans.
n_upper = 100
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 42

def find_maximum(x):
    """
    Finner maksimum i en rotert unimodal tabell uten å endre den.
    Returnerer None for tom input.

    Løkkeinvariant: Maksimum finnes alltid i x[l..r].

    Vi vurderer endenes retning på nytt for hvert søkeområde:

    1. Begge ender stiger innover:
       Området inneholder en topp. Følg stigningen fra midten.

    2. Begge ender synker innover:
       Maksimum må være et av endepunktene.

    3. Én ende stiger innover, den andre synker:
       Området kan inneholde både en bunn og en topp.

       a) Venstre ende stiger innover:
          - Midten synker mot høyre: Søk venstre.
          - Midten stiger mot høyre: Sammenlign med x[l].
            Er x[mid] < x[l], er midten etter bunnen: Søk venstre.
            Ellers er midten før toppen: Søk høyre.

       b) Høyre ende stiger innover:
          - Midten stiger mot høyre: Søk høyre.
          - Midten synker mot høyre: Sammenlign med x[r].
            Er x[mid] < x[r], er midten før bunnen: Søk høyre.
            Ellers er midten etter toppen: Søk venstre.

    Hvis midten selv er toppen, returnerer vi den.
    Hvis midten er bunnen, søker vi mot det største endepunktet.

    Hvert søketrinn forkaster omtrent halvparten av området.
    Verste kjøretid: Theta(log n). Ekstra plass: O(1).
    """
    if len(x) == 0:
        return None

    l, r = 0, len(x) - 1

    # Med minst fire elementer ligger midtens naboer innenfor området.
    while r - l > 2:
        left_growing_inward = x[l] < x[l + 1]
        right_growing_inward = x[r] < x[r - 1]

        # Tilfelle 2: Maksimum er et endepunkt.
        if not left_growing_inward and not right_growing_inward:
            return max(x[l], x[r])

        mid = (l + r) // 2

        mid_growing_right = x[mid] < x[mid + 1]
        mid_growing_left = x[mid] < x[mid - 1]

        # Midten er en topp.
        if not mid_growing_left and not mid_growing_right:
            return x[mid]

        # Midten er en bunn.
        if mid_growing_left and mid_growing_right:
            if x[r] > x[l]:
                l = mid + 1
            else:
                r = mid - 1
            continue

        # Utgangspunkt: Følg stigningen.
        direction_right = mid_growing_right

        # Tilfelle 3: Nøyaktig én ende stiger innover.
        if left_growing_inward != right_growing_inward:

            # Stigende midtparti kan være før toppen eller etter bunnen.
            if direction_right and left_growing_inward:
                if x[mid] < x[l]:
                    direction_right = False

            # Synkende midtparti kan være før bunnen eller etter toppen.
            elif not direction_right and right_growing_inward:
                if x[mid] < x[r]:
                    direction_right = True

        if direction_right:
            l = mid + 1
        else:
            r = mid - 1

    # Bare 1–3 elementer gjenstår, så dette tar konstant tid.
    return max(x[i] for i in range(l, r + 1))
        


    
        

        


# Hardkodete tester på format: (x, svar)
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]

# En liste som ikke kan skrives til
class List:
    def __init__(self, li):
        self.__internal_list = li

    def __getitem__(self, key):
        return self.__internal_list[key]

    def __len__(self):
        return len(self.__internal_list)

    def __setitem__(self):
        raise NotImplementedError(
            "Du skal ikke trenge å skrive til listen"
        )

# Genererer tilfeldige instanser med svar
def generate_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        x = random.sample(range(5*n), k=n)
        answer = max(x)
        t = x.index(answer)
        x = sorted(x[:t]) + [answer] + sorted(x[t + 1:], reverse=True)
        t = random.randint(0, n)
        x = x[t:] + x[:t]
        yield x, answer


if generate_random_tests:
    if seed:
        random.seed(seed)

    tests.extend(generate_examples(random_tests, n_lower, n_upper))


failed = False
for x, answer in tests:
    x_ro = List(x[:])
    student = find_maximum(x_ro)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
Koden ga feil svar for følgende instans:
x: {x}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")