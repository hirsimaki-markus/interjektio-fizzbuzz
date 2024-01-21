from __future__ import division, print_function

import argparse
import hashlib
import subprocess
import tempfile

POSIX_OUTPUT_HASH   = "d0e6e868d231a6e1fbd87cc2c092676b"
WINDOWS_OUTPUT_HASH = "e76a2755500f4d16c3e49a65d39ddd1e"

def get_output_hash(program, python27):
    python = "python2.7" if python27 else "python3"

    with tempfile.NamedTemporaryFile(mode="w+b") as f:
        f.write(program)
        f.flush()
        try:
            output = subprocess.check_output([python, "-c", program])
        except:
            return "Running with {} failed".format(python)

        output_hash = hashlib.md5(output).hexdigest()

    return output_hash


def main(args):
    with open(args.program, "rb") as f:
        program = f.read()

    # python27_hash = get_output_hash(program, python27=True)
    python3_hash = get_output_hash(program, python27=False)
    # print("Python 2.7 hash: {}".format(python27_hash))
    print("Python 3 hash: {}".format(python3_hash))

    # if python27_hash in [POSIX_OUTPUT_HASH, WINDOWS_OUTPUT_HASH]:
    #     print("Python 2.7 output matches!")
    # else:
    #     print("Python 2.7 output does not match!")

    if python3_hash in [POSIX_OUTPUT_HASH, WINDOWS_OUTPUT_HASH]:
        print("Python 3 output matches!")
    else:
        print("Python 3 output does not match!")

    total_bytes = len(program)
    total_lines = program.count(b"\n")

    print("Total bytes: {}".format(total_bytes))
    print("Total lines: {}".format(total_lines))

    contains_cfvwx = any(i in program for i in (b'c', b'f', b'v', b'w', b'x'))
    print("Contains any of 'cfvwx': {}".format(contains_cfvwx))

    for i in [100, 85]:
        print("Under {} bytes: {}".format(i, total_bytes < i))

    program_hash = hashlib.md5(program).hexdigest()
    print("Program hash: {}".format(program_hash))
    print("Program hash equals desired:", program_hash == "5d4dcb62fdf1fadf549344f449ba483d")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("program", help="program.py (a python file)")
    args = parser.parse_args()
    main(args)
