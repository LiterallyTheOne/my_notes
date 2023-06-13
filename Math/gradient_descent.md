# Gradient descent

## definition

`Gradient descent`:

* optimization algorithm
* iterative
* first-order: only uses the first `derivative` of a function.

$$ p_{n+1}=p_n + \alpha \times \nabla f(p_n) $$

## Some problems with `alpha`

* vanishing gradient: `alpha` is too low, learning is too slow.
* exploding gradient: `alpha` is too large, it doesn't converge.

