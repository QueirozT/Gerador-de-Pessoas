from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
	script="main.py",
	base="Win32GUI",
	icon="icon.ico"
)

# SETUP CX FREEZE
setup(
	name = "Gerador de Pessoas",
	version = "1.0",
	description = "Um programa simples que gera dados falsos de pessoas",
	author = "Tiago Q. Gonçalves",
	options = {'build_exe' : {'include_files' : files}},
	executables = [target]
)