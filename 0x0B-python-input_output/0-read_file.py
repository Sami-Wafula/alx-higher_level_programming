#!/usr/bin/python3
"""Read text file"""

def read_line(filename=""):
    """open file"""
    with open('my_file_0.txt', encoding="utf-8") as a:
        read_data = a.read()
