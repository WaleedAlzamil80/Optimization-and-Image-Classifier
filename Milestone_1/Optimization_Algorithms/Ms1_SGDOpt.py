import numpy as np
import tensorflow as tf

def SGD(loss_func, X_init , X_vals, loss_vals, eta = 0.01):
  """
  Stochastic Gradient Descent (SGD) optimization algorithm for updating the values of a given variable.

  Args:
    - loss_func: Callable, the loss function that computes the loss given the current variable values.
    - X_init: tf.Variable, the initial variable values to be updated.
    - eta: float, the learning rate used to control the size of the update steps (default is 0.01).
    - X_vals: list(), empty list used to save X at each iteration.
    - loss_vals: list(), empty list used to save the loss values at each iteration.


  Returns:
    None
  """

  with tf.GradientTape(persistent=True) as t:
    # Compute the current loss
    current_loss = loss_func(X_init)

  # Compute the gradient of the loss with respect to the variables
  dx = t.gradient(current_loss, X_init)

  # Update the variables using the SGD update rule
  X_init.assign_sub(eta * dx)

  # calc the loss value and append it to the list
  loss_vals.append(tf.squeeze (loss_func(X_init)))

  #append X to the list
  X_vals.append(X_init.numpy())