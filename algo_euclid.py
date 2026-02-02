# GCD Calculator
# Adrian Velasquez

import sys

def euclid ( a, b ) -> int:
    """
    Determines the GCD (Greatest Common Divisor) of 2 integer numbers
    :param a: First integer number of the pair to evaluate
    :param b: Second integer number of the pair to evaluate
    :return: GCD of numbers a and b
    """
    # Make a the bigger number
    if b > a:
        temp = a
        a = b
        b = temp
    return rec_euclid( a, b )


def rec_euclid ( a, b ) -> int:
    """
    Recursively determine the GCD of 2 integer numbers
    :param a: First integer number of the pair to evaluate
    :param b: Second integer number of the pair to evaluate
    :return: GCD of numbers a and b
    """
    r = a % b # a mod b = r
    if ( r == 0 ):
        return b
    return rec_euclid( b, r )


def run() -> None:
    """
    Run function of the CLI
    :return: None
    """
    success = False
    while not success:
        try:
            a = int(input("\n>> Insert positive integer a: "))
            if a <= 0:
                print("\n>> [ERROR] Please try again. Value a must be greater than 0")
                return

            b = int(input(">> Insert positive integer b: "))
            if b <= 0:
                print("\n>> [ERROR] Please try again. Value b must be greater than 0")
                return

            success = True

        except KeyboardInterrupt:
            print("\n\n>> Closing program...")
            sys.exit(0)

        except Exception as e:
            print(f"\n>> [ERROR]: Please try again. Values a and b should be positive integers: {e}")

    print( ">> Calculating..." )
    print( f">> The GCD of {a} and {b} is {euclid( a, b )}" )


if __name__ == "__main__":
    print("\nWelcome to the GCD (Greatest Common Divisor) calculator!")
    print("Press ^C (control-C) to exit")
    while True:
        run()
