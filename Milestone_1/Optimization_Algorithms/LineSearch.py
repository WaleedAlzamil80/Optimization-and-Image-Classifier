import tensorflow as tf
import numpy as np

def LineSearch(X, loss_func, eta = 0.01):
    """
    Adam optimization algorithm for updating the values of a given variable.

    Args:
        - X: tf.Variable, the variable value at which we want to the the optimal learning rate.
        - loss_func: Callable, the loss function that computes the loss given the current variable values.
        - eta: tf.Variable, the learning rate to be updated to control the size of the update steps (default is 0.01).

    Returns:
        None
    """

    with tf.GradientTape(persistent=True) as t:
      current_loss = loss_func(X)
    dX = t.gradient(current_loss, X)

    with tf.GradientTape(persistent=True) as t2:
      with tf.GradientTape(persistent=True) as t1:
        Q = loss_func(X - eta * dX)
      dQ = t1.gradient(Q, eta)
    d2Q = t2.gradient(dQ, eta)
    eta.assign_sub(dQ/d2Q)

    return eta
