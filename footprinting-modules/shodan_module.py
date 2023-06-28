from decouple import config
from shodan import Shodan
from nslookup_module import get_ips

api = Shodan(config('SHODAN_API_KEY'))

# Lookup an IP
def get_shodan_byip(IP):
    ipinfo = api.host(IP)
    infoshow=str(ipinfo).replace(",", ", \n")
    return infoshow

# Lookup multiples IP's
def get_shodan_bydomain(domain):
    LINE="<-------------------------> \n"
    IPs=get_ips(domain)
    out_shodan=''
    
    for i in IPs:
        out_shodan=out_shodan + LINE +"IP: " + i + '\n\n' + get_shodan_byip(i) + "\n\n\n\n"
    
    return out_shodan
    
