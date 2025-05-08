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

base_command = "pstopng -0.6 d d d 50 sigil_dump.ps -Lset_nib_matrix -Pimages/".split()
big_sigils = [s for s in ["COMPLETE", "RETURN"] if s in sigils]
small_sigils = [s for s in sigils if s not in big_sigils]
sigils_by_size = [("-1.1", big_sigils), ("-0.6", small_sigils)]
for sigil_size, sigil_list in sigils_by_size:
    if sigil_list:
        base_command = f"pstopng {sigil_size} d d d 50 sigil_dump.ps -Lset_nib_matrix -Pimages/".split()
        command = base_command + [f"sigil_{sigil_name}" for sigil_name in sigil_list]
        subprocess.run(command, check=True)
