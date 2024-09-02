print("success m6")

#Absolute imports --> works with python main.py from ./root_package
# import module1
# import module2
# from package1 import module3
# from package1 import module4
# from package2 import module5
# from package2.package3 import module7
# from package2.package3 import module8


# Absolute imports --> use python -m root_package.main from ../root_package
# from root_package import module1
# from root_package import module2
# from root_package.package1 import module3
# from root_package.package1 import module4
# from root_package.package2 import module5
# from root_package.package2.package3 import module7
# from root_package.package2.package3 import module8



# Relative imports relative to this module --> use python -m root_package.main from ../root_package
# from .. import module1
# from .. import module2
# from ..package1 import module3
# from ..package1 import module4
# from .import module5
# from .package3 import module7
# from .package3 import module8