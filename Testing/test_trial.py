#Test
from nearest_square import nearest_square
# print("Nearest square <=5:",nearest_square(5))
# print("Nearest square <=-12:",nearest_square(-12))
# print("Nearest square <=9:",nearest_square(9))
# print("Nearest square <=23:",nearest_square(23))
# assert(nearest_square(23) == 16)

def test_nearest_square_5():
    assert(nearest_square(5) == 4)

def test_nearest_square_n12():
    assert(nearest_square(-12) == 0)

def test_nearest_square_9():
    assert(nearest_square(9) == 9)
    assert(17 == 16)

def test_nearest_square_23():
    assert(nearest_square(23) == 16)
    