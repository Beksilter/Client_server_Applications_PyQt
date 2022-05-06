import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "log", "client", "unit_tests"],
}
setup(
    name="beksilter_messenger_client",
    version="0.3.3",
    description="beksilter_messenger_client",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client_side.py',
                            # Чтобы убрать консоль, необходимо раcкоментировать строку:
                            # base='Win32GUI',
                            targetName='client.exe',
                            )]
)