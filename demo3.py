# -*- coding:utf-8 -*-

import win32com.client


def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        print '%s is exists' % process_name
    else:
        print '%s is not exists' % process_name
    for child in processCodeCov:
        print '\t', child.Name, child.Properties_('ProcessId'), \
            int(child.Properties_('UserModeTime').Value) + int(child.Properties_('KernelModeTime').Value)

    


if __name__ == '__main__':
    check_exsit('terminal.exe')