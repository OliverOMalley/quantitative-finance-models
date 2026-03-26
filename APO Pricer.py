#Scalar Processing for ECO Pricing
import numpy as np

S = 100
K = 105
r = 0.05
vol = 0.20
T = 1
simulations = 100000

Z = np.random.standard_normal(simulations)
St = S * np.exp(((r - (0.5 * (vol**2))) * T) + (vol * np.sqrt(T) * Z))
payoffs = np.maximum(St - K, 0)

Final_option_price = np.mean(payoffs) * np.exp(-r*T)
print(Final_option_price)


#---American Put Option Pricer---


import numpy as np 
import math 

S = 100 
K = 105 
r = 0.05
vol = 0.20
T = 1 
N = 100       #number of discrete steps in tree

dt = T / N 
u = math.exp(vol * math.sqrt(dt))
d = 1 / u 
q = (math.exp(r*dt) - d ) / (u - d)
discount = math.exp( -r * dt ) 

# figuring out what the option is worth on the last day on all 101 possible ending nodes
V = np.zeros(N+1)  # creating an arrray 
for i in range(N+1):
  St = S * (u**i) * (d**(N-i)) # price of option at end for each node
  V[i] = max(K - St, 0)    # array with payoffs , so now need to calculate whether to exercise early at each step back
for j in range(N-1, -1, -1):   # range steps us back from 99 , -1 each time 
  for i in range (j + 1):      # i means how many nodes are on day j , i,e. day 1 has 2 nodes 
    cont_value = discount * (q*V[i+1] + ((1-q)*V[i]))
    current_stock_price = S * (u**i) * (d**(j-i))
    exercise_value = K - current_stock_price 
    V[i] = max(cont_value , exercise_value)        # this loop repeatedly is changing V to new values as it steps backwards in time, getting rid of the excess value at each time , since a step back in time means there are less nodes

print(V[0])
