# Generate a list of all permutations for the numbers 1 through n
def perm(n):
    l = list(range(1, n+1))
    perm_recursive(n, l)


def perm_recursive(n, l):
    if n == 1:
        print(l)
    else:
        for i in range(n):
            perm_recursive(n - 1, l)
            if n % 2 == 1:
                i = 1
            l[i], l[n - 1] = l[n - 1], l[i]


# Get the mth permutation from the list of generated permutations
def search_perm(n, m):
    l = list(range(1, n+1))
    counter = [0]
    c2 = [0]
    search_perm_recursive(n, l, 5, counter, c2)


def search_perm_recursive(n, l, m, counter, c2):
    c2[0] += 1
    print(c2[0])
    if n == 1:
        counter[0] += 1
        if counter[0] == m:
            print(l)
    else:
        for i in range(n):
            search_perm_recursive(n - 1, l, m, counter, c2)
            if n % 2 == 1:
                i = 1
            l[i], l[n - 1] = l[n - 1], l[i]


if __name__ == '__main__':
    perm(4)
    print('\n')
    search_perm(4, 5)
