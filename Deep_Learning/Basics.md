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
