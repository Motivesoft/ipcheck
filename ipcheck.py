import urllib.request

def get_external_ip():
    site = urllib.request.urlopen("https://ident.me").read().decode('utf8')
    return site

print(get_external_ip())