"""
Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and Rachel Zhang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()


def run_test_problem1a():
    """ Tests the   problem1a  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem1a  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem1a: '
    title += 'red & blue, then black & magenta'
    window = rg.RoseWindow(450, 250, title)

    rectangle = rg.Rectangle(rg.Point(100, 120), rg.Point(200, 170))
    rectangle.outline_color = 'blue'
    square = rg.Square(rg.Point(125, 50), 30)
    square.fill_color = 'red'

    problem1a(rectangle, square, 5, window)
    window.continue_on_mouse_click()

    rectangle = rg.Rectangle(rg.Point(300, 70), rg.Point(400, 20))
    rectangle.outline_color = 'magenta'
    rectangle.outline_thickness = 5
    square = rg.Square(rg.Point(250, 100), 50)

    problem1a(rectangle, square, 10, window)
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem1a: yellow & black'
    window = rg.RoseWindow(400, 300, title)

    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(50, 250))
    rectangle.outline_color = 'black'
    rectangle.outline_thickness = 5
    square = rg.Square(rg.Point(300, 50), 80)
    square.fill_color = 'yellow'

    problem1a(rectangle, square, 15, window)
    window.close_on_mouse_click()


def problem1a(rectangle, square, thickness, window):
    """
    See   problem1a_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Rectangle.
      -- An rg.Square.
      -- A positive integer
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      -- Draws, on the given rg.RoseWindow:
           -- The given rg.Rectangle.
           -- The given rg.Square.
           -- An rg.Line for which:
               -- One endpoint is the center of the given rg.Square
               -- The other endpoint is the midpoint of the top edge
                    of the given rg.Rectangle.  (SEE THE PICTURES.)
               -- Its thickness is the given thickness.
               -- Its color is the outline color of the given rg.Rectangle.

      Note: Attach the rg.Line  AFTER  attaching the rg.Rectangle and rg.Square.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type rectangle: rg.Rectangle
      :type square:    rg.Square
      :type thickness: int
      :type window:    rg.RoseWindow
    """
    center = square.center
    top_left = rectangle.get_upper_left_corner()
    top_right = rectangle.get_upper_right_corner()
    save_me = rg.Line(top_left, top_right)
    midpoint = save_me.get_midpoint()
    line1 = rg.Line(center, midpoint)
    line1.thickness = thickness
    line1.color = rectangle.outline_color

    rectangle.attach_to(window)
    square.attach_to(window)

    line1.attach_to(window)

    window.render()
    # --------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the  problem1b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Test 1, followed by Test 2, of problem1b'
    window = rg.RoseWindow(300, 300, title)

    p = rg.Point(60, 50)
    problem1b(p, window, 100, 150, 'pink')
    window.continue_on_mouse_click()

    p = rg.Point(200, 100)
    problem1b(p, window, 200, 100, 'black')
    window.close_on_mouse_click()

    title = 'Test 3 of problem1b'
    window = rg.RoseWindow(300, 200, title)

    p = rg.Point(100, 50)
    problem1b(p, window, 150, 150, 'purple')
    window.close_on_mouse_click()


def problem1b(point, win, width, height, color):
    """
    See   problem1b_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Point.
      -- An rg.RoseWindow.
      -- Two positive integers.
      -- A string suitable for a color in RoseGraphics.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws an rg.Ellipse for which:
        -- The topmost point of the rg.Ellipse is the given rg.Point.
        -- The width of the rg.Ellipse is the given width.
        -- The height of the rg.Ellipse is the given width.
        -- The fill color of the rg.Ellipse is the given color.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:  rg.Point
      :type win:    rg.RoseWindow
      :type width:  int
      :type height: int
      :type color:  str
    """
    point.attach_to(win)
    corner_1_x = point.x - (width * 1/2)
    corner_2_x = point.x + (width * 1/2)
    ellipse_y = point.y + height
    corner_1 = rg.Point(corner_1_x,point.y)
    corner_2 = rg.Point(corner_2_x, ellipse_y)
    ellipse = rg.Ellipse(corner_1, corner_2)
    ellipse.fill_color = color
    ellipse.attach_to(win)
    win.render()
    # --------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ------------------------------------------------------------------------------
main()
