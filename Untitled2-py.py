
# coding: utf-8

# In[2]:

v=range(1,6)


# In[3]:

print v


# In[4]:

2*v


# In[5]:

import numpy as np


# In[6]:

v=np.arage(1,6)


# In[7]:

v=np.arange(1,6)


# In[8]:

v


# In[9]:

2*v


# In[25]:

import matplotlib.pyplot as plt
plt.plot(1:26,3:56)
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')


# In[15]:

import numpy as np
import pandas as pd
import pandas_datareader as web


# In[ ]:




# In[16]:

import numpy as np
import pandas as pd
import pandas.io.data as web


# In[17]:

sp500=web.DataReader('^GSPC',data_source='yahoo',
                    start='1/1/2000',end='4/14/2014')
sp500.info()


# In[19]:

sp500['Close'].plot(grid=True,figsize=(8,5))


# In[20]:

sp500['Close'].plot(grid=True, figsize=(8,5))


# In[21]:

sp500['Close'].plot(grid=True, figsize=(8,5))


# In[23]:

sp500['Close'].plot(grid=True, figsize=(8,5))


# In[24]:

#以上代码在spyder中间可以显示图表。在notebook中无法显示


# In[ ]:



