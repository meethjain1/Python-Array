import numpy as np
array_1d = np.arange(16)
print(f"Original 1D Array : {array_1d}")

    # Reshaping 1D Array to 2D Array
array_2d = array_1d.reshape(4, 4)
print(f"Reshaped to 4x4 :\n{array_2d}")

    # Flattening 2D Array to 1D Array
flattened_arr = array_2d.flatten()
print(f"Flattened Array : {flattened_arr}")

    # Transposing the 2D Array
transposed_arr = array_2d.T
print(f"Transposed Array :\n{transposed_arr}")
print("-"*50)
