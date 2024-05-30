# pip_packages.sh

# #!/bin/bash

# python ex1_0_setup.py
# pip list

import pkg_resources
import sys

inst_pck = [pkg.key for pkg in pkg_resources.working_set]

for pack in inst_pck:
    print(pack)
    
print("pythov -V", sys.version)