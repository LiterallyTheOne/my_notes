# Max pooling

`Max pool` replaces the maximum of each patch with
all elements of that patch.

```python
import numpy as np

a = np.array(
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
)

# pool_size = 2
# output_shape = a.shape
max_pool_a = np.array(
    [8, 8, 10, 10, 12, 12],
    [8, 8, 10, 10, 12, 12]
)
```

```python
import tensorflow as tf

tf.nn.pool(
    input=image,
    window_shape=(2, 2),
    pooling_type='MAX',
    strides=(2, 2),
    padding='SAME',
)
```

## Translation invariance

Moving one figure from one location to other location
without rotating it.

`Max pooling` help our model to take less care about
`positional infromation`.

`Max pooling` only creates `translation invariance`
in small distances.


[//]: # (TODO Add images)
