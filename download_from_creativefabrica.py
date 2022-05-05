import requests
import re

def getFilename_fromCd(cd):
#Get filename from content-disposition
    if not cd:
    return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
    return None
    return fname[0]

def download_file(url): #herausfinden wo Dateien gespeichert werden
    r = requests.get(url, allow_redirects=True)
    filename = getFilename_fromCd(r.headers.get('content-disposition'))
    open(filename, 'wb').write(r.content)

download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=13603093&_wpnonce=9ac01f884b')
download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=28114472&_wpnonce=5d584069cf')
download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=28593430&_wpnonce=f2c3d96ba1')