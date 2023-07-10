#!/usr/bin/python3
"""Defines AClass MyInt That Inherits from int."""


class MyInt(int):
    """Invert INT Operators != and ==."""

    def __eq__(self, value):
        """Override == with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != with == behavior."""
        return self.real == value
