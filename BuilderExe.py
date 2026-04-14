import PyInstaller.__main__
# import os

# vers = input("Введите версию")


PyInstaller.__main__.run([
    "--onefile",
    "--noconsole",
    # f"--distpath {os.path.abspath('dist/SnakeGame')}",
    "-n Змейка",
    "SnakeGame.py"
    # --version-file FILE
])