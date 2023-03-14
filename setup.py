import cx_Freeze

executables = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name='Alien Invasion',
    version='1.0.0',
    description='This package is a Galaga style game called "Alien Invasion"',
    author='Ashley Reiss',
    url='https://github.com/ashleyrreiss/csc121',
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["alien.bmp", "ship.bmp"]}},
    executables = executables
)