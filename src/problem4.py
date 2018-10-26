"""
Exam 3, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Shuang Xia.  October, 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=14')
    shape(14)


def shape(n):
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle,per the pattern in the examples below.

    When the pattern calls for a number with more than one digit,
    just use the last (rightmost) digit when you print that number.
    [But handling patterns with more than 1 digit is just 1 point of the exam!]

    It looks like this example for n=5:
    1 ** 54321
   12 *** 4321
  123 **** 321
 1234 ***** 21
12345 ****** 1

    And this one for n=3:
  1 ** 321
 12 *** 21
123 **** 1


And this one for n=14:
             1 ** 43210987654321
            12 *** 3210987654321
           123 **** 210987654321
          1234 ***** 10987654321
         12345 ****** 0987654321
        123456 ******* 987654321
       1234567 ******** 87654321
      12345678 ********* 7654321
     123456789 ********** 654321
    1234567890 *********** 54321
   12345678901 ************ 4321
  123456789012 ************* 321
 1234567890123 ************** 21
12345678901234 *************** 1

    :type n: int
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################

    for k in range(n):
        for j in range(n - k - 1):
            print(' ', end='')
        if n > 10:
            for h in range(k + 1):
                if h >= 9:
                    h -= 10
                print(h + 1, end='')
        else:
            for h in range(k + 1):
                print(h + 1, end='')
        print(' ', end='')
        for z in range(k + 2):
            print('*', end='')
        print(' ', end='')
        if n > 10:
            for l in range(n - k, 0, -1):
                if l >= 10:
                    l -= 10
                print(l, end='')
        else:
            for l in range(n - k, 0, -1):
                print(l, end='')
        print()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
