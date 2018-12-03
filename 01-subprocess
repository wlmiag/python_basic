import sys
import subprocess

cmds = ["pwd",
        "sleep 1",
        "pwd;sleep 1",
        "pwdddd",
        "pwd"
        ]
for cmd in cmds:
    subp = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    res = subp.communicate()
    if subp.returncode == 0:
        print('命令:%s \n成功: %s' % (cmd, res[0].decode('utf8')))
    else:
        print('命令:%s \n失败: %s' % (cmd, res[1].decode('utf8')))
        sys.exit(1)


# 运行结果：

# 命令:pwd 
# 成功: /home/keyide/Desktop/python_basic
# 
# 命令:sleep 1 
# 成功: 
# 命令:pwd;sleep 1 
# 成功: /home/keyide/Desktop/python_basic
# 
# 命令:pwdddd 
# 失败: /bin/sh: 1: pwdddd: not found
