import numpy as np
import math
import matplotlib.pyplot as plt
#a = np.zeros((1,5))
#print (a)
def v(x,n):
    '''泰勒展开逼近求e^x,需要误差曲线'''
    num=1
    fun=1
    fun1=0
    if x>0:
        for i in range(1,n+1):
            #print(i)
            num=num*i#阶乘
            #print(x)
            fun=fun+(1/num)*(pow(x,i))
            #print(fun)
            print("x>0")
        return fun
    elif x==0:
        fun2=1
        print("x=0")
        return fun2
    else:
        for j in range(1,n+1):
            num=num*j
            fun=fun+(1/num)*(pow(-x,j))
            #print(fun)
            fun1=1/fun
            print("x<0")
        return fun1;
def truev(x):# e^2,e^-2真实值
    fun3=math.exp(x)
    #print(fun3)
    return fun3

def taylorv(x,n):#使用taylor展开求e^-2
    num1=1
    funt=1
    for i in range(1,n+1):
            #print(i)
            num1=num1*i#阶乘
            #print(x)
            funt=funt+(1/num1)*(pow(x,i))
            #print(funt)
    return funt
'''e^2taylor展开公式（n为变量）'''
a = np.zeros(20) 
b = np.arange(1,21)
for i in range(0,20):
    a[i]=v(2, i+1)-truev(2)#x取值-2/2；
    print(a)
#fig=plt.figure(figsize=(50,230));
plt.figure(figsize=(30,15))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False#设置汉语显示
plt.plot(b,a, label='weight changes', linewidth=3, color='r', marker='o',
         markerfacecolor='blue', markersize=6)
plt.title(" e^2泰勒展开后取倒数得到e^-2绝对误差与展开项数的关系图",fontsize=14)
plt.xticks(b)
plt.xlabel('n')
plt.ylabel('absolute error')

for x, y in zip(b, a):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=8,rotation=18)
plt.savefig("./temp.png",dpi=300)#解决图片不清晰，不完整的问题
plt.show()




'''e^-2taylor展开公式（n为变量）
c = np.zeros(20) 
d = np.arange(1,21)
for i in range(0,20):
    c[i]=taylorv(-2, i+1)-truev(-2)#x取值-2
    print(c)
plt.figure(figsize=(20,10))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(d,c, label='weight changes', linewidth=3, color='r', marker='o',
         markerfacecolor='blue', markersize=6)
plt.title("e^-2直接泰勒展开后绝对误差与展开项数关系图",fontsize=14)
plt.xticks(d)
plt.xlabel('n')
plt.ylabel('absolute error')

for x, y in zip(d, c):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=8,rotation=-15)
plt.savefig("./temp.png",dpi=300)#解决图片不清晰，不完整的问题
plt.show()
'''