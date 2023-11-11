@echo off
rmdir /s /q build
rmdir /s /q out
del /s /q *.spec

mkdir out

pyinstaller -i ".\icon\icon_wallpaper.ico" --distpath out --add-binary ".\Wallpaper\Seewo_3840_2160.jpg;." --name "SeewoWallpaper" --onefile SeewoWallpaper.py
pyinstaller -i ".\CCleaner\CCleaner.exe" --distpath out --add-binary "CCleaner;CCleaner" --name "CCleaner" --hide-console hide-early --onefile CCleaner.py
pyinstaller -i ".\CCleaner\CCleaner.exe" --distpath out --add-binary "CCleaner;CCleaner" --name "CCleaner Portable" --hide-console hide-early --onefile CCleaner_Protable.py
pyinstaller --distpath out --add-binary ".\bin\hosts;." --name "Hosts Pather" --hide-console hide-early --onefile hosts_patch.py