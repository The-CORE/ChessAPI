from .discrete_vector import DiscreteVector


def iterable_to_discrete_vector(value):
    """
    If this recieves an iterable, it will return a DiscreteVector with x =
    iterable[0], y = iterable[1]. But, if it recieves anything else, it will
    just return that.
    """
    try:
        return DiscreteVector(*value)
    except TypeError:
        # value wasn't iterable or didn't have two items in it.
        pass
    return value
