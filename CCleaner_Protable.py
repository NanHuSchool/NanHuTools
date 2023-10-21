# -*- coding: utf-8 -*-
'''
隐藏运行 CCleaner 并执行清理
'''
import os
import sys

def main():
    # 文件夹以及可执行文件路径
    dir_name = 'CCleaner'
    dir_path = os.path.join(os.path.dirname(__file__), dir_name)
    exec_name = 'CCleaner.exe'
    exec_path = os.path.join(dir_path, exec_name)
    # 检测文件是否存在
    if os.path.exists(exec_path) == False:
        print(f'没有找到可执行程序：{exec_path}')
        sys.exit
    # 开始执行
    command = f"\"{exec_path}\" /AUTOSC"
    try:
        os.system(command)
        print(f'运行命令成功：{command}')
    except Exception as e:
        print(f'命令运行失败！：\n{str(command)}')

if __name__ == '__main__':
    main()