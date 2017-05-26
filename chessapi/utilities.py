from .discrete_vector import DiscreteVector


def tuple_to_discrete_vector(value):
    """
    If this recieves a tuple, it will return a DiscreteVector with x = tuple[0],
    y = tuple[1]. But, if it recieves anything else, it will just return that.
    """
    return DiscreteVector(*value) if isinstance(value, tuple) else value
