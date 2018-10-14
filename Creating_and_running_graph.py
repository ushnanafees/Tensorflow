import tensorflow as tf
x = tf.Variable(4, name="x")
y = tf.Variable(3, name="y")
f = x*x*y + y + 2

init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
init.run()
result = f.eval()
print(result)
sess.close()

x1 = tf.Variable(1)
x1.graph is tf.get_default_graph