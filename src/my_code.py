"""This module ships code to implement some complex-valued math in python."""
from __future__ import annotations

from math import atan2, cos, sin, sqrt
import numpy as np

def my_function() -> bool:
    """Return True immediately to demonstrate a working test.

    Returns:
        bool: Hardcoded to True.
    """

    return True


class Complex(object):
    """Implement a complex number class with addition and multiplication."""

    def __init__(self, realpart: float, imagpart: float):
        """Create a complex number object.

        Args:
            realpart (float): The real part of the number.
            imagpart (float): The complex part of the number.
        """
        # TODO: Implement me.
        self.realpart = realpart
        self.imagpart = imagpart

    def add(self, other: Complex) -> Complex:
        """Add to complex numbers.

        For two complex numbers x_1 + iy_1, x_2 + iy_2,
        compute (x_1 + iy_1) + (x_2 + iy_2) = x_1 + x_2 + i(y_1 + y_2).

        Args:
            other (Complex): The number to add to self.

        Returns:
            Complex: A complex number object containig the sum of the two.
        """
        # TODO: Implement me.
        return Complex(self.realpart + other.realpart, self.imagpart + other.imagpart)

    def radius(self) -> float:
        """Compute the radius of the compelex number.

        According to Pythagoras, the radius is given by sqrt(x^2 + y^2)

        Returns:
            float: The radius of self.
        """
        # TODO: Implement me.
        return np.sqrt(self.realpart**2 + self.imagpart**2)

    def angle(self) -> float:
        """Compute the angle of the complex number.

        For a complex number c = x + iy,
        the angle is typically given by atan2(y, x)

        Returns:
            float: The angle of self.
        """
        # TODO: Implement me.
        return np.arctan2(self.imagpart, self.realpart)

    def multiply(self, other: Complex) -> Complex:
        """Multiply two complex numbers (x_1 + jy_1) * (x_2 + jy_2).

        Complex numbers are often multiplied in polar form via
        c_mul = r_1 * r_2 * e^(theta_1 + theta_2).
        In other words the new radius is the product of the incoming radii.
        The new angle is given by the sum of the incoming angles.
        Radius and angle can be converted back to the karthesian form via,
        x = r_mul * cos(theta_mul),
        y = r_mul * sin(theta_mul).

        Args:
            other (Complex): The number to multiply self by.

        Returns:
            Complex: The product of self and other.
        """
        # TODO: Implement me.
        r1 = self.radius()
        r2 = other.radius()
        theta1 = self.angle()
        theta2 = other.angle()
        r_mul = r1 * r2
        theta_mul = theta1 + theta2
        x = r_mul * np.cos(theta_mul)
        y = r_mul * np.sin(theta_mul)
        return Complex(x, y)

