# -*- coding: utf-8 -*-
import sys, socket


def run(**args):
    sys.stdout.write("[*] In helloworld module.\n")
    sys.stdout.flush()
    
    return "{} says Hello World!".format(socket.gethostname())