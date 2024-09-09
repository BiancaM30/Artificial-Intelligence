class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = [0.0, 0.0]

    def transpose(self, mat):
        result = []
        for i in range(len(mat[0])):
            # iterate through columns
            row = []
            for j in range(len(mat)):
                row.append(mat[j][i])
            result.append(row)
        return result

    def multiplication(self, mat1, mat2):
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2[0])):
                sum = 0
                for k in range(len(mat2)):
                    sum += mat1[i][k] * mat2[k][j]
                row.append(sum)
            result.append(row)
        return result

    def determinant_recursive(self, A, total=0):
        # Section 1: store indices in list for row referencing
        indices = list(range(len(A)))

        # Section 2: when at 2x2 submatrices recursive calls end
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val

        # Section 3: define submatrix for focus column and
        #      call this function
        for fc in indices:  # A) for each focus column, ...
            # find the submatrix ...
            As = A  # B) make a copy, and ...
            As = As[1:]  # ... C) remove the first row
            height = len(As)  # D)

            for i in range(height):
                # E) for each remaining row of submatrix ...
                #     remove the focus column elements
                As[i] = As[i][0:fc] + As[i][fc + 1:]

            sign = (-1) ** (fc % 2)  # F)
            # G) pass submatrix recursively
            sub_det = self.determinant_recursive(As)
            # H) total all returns from recursion
            total += sign * A[0][fc] * sub_det

        return total

    def getMatrixMinor(self, m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def inverse(self, m):
        determinant = self.determinant_recursive(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.determinant_recursive(minor))
            cofactors.append(cofactorRow)

        cofactors = self.transpose(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def fit(self, x, y):
        pass

        X = [[1, x[i][0], x[i][1]] for i in range(0, len(x))]
        Y = [[y[i]] for i in range(0, len(y))]

        beta = self.transpose(X)
        beta = self.multiplication(beta, X)
        beta = self.inverse(beta)
        beta = self.multiplication(beta, self.transpose(X))
        beta = self.multiplication(beta, Y)

        w0 = beta[0][0]
        w1 = beta[1][0]
        w2 = beta[2][0]

        self.intercept_, self.coef_ = w0, [w1, w2]

    def predict(self, x):
        if (isinstance(x[0], list)):
            return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in x]
        else:
            return self.intercept_ + self.coef_[0] * x[0] + self.coef_[1] * x[1]

    def meanSquareError(self, myinput, myoutput):
        error = 0.0
        for t1, t2 in zip(self.predict(myinput), myoutput):
            error += (t1 - t2) ** 2
        error = error / len(myoutput)
        return error
