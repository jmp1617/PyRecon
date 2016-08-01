from tld import get_tld
__author__ = 'Jacob'


def get_domain_name(url):
    print('Getting Top Level Domain')
    domain_name = get_tld(url)
    return domain_name