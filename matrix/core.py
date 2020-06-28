from IPython.display import Latex


class Matrix2D:
    def __init__(self, data: list):
        self._data = data

    def __repr__(self):
        matrix_string = ""
        for row in self._data:
            matrix_string += "\n{}".format(row)
        return matrix_string.lstrip("\n")

    def __mul__(self, constant):
        assert isinstance(constant, int) or isinstance(constant, float), 'Not a constant'
        result = []

        for r in range(self.shape[0]):
            current_row = []
            for c in range(self.shape[1]):
                current_row.append(self[r][c] * constant)
            result.append(current_row)
        return Matrix2D(result)

    def latex(self):
        string = "\\begin{bmatrix} \n "
        for row in self._data:
            for c in row:
                string += '{} & '.format(c)
            string = string.rstrip('& ')
            string += r" \\ "
        string += "\n\\end{bmatrix}"
        return Latex(string)

    @property
    def shape(self):
        return len(self._data), len(self._data[0])

    def __getitem__(self, item):
        return self._data[item]

    def __eq__(self, other):
        assert isinstance(other, Matrix2D)
        assert self.shape[0] == other.shape[0]
        assert self.shape[1] == other.shape[1]

        try:
            for row_idx in range(self.shape[0]):
                for col_idx in range(self.shape[1]):
                    assert self[row_idx][col_idx] == other[row_idx][col_idx]
            return True
        except AssertionError:
            return False

    def __add__(self, other):
        assert self.shape[0] == other.shape[0]
        assert self.shape[1] == other.shape[1]
        result = []

        for r in range(self.shape[0]):
            current_row = []
            for c in range(self.shape[1]):
                current_row.append(self[r][c] + other[r][c])
            result.append(current_row)
        return Matrix2D(result)

    def cross(self, other):
        assert isinstance(other, Matrix2D), 'Invalid argument'
        assert self.shape[1] == self.shape[0], 'Incorrect dimensions'
        data = []

        for r1 in range(self.shape[0]):
            current_row = []
            for c1 in range(self.shape[1]):
                val_sum = 0
                for c2 in range(other.shape[1]):
                    val_sum += self[r1][c2] * other[c2][c1]
                current_row.append(val_sum)
            data.append(current_row)
        return Matrix2D(data)


class ZeroMatrix2D(Matrix2D):
    def __init__(self, shape: tuple):
        n_rows, n_cols = shape[0], shape[1]
        mat = []
        for r in range(n_rows):
            current_row = []
            for c in range(n_cols):
                current_row.append(0)
            mat.append(current_row)
        Matrix2D.__init__(self, mat)


class IdentityMatrix2D(Matrix2D):
    def __init__(self, shape: int):
        n_rows, n_cols = shape, shape
        mat = []
        for r in range(n_rows):
            current_row = []
            for c in range(n_cols):
                if r == c:
                    current_row.append(1)
                else:
                    current_row.append(0)
            mat.append(current_row)
        Matrix2D.__init__(self, mat)
