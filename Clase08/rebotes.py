
def rebotar(altura, rebotes_max):
    altura = int(altura)
    rebotes_max = int(rebotes_max)

    amortiguacion = 3/5
    cant_rebotes = 1
    while cant_rebotes <= rebotes_max:
        altura *= amortiguacion
        print(cant_rebotes, round(altura, 4))
        cant_rebotes += 1


if __name__ == '__main__':
    import sys
    altura = sys.argv[1]
    rebotes_max = sys.argv[2]
    rebotar(altura, rebotes_max)
