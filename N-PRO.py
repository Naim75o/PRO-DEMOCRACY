import os, sys
try:
    __import__("socks4")
except Exception as e:
    exit(str(e))
