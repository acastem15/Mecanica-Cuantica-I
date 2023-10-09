import numpy as np
import matplotlib.pyplot as plt
#Discretización del dominio

def x_discrete(a,b): 


    return np.linspace(-5,5,1000)



def potential (x,w): 
    return (1/2)*w*(x**2)



#Recursive function to find phi
"""
def phi(x, E):

    w = 1
    h_barra = 1
    m = 1
    h = 10/999
    if x == -5: 
        return 0 
    elif x == -5+ 10/999: 
        return 1e-5
    else: 
        r_n = ((2*m)/(h_barra**2))*(potential(x-h,w)-E)
        r_n_m= ((2*m)/(h_barra**2))*(potential(x-h,w)-E)
        r_n_m_m= ((2*m)/(h_barra**2))*(potential(x-2+h,w)-E)

        num = (2*phi(x-h,E)*(1+((5*(h**2)*r_n_m)/(12))))-(phi(x-(2*h),E)*(1-(((h**2)*r_n_m_m)/(12))))
        den = (1-(((h**2)*r_n)/(12)))

        return num/den
"""

#Using dynamic programming to find phi
def phi2(x_array,E):

    w = 1
    h_barra = 1
    m = 1
    h = 10/999
    result = []

    i = 0
    for x in x_array: 
        
        if i ==0: 
            result.append(0)
        elif i ==1: 
            result.append(1e-5)
        else: 
            r_n = ((2*m)/(h_barra**2))*(potential(x_array[i],w)-E)
            r_n_m= ((2*m)/(h_barra**2))*(potential(x_array[i-1],w)-E)
            r_n_m_m= ((2*m)/(h_barra**2))*(potential(x_array[i-2],w)-E)

            num = (2*result[i-1]*(1+((5*(h**2)*r_n_m)/(12))))-(result[i-2]*(1-(((h**2)*r_n_m_m)/(12))))
            den = (1-(((h**2)*r_n)/(12)))

            result.append(num/den)

        i+=1

    return result


    
x = x_discrete(-5,5)
E = 5.5

result =phi2(x,E)
print(result,x)
plt.plot(x,result)
plt.show()


    


    

