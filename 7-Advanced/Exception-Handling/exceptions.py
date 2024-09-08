


'> Try-Except'
' > used for exception handling in python'

try:
    'Code Block that might raise an exception'

except:
    'Code Block to execute if the expection occurs'

#Handling specific errors

try:
    ...
except TypeError:
    ...
except ValueError:
    ...

try:
    ...
except Exception:
    ...
else:
    "Code Block to execute if no exception occurs"

try:
    ...
except Exception:
    ...
finally:
    'Code Block that always executes'