frase = tuple(str("Thus, Adam and Eve came to be the father and mother of all humankind. Later, when a flood wiped out most of the" \
        " earth’s population, four couples survived—Noah and his wife along with their three sons and their wives. The " \
        "Bible teaches that all of us descended from Noah’s sons.").split(" "))
for n in frase:
    print("A palabra", end=" ")
    print(n.upper(), end=" ")
    print("tem as seguintes vogais:", end=" ")
    for x in range(0,len(n)):
        if n[x].upper() in "AEIOU":
            print(n[x],end=" ")
    print("")

