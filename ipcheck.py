import urllib.request

def get_external_ip():
    """
    A function that retrieves the external IP address by querying a specific website.
    No parameters are needed.
    Returns a string representing the external IP address.
    """
    site = urllib.request.urlopen("https://ident.me").read().decode('utf8')
    return site

print(get_external_ip())