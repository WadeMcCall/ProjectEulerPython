from lib.convenience import are_permutations, count_digits
import itertools

def cubicNumberGenerator():
    for i in itertools.count(1):
        yield i ** 3

def findAllCubesWithxDigits(x):
    gen = cubicNumberGenerator()
    cubes = []

    for cube in gen:
        digits = count_digits(cube)
        if digits < x:
            continue
        elif digits > x:
            return cubes
        else:
            cubes.append(cube)

def find5LongPerms(cubes):
    for i in range(len(cubes)):
        numPerms = 0
        perms = []
        for j in range(i, len(cubes)):
            if are_permutations(str(cubes[i]), str(cubes[j])):
                numPerms += 1
                perms.append(cubes[j])
        if numPerms >= 5:
            print(cubes[i], perms)
            return perms


def main():
    numdigits = 4
    cubes = findAllCubesWithxDigits(numdigits)
    while True:
        perms = find5LongPerms(cubes)
        if perms is not None:
            print(perms[0])
            return
        numdigits += 1
        cubes = findAllCubesWithxDigits(numdigits)
        print(numdigits)

if __name__ == "__main__":
    main()