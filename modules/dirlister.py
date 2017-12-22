# -*- coding: utf-8 -*-
import os, sys


def run(**args):
    sys.stdout.write("[*] In dirlister module.\n")
    sys.stdout.flush()
    files = os.listdir(".")
    
    return str(files)