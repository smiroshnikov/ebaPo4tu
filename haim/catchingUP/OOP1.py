import sys
import os
import math
import hutils


if __name__ == '__main__':
    print("use 'main' ")
    print(f"{[v for k, v in sys.modules.items() if v =='utils']}list of modules imported by this script  ")

    # updating list of paths can be done via sys.path.append
    # print(sys.path)
    sys.path.append("c:\\Webdriver")
    # print(sys.path)
    a = 3
    b = 12
    print(hutils.summ(a, b))

