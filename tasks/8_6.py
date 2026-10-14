#!/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 1000 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True.
use_extra_tests = False


def compatibility_graph(donors, recipients, k):
    if len(donors) == 0:
        return []
    
    donor_edges = [[] for _ in donors]

    for don_i, don in enumerate(donors):
        for rec_i, rec in enumerate(recipients):
            n = 0
            for j in range(min(len(don), len(rec))):
                if don[j] == rec[j]:
                    n += 1
            if n >= k:
                donor_edges[don_i].append(rec_i)

    return donor_edges
                    


# Hardkodete tester på format: (donors, recipients, k), answer
tests = [
    (([], [], 0), []),
    (([["ab"]], [], 0), [[]]),
    (([], [["ab"]], 0), []),
    (([["ab"]], [["ab"]], 1), [[0]]),
    (([["ab"]], [["ac"]], 1), [[]]),
    (([["ab"]], [["ac"]], 0), [[0]]),
    (([["ab"]], [["ac"], ["ab"]], 1), [[1]]),
    (([["ab"], ["ac"]], [["ab"]], 1), [[0], []]),
    (([["ab"], ["ac"]], [["ac"], ["ab"]], 1), [[1], [0]]),
    (([["ab"], ["ac"]], [["ac"], ["ab"]], 0), [[0, 1], [0, 1]]),
    (([["ab", "ac"]], [["ac", "ab"]], 1), [[]]),
    (
        ([["ab", "12"], ["ac", "22"]], [["ab", "22"], ["ac", "22"]], 2),
        [[], [1]],
    ),
    (([], [[], []], 1), []),
    (
        (
            [],
            [
                ["IRk", "s", "S", "9zF"],
                ["V2xa", "JqZV", "PxbUl", "WbKZw"],
                ["V2xa", "s", "PxbUl", "7NoD"],
            ],
            2,
        ),
        [],
    ),
    (
        (
            [["dwfAa", "bt7c", "d1iP"], ["dwfAa", "bt7c", "d1iP"]],
            [
                ["dwfAa", "H", "vN82"],
                ["dwfAa", "bt7c", "vN82"],
                ["dwfAa", "H", "vN82"],
            ],
            4,
        ),
        [[], []],
    ),
    (
        ([["oLfIi", "wPAw"], ["gTnJf", "wPAw"], ["gTnJf", "LERhd"]], [], 1),
        [[], [], []],
    ),
    (
        ([["uw"], ["uw"], ["Lb"], ["uw"]], [["4r7lb"], ["Lb"]], 1),
        [[], [], [1], []],
    ),
    (([["wcaP", "zXgJ"]], [], 1), [[]]),
    (([], [], 1), []),
    (
        (
            [["w", "oA", "oIa"]],
            [["w", "oA", "oIa"], ["d", "oA", "vodI"], ["w", "oA", "5"]],
            1,
        ),
        [[0, 1, 2]],
    ),
    (([], [["x", "7HyQl", "Wr38", "Ww"], ["x", "7HyQl", "yq", "Ww"]], 9), []),
    (([["rX1", "z"], ["rX1", "ZY2w"]], [["qX1Ph", "7a0M"]], 1), [[], []]),
]

failed = False
for test_case, answer in tests:
    donors, recipients, k = test_case
    student = compatibility_graph(donors, recipients, k)
    try:
        incorrect = len(student) != len(answer) or not all(
            [sorted(stu) == ans for stu, ans in zip(student, answer)]
        )
    except:
        incorrect = True

    if incorrect:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
Koden feilet for følgende instans.
donors: [
    {(chr(10) + '    ').join(map(str, donors))}
]
recipients: [
    {(chr(10) + '    ').join(map(str, recipients))}
]
k: {k}

Ditt svar: {student}
Riktig svar: {answer}
        """)

if use_extra_tests:
    with open("tests_compatibility_graph.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            donors, recipients, k, answer = map(eval, line.strip().split(" | "))
            extra_tests.append(((donors, recipients, k), answer))

    n_failed = 0
    for test_case, answer in extra_tests:
        donors, recipients, k = test_case
        student = compatibility_graph(donors, recipients, k)
        try:
            incorrect = len(student) != len(answer) or not all(
                [sorted(stu) == ans for stu, ans in zip(student, answer)]
            )
        except:
            incorrect = True

        if incorrect:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans.
donors: [
    {(chr(10) + '    ').join(map(str, donors))}
]
recipients: [
    {(chr(10) + '    ').join(map(str, recipients))}
]
k: {k}

Ditt svar: {student}
Riktig svar: {answer}
                """)
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
