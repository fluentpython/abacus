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

    >>> import abacus
    >>> dir(abacus)
    ['Abacus', 'add', 'new_abacus', 'sub']
"""

command_names = []


def command(method):
    command_names.append(method.__name__)
    return method


class Abacus:
    def __init__(self, start=0):
        self.total = start

    def __repr__(self):
        return f'Abacus({self.total})'

    @command
    def add(self, value):
        self.total += value

    @command
    def sub(self, value):
        self.total -= value


# imperative API

# _install_commands() will add names
__all__ = ['Abacus', 'new_abacus']


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


def _make_command(name):
    def command(*args):
        abacus = _get_abacus()
        getattr(abacus, name)(*args)
        return abacus

    return command


def _install_commands():
    for name in command_names:
        globals()[name] = _make_command(name)
        __all__.append(name)


_install_commands()
