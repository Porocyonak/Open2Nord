from cx_Freeze import setup, Executable
import os

# REPLACE THESE DIRECTORIES WITH YOUR LOCAL MACHINE'S DIRECTORIES! wish this wasn't an issue :(
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tk8.6'

base = None    

# https://stackoverflow.com/questions/10527454/change-icon-for-a-cx-freeze-script
executables = [Executable("Open2Nord.py", base=base, icon="Sad.ico")]

packages = ["idna", "json", "requests", "shutil", "subprocess", "os", "ctypes", "time"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<OpenVPNxNordServerFinder>",
    options = options,
    version = "<1.0.3>",
    description = '<the coolest program around>',
    executables = executables
)