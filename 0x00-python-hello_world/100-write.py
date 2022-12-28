#!/usr/bin/python3
import sys

def write_to_stderr(*input):
    sys.stderr.write(*input)

write_to_stderr("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)
