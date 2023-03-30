# Keras

Keras is a package for python that provides an interface
for artificial intelligence.

## Make a simple layer in Keras

```python

from tensorflow.keras import layers

layer = layers.Dense(units=m, input_shape=[n])

```

* units: number of neurons
* input_shape: the size of the input

## Make a simple model in Keras

```python

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(units=m, input_shape=[n]),
])

```

* units: number of neurons
* input_shape: the size of the input

## Tensor

Tensor is a data structure like a `NumPy` array which is designed
to work better with `GPU`s and `TPU`s.

## Model compile

example:

```python

model.compile(
    optimizer="adam",
    loss="mae"
)

```

[source of the code](https://www.kaggle.com/)

## Model fit with the batch size and epoch

example:

```python

model.fit(
    x_train, y_train,
    validation_data=(x_validation, y_validation),
    batch_size=256,
    epochs=10
)
```

[source of the code](https://www.kaggle.com/)
