# Object Oriented Programming in Python

## Abstraction

Defining a general definition to use for each implementation.
We can make sure each implementation of this definition has implemented
the functionality required by the general definition.

### Abstraction Example

We define a general definition named: `Polygon`.
Our `Polygon` has a function called: `get_angles`.
This function returns how many angles a `Polygon` has.
Now we define a `Triangle` function, which is a `Polygon` with
3 angles. So in this implementation, we return 3, in `get_angles` function.
If we define a `Square`, we return 4, in `get_angles` function.

```python

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def get_angles(self):
        pass


class Triangle(Polygon):
    def get_angles(self):
        return 3


class Rectangle(Polygon):
    def get_angles(self):
        return 4

```

*[abstraction code](abstraction.py)*

*[abstraction test](tests/test_abstraction.py)*

## Encapsulation

pass

## Polymorphism

pass

## Inheritance

pass
