# Create your first submission

## TPU

`TPU` is a like having 8 `gpu` working together.(?)

## Distribution strategy

In `tensorflow`, `distribution strategy` is a strategy
that tells `tpu`, how to distribute computation in its
cores.

## Confusion matrix

Puts the class of the `predicted result` alongside with the
class of the `grand truth`.

example:

```python
classes = [1, 2, 3, 4]

grand_truth = [2, 3, 1, 4, 2, 2, 1]
prediction = [2, 2, 1, 3, 2, 2, 4]

confusion_matrix = [
    [2, 3, 1, 4, 2, 2, 1],
    [2, 2, 1, 3, 2, 2, 4]
]
```

## Precision

formula: PredictionGrandTruth

$$ \frac{TrueTrue}{TrueTrue+FalseFalse} $$

## Recall

formula: PredictionGrandTruth

$$ \frac{TrueTrue}{TrueTrue+FalseTrue} $$

## f1

$$ \frac{2}{Precision^{-1}+Recall^{-1}} $$
