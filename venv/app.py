""" Implement a class for fractions that supports
    addition, subtraction, multiplication, division and checking equation
"""

class Fraction:
    """ Support addition, subtraction, multiplication, division
        and checking the equation of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator
        """
        if denom == 0:
            raise ZeroDivisionError

        self.num: float = num
        self.denom: float = denom

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{self.num}/{self.denom}"

    def plus(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        new_self_num = self.num * other.denom
        new_other_num = other.num * self.denom

        final_num = new_self_num + new_other_num
        final_denom = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def minus(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_self_num = self.num * other.denom
        new_other_num = other.num * self.denom

        final_num = new_self_num - new_other_num
        final_denom = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        final_num = self.num * other.num
        final_denom = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        final_num = self.num * other.denom
        final_denom = self.denom * other.num

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def equal(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """
        if self.num * other.denom == self.denom * other.num:
            return True
        else:
            return False # the fractions are not equal


def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus
        the expected answer to help to quickly identify if everything works properly.
    """
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f41: Fraction = Fraction(4, 1)
    f44: Fraction = Fraction(4,4)
    f52: Fraction = Fraction(5,2)
    f55: Fraction = Fraction(5, 5)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)
    f1510: Fraction = Fraction(15, 10)

    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f34} + {f55} + {f912} = {f34.plus(f55).plus(f912)} [600/240]")

    print(f"{f44} - {f68} = {f44.minus(f68)} [8/32]")
    print(f"{f41} - {f55} - {f32} = {f41.minus(f55).minus(f32)} [15/10]")

    print(f"{f128} * {f41} = {f128.times(f41)} [48/8]")
    print(f"{f52} * {f34} * {f68} = {f52.times(f34).times(f68)} [90/64]")

    print(f"{f32} / {f912} = {f32.divide(f912)} [36/18]")
    print(f"{f34} / {f55} / {f912} = {f34.divide(f55).divide(f912)} [180/180]")

    print(f"{f41} == {f34} is {f41.equal(f34)} [False]")
    print(f"{f1510} == {f128} is {f1510.equal(f128)} [True]")

    print(f"f12 = 1/2 [{f12}]")
    print(f"f912 = 9/12 [{f912}]")

def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction(count: int) -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        num = get_number(f"Enter a numerator for Fraction {count}: ")
        denom = get_number(f"Enter a denominator for Fraction {count}: ")
        fraction: Fraction = Fraction(num, denom)

        return fraction

def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    result: Fraction  # just define the type of result, don't set a value
    equality: bool = False
    okay: bool = True # a variable to decide printing the result

    if operator == '+':
        result = f1.plus(f2)
    elif operator == "-":
        result = f1.minus(f2)
    elif operator == "*":
        result = f1.times(f2)
    elif operator == "/":
        result = f1.divide(f2)
    elif operator == "==":
        equality = f1.equal(f2)
        print(f"{f1} {operator} {f2} = {equality}")
        okay = False
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False # unrecognized operator --> do not print the result

    if okay:
        print(f"{f1} {operator} {f2} = {result}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction(1)
    operator: str = input("Operation (+, -, *, /, ==): ")
    f2: Fraction = get_fraction(2)

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    test_suite()
    main()