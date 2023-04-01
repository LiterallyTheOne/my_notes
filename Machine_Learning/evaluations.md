# Evaluation

Different methods that we use to evaluate our model

## MAE

Mean Absolute Error

$$ \frac{1}{n}\sum_{i=1}^{n} |y_i-p_i| $$

* n: number of data
* y: labels
* p: predictions
* i: iterator

### MAE in scikit-learn

```python

from sklearn.metrics import mean_absolute_error

```

## MSE

Mean Squared Error

$$ \frac{1}{n}\sum_{i=1}^{n} (y_i-p_i)^2 $$

* n: number of data
* y: labels
* p: predictions
* i: iterator

### MSE in scikit-learn

```python

from sklearn.metrics import mean_squared_error

```

## Accuracy

Number of correct predictions divided by all the predictions.

$$ Accuracy = \frac{TrueTrue}{All} $$

## Cross entropy

$$ H(p,q)=-\sum_{x \in X}p(x) log(q(x)) $$