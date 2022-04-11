from phpipam_client import PhpIpamClient, GET, PATCH
import sys
import json

ip = sys.argv[1]
ipam = PhpIpamClient(
    url = 'http://ipmanager.info.ufrn.br/',
    app_id='horus',
    token='3ecbea6ab487e3d38ab1f8a50481ae2b',
    encryption=True,)

def get_info(ip):
    return ipam.get('/addresses/search/'+ ip +'/')

print(json.dumps(get_info(ip), indent=4))