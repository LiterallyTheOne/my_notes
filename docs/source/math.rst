Math
====

Expected value
--------------

.. math::

    E(x) = \sum_{i}^{n} x_i p(x_i)

Taylor expansions
-----------------

.. math::

    \sum_{n=0}^\infty \frac{\frac{d^n f(a)}{d a^n}}{n!}(x-a)^n

.. list-table:: some useful taylor expansions

    * - function
      - taylor expansion
    * - :math:`\frac{1}{1-x}`
      - :math:`1+x+x^2+x^3+...`
    * - :math:`sin(x)`
      - :math:`x - \frac{x^3}{3!} + \frac{x^5}{5!} - ...`
    * - :math:`cos(x)`
      - :math:`1 - \frac{x^2}{2!} + \frac{x^4}{4!} - ...`

UV formula integral
-------------------

.. math::

    \int udv = uv - \int vdu

Derivatives and Integrals
-------------------------

.. list-table:: Derivatives and integrals

    * - Equation
      - Condition
      - Derivative
      - Integral
    * - :math:`x^n`
      - :math:`n>1`
      - :math:`nx^{n-1}`
      - :math:`\frac{1}{n+1}x^{n+1} + c`
    * - :math:`ln(x)`
      -
      - :math:`\frac{1}{x}`
      - :math:`x ln(x) - x + c`
