import os
__author__ = 'Jacob'


def get_ip_address(url):
    print('Getting Ip Adress')
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]
