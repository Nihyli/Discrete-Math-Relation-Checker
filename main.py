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

    Matrix = []
    index = 1
    for i in range(n):
        row = []
        for j in range(n):
            value = int(tokens[index])
            row.append(value)
            index += 1
        Matrix.append(row)
    return Matrix


def is_reflexive(Matrix):
    n = len(Matrix)
    for i in range(n):
        if Matrix[i][i] != 1:
            return False
    return True


def is_irreflexive(Matrix):
    n = len(Matrix)
    for i in range(n):
        if Matrix[i][i] != 0:
            return False
    return True


def is_symmetric(Matrix):
    n = len(Matrix)
    for i in range(n):
        for j in range(n):
            if Matrix[i][j] != Matrix[j][i]:
                return False
    return True


def is_antisymmetric(Matrix):
    n = len(Matrix)
    for i in range(n):
        for j in range(n):
            if i != j and Matrix[i][j] == 1 and Matrix[j][i] == 1:
                return False
    return True


def is_asymmetric(Matrix):
    if not is_irreflexive(Matrix):
        return False
    if not is_antisymmetric(Matrix):
        return False
    return True


def is_transitive(Matrix):
    n = len(Matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if Matrix[i][j] == 1 and Matrix[j][k] == 1 and Matrix[i][k] == 0:
                    return False
    return True


def print_matrix(Matrix):
    n = len(Matrix)
    print(n)
    for row in Matrix:
        line = ''
        for x in row:
            line += str(x) + ' '
        print(line.strip())


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    Matrix = read_matrix(sys.argv[1])

    reflexive = is_reflexive(Matrix)
    irreflexive = is_irreflexive(Matrix)
    symmetric = is_symmetric(Matrix)
    antisymmetric = is_antisymmetric(Matrix)
    asymmetric = is_asymmetric(Matrix)
    transitive = is_transitive(Matrix)

    print("Reflexive: " + ("Yes" if reflexive else "No"))
    print("Irreflexive: " + ("Yes" if irreflexive else "No"))
    print("Symmetric: " + ("Yes" if symmetric else "No"))
    print("Antisymmetric: " + ("Yes" if antisymmetric else "No"))
    print("Asymmetric: " + ("Yes" if asymmetric else "No"))
    print("Transitive: " + ("Yes" if transitive else "No"))

    equivalence = reflexive and symmetric and transitive
    print("Equivalence relation: " + ("Yes" if equivalence else "No"))

    if not equivalence:
        # Reflexive closure
        if not reflexive:
            reflexive_matrix = []
            for i in range(len(Matrix)):
                row = []
                for j in range(len(Matrix)):
                    if i == j:
                        row.append(1)
                    else:
                        row.append(Matrix[i][j])
                reflexive_matrix.append(row)
            print("\nReflexive closure:")
            print_matrix(reflexive_matrix)
        else:
            reflexive_matrix = Matrix

        # Symmetric closure
        if not symmetric:
            symmetric_matrix = []
            n = len(reflexive_matrix)
            for i in range(n):
                row = []
                for j in range(n):
                    if reflexive_matrix[j][i] == 1:
                        row.append(1)
                    else:
                        row.append(reflexive_matrix[i][j])
                symmetric_matrix.append(row)
            print("\nSymmetric closure:")
            print_matrix(symmetric_matrix)
        else:
            symmetric_matrix = reflexive_matrix

        # Transitive closure
        if not transitive:
            transitive_matrix = []
            n = len(symmetric_matrix)
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(symmetric_matrix[i][j])
                transitive_matrix.append(row)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if transitive_matrix[i][k] == 1 and transitive_matrix[k][j] == 1:
                            transitive_matrix[i][j] = 1
            print("\nTransitive closure:")
            print_matrix(transitive_matrix)

if __name__ == '__main__':
    main()