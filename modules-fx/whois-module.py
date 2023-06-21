#Recordar instalar whois en la vm donde vaya a correr el servicio web
import whois
from ipwhois import IPWhois

#    except Exception as e:
#        return f"Error retrieving WHOIS information: {e}"

def get_whois_info_domain(url):
    w = whois.query(url)
    return str(w.__dict__).replace(", '"," \n'")


def get_whois_info_ip(ip):
    w = IPWhois(ip)
    return str(w.lookup_whois()).replace(", '"," \n'")

def get_whois_info(asset):
    try:
        return get_whois_info_domain(asset)
    except Exception as e1:
        try:
            return get_whois_info_ip(asset)
        except Exception as e2:
            return f"Error retrieving WHOIS information: {e1} \nError retrieving WHOIS information: {e2}"