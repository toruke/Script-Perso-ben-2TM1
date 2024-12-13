class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num & den sont des int
        POST : création de l'objet num & den
        RAISES : ValueError : si num < 0 ou si den <= 0
                TypeError : si num ou den sont autre chose que des int

        """
        if den == 0:
            raise ValueError("")
        self.__num = int(num)
        self.__den = int(den)
            raise TypeError("le numérateur et le dénominateur ne peuvent pas etre autre chose que des int")


    @property
    def numerator(self):
        """retourn le numérateur de la fraction
        PRE:
        POST:
        RAISES:
        """
        return self.__num

    @property
    def denominator(self):
        """retourn le denominateur de la fraction
        PRE:
        POST:
        RAISES:
        """
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : ?
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : ?
         POST : ?
         """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : ?
        POST : ?
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : ?
        POST : ?
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : ?
        POST : ?
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : ?
        POST : ?
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : ?
        POST : ?

        """

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        pass

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : ?
        POST : ?
        """
        pass

