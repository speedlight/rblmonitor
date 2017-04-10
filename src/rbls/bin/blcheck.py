import dns.resolver
import dns.reversename
import ipaddress

data = []
resol = dns.resolver.Resolver(configure=False)
resol.timeout = 5
resol.nameservers = ['192.168.4.20']


def _get_addr(query):
    if ipaddress.ip_address(query):
        return query
    else:
        raise ValueError()
    try:
       addr = resol.query(query, 'a')
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
       pass
    if not addr:
        raise ValueError("There isn't any a records for the domain")
    return addr[0]


def _ipstatus(address, bl):
    ip_addr = _get_addr(address)
    reverse_ip = dns.reversename.from_address(ip_addr)
    full_reverse_addr = str(reverse_ip.split(3)[0]) + '.' + bl

    try:
        response_txt = resol.query(full_reverse_addr, 'TXT')
        response_a = resol.query(full_reverse_addr, 'A')
        state = True
        message = {'address': address, 'bl': bl, 'txt': response_txt[0], 'a': response_a[0], 'state': state}
        data.append(message)
        print(message)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
        state = False
        message = {'address': address, 'bl': bl, 'state': state}
        data.append(message)
        print(message)
        pass

    return message



