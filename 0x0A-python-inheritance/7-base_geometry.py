#/usr/bin/python3
"""create class BaseGeometry"""


class BaseGeometry:
    """repr base geo"""
    def area(sel):
        """raises exept"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """checks if valid value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
