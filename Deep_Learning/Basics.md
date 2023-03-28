# Deep Learning's basics

`Deep learning` is a subset of `machine learning` which has
really deep layers of computations.

## Neuron

Every unit in a `neural network` is called: `neuron`.

### Linear neuron

$$y = xw + b$$

* $x$: input
* $w$: weight
* $b$: bias
* $y$: output of the `neuron`

## Layer

`Layer` is a set of `neurons`.

[//]: # (TODO add a  figure)

### Dense layer (fully-connected layer)

`Dense layer` (`fully-connected layer`) is a `layer` which all its neurons
have the same input which is that input is the output of the previous layer.

[//]: # (TODO add a  figure)

## Activation functions

`Activations functions` are some functions that we applu to the output of
each computational layer.

The purpose of each `activation function`, is to make the output of each
computational layer, nonlinear.

[//]: # (TODO make the purpose more general)

### ReLU

`ReLU`, Rectified Linear Unit, is an `activation function` that makes the
negative part of its input, 0.

$$ max(0,x) $$

* x: input

[//]: # (TODO add plot of ReLU)
