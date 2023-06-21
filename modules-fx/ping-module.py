from pythonping import ping

#Corroboramos el icmp
def check_icmp_availability(target):
    try:
        response = ping(target, count=4)
        if response.success():
            return f"ICMP protocol is available on {target} \n" + str(response)
            
        else:
            return f"ICMP protocol is not available on {target} \n" + str(response)
            
    except Exception as e:
        return f"An Error occurred while checking ICMP availability: {str(e)}"
        
#Gestionamos el archivo.tex para la generacion de reportes.