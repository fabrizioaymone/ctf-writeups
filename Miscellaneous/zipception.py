import subprocess
import shlex 
import re

for i in reversed(range(101)):
    subprocess.run([f"zip2john {i}.zip > {i}.hash"], shell=True)
    subprocess.run([f"john {i}.hash"], shell=True, capture_output=True)
    p=subprocess.run([f"john {i}.hash --show"], shell=True, capture_output=True)
    res = p.stdout.decode()
    password = re.search(rf".zip:\w+:", res).group()
    password = password[5:-1]
    print("THE PASSOWRD IS", password)
    print(" THIS IS ", i)
    d = subprocess.run([f"unzip -P '{password}' {i}.zip"], shell=True)
    print(d.args)
