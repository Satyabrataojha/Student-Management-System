from cx_Freeze import *
import sys


includefiles = ['mana.ico']
excludes = []
pakages = []
base = None

if sys.platform == 'win32':
				base = 'win32GUI'

Shortcut_table = [
				('DesktopShortcut',  #
				 'DesktopFolder',
				 'StudentManagementSystem',
				 'TARGETDIR',
				 '[TARGETDIR]\StudentManagementSystem.exe',
				 None,
				 None,
				 None,
				 None,
				 None,
				 None,
				 'TARGEDIR',
				 )
]

msi_data = {'Shortcut': Shortcut_table}
bdist_msi_options = {'data': msi_data}

setup(
				version='0.1',
				description="Student Management System Devloped By Satyabrata Ojha",
				author='Satyabrata Ojha',
				name='Student Management System',
				options={'build.exe': {'include_files': includefiles}, 'bdist_msi': bdist_msi_options, },
				executables=[
								Executable(
												script='StudentManagementSystem.py',
												base=base,
												icon='mana.ico',
								
								)
				]
)