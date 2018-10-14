import tensorflow as tf
#zero_tsr = tf.zeros([2,3])      # (2 rows and 3 columns) 
##print(zero_tsr)
#
#one_tsr = tf.ones([2,4])
##print(one_tsr)
#
##a_var = tf.constant(42)
#filled_tsr = tf.fill([2,4],42)
##print(filled_tsr)
#
#cnstnt_tsr = tf.constant([3,5,9])
#print(cnstnt_tsr)
#
#zero_similar = tf.zeros_like(cnstnt_tsr)
#print(zero_similar)

#linear_tsr = tf.linspace(start=1,delta= 3)
#print(linear_tsr)

integer_seq_tsr = tf.range(start=6, limit=15, delta=3)
print(integer_seq_tsr)