import numpy as np

mu = 0 # 均值
sigma = 0.5 #标准差
rarray = np.random.normal(mu,sigma,100)
rarray[rarray > 0] = 0
print(rarray)


'''
for i in range(len(rarray)):
    if(rarray[i] < 0):
        print(rarray[i])
        rarray[i] = 0
    else
        rarray[i] = rarray[i]
'''