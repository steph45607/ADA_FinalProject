def createAux(W):
    aux = [0] * len(W)

    # for index 0, it will always be 0 so starting from index 1
    i = 1
    # m can also be viewed as index of first mismatch
    m = 0
    while i < len(W):
        # prefix = suffix till m-1
        if W[i] == W[m]:
            m += 1
            aux[i] = m
            i += 1
        # we will check the index of previous possible prefix.
        elif W[i] != W[m] and m != 0:
            m = aux[m - 1]
        else:
            aux[i] = 0
            i += 1

    return aux


def finPattern(pat, txt):
    found = False
    # this method is from above code snippet.
    aux = createAux(pat)

    i = 0
    j = 0
    while j < len(txt):
        # We need to handle 2 conditions when there is a mismatch
        if pat[i] != txt[j]:
            # 1st condition
            if i == 0:
                # starting again from the next character in the text T
                j += 1
            else:
                # aux[i-1] will tell from where to compare next
                i = aux[i - 1]
        else:
            i += 1
            j += 1
            # we found the pattern
            if i == len(pat):
                found = True
                print("found pattern at " + str(j - i))
                # to find more patterns
                i = aux[i - 1]

    if not found:
        print("This pattern is not present in the text given")


pat = "んに"
txt = "こんにちはこんにちは私の名前はディボです"

finPattern(pat, txt)
