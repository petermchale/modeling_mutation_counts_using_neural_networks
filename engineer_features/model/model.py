import tensorflow as tf
import os
import pandas as pd
import numpy as np


def train(data_df, l_heading_list, X_heading_list, y_heading_list, number_hidden_nodes=1):
    # turn off tensorflow warning messages
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    tf.reset_default_graph()

    tf.set_random_seed(1)

    sample_size = len(data_df)

    number_exposure_input_nodes = len(l_heading_list)
    number_feature_input_nodes = len(X_heading_list)
    number_output_nodes = len(y_heading_list)

    # exposure input to neural network
    with tf.variable_scope('exposure_input_layer'):
        l = tf.placeholder(tf.float32, shape=(sample_size, number_exposure_input_nodes))

    # feature inputs to neural network
    with tf.variable_scope('feature_input_layer'):
        X = tf.placeholder(tf.float32, shape=(sample_size, number_feature_input_nodes))

    # output layer of neural network
    with tf.variable_scope('output_layer'):
        weights = tf.get_variable(name="weights",
                                  shape=(number_feature_input_nodes, number_output_nodes),
                                  initializer=tf.contrib.layers.xavier_initializer())
        biases = tf.get_variable(name="biases",
                                 shape=number_output_nodes,
                                 initializer=tf.zeros_initializer())
        h = tf.exp(tf.matmul(X, weights) + biases)
        prediction = l * h

    # cost function
    with tf.variable_scope('cost'):
        y = tf.placeholder(tf.float32, shape=(sample_size, 1))
        cost = tf.reduce_mean(prediction - y * tf.log(prediction + 1e-10) + tf.lgamma(y + 1.0))

    # optimization method
    with tf.variable_scope('train'):
        training_step = tf.train.AdamOptimizer(learning_rate=0.1).minimize(cost)

    # fill placeholders with data
    feed_dict = {l: data_df[l_heading_list].values,
                 X: data_df[X_heading_list].values,
                 y: data_df[y_heading_list].values}

    # log data
    log_df = pd.DataFrame(columns=['epoch', 'cost', 'likelihood', 'bias', 'weight'])
    log_row = 0

    # train neural network
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        for epoch in range(300):
            _, cost_eval, prediction_eval, h_eval = session.run([training_step, cost, prediction, h],
                                                                feed_dict=feed_dict)
            if epoch % 10 == 0:
                log_df.loc[log_row] = [epoch,
                                       cost_eval,
                                       np.exp(-sample_size * cost_eval),
                                       biases.eval(),
                                       weights.eval()]
                log_row += 1

    data_df['h'] = h_eval
    data_df['expected_counts'] = prediction_eval

    return log_df
