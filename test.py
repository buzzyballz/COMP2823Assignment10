from union_box import UnionBox
from box import Box

ub = UnionBox()

# Example Test Case

"""
Tests the example of multiple boxes

4 |                   ______
3 |     ____         |    __|_______________
2 |   _|__  |    ____|   |  |               |
1 |  | |  | |   |    |   |  |               |
0 |__|_|__|_|___|____|___|__|_______________|________
     2 4  7 9   13   18  22 25              40


"""

boxes = []
boxes.append(Box(2, 7, 2))
boxes.append(Box(4, 9, 3))
boxes.append(Box(13, 18, 2))
boxes.append(Box(18, 25, 4))
boxes.append(Box(22, 40, 3))

coord_list = [x.get_box_coordinates() for x in boxes]

expected_res = [(2, 0), (2, 2), (4, 2), (4, 3), (9, 3), (9, 0),
                (13, 0), (13, 2), (18, 2), (18, 4), (25, 4),
                (25, 3), (40, 3), (40, 0)]

res = ub.union(coord_list)

print("Expected: {}".format(expected_res))
print("Got: {}".format(res))
print("Pass: {}".format(res == expected_res))


# Test case Recursive Gotcha


"""
Tests the recursive box test.
10   _______________
9 | |  _________   |
8 | | |  ______  | |
7 | | | |      | | |
6 | | | |      | | |
5 | | | |      | | |
4 | | | |      | | |
3 | | | |      | | |
2 | | | |  _   | | |
1 | | | | | |  | | |
0 |_|_|_|_|_|__|_|_|_____
    2 4 6 7 10 131517
"""

ub = UnionBox()

boxes = []
boxes.append(Box(2, 17, 10))
boxes.append(Box(4, 15, 9))
boxes.append(Box(6, 13, 8))
boxes.append(Box(7, 10, 2))
coord_list = [x.get_box_coordinates() for x in boxes]

expected_res = Box(2, 17, 10).get_box_coordinates()

res = ub.union(coord_list)

print("Expected: {}".format(expected_res))
print("Got: {}".format(res))
print("Pass: {}".format(res == expected_res))
