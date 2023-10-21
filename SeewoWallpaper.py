# -*- coding: utf-8 -*-
'''
更换希沃默认壁纸
'''
import os
import shutil

def main():
    # 投放壁纸的文件夹
    wallpaper_dir = r'C:\Windows\Web\Wallpaper\Seewo'
    # 投放的壁纸文件名
    wallpaper_filename = 'Seewo_3840_2160.jpg'
    # 壁纸文件绝对路径
    wallpaper_path = os.path.join(wallpaper_dir, wallpaper_filename)
    print("壁纸文件：" + wallpaper_path)
    # 待复制的文件路径
    file_path = os.path.join(os.path.dirname(__file__), 'Seewo_3840_2160.jpg')
    print("复制源文件：" + file_path)
    if os.path.exists(file_path) == False:
        print(f'未找到文件 {file_path}')
    # 创建壁纸文件夹
    if os.path.exists(wallpaper_dir):
        # 删除文件夹
        try:
            shutil.rmtree(wallpaper_dir)
            print("删除文件夹成功：" + wallpaper_dir)
        except OSError as e:
            print("删除文件夹失败：" + wallpaper_dir)
    try:
        os.makedirs(wallpaper_dir, exist_ok=True)
        print(f'文件夹创建成功：{wallpaper_dir}')
    except OSError as e:
        print(f'创建失败：{wallpaper_dir}')
    
    # 复制壁纸
    shutil.copy2(file_path, wallpaper_path)
    # 设置壁纸
    setpaper_command = f"REG ADD \"HKCU\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d \"{wallpaper_path}\" /f"
    print("正在执行：" + setpaper_command)
    os.system(setpaper_command)
    # 刷新壁纸
    reflush_command = "RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters"
    print("正在执行：" + reflush_command)
    os.system(reflush_command)

if __name__ == '__main__':
    main()