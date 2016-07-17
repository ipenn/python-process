import os
ret = os.system('tasklist | find "terminal.exe"')
print(ret)
