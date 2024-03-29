import tensorflow as tf


def ThreeHumpCamel(X):
    """
    Computes the value of the 3-Hump Camel function at a given point x using TensorFlow.

    Parameters:
        X (tf.Tensor of shape (2, n)): A TensorFlow tensor representing the decision variable.

    Returns:
        tf.Tensor of shape (n, ): The value of the EggHolder function at X.
    """
    X = tf.cast(X, dtype=tf.float32)  # Cast X to float32
    X_square = tf.square(X)
    term1 = 2 * X_square[0]
    term2 = -1.05 * X_square[0] ** 2 + X_square[0] ** 3 / 6.0
    result = term1 + term2 + X[0] * X[1] + X_square[1]

    return result
