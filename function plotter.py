import numpy as np
import matplotlib.pyplot as plt

print('Pltting a fun : A*x^[n] + b*x^[n-1].....+ c')
print('\n\n')

degree = input(('enter the highest degree of the fun (''integer''): '))

if not str(degree).isnumeric():
    print('invalide degree!!')

else:
    max1 = input('enter the max value: ')
    assert isinstance(int(max1), int),'error: invalide max value!!'
    min1 = input('enter the min value: ')
    assert isinstance(int(min1), int),'error: invalide min value!!'

    x = np.linspace(int(max1) , int(min1))
    y = np.zeros((len(x),1)) 
    constants=np.zeros((int(degree)+1,1))
    for i in range(int(degree)+1):
        cont=input('Enter the constant number '+str(i+1)+' :')
        constants[i] = cont
    for i in range(len(x)):
        for j in range(int(degree),0,-1):
            y[i] += (constants[-j-1])*(x[i]**(j))
    plt.plot(x,y)    
    plt.show()