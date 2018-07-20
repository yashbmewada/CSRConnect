import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # called in order to minimize the warnings about SSE4.1 instructions.
import tensorflow as tf
import pandas as pd

def predictScore():
    df = pd.read_csv('NGO.csv')
    x1 = df["new_donor_growth"]
    x2 = df["donor_opt_out_rate"]
    x3 = df["donations_per_year"]
    x4 = df["cost_per_dollar_raised"]
    x5 = df["new_internal_projects"]
    x6 = df["project_delay_rate"]
    ys = df["score"]




    m_initial = 0.50

    b_initial = 1.00

    m1 = tf.Variable(m_initial)
    m2 = tf.Variable(m_initial)
    m3 = tf.Variable(m_initial)
    m4 = tf.Variable(m_initial)
    m5 = tf.Variable(m_initial)
    m6 = tf.Variable(m_initial)
    b = tf.Variable(b_initial)

    error = 0.0

    print(x1)

    for x1,x2,x3,x4,x5,x6,y in zip(x1, x2 ,x3, x4, x5,x6, ys):
        predicted_y = m1*x1 - m2*x2 + m3*x3 - m4*x4 + m5*x5 - m6*x6 + b
        error += (y-predicted_y)**2  # this is the square of difference of error added to the total error 'cost' which we minimize.

    optimizer_op = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(error)

    init_op = tf.global_variables_initializer()


    with tf.Session() as session:
        session.run(init_op)

        _ITERATIONS = 1000 #number of passes on the dataset

        for iteration in range(_ITERATIONS):
            session.run(optimizer_op) #calling our optimization operator to minimize error

        m1,m2,m3,m4,m5,m6 , intercept = session.run((m1,m2,m3,m4,m5,m6,b)) #calling our adjusted values
        print('slope: ', m1, m2 ,m3,m4,m5,m6 , 'Intercept: ', intercept)
    return m1,m2,m3,m4,m5,m6,intercept