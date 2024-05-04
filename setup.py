from cx_Freeze import setup, Executable

setup(
    name="NetHawk",
    version="1.0",
    description="NetHawk",
    executables=[Executable("main.py")]
)
