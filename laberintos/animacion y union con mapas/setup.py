from cx_Freeze import *

import cx_Freeze
 
executables = [cx_Freeze.Executable("PONGfinal.py",
                                 base = "Win32GUI",
                                 icon = "icon.ico")]
 
build_exe_options = {"packages": ["pygame"],
                     "include_files":["arial.ttf",
                                      "pierdes.wav",
                                      "rebote.wav",
                                      "icon.png"]}
 
cx_Freeze.setup(
    name = "PONG",
    version = "1.0",
    description = "Juego PONG",
    options={"build_exe": build_exe_options},
    executables = executables
    )
