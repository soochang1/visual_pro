import subprocess

ret_v=subprocess.run(['dir'], shell=True, capture_output=True, encoding='cp949')

ret_v

a='dir'

b=a.split()