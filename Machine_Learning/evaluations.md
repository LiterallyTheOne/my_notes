# Evaluation

Different methods that we use to evaluate our model

## MAE

Mean Absolute Error

$$ \frac{\sum_{i=1}^{n} |y_i-p_i|}{n} $$

* n: number of data
* y: labels
* p: predictions
* i: iterator

### mae in scikit-learn

```python

from sklearn.metrics import mean_absolute_error

```

## MSE

Mean Squared Error

$$ \frac{\sum_{i=1}^{n} (y_i-p_i)^2 }{n} $$

* n: number of data
* y: labels
* p: predictions
* i: iterator

### mse in scikit-learn

```python

from sklearn.metrics import mean_squared_error

```
