#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
a=int(input())
pi=math.pi
a=2*pi*a
print(a)


# In[14]:


import random
a=[1,5,62,"зима",9]
e=random.choice(a)
print(e)


# In[34]:


import random
random.randrange(19909090)


# In[35]:


import random
a=[1,5,62,"зима",9]
random.shuffle(a)
print(a)


# In[49]:


import random
print("добро пожаловать в розыгрыш призов")
t=['николай',"Елена","ДМИТРИЙ","БЕТОНОМЕШАЛКА"]
print("победитель розыгрыша",random.choice(t))


# In[17]:


import random
print("че ты тут делаешь?")
h=input("черкани кликуху с района :")
r=input("второго как зовут?: /n ")
w=[1,2,3,4,5,6,7,8,9,10]
n=[1,2,3,4,5,6,7,8,9,10]
ScoreOne=0
ScoreTwo=0
def throwDise():
    for j in range(5):
        random.shuffle(w)
        random.shuffle(n)
    return w[0] + n[0]
for j in range(3):
    result = throwDise()
    ScoreOne +=result
    print(" Игрок",h,"выбросил:",result)
    print("Сумма очков у игрока",h,":",ScoreOne)
if (h>r):
    print("игрок",h,"победил!")
    print(h,"набрал",ScoreOne,"очков!")
elif (h>r):
    print("игрок",r,"победил!")
    print(h,"набрал",ScoreTwo,"очков!")
else:
    print("ничья.-.")


# In[ ]:




