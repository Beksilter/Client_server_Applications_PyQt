import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "log", "server", "unit_tests"],
}
setup(
    name="beksilter_messenger_server",
    version="0.3.3",
    description="beksilter_messenger_server",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('server_side.py',
                            # Чтобы убрать консоль, необходимо раскоментировать строку:
                            # base='Win32GUI',
                            targetName='server.exe',
                            )]
)