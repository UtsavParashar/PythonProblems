import numpy as np

def gradient_descent(x, y):
    m_curr = c_curr = 0 # starting with 0
    iterations = 10000 # take a random number for iterations to find the global minima
    learning_rate = .08 # again, take a random number and then optimize
    n = len(x) # for mse formula 1/n 

    
    for i in range(iterations):
        y_predicted = m_curr * x + c_curr
        prev_cost = 0
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)]) # MSE 
        m_partial_derivative = -(2/n) * sum(x*(y-y_predicted))
        c_partial_derivative = -(2/n) * sum(y-y_predicted)

        m_curr = m_curr - learning_rate * m_partial_derivative # step size = learning_rate * m_partial_derivative
        c_curr = c_curr - learning_rate * c_partial_derivative

        print(f'iteration - {i} --> m - {m_curr}, c - {c_curr} and cost {cost} ')

        # Stop iteration if the steps have reduced substancially
        if (cost - prev_cost) < 1e-20:
            break

x = np.array([1, 2, 3, 4, 5])
y = np.array([7, 9, 11, 13, 15])

# expected equation is -> y = 2x+5
gradient_descent(x, y) # Output - iteration - 1071 --> m - 2.000000000000196, c - 4.999999999999291 and cost 9.660706189698599e-26