# Convolution and ReLU

## Convolutional layer

This is a layer that works like a filter
to extract features.

```python
import tensorflow as tf

conv_layer = tf.keras.layers.Conv2D(filters=64, kernel_size=3)
```

### kernel

`kernel` is an array (like a 2D array) that
we move that `kernel` over the image and multiply
`kernel` weights and image values then we sum the
result and add that to the result matrix.

kernel example:

```python
import numpy as np

a = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])
```

The size of the `kernel` is most of the time an odd number.
(like 5x5 or 3x3)
because we want the result of the multiplication and sum to
be in the center of it.

## Relu activation

Detect features in filtered image.

ReLU stands for: Rectified Linear Unit

ReLU function:

```python
relu = lambda x: x if x > 0 else 0
```

ReLU example:

```python
import tensorflow as tf

relu_layer = tf.keras.layers.ReLU()
```

Or add it as an activation to another layer:

```python
import tensorflow as tf

conv_layer = tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu')
```

## Max pooling

Condense the result to highlight the
features.

