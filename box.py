class Box:
    """
    Box class

    Provides the primitives that creates a "box" on the graph.
    Attributes:
        - left: left X coordinate.
        - right: right X coordinate.
        - height: height of the box (Y coordinate)

    Assumptions:
        - There are no negative box heights.
        - Each box will take up 1 or more units (all integers)
        - Left will always be < right.
    """

    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

    def get_left(self):
        """
        Box's left X coordinate.
        :return: This box's left position.
        """
        return self.left

    def get_right(self):
        """
        Box's right X coordinate.
        :return: This box's right position.
        """
        return self.right

    def get_height(self):
        """
        The box's height - equivalent to the Y coordinate.
        :return: Box height.
        """
        return self.height

    def get_top_left(self):
        """
        Returns the (x, y) coordinate for the box top left corner.
        :return: (x, y) of top left.
        """
        return self.left, self.height

    def get_bottom_left(self):
        """
        Returns the (x, y) coordinate for the box bottom left corner.
        :return: (x, y) of the bottom left. (Note: y will always be 0)
        """
        return self.left, 0

    def get_top_right(self):
        """
        Returns the (x, y) coordinate for the box top right corner.
        :return: (x, y) of top right.
        """
        return self.right, self.height

    def get_bottom_right(self):
        """
        Returns the (x, y) coordinate for the box bottom right corner.
        :return: (x, y) of the bottom right. (Note: y will always be 0)
        """
        return self.right, 0

    def get_box_coordinates(self):
        """
        Returns the coordinates of the box.
        :return: Array[bottom_left, top_left, top_right, bottom_right] coordinates.
        """
        return [
            (self.left, 0),
            (self.left, self.height),
            (self.right, self.height),
            (self.right, 0)
        ]
