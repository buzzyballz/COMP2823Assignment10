from box import Skyline
from box import Strip
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
        res = []
        h1 = 0
        h2 = 0
        i = 0
        j = 0
        print(l)
        print(r)
        #while i < len(l) && j < len(r):
            #if l.arr[i].left < r.arr[j].left:


        return res

    def union(self, box_list):
        """
        Performs the union of a list of boxes (in the form of x, y coordinate tuples)

        e.g. box_list = [ [(2,2), (2, 2), (7, 2), (7, 0)], [(4,0), (4,3), (9,3), (9,0)] ]
        :param box_list: List of boxes represented as coordinates.
        :return: The union of all the boxes.  (As presented in the example above)
        """
        '''
        if not box_list:
            return []

        if len(box_list) == 1:
            return box_list[0]

        if len(box_list) == 2:
            left_box = box_list[0]
            right_box = box_list[1]
            merged = self.merge(left_box, right_box)
            return merged
        '''
        new_box_list = []
        for box in box_list:
            left = box[0][0]
            height = box[1][1]
            right = box[2][0]
            new_box_list.append((left, height, right))

        edges = []
        edges.extend([building[0], building[2]] for building in new_box_list)
        edges = sorted(sum(edges, []))  # sorting and flatening the list of building edges

        current = 0
        points = []
        points.append((edges[0],0))

        for i in edges:
            active = []
            active.extend(building for building in new_box_list if (building[0] <= i and building[2] > i))
            # current observed point is within borders of these buildings (active buildings)
            if not active:
                # if there is no active buildings, highest point is 0
                current = 0
                points.append((i, 0))
                continue
            max_h = max(building[1] for building in active)
            if max_h != current:
                # if current highest point is lower then highest point of current active buildings change current highest point
                current = max_h
                points.append((i, max_h))
        res = []
        for i in range(len(points)):
            if i >= 2:
                res.append((points[i][0], points[i-1][1]))

            res.append(points[i])


        return res

    def helper(self, box_list, l, h):
        if(l == h):
            res = Skyline(2)
            res.append(Strip(box_list[l][0], box_list[l][1]))
            res.append(Strip(box_list[l][2], 0))
            return res

        # Else, time to do me a recursion
        left_list = self.helper(box_list, l, int((l+2)/2))
        right_list = self.helper(box_list, 1+int((l+2)/2), h)
        merged = self.merge(left_list, right_list)
        return merged
