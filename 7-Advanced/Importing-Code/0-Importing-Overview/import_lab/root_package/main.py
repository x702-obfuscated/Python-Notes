from os import sep #IGNORE --> imports the correct filepath seperator based on the operating system. 

'''Display the import context'''
import __main__  # Imports __main__ (the currently executed script)
print(f"Executing {__file__.split(sep)[-1]}")
print(f"__main___.__name__ : {__main__.__name__}")
print(f"__name__    : {__name__}")
print(f"__package__ : {__package__}")
print(f"__file__    : {__file__}\n")



''' Absolute Imports
from .\\root_package > python main.py 
from ./root_package $ python3 main.py   
'''
# import module1
# import module2
# from package1 import module3
# from package1 import module4
# from package2 import module5
# from package2 import module6
# from package2.package3 import module7
# from package2.package3 import module8


''' Absolute Imports
from ..\\root_package > python -m root_package.main 
from ../root_package $ python3 -m root_package.main     
'''
# from root_package import module1
# from root_package import module2
# from root_package.package1 import module3
# from root_package.package1 import module4
# from root_package.package2 import module5
# from root_package.package2 import module6
# from root_package.package2.package3 import module7
# from root_package.package2.package3 import module8



''' Relative imports (relative to this module)
from ..\\root_package > python -m root_package.main 
from ../root_package $ python3 -m root_package.main     
'''
# from . import module1
# from . import module2
# from .package1 import module3
# from .package1 import module4
# from .package2 import module5
# from .package2 import module6
# from .package2.package3 import module7
# from .package2.package3 import module8


''' Relative imports (relative to this module)
from .\\root_package > python main.py 
from ./root_package $ python3 main.py
'''
'''These imports will result in: 
ImportError: attempted relative import with no known parent package'''
# from . import module1
# from . import module2
# from .package1 import module3
# from .package1 import module4
# from .package2 import module5
# from .package2 import module6
# from .package2.package3 import module7
# from .package2.package3 import module8

'''No relative imports will work without error in this context'''

