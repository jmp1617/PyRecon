import os
__author__ = 'Jacob'


def get_whois(url):
    print('Generating Whois')
    command = "whois "+url
    process = os.popen(command)
    results = str(process.read())
    return results
