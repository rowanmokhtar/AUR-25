#!/usr/bin/env python3
from pathlib import Path

def save_sentence(sentence: str, file_name: str = 'output.txt') :
    file_path = Path(file_name)
    try:
        with file_path.open('a') as file:
            file.write(sentence + "\n")    
        return True
    except Exception:
        return False
try:
    while True:
        save_sentence(input())
except KeyboardInterrupt:
    print("exit")
