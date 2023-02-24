#!/usr/bin/env python
# coding: utf-8

# ## f(x) = x^3 - 6x^2 + 4x + 12
# ### Определить корни
# ### Найти интервалы, на которых функция возрастает
# ### Найти интервалы, на которых функция убывает
# ### Построить график
# ### Вычислить вершину
# ### Определить промежутки, на котором f > 0
# ### Определить промежутки, на котором f < 0
# ### Оформить работу с заголовками в Markdown.

# In[1]:


from sympy import symbols, solve
import matplotlib.pyplot as plt
import matplotlib as mp1
from pylab import rcParams
rcParams ['figure.figsize']


# In[2]:


import numpy as np


# In[3]:


x = symbols ("x")
solve(x**3-6*x**2+4*x+12, x)


# In[4]:


solve(x**3-6*x**2+4*x+12, x, cubics=False)


# ### Применим библиотеку numpy

# In[5]:


np.roots ([1,-6,4,12])


# ### Определяем промежутки, на которых f>0 и f<0

# In[6]:


x1,x2,x3 = np.roots([1,-6,4,12])


# In[7]:


print(f'Функция больше нуля: (-inf; {round(x3, 4)}) & ({round(x2, 4)}; {round(x1, 4)})')
print(f'Функция меньше нуля: ({round(x3,4)}; {round(x2,4)}) & ({round(x1,4)}; + inf ')


# ### Строим график

# In[8]:


x=list(range(-3,7))
fx=[i**3-6*(i**2)+4*i+12 for i in x]


# In[9]:


plt.plot(x,fx)
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show


# ### Рассчитаем вершину

# In[10]:


np.polyder([1,-6,4,12])


# In[11]:


np.roots(np.polyder([1,-6,4,12]))


# In[12]:


max_point = np.roots(np.polyder([1,-6,4,12]))[1]
min_point = np.roots(np.polyder([1,-6,4,12]))[0]
max_point, min_point


# In[13]:


y_max_point = np.polyval([1,-6,4,12], max_point)
y_max_point


# In[14]:


y_min_point = np.polyval([1,-6,4,12], min_point)
y_min_point


# In[15]:


print(f'Точка максимума: {max_point, y_max_point}')
print(f'Точка миниммума: {min_point, y_min_point}')


# In[ ]:




