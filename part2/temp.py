import sys
print(sys.platform,sys.maxsize,sys.version)

if sys.platform[:3] == 'win' : print('hello windows')

print(sys.path)

sys.path.append(r'C:\mydir')
print(sys.path)
print(sys.modules)
print(list(sys.modules.keys()))

print(sys)
print(sys.modules['sys'])

import traceback,sys
# def grail(x):
#     raise TypeError('already got one')
# try:
#     grail('arthur')
# except:
#     exc_info=sys.exc_info()
#     print(exc_info[0])
#     print(exc_info[1])
#     traceback.print_tb(exc_info[2])
import os
print(os.getpgid())
print(os.getcwd())

print(os.chdir(r'C:\Users'))
print(os.getcwd())