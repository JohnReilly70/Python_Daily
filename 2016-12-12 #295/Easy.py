def letter_by_letter(string1, string2):
    string2 = list(string2)
    print("".join(string2))
    for i, v in enumerate(list(string1)):
        try:
            string2[i] = v
            print("".join(string2))
        except IndexError:
            break


letter_by_letter("Steve", "bob")

