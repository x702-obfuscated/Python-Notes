# `Python Difference`

```python 
import difflib

#create a Differ object
diff = difflib.Differ()

print("\n".join(list(diff.compare("Hello World", "Hello world!"))))
```

