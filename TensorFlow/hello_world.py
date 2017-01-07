
# import tensorflow
import tensorflow as tf

# Create a tensorflow object called hello_constant
hello_constant = tf.constant('Hello World!')

# Create a tensorflow session
with tf.Session() as sess:
  # Run the tf.constant operation in the session
  output = sess.run(hello_constant)
  print(output)
