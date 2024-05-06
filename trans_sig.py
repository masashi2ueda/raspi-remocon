#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
from subprocess import PIPE
import argparse

def trans_sig(sig_name):
    python_str = "/usr/bin/python"
    sig_dir_path = "/home/pi/I2C0x52-IR/datas"
    sig_path = f"{sig_dir_path}/{sig_name}.dat"
    script_path = f"/home/pi/I2C0x52-IR/IR-remocon02-commandline.py"
#     cmd_str = f"{python_str} {script_path} t  'cat {sig_path}'"
    cmd_str = f"{python_str} {script_path} t `cat {sig_path}`"
    print(cmd_str)    
    proc = subprocess.run(cmd_str, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    date = proc.stdout
    print('STDOUT: {}'.format(date))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('sig_name')
    args = parser.parse_args()
    trans_sig(args.sig_name)
#     trans_sig("bed_l")
    

