#Recordar instalar whois en la vm donde vaya a correr el servicio web
import whois

def get_whois_info(url):
    try:
        w = whois.query(url)
        return str(w.__dict__).replace(", '"," \n'")
    except Exception as e:
        return f"Error retrieving WHOIS information: {e}"
