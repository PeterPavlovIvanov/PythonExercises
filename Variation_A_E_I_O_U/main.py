count = 1
word = ""
letters = ['a', 'e', 'i', 'o', 'u']

for A in letters:
    for E in letters:
        for I in letters:
            for O in letters:
                for U in letters:
                    if (A != E) & (A != I) & (A != O) & (A != U):
                        if (E != I) & (E != O) & (E != U):
                            if (I != O) & (I != U):
                                if O != U:
                                    word += A + E + I + O + U
                                    print(f'{count}: {word}')
                                    count += 1
                    word = ""
