from rbls.models import Rbllist
import dns.resolver
import dns.reversename

def _ipstatus(ip, bl):

    data = []
    reverse_ip = dns.reversename.from_address(ip)
    resol = dns.resolver.Resolver(configure=False)
    resol.timeout = 5
    resol.nameservers = ['192.168.1.1']
    full_reverse_addr = str(reverse_ip.split(3)[0]) + '.' + bl

    try:
        addr_txt = resol.query(full_reverse_addr, 'TXT')
        addr_a = resol.query(full_reverse_addr, 'A')
        state = True
        response = { 'ip': ip,
                'bl': bl,
                'txt': addr_txt[0],
                'a': addr_a[0],
                'state': state
                }

        data.append(response)
        print(response)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
        state = False
        response = { 'ip': ip, 'bl': bl, 'state': state }
        data.append(response)
        print(response)
        pass

    return response
