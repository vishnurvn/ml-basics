import unittest

from core import Matrix2D, IdentityMatrix2D


class TestAddition(unittest.TestCase):
    def test_add_square_matrix(self):
        matrix_one = Matrix2D([[1, 1], [1, 1]])
        result = matrix_one + matrix_one
        self.assertTrue(isinstance(result, Matrix2D))
        target = Matrix2D([[2, 2], [2, 2]])
        self.assertTrue(result == target)

    def test_add_rectangular_matrix(self):
        matrix_one = Matrix2D([[1, 1], [1, 1], [1, 1]])
        matrix_two = Matrix2D([[0, 2], [2, 0], [2, 2]])
        result = matrix_one + matrix_two
        target = Matrix2D([[1, 3], [3, 1], [3, 3]])
        self.assertTrue(isinstance(result, Matrix2D))
        self.assertTrue(result == target)

    def test_invalid_matrix_addition(self):
        pass


class TestSubtraction(unittest.TestCase):
    pass


class TestScalarMultiplication(unittest.TestCase):
    pass


class TestMatrixMultiplication(unittest.TestCase):
    def test_multiplication_valid2d(self):
        matrix_one = Matrix2D([[1, 0], [0, 2]])
        matrix_two = Matrix2D([[3, 4], [5, 6]])
        result = matrix_one.cross(matrix_two)
        target = Matrix2D([[3, 4], [10, 12]])
        self.assertTrue(isinstance(result, Matrix2D))
        self.assertListEqual(result._data, target._data)

    def test_multiplication_valid3d(self):
        matrix_one = Matrix2D([[1, 0, 1], [0, 2, 0], [3, 0, 3]])
        matrix_two = Matrix2D([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        result = matrix_one.cross(matrix_two)
        target = Matrix2D([[2, 2, 2], [2, 2, 2], [6, 6, 6]])
        self.assertTrue(isinstance(result, Matrix2D))
        self.assertListEqual(result._data, target._data)

    def test_multiplication_identity(self):
        matrix_one = Matrix2D([[2, 2], [2, 2]])
        identity_matrix = IdentityMatrix2D(shape=2)
        result = matrix_one.cross(identity_matrix)
        self.assertTrue(result == matrix_one)
