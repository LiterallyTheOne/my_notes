# Deep Learning's basics

`Deep learning` is a subset of `machine learning` which has
really deep layers of computations.

## Neuron

Every unit in a `neural network` is called a `neuron`.

### Linear neuron

$$y = xw + b$$

* $x$: input
* $w$: weight
* $b$: bias
* $y$: output of the `neuron`

## Layer

A `layer` is a set of `neurons`.

[//]: # (TODO add a  figure)

### Dense layer (fully-connected layer)

A `dense layer` (`fully-connected layer`) is a `layer` which all its neurons
have the same input. The input of each `dense layer` is the output of the previous layer.

[//]: # (TODO add a  figure)

## Activation functions

`Activations functions` are some functions that we apply to the output of
each computational layer.

The purpose of each `activation function` is to make the output of each
computational layer, nonlinear.

[//]: # (TODO make the purpose more general)

### ReLU

`ReLU`, Rectified Linear Unit, is an `activation function` that makes the
negative part of its input, 0.

$$ max(0,x) $$

* x: input

[//]: # (TODO add plot of ReLU)

## Loss function

The `loss function` Measures how much different our results and `ground truth` are.

example:

* MAE (Mean Absolute Error)

## Optimizer

The `optimizer` tries to decrease the result of the `loss function`.

## Minibatch

A sample iteration of all training data.

* small batch: Because weights are getting an update after each batch,
  if we have a small batch size, the updates will be so noisy.

## epoch

A complete iteration of all training data.

## Learning rate

A `learning rate` (alpha) is a hyperparameter that controls how much
the estimated error should apply to our weights.

* small learning rate: makes the fitting take longer
* high learning rate: we might lose the optimal answer

## Huber loss

pass

## Stochastic Gradient Descent

pass

## Adam optimizer

pass

## Model Capacity

size and complexity of a model.

In `neural network`s, mostly, capacity refers to the number of `neuron`s and how
they are connected together.

## how to deal with underfitting

* Adding more layers (deeper): Learning takes more time, adds more nonlinearity
* Add more `neuron`s to a layer (wider): Learning takes less time

## Dropout

We randomly drop out some `neuron`s from our neural network to
prevent overfitting.

## Batch normalization

We normalize each batch according to its own `mean` and `standard deviation`.
