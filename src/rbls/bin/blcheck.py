from rbls.models import Rbllist
import dns.resolver
import dns.reversename

def _ipstatus(ip, bl):

    reverse_ip = dns.reversename.from_address(ip)
    resol = dns.resolver.Resolver(configure=False)
    resol.nameservers = ['192.168.1.1']
    full_reverse_addr = str(reverse_ip.split(3)[0]) + '.' + bl

    try:
        addr_txt = resol.query(full_reverse_addr, 'TXT')
        addr_a = resol.query(full_reverse_addr, 'A')
        result = "The {} in {} is listed: {} with {}!".format(ip, bl, addr_txt[0], addr_a[0])
        print(result)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
        result = "The {} is not listed in {}!".format(ip, bl)
        print(result)
        pass

    return result