@echo off
rmdir /s /q build
rmdir /s /q out
del /s /q *.spec

mkdir out

pyinstaller -i ".\icon\icon_wallpaper.ico" --distpath out --add-binary ".\Wallpaper\Seewo_3840_2160.jpg;." --name "SeewoWallpaper" --onefile SeewoWallpaper.py