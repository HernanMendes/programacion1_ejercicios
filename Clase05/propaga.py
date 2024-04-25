def propagar(fosforos):
    propaga = False
    i = 0
    while i < len(fosforos):
        if fosforos[i] == 1:
            propaga = True
        elif fosforos[i] == 0 and propaga:
            fosforos[i] = 1
        elif fosforos[i] == -1:
            propaga = False
            fosforos[i] = -1
        i += 1

    propaga = False
    i = len(fosforos)
    while i > 0:
        i -= 1
        if fosforos[i] == 1:
            propaga = True
        elif fosforos[i] == 0 and propaga:
            fosforos[i] = 1
        elif fosforos[i] == -1:
            propaga = False
            fosforos[i] = -1

    return fosforos
