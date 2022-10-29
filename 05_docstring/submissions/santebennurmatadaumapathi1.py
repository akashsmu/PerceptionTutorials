def afunc(array1: list, array2: list, mode: str = "+", pow: int = 2) -> list:
    """Performs arthimetic operations on the data.

    Performs addition or subtraction of the arrays and raises each element
    to the power.

    Args:
        array1 ,array2: list of elements. Integer or floating type.
        mode: a symbol of the operation to be performed. A string type.
        pow: A integer. which raises the each element of the array

    Returns:
       A list of elements after the "mod" operation raised by "pow". For
        example:

        [6.25 , 9, 11.25]


    Raises:
        ValueError: An error when the mode is not addition (+) or subtraction(-)  # noqa E501
    """

    assert array1.shape == array2.shape, "size mismatch"
    assert type(pow) == int, "pow should be type int"

    if mode == "+":
        result = array1 + array2
    elif mode == "-":
        result = array1 - array2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result**pow
    return result
