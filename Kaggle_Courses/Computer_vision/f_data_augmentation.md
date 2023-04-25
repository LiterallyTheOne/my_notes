# Data augmentation

Increasing the size of the database by adding
artificial data.

Data augmentation helps the model to ignore
some positional and unnecessary features. For
example in classification it doesn't matter if
the object is on the left or right or upside down,
it still has the same class as before.

![data augmentation example](figures/data_augmentation_example.jpg)

Most of the time, we use `data augmentation` at the
same time that we want to give them to our model.

`Data augmentation` helps model to see data with more
variance and this have a positive result on behaving
better with the real world data.

Example in keras:

```python
from tensorflow import keras
from tensorflow.keras.layers.experimental import preprocessing

layer_contrast = preprocessing.RandomContrast(factor=0.5),
layer_flip_horizantal = preprocessing.RandomFlip(mode='horizontal'),  # meaning, left-to-right
layer_flip_vertical = preprocessing.RandomFlip(mode='vertical'),  # meaning, top-to-bottom
layer_stretch = preprocessing.RandomWidth(factor=0.15),  # horizontal stretch
layer_rotation = preprocessing.RandomRotation(factor=0.20),
layer_translaation = preprocessing.RandomTranslation(height_factor=0.1, width_factor=0.1),

```