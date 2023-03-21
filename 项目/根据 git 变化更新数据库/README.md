Windows 需要修改 subprocess.py line:760
把 encoding=None 修改为 encoding="utf-8"