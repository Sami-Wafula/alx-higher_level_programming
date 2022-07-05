#!/usr/bin/python3
"""Read text file"""


def read_line(filename=""):
    """open file"""
    with open(filename, encoding="utf-8") as a:
        read_data = a.read()
