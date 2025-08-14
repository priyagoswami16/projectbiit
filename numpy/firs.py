import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)


# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# Create a 0-D array with value 42

import numpy as np
arr = np.array(42)
print(arr)


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
# Create a 1-D array containing the values 1,2,3,4,5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)