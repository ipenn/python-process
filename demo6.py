import win32api,win32process, win32con
aa = win32api.ShellExecute(0, 'open', "C:\\Program Files\\aa\\terminal.exe", '', '', 0)
# print aa
si = win32process.STARTUPINFO()
si.dwFlags =  win32process.STARTF_USESTDHANDLES
si.wShowWindow = win32con.SW_HIDE
create_flags = win32process.CREATE_NEW_CONSOLE
#aa = win32process.CreateProcess("C:\\Program Files\\aa\\terminal.exe", '', None, None, 0, create_flags,None, None, si)
print aa
