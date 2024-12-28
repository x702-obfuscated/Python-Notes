*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python difflib Module`
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

[Back To Top](#python-difflib-module)

___

<br>

*Created and maintained by Mr. Merritt*

```python 
import difflib

#create a Differ object
diff = difflib.Differ()

print("\n".join(list(diff.compare("Hello World", "Hello world!"))))
```

