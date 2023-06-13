# Gradient descent

## definition

`Gradient descent`:

* optimization algorithm
* iterative
* first-order: only uses the first `derivative` of a function.
* to find minimum of a function

$$ p_{n+1}=p_n + \alpha \times \nabla f(p_n) $$

## Some problems with `alpha`

* vanishing gradient: `alpha` is too low, learning is too slow.
* exploding gradient: `alpha` is too large, it doesn't converge.

## Different types of gradient descent

### Batch gradient descent

Applies the change on all data.

We use it when we have a smooth convex.

1. Feed all the data to our `neural network`
2. Calculate the mean gradient of all data
3. Use the mean gradient to update weights.
4. repeat the steps from 1 to 3

### Stochastic gradient descent

Applies the change on every single example.

We use it on a large dataset.

1. Take a single example
2. Feed that example to `neural network`
3. Calculate the gradient of it
4. Use the calculated gradient to update the weights
5. repeat the steps from 1 to 4

### Mini-batch gradient descent

Applies the change on a mini-batch of data (certain number of examples).

1. Pick a mini-batch of our data
2. Feed that mini-batch to `neural network`
3. Calculate the mean of the gradient of the results
4. Use the calculated mean of gradient to update the weights
5. Repeat the steps from 1 to 4

## References

https://towardsdatascience.com/gradient-descent-algorithm-a-deep-dive-cf04e8115f21

https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a

https://www.ibm.com/topics/gradient-descent#:~:text=Gradient%20descent%20is%20an%20optimization,each%20iteration%20of%20parameter%20updates.

