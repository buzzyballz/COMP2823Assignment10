package main;

import java.util.Arrays;
/**
 *  Union Box
 *
 *  From a graph of boxes, get the union of boxes
 *
 *  Example:
 *  4 |                   ______
 *  3 |     ____         |    __|_______________
 *  2 |   _|__  |    ____|   |  |               |
 *  1 |  | |  | |   |    |   |  |               |
 *  0 |__|_|__|_|___|____|___|__|_______________|________
 *       2 4  7 9   13   18  22 25              40
 *
 *  union = [
 *      # Illustrates the first set of boxes:
 *      (2, 0), (2, 2), (4, 2), (4, 3), (9, 3), (9, 0),
 *      # Illustrates the second set of boxes:
 *      (13, 0), (13, 2), (18, 2), (18, 4), (25, 4), (25, 3), (40, 3), (40, 0)
 *  ]
 *
 *  (Visual representation):
 *
 *   4 |                    _____
 *   _
 *   3 |      ____         |      |_______________
 *   2 |    _|    |    ____|                      |
 *   1 |   |      |   |                           |
 *   0 |___|______|___|___________________________|________
 *         2 4  7 9   13   18  22 25              40
 *
 */
public class UnionBox implements UnionInterface {

    /**
     * Merge the two "boxes" together.
     *    ____           ____
     *  _|__  |        _|    |
     * | |  | |  ==>  |      |
     * |_|__|_|       |      |
     *
     * Example:
     * input:
     *     l: [ (2,0), (2,2), (7,2), (7,0) ]
     *     r: [ (4,0), (4,3), (9,3), (9,0) ]
     * return:
     *     [ (2,0), (2,2), (4,2), (4,3), (9,3), (9,0) ]
     *
     * @param l: Array of coordinates representing one box.
     * @param r: Array of coordinates representing another box.
     * @return: The merged coordinates to present.
     */
    public Coordinate[] merge(Coordinate[] l, Coordinate[] r) {
        // TODO implement me
        return new Coordinate[0];
    }

    /**
     * Performs the union of a list of boxes (in the form of x, y coordinate tuples)
     *
     * e.g. box_list = [
     *          [(2,2), (2, 2), (7, 2), (7, 0)],
     *          [(4,0), (4,3), (9,3), (9,0)]
     *      ]
     * @param boxList: List of boxes represented as coordinates.
     * @return: The union of all the boxes.  (As presented in the example above)
     */
    public Coordinate[] union(Coordinate[][] boxList) {
        if (boxList.length == 0) {
            return new Coordinate[0];
        } else if (boxList.length == 1) {
            return boxList[0];
        } else if (boxList.length == 2) {
            Coordinate[] leftBox = boxList[0];
            Coordinate[] rightBox = boxList[1];
            Coordinate[] merged = this.merge(leftBox, rightBox);
            return merged;
        }

        // Else time to do me a recursion
        Coordinate[] leftBoxes = this.union(Arrays.copyOfRange(boxList, 0, boxList.length / 2));
        Coordinate[] rightBoxes = this.union(Arrays.copyOfRange(boxList, boxList.length / 2, boxList.length));
        Coordinate[] merged = this.merge(leftBoxes, rightBoxes);
        return merged;
    }
}
