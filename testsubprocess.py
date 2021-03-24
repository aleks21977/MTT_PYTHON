# -*- coding: utf-8 -*-
"""
import subprocess

code = subprocess.call("notepad.exe")
if code == 0:
    print("Success!")
else:
    print("Error!")
"""

"""
import subprocess as sp

# prog = sp.Popen(['runas', '/noprofile', '/user:Администратор', 'notepad.exe'],stdin=sp.PIPE)
prog.stdin.write(b'123123+x\n')
prog.communicate()
"""

"""
import subprocess

proc = subprocess.call(['runas','/user:Administrator','myfile.exe'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.stdin.write(b'password\r\n')
"""
"""
import subprocess
# processjl = subprocess.Popen([
      'psexec.exe', '-u', 'username', '-p', 'password',
       r'notepad.exe'
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True)
stdout, stderr = processjl.communicate()
"""
"""
import subprocess
args = ['runas', '/user:Администратор', 'calc.exe']
# proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc.stdin.write(b'123123+x\n')
proc.stdin.flush()
stdout, stderr = proc.communicate()
print (stdout)
print (stderr)
"""