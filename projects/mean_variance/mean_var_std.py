import numpy as np
def calculate(A):

  if len(A) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
  
    a3 = np.array([A[0:3],A[3:6],A[6:9]])

    mean = [list(np.mean(a3,axis = 0)),list(np.mean(a3,axis = 1)),np.mean(a3)]

    variance = [list(np.var(a3,axis=0)),list(np.var(a3,axis=1)),np.var(a3)]

    standard_deviation =[list(np.std(a3,axis=0)),list(np.std(a3,axis=1)),np.std(a3)]

    maximum = [list(np.max(a3,axis=0)),list(np.max(a3,axis=1)),np.max(a3)]
 
    minimum = [list(np.min(a3,axis=0)),list(np.min(a3,axis=1)),np.min(a3)]

    total = [list(np.sum(a3,axis=0)),list(np.sum(a3,axis=1)),np.sum(a3)]


  calculations = {
               'mean':mean,
               'variance':variance,
               'standard deviation':standard_deviation,
               'max': maximum,
               'min': minimum,
               'sum':total  
  }

  return calculations