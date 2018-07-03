import numpy as np
import tensorflow as tf

learning_rate = 0.01
num_inputs = 3
data_set_size = 100
num_epochs = 100
print_step = 10

inputs, labels = [], []
for i in range(data_set_size):
    input = np.random.uniform(-10, 10, num_inputs)
    inputs.append([input])
    labels.append([(np.sum(input) > 0).astype(int)])

x = tf.placeholder(tf.float32, [1, num_inputs])
y = tf.placeholder(tf.float32, [1])

weights = tf.Variable(tf.random_normal([num_inputs, 1]))
bias = tf.Variable(tf.random_normal([1]))

weighted_sum = tf.matmul(x, weights) + bias
prediction = tf.sigmoid(weighted_sum)[0]

loss = tf.losses.mean_squared_error(y, prediction)

train = tf.train.AdamOptimizer(learning_rate).minimize(loss)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for i in range(num_epochs):
        epoch_loss = 0
        epoch_correct = []
        for j in range(len(inputs)):
            _, l, pred, label = session.run([train, loss, prediction, y], {x: inputs[j], y: labels[j]})
            epoch_loss += l
            epoch_correct.append(np.round(pred) == label)
        if i == 0 or (i + 1) % print_step == 0:
            print("Epoch:", i + 1)
            print("Error:", (epoch_loss / len(inputs)))
            print("Acc  :", (np.sum(epoch_correct) / len(inputs)) * 100, "%\n")