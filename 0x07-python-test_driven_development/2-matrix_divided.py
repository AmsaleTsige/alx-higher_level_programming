#!/usr/bin/python3
<<<<<<< HEAD
"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""
def matrix_divided(matrix, div):
    ""matrix must be a list of lists of integers/floats
    Returns a new matrix
    """
    newmatrix = []
    length = 0
    # Divides all elements of a matrix
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    # Matrix must be a list of integers or floats, TypeError
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                'of integers/floats')
        if not isinstance(matrix[0], list):
            raise TypeError('matrix must be a matrix (list of lists) '
                    'of integers/floats')
                    if not isinstance(matrix, list):
                    raise TypeError('matrix must be a matrix (list of lists) '
                    'of integers/floats')
                    # mats aof the specified number
                    # with the specified number of decimals
                    newrow.append(round(item / div, 2))
                    to 0
                    if len(matrix[0]) <= 0:
                    raise TypeError('matrix must be a matrix (list of lists) '
                    'of integers/floats')
                    # 1.let's create new matrix with newrow
                    for row in matrix:
                        newrow = []
                        # matrix raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
                        # 2. row is empty
                        if length is 0:
                        length = len(row)
                        # Each row must be the same size, TypeError
                        elif leow of the matrix must have the same size')
                        # 3. each item has to be an integer or float
                        for item in rnot float:
                        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
                        # 4. add content to the row
                        # elements will be divided by div 
                        =======
                        # 2-matrix_divided.py
                        """Defines a matrix division function."""
                        def matrix_divided(matrix, div):
                        """Divide all elements of a matrix.
                        Args:
                        matrix (list): A list of lists of ints or floats.
                        div (int/float): The divisor.
                        Raises:
                        TypeError: If the matrix contains non-numbers.
                        TypeError: If the matrix contains rows of different sizes.
                        TypeError: If div is not an int or float.
                        ZeroDivisionError: If div is 0.
                        Returns:
                        A new matrix representing the result of the division.
                        """
                        if (not isinstance(matrix, list) or matrix == [] or
                        not all(isinstance(row, list) for row in matrix) or
                        not all((isinstance(ele, int) or isinstance(ele, float))
                        for ele in [num for row in matrix for num in row])):
                        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
                        if not all(len(row) == len(matrix[0]) for row in matrix):
                        raise TypeError("Each row of the matrix must have the same size")
                        if not isinstance(div, int) and not isinstance(div, float):
                        raise TypeError("div must be a number")
                        if div == 0:
                        raise ZeroDivisionError("division by zero")
                        return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
                        >>>>>>> d18cc8ec958c9b025557a4d503ca7454310e2fdb
