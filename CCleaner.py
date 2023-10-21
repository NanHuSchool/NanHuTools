# -*- coding: utf-8 -*-
'''
释放CCleaner并执行清理
'''
import os
import shutil
import sys

def main():
    # CClenaer 文件
    Main_path = r'C:\Program Files'
    CCleaner_path = os.path.join(Main_path, "CCleaner")
    CCleaner_exec = os.path.join(CCleaner_path, "CCleaner.exe")
    # 将要释放的文件
    file_dirname = 'CCleaner'
    file_path = os.path.join(os.path.dirname(__file__), file_dirname)
    print('Main_path: ' + Main_path)
    print('CCleaner_path: ' + CCleaner_path)
    # 判断目标文件夹是否存在，并删除
    try:
        if os.path.exists(CCleaner_path):
            print(f"存在文件夹：{CCleaner_path}")
            shutil.rmtree(CCleaner_path)
            print('删除成功！！！')
    except OSError as e:
            print(f'无法获取文件状态！：\n{str(e)}')
            sys.exit()
    # 开始释放文件
    try:
         if os.path.exists(file_path):
            shutil.copytree(file_path, CCleaner_path)
         else:
              print("源文件不存在！")
              sys.exit
         print(f'正在释放源文件：{file_path}')
         print(f'成功释放文件：{CCleaner_path}')
    except Exception as e:
         print(f'正在释放源文件：{file_path}')
         print(f'释放文件失败！：\n{str(e)}')
         sys.exit()
    # 运行CCleaner
    command = f"\"{CCleaner_exec}\" /AUTOSC"
    try:
        os.system(command)
        print(f'运行命令成功：{command}')
    except Exception as e:
        print(f'命令运行失败！：\n{str(command)}')

if __name__ == '__main__':
    main()