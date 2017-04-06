from rbls.models import Rbllist
import dns.resolver
import dns.reversename

bls = Rbllist.objects.values_list('url', flat=True)

def _ipstatus(ip):

    reverse_ip = dns.reversename.from_address(ip)
    resol = dns.resolver.Resolver(configure=False)
    resol.nameservers = ['190.11.248.6']

    for bl in bls:
        try:
            full_reverse_addr = str(reverse_ip.split(3)[0]) + '.' + bl
            addr_txt = resol.query(full_reverse_addr, 'TXT')
            addr_a = resol.query(full_reverse_addr, 'A')
            result = "The {} in {} is listed: {} with {}!".format(ip, bl, addr_txt[0], addr_a[0])
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            result = "The {} is not listed in {}!".format(ip, bl)

    #print ("full_reverse_addr : {}, {}".format(addr_a[0], addr_txt[0]))

    data = { result }
    return data