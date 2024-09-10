import os
import shutil
from robot.bot import GameRobot

main = 'main'
cmd = f'pyinstaller {main}.py -y -w'
cmd += ' -i ./ui/icon.ico'
bot = GameRobot()
print(bot.plugins)
for plugin in bot.plugins.keys():
    cmd += f' --hidden-import plugins.{plugin}'

requirements = [
    'cv2',
    'pywin32',
    'Pillow',
    'shapely',
    'pyclipper',
    'six',
    'onnxruntime',
    'PyQt6',
]
for module in requirements:
    cmd += f' --hidden-import {module}'

print(cmd)
os.system(cmd)

shutil.copytree('./plugins', f'./dist/{main}/_internal/plugins')
shutil.copytree('./ui', f'./dist/{main}/_internal/ui')
shutil.copytree('./source', f'./dist/{main}/_internal/source')
shutil.rmtree('./build', ignore_errors=True)
os.remove('./main.spec')
