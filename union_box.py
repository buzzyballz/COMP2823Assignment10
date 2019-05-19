
from union_interface import UnionInterface


class UnionBox(UnionInterface):
    """
    Union Box

    From a graph of boxes, get the union of boxes

    Example:
    4 |                   ______
    3 |     ____         |    __|_______________
    2 |   _|__  |    ____|   |  |               |
    1 |  | |  | |   |    |   |  |               |
    0 |__|_|__|_|___|____|___|__|_______________|________
         2 4  7 9   13   18  22 25              40

    union = [
        # Illustrates the first set of boxes:
        (2, 0), (2, 2), (4, 2), (4, 3), (9, 3), (9, 0),
        # Illustrates the second set of boxes:
        (13, 0), (13, 2), (18, 2), (18, 4), (25, 4), (25, 3), (40, 3), (40, 0)
    ]

    (Visual representation):

     4 |                    ______
     3 |      ____         |      |_______________
     2 |    _|    |    ____|                      |
     1 |   |      |   |                           |
     0 |___|______|___|___________________________|________
           2 4  7 9   13   18  22 25              40

    """

    def merge(self, l, r):
        """
        Merge the two "boxes" together.
           ____           ____
         _|__  |        _|    |
        | |  | |  ==>  |      |
        |_|__|_|       |      |

        Example:
        input:
            l: [ (2,0), (2,2), (7,2), (7,0) ]
            r: [ (4,0), (4,3), (9,3), (9,0) ]
        return:
            [ (2,0), (2,2), (4,2), (4,3), (9,3), (9,0) ]

        :param l: Array of coordinates representing one box.
        :param r: Array of coordinates representing another box.
        :return: The merged coordinates to present.
        """
        # TODO implement me.
        # Start from left side and clockwise
        print(l)
        print(r)
        res = []
        # initialise with left-bottom corner
        res.append(l[0])
        res.append(l[1])
        # Two cases - left is higher vs right is higher
        # Height will be the y2 - y1
        left_height = l[1][1] - l[0][1]
        right_height = r[1][1] - r[0][1]
        # Case right is higher
        if left_height > right_height:
            # Append the left top corner
            res.append(l[2])
        else:
            res.append(r[1])
        merged = (r[1][0], l[2][1])
        res.append(merged)
        res.append(r[2])
        res.append(r[3])
        return res

    def union(self, box_list):
        """
        Performs the union of a list of boxes (in the form of x, y coordinate tuples)

        e.g. box_list = [ [(2,2), (2, 2), (7, 2), (7, 0)], [(4,0), (4,3), (9,3), (9,0)] ]
        :param box_list: List of boxes represented as coordinates.
        :return: The union of all the boxes.  (As presented in the example above)
        """
        if not box_list:
            return []

        if len(box_list) == 1:
            return box_list[0]

        if len(box_list) == 2:
            left_box = box_list[0]
            right_box = box_list[1]
            merged = self.merge(left_box, right_box)
            return merged

        # Else, time to do me a recursion
        left_list = self.union(box_list[:int(len(box_list) / 2)])
        right_list = self.union(box_list[int(len(box_list) / 2):])
        merged = self.merge(left_list, right_list)
        return merged
