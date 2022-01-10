"""
Source code from Real Python's "Data Classes in Python 3.7+ (Guide)" guide by
Geir Arne Hjelle.

URL: https://realpython.com/python-data-classes/
Section URL: https://realpython.com/python-data-classes/#type-hints
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class WithoutExplicitTypes:

    name: Any
    value: Any = 42

any_class = WithoutExplicitTypes("Javier")
print(any_class)
