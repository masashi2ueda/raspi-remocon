#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
from subprocess import PIPE
import argparse

def save_sig(no, dst_name):
    python_str = "/usr/bin/python"
    dst_dir_path = "/home/pi/I2C0x52-IR/datas"
    dst_path = f"{dst_dir_path}/{dst_name}.dat"
    script_path = f"/home/pi/I2C0x52-IR/IR-remocon02-commandline.py"
    cmd_str = f"{python_str} {script_path} r {no} > {dst_path}"
    print(cmd_str)
    proc = subprocess.run(cmd_str, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    date = proc.stdout
    print('STDOUT: {}'.format(date))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('no')
    parser.add_argument('dst_name')
    args = parser.parse_args()
    save_sig(args.no, args.dst_name)

