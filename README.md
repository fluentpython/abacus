# abacus

The `abacus` module is an example of module metaprogramming
in service of developer experience.

The end-user APIs for `plain_abacus` and `abacus` are the same.
Please view their module-level docstrings for examples.

But `abacus` uses metaprogramming to elliminate the code
duplication in the `add` and `sub` functions of `plain_abacus`.

The metaprogramming features are:

* `@command`: decorator to register names of commands;
* `_make_command`: builds a stand-alone function from an `Abacus` method;
* `_install_commands`: makes commands and installs them as global functions;

**Note**: `abacus` has more lines of code and is much harder to understand than `plain_abacus`.
However, this example was inspired by the
[jupyturtle](https://github.com/ramalho/jupyturtle) project,
where the `Turtle` class has many more methods than `Abacus`,
therefore coding each global function by hand would require
a lot of duplication and many more lines of code.

When using metaprogramming, it's always a good idea to consider
whether the added complexity is worthwhile.
