import sys
import os
from cx_Freeze import setup, Executable

setup(
	name="Hahaha",
	version = "2.0",
	description = "Null",
	executables = [Executable(("C:\\Users\\anony\\Documents\\Python\\curiosity\\debug\\create_executable"), base = "Win32GUI")])
