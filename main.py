import sys

#This function reads the matrix from the provided test cases usuing command line arguments
def read_matrix(filename):
    try:
        f = open(filename)
    except IOError:
        print(f"Error: Cannot open file {filename}")
        sys.exit(1)
    tokens = f.read().split()
    f.close()
    if len(tokens) == 0:
        print(f"Error: Empty file {filename}")
        sys.exit(1)

    n = int(tokens[0])
    if n < 0:
        print("Error: Invalid matrix size.")
        sys.exit(1)

    expected = 1 + n * n
    if len(tokens) < expected:
        print("Error: Matrix entries missing no the correct dimensions.")
        sys.exit(1)

    M = []
    index = 1
    for i in range(n):
        row = []
        for j in range(n):
            value = int(tokens[index])
            row.append(value)
            index += 1
        M.append(row)
    return M


def is_reflexive(M):
    n = len(M)
    for i in range(n):
        if M[i][i] != 1:
            return False
    return True


def is_irreflexive(M):
    n = len(M)
    for i in range(n):
        if M[i][i] != 0:
            return False
    return True


def is_symmetric(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False
    return True


def is_antisymmetric(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] == 1 and M[j][i] == 1:
                return False
    return True


def is_asymmetric(M):
    if not is_irreflexive(M):
        return False
    if not is_antisymmetric(M):
        return False
    return True


def is_transitive(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if M[i][j] == 1 and M[j][k] == 1 and M[i][k] == 0:
                    return False
    return True


def print_matrix(M):
    n = len(M)
    print(n)
    for row in M:
        line = ''
        for x in row:
            line += str(x) + ' '
        print(line.strip())


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    M = read_matrix(sys.argv[1])

    r = is_reflexive(M)
    ir = is_irreflexive(M)
    s = is_symmetric(M)
    asym = is_antisymmetric(M)
    a = is_asymmetric(M)
    t = is_transitive(M)

    print("Reflexive: " + ("Yes" if r else "No"))
    print("Irreflexive: " + ("Yes" if ir else "No"))
    print("Symmetric: " + ("Yes" if s else "No"))
    print("Antisymmetric: " + ("Yes" if asym else "No"))
    print("Asymmetric: " + ("Yes" if a else "No"))
    print("Transitive: " + ("Yes" if t else "No"))

    eq = r and s and t
    print("Equivalence relation: " + ("Yes" if eq else "No"))

    if not eq:
        # Reflexive closure
        if not r:
            R = []
            for i in range(len(M)):
                row = []
                for j in range(len(M)):
                    if i == j:
                        row.append(1)
                    else:
                        row.append(M[i][j])
                R.append(row)
            print("\nReflexive closure:")
            print_matrix(R)
        else:
            R = M

        # Symmetric closure
        if not s:
            S = []
            n = len(R)
            for i in range(n):
                row = []
                for j in range(n):
                    if R[j][i] == 1:
                        row.append(1)
                    else:
                        row.append(R[i][j])
                S.append(row)
            print("\nSymmetric closure:")
            print_matrix(S)
        else:
            S = R

        # Transitive closure
        if not t:
            T = []
            n = len(S)
            # Copy S into T
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(S[i][j])
                T.append(row)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if T[i][k] == 1 and T[k][j] == 1:
                            T[i][j] = 1
            print("\nTransitive closure:")
            print_matrix(T)

if __name__ == '__main__':
    main()