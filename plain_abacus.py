"""
This module is an example of using metaprogramming to implement
an imperative API to hide a class implementation.

The OO API:

    >>> a = Abacus()
    >>> a
    Abacus(0)
    >>> a.add(5)
    >>> a
    Abacus(5)
    >>> a.sub(3)
    >>> a
    Abacus(2)

The imperative API uses a global instance of `Abacus`:

    >>> add(7)
    Abacus(7)
    >>> sub(4)
    Abacus(3)

Use `new_abacus` to start a new calculation:

    >>> new_abacus()
    >>> add(1)
    Abacus(1)

Custom module `dir`:

    >>> import plain_abacus
    >>> dir(plain_abacus)
    ['Abacus', 'add', 'new_abacus', 'sub']

"""


class Abacus:
    def __init__(self, start=0):
        self.total = start

    def __repr__(self):
        return f'Abacus({self.total})'

    def add(self, value):
        self.total += value

    def sub(self, value):
        self.total -= value


# imperative API

__all__ = ['Abacus', 'new_abacus', 'add', 'sub']


def __dir__():
    return sorted(__all__)


_main_abacus = None


def _get_abacus():
    global _main_abacus
    if _main_abacus is None:
        _main_abacus = Abacus()
    return _main_abacus


def new_abacus():
    global _main_abacus
    _main_abacus = Abacus()


def add(value):
    abacus = _get_abacus()
    abacus.add(value)
    return abacus


def sub(value):
    abacus = _get_abacus()
    abacus.sub(value)
    return abacus
