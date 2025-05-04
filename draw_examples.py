#!/usr/bin/env python3
import subprocess
import sys

examples: dict[str, list[int]] = {
    'xarray_example': [-2, -2, 2.5, 2],
    'array_example': [-2, -2, 2, 2],
    'dict_example': [-2.5, -2.5, 2.5, 2.5],
}
base_command = "pstopng -0.6 d d d 100 examples.ps -Pimages/".split()
for name, dimensions in examples.items():
    command = base_command + [name]
    command[1:5] = [str(d) for d in dimensions]
    print(' '.join(command))
    subprocess.run(command, check=True)
