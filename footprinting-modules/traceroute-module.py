import subprocess

def traceroute(url):
    try:
        result = subprocess.check_output(["traceroute", url])
        return result.decode()
    except Exception as e:
        return f"An Error occurred while checking the traceroute: {str(e)}"