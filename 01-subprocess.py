import sys
import subprocess

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
END = "\033[0m"

cmds = ["pwd",
        "sleep 1",
        "pwd;sleep 1",
        "ping www.baidu.com -c 5",
        "pwdddd",
        "pwd"
        ]
for cmd in cmds:
    subp = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    while subp.poll() is None:
        line = subp.stdout.readline()
        if line:
            print(line.decode("utf8").strip())
    if subp.returncode == 0:
        print(GREEN + "成功---命令: " + cmd + END)
    else:
        err = subp.stderr.read().decode("utf8").strip()
        print(RED + "失败---命令: " + cmd + END)
        print(YELLOW + "错误信息: " + err + END)
        sys.exit(1)
