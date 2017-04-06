from django.conf import settings
from rbls.models import Rbllist
import dns.resolver
import dns.reversename

bls = Rbllist.objects.all()

def _ipstatus(ip):

    reverse_ip = dns.reversename.from_address(ip)
    full_addr = str(reverse_ip.split(3)[0]) + '.' + str(bls[0])

    resol = dns.resolver.Resolver()
    ans = resol.query(full_addr, "TXT")


    data = { ans[0] }
    return data