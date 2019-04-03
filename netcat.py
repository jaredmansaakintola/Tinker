import sys
import socket
import getopt
import threading
import subprocess


listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "Netcat Net Tool"
    print
    print "Usage: netcat.py - target_host -p port"
    print "-l --listen                        - listen on [host]:[port] for\
                                                incoming connections"
    print "-e --execute=file_to_run - execute the given file upon recieving \
        a connection"
    print "-c --command -initialize a command shell"
    print "-u --upload=destination - upon recieving connection upload a file \
        and write to [destination]"
    print
    print
    print "Examples: "
    print "netcat.py -t 192.168.0.1 -p"
