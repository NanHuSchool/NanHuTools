# -*- coding: utf-8 -*-
'''
修改Host文件并刷新
'''
import os
import shutil
import sys

def main():
    # Hosts 路径
    hosts_dir = r'C:\Windows\System32\drivers\etc'
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    try:
        if os.path.exists(hosts_path):
            with open(hosts_path, mode='r', encoding='utf-8') as f:
                context = f.read()
                print(f"原Host文件内容：\n{context}\n")
    except OSError as e:
        print(f'无法打开Hosts文件：\n{e}')
        sys.exit()
    # 替换准备好的Host文件
    hosts_mod_name = "hosts"
    hosts_mod_path = os.path.join(os.path.dirname(__file__), hosts_mod_name)
    if os.path.exists(hosts_mod_path):
        try:
            shutil.copyfile(hosts_mod_path, hosts_path)
            with open(hosts_path, mode='r', encoding='utf-8') as f:
                context = f.read()
                print(f'替换成功！替换后的内容：\n{context}')
        except Exception as e:
            print(f'无法替换！：\n{str(e)}')
            sys.exit()
    else:
        print(f'没有找到需要替换的文件：{hosts_mod_path}')
        sys.exit()
    # 刷新DNS
    flushdns_command = 'ipconfig /flushdns'
    os.system(flushdns_command)
    print('刷新DNS解析成功')

if __name__ == '__main__':
    main()