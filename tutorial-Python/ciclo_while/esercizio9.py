s = input("Inserisci una stringa: ")
i = 0

while i < len(s):
    if s[i] not in "aeiouAEIOU":
        print(s[i], end="")
    i += 1
