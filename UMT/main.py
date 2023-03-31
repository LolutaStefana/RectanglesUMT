
import unittest


def count_rectangles(points):
    """
    This function returns the number of rectangles that can be created by the given points
    :param points:list of the given points
    :return: number_of_rectangles- integer
    time complexity : O(n^2)

    """

    number_of_points = len(points)
    y_coordinates_count = dict()
    number_of_rectangles = 0
    for i in range(number_of_points): #iterating through each point
        x, y = points[i] # saving the x and y of the current point
        for j in range(number_of_points): #iterating through each point
            current_point_x,current_point_y=points[j] # saving the x and y of the second point
            if y < current_point_y and x ==current_point_x:
                number_of_rectangles += y_coordinates_count.get((y, current_point_y), 0)
                y_coordinates_count[(y, current_point_y)] = y_coordinates_count.get((y, current_point_y), 0) + 1
    return number_of_rectangles
class Tests(unittest.TestCase):
    def test_count_rectangles(self):
        points = [(1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3)]
        self.assertEqual(count_rectangles(points), 3)
        points1 = [(1, 1), (1, 3), (2, 1),  (3, 1), (3, 3)]
        self.assertEqual(count_rectangles(points1), 1)
        points2=[(1, 1), (1, 3), (2, 1), (3, 1), (3, 3)]
        self.assertEqual(count_rectangles(points2), 1)

def main():
    # Ask the user to enter the list of points
    tests = Tests()
    tests.test_count_rectangles()
    print("Tests passed! :)")
    while True:
        try:
            number_of_points = int(input("Enter the number of points: "))
            break
        except ValueError:
            print("Invalid input format. Please enter an integer")# if the given value is  any other input than an
            #integer, he gets a message that the input is not valid  and is requested to try again.


    points = []
    for i in range(number_of_points):
        while True:
            try:
                point_x, point_y = map(int, input(f"Enter point {i + 1}: ").split())
                break
            except ValueError:
                print("Invalid input format. Please enter two integers separated by a space.")
        points.append((point_x, point_y))

    # Call the count_rectangles() function and print the output
    rectangle_count = count_rectangles(points)
    print("Number of rectangles:", rectangle_count)


main()