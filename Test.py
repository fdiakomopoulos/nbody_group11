# Scrip to test the difference in time between C++ and Python

import subprocess
import sys
from time import perf_counter_ns

if __name__ == "__main__":
    cmd_cpp_release = [".\\cmake-build-release\\nbody.exe"]
    cmd_cpp_debug = [".\\cmake-build-debug-visual-studio\\Debug\\nbody.exe"]
    cmd_python = ["python", ".\\nbody.py"]
    for number in ["5000", "500000", "5000000", "50000000"]:
        for file in [cmd_cpp_release,cmd_cpp_debug,cmd_python]:
            sub_file = file + [number, "testing", "false"]
            if file[0].startswith("python"):
                p = subprocess.run(sub_file)
            else:
                p = subprocess.check_call(sub_file, shell=True)
                print("The above values from: ", file)
                print(p)




