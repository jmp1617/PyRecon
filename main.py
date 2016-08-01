
from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_text import *
from whois import *
__author__ = 'Jacob'


ROOT_DIR = 'PyReconScan'
create_dir(ROOT_DIR)


def using_ip():
    print("Enter name of scan")
    name = input('>')
    print("Enter ip address")
    ip = input('>')
    gather_info_ip(name, ip)


def using_url():
    print("Enter name of scan")
    name = input(">")
    print("Enter full url")
    fullUrl = input('>')
    print("Name: "+name+"  Full Url: "+fullUrl)
    gather_info(name, fullUrl)

def gather_info_ip(name, ip):
    nmap = get_nmap(ip)
    whois = get_whois(ip)
    create_report_ip(name,ip,nmap,whois)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap(ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name,nmap,ip_address,robots_txt, whois)

def create_report_ip(name, ip_address, nmap, whois):
    project_dir = ROOT_DIR+'/'+name
    create_dir(project_dir)
    write_file(project_dir+'/ip_address.txt', ip_address)
    write_file(project_dir+'/nmap.txt', nmap)
    write_file(project_dir+'/whois.txt', whois)

def create_report(name, full_url, domain_name,nmap, ip_address,robots_txt,whois):
    project_dir = ROOT_DIR+'/'+name
    create_dir(project_dir)
    write_file(project_dir+'/full_url.txt', full_url)
    write_file(project_dir+'/domain_name.txt', domain_name)
    write_file(project_dir+'/ip_address.txt', ip_address)
    write_file(project_dir+'/nmap.txt', nmap)
    write_file(project_dir+'/robots_txt.txt', robots_txt)
    write_file(project_dir+'/whois.txt', whois)


def main():
    print("Python Recon")
    print("Use an IP address(Nmap and Whois) or a full URL(IP/URL)")
    print("Enter URL or IP")
    ans = ""
    while (not(ans == "URL"))and(not(ans == "IP")):
        ans = input('(All Caps)>')
    if ans=="URL":
        using_url()
    elif ans=="IP":
        using_ip()
main()
