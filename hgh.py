#!/usr/bin/env python3
from pathlib import Path

class COUT_FILE:
    def __init__(self, file_name):
        self.file_path = Path(file_name)
        self.file_path.open('a')

    def __lshift__(self, out_str):
         self.file.write(out_str) 

    def __del__(self):
            self.file.close()


f = COUT_FILE('output.txt')
f << "hello world\n"
