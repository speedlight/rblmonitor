from django.conf import settings
from rbls.models import Rbllist
import dns.resolver
import dns.reversename

allbls = Rbllist.objects.values_list('url', flat=True)

def _ipstatus(ip):

    reverse_ip = dns.reversename.from_address(ip)
    resol = dns.resolver.Resolver()

    testbl = "zen.spamhaus.org"

    # for bls in allbls:
    full_reverse_addr = str(reverse_ip.split(3)[0]) + '.' + testbl
    addr_txt = dns.resolver.query(full_reverse_addr, "TXT")
    # addr_a = resol.query(full_addr, "A")
    # result = "ip got " + addr_a + addr_txt
    print (full_reverse_addr + addr_txt)
    data = {  }
    return data