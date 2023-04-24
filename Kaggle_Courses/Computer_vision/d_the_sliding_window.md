# The sliding window

## sliding window

* In convolution: we have a sliding window, `kernel_size`
* In max_pooling: we have a pool window, `pool_size`

## Stride

The step of the sliding window, when it
goes over the image.

```python
stride = 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
stride = 2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [1, 3, 5, 7, 9]
```

## Padding

How many rows and columns should we
append to the `image`.

We do padding to be able to get the output
in the shape that we want.

An example of zero-padding:

```python
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
padding = 1

result = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 4, 5, 6, 0],
    [0, 7, 8, 9, 0],
    [0, 0, 0, 0, 0]
])

```

padding is keras, is in two ways:

* `padding='valid'`: doesn't pad
* `padding='same'`: pads the input with zeros
  as much as needed to make the result
  with the same shape of input

## receptive field

Tells which part of the image is more important
for a specific neuron.

## One dimensional kernels

```python
import tensorflow as tf

detrend = tf.constant([-1, 1], dtype=tf.float32)

average = tf.constant([0.2, 0.2, 0.2, 0.2, 0.2], dtype=tf.float32)

spencer = tf.constant([-3, -6, -5, 3, 21, 46, 67, 74, 67, 46, 32, 3, -5, -6, -3], dtype=tf.float32) / 320
```