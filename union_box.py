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

    def union(self, box_list):
        """
        Performs the union of a list of boxes (in the form of x, y coordinate tuples)

        e.g. box_list = [ [(2,2), (2, 2), (7, 2), (7, 0)], [(4,0), (4,3), (9,3), (9,0)] ]
        :param box_list: List of boxes represented as coordinates.
        :return: The union of all the boxes.  (As presented in the example above)
        """

        new_box_list = []
        for box in box_list:
            left = box[0][0]
            height = box[1][1]
            right = box[2][0]
            new_box_list.append((left, height, right))

        edges = []
        edges.extend([box[0], box[2]] for box in new_box_list)
        new_edges = []
        for i in edges:
            new_edges.append(i[0])
            new_edges.append(i[1])
        new_edges = sorted(new_edges)

        current = 0
        points = []
        points.append((new_edges[0],0))

        for i in new_edges:
            active = []
            active.extend(box for box in new_box_list if (box[0] <= i and box[2] > i))
            if not active:
                current = 0
                points.append((i, 0))
                continue
            max_h = max(box[1] for box in active)
            if max_h != current:
                current = max_h
                points.append((i, max_h))
        res = []
        for i in range(len(points)):
            if i >= 2:
                res.append((points[i][0], points[i-1][1]))

            res.append(points[i])


        return res
