# Keras

Keras is a package for python which provides an interface
for artificial intelligence.

## Make one neuron in Keras

```python

from tensorflow import keras
from tensorflow.keras import layers

# Create a network with 1 linear unit
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
])

```

code source: [Kaggle, Deep learning course](https://www.kaggle.com/code/ryanholbrook/a-single-neuron)

* units: number of neurons
* input_shape: the size of the input
