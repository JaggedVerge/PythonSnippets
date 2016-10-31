"""This provides a decorator that lets you precompute expensive methods"""

class lazy_property:
    """
    Allows lazy evaluation of properties of non-mutable data.
    Useful when these are expensive to compute and are immutable.
    The data must not be mutable because the method gets
    replaced with the computed value in the original object.
    """
    def __init__(self, fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj, self.func_name, value)
        return value
