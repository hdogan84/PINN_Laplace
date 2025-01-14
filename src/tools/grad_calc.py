import torch


def grad_x(p, len_x): 
    """Calculate the gradient of the input p in x-direction
       It assumes uniformly distributed nodes in a domain D=[0,1] x [0,1].
       Hence, len_x = len_y.
       Adjust coordinates and geometry if needed, or alternatively transform variables.
    """
    epsilon = 1e-8 #
    dX = 1.0/(len_x-1) #Spacing h is denoted with dX
    gradp_x=torch.zeros_like(p) + epsilon

    for i in range(1,len_x-1):
        for j in range(0,len_x):
            gradp_x[i*len_x+j] = (p[(i+1)*len_x+j] - p[(i-1)*len_x+j]) * 0.5/dX

    #One-sided gradient for @ x=0. It means i==0. 
    for j in range(0,len_x):
        gradp_x[j] = ( -p[2*len_x+j] +4*p[len_x+j] - 3*p[j]) * 0.5/dX


    #One-sided gradient for @ x=1. It means i==lenX-1. Second-order accurate
    for j in range(0,len_x):
        gradp_x[(len_x-1)*len_x+j] =  (3*p[(len_x-1)*len_x+j] - 4*p[(len_x-2)*len_x+j] + p[(len_x-3)*len_x+j]) * 0.5/dX

    return gradp_x


def grad_y(p, len_x): 
    """Calculate the gradient of the input p in y-direction
       It assumes uniformly distributed nodes in a domain D=[0,1] x [0,1].
       Hence, len_x = len_y.
       Adjust coordinates and geometry if needed, or alternatively transform variables.
    """
    epsilon = 1e-8 #
    dX = 1.0/(len_x-1) #Spacing h is denoted with dX
    gradp_y=torch.zeros_like(p) + epsilon

    for i in range(0,len_x):
        for j in range(1,len_x-1):
            gradp_y[i*len_x+j] = (p[i*len_x+j+1] - p[i*len_x+j-1]) * 0.5/dX

    # One-sided @ y=0. Corresponds j=0.
    for i in range(0,len_x):
            gradp_y[i*len_x] = (-p[i*len_x+2] + 4*p[i*len_x+1] - 3*p[i*len_x]) * 0.5/dX

    # One-sided @ y=1. Corresponds j=lenY-1.
    for i in range(0,len_x):
            gradp_y[(i+1)*len_x-1] = (-p[(i+1)*len_x-3] + 4*p[(i+1)*len_x-2] - 3*p[(i+1)*len_x-1]) * 0.5/dX
    
    return gradp_y