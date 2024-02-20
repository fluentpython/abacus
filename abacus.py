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
    >>> a.subtract(3)
    >>> a
    Abacus(2)

The imperative API uses a global instance of `Abacus`:

    >>> add(7)
    Abacus(7)
    >>> subtract(4)
    Abacus(3)

The imperative API provides shorter aliases for command names:

    >>> sub(1)
    Abacus(2)

Use `new_abacus` to start a new calculation:

    >>> new_abacus()
    >>> add(1)
    Abacus(1)

Custom module `dir`:

    >>> import abacus
    >>> dir(abacus)
    ['Abacus', 'add', 'new_abacus', 'sub', 'subtract']
"""

# mapping of method names to global aliases
_commands = {}


def command(method):
    _commands[method.__name__] = []  # no alias
    return method


def command_alias(*names):
    def decorator(method):
        _commands[method.__name__] = list(names)
        return method

    return decorator


class Abacus:
    def __init__(self, start=0):
        self.total = start

    def __repr__(self):
        return f'Abacus({self.total})'

    @command
    def add(self, value):
        self.total += value

    @command_alias('sub')
    def subtract(self, value):
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


def _install_command(name, function):
    if name in globals():
        raise ValueError(f'duplicate name: {name}')
    globals()[name] = function
    __all__.append(name)


def _install_commands():
    for name, aliases in _commands.items():
        new_command = _make_command(name)
        _install_command(name, new_command)
        for alias in aliases:
            _install_command(alias, new_command)


_install_commands()
