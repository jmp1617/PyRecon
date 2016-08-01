import os
__author__ = 'Jacob'


def get_nmap(ip):
    print('Nmap Scan')
    command = "nmap -F "+ip
    process = os.popen(command)
    results = str(process.read())
    return results
