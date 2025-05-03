#!/usr/bin/env python3
import subprocess
import sys

filename = "sigils.ps"

sigils: list[str] = []
if len(sys.argv) > 1:
    sigils = sys.argv[1:]
else:
    with open(filename, 'r') as f:
        in_sigils = False
        for line in f:
            if line.startswith('/sigil_bank <<'):
                in_sigils = True
                continue
            if in_sigils and line.startswith('    /'):
                sigil_name = line.split()[0][1:]
                sigils.append(sigil_name)

base_command = "pstopng -0.6 d d d 100 sigil_dump.ps -Lset_nib_matrix -Pimages/".split()
for sigil_name in sigils:
    command = base_command + [f"sigil_{sigil_name}"]
    if sigil_name in ["COMPLETE", "RETURN"]:
        command[4] = '1.1'
    subprocess.run(command, check=True)
