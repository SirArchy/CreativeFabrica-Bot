import requests
import re
from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=10, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x
secs=delta_t.total_seconds()
t1 = Timer(secs, download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=13603093&_wpnonce=9ac01f884b'))
t2 = Timer(secs, download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=28114472&_wpnonce=5d584069cf'))
t3 = Timer(secs, download_file('https://www.creativefabrica.com/de/cfsecure/download/?dg=28593430&_wpnonce=f2c3d96ba1'))
t1.start()
t2.start()
t3.start()


def getFilename_fromCd(cd):
#Get filename from content-disposition
    if not cd:
    return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
    return None
    return fname[0]

def download_file(url):
    r = requests.get(url, allow_redirects=True)
    filename = getFilename_fromCd(r.headers.get('content-disposition'))
    open(filename, 'wb').write(r.content)
