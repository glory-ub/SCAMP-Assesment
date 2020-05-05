
# coding: utf-8

# In[4]:


def fibbonacci (number):
    '''Returns the fibonacci sequence of a given number'''
    output = [0,1]  # defines the first two terms
    for i in range(number-2):
        # updates value
        n1 = output[-2]
        n2 = output[-1]
        n3 = n1 + n2 
        output.append(n3)      
    return(output)


# In[3]:


fibbonacci(8)

