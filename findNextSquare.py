""" 7kyu
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.
"""

def find_next_square(sq):
    import math
    if float(math.sqrt(sq)).is_integer():
        return (int(math.sqrt(sq)) + 1) ** 2
    return -1


print(find_next_square(121))            # return 144
print(find_next_square(625))            # return 676
print(find_next_square(319225))         # return 320356
print(find_next_square(15241383936))    # return 15241630849
print(find_next_square(155))            # return -1
print(find_next_square(342786627))      # return -1