#!/usr/bin/env python3
import subprocess
import sys

examples: dict[str, list[int]] = {
    'xarray_example': [-2, -2, 2.5, 2],
    'array_example': [-2, -2, 2, 2],
    'dict_example': [-2.5, -2.5, 2.5, 2.5],
    'link_example': [-1.75, -7, 5.5, 1.75],
    'ligature_example': [-1.5, -7.5, 2, -1],
    'operator_array': [-1.1, -1.1, 1.1, 1.1],
    'name_array': [-1.1, -1.1, 1.1, 1.1],
    'string_array': [-1.1, -1.1, 1.1, 1.1],
    'operator_foo': [-1.1, -1.1, 1.1, 1.1],
    'name_foo': [-1.1, -1.1, 1.1, 1.1],
    'name_foobar': [-1.1, -1.1, 1.1, 1.1],
    'quicksort_example': [-4, -4.5, 4.25, 3.5, 2.5],
    'gcd_example': [-4, -3, 1.5, 2, 2.5],
    'smily_example': [-1, -1, 1, 1, 3],
    'comment_example': [-3, -3, 6.5, 3,],
}
base_command = "pstopng -0.6 d d d 50 examples.ps -Pimages/".split()
for name, dimensions in examples.items():
    command = base_command + [name]
    command[1:5] = [str(d) for d in dimensions[:4]]
    if len(dimensions) >= 5:
        command[5] = str(int(command[5]) * dimensions[4])
    print(' '.join(command))
    subprocess.run(command, check=True)
