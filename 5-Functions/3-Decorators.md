*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python Decorators`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [``]()


<br>

___

<br>

# ``

<br>

[Back To Top](#python-decorators)

___

<br>

*Created and maintained by Mr. Merritt*


```python
import time;


def time_this(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()-t0
        print(f"{func} took {t1} seconds")
    return wrapper


@time_this
def linear_search(list1d, item):
    indexes = []
    for i,elem in enumerate(list1d):
        if(elem == item):
            indexes.append(i)

    return indexes
    

list1d = [chr(x) for x in range(65,91)]

linear_search(list1d,"z")



# property decorators
```