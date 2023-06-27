from nslookup import Nslookup

domain = "microsoft.com"


def get_nslookup_info(domain):
    dns_query = Nslookup()
    
    dns_query = Nslookup(dns_servers=["8.8.8.8"], verbose=True, tcp=False)
    
    ips_record = dns_query.dns_lookup(domain)
    soa_record = dns_query.soa_lookup(domain)
    
    nsresponse = str(ips_record.response_full) + "\n" + str(ips_record.answer) + "\n\n" + str(soa_record.response_full) +"\n" + str(soa_record.answer) 
    nsresponse = nsresponse.replace("',", "', \n ")
    return nsresponse

