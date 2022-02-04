from django.shortcuts import render
import requests

import data
from django.views import View


class Fingerprint(View):

    def get(self, request):
        is_tor = False

        request_ip = str(request.headers.get('X-Real-IP'))
        proxy_ip1 = str(request.headers.get('X-Forwarded-For'))
        proxy_ip2 = str(request.headers.get('Forwarded'))
        proxy_ip3 = str(request.headers.get('X-Forwarded-Host'))
        proxy_ip4 = str(request.headers.get('X-Forwarded-Proto'))
        proxy_ip5 = str(request.headers.get('Via'))
        proxy_ip6 = str(request.headers.get('Proxy-Authenticate'))
        proxy_ip7 = str(request.headers.get('Proxy-Authentication-Info'))
        proxy_ip8 = str(request.headers.get('Proxy-Authorization'))
        proxy_ip9 = str(request.headers.get('Proxy-Connection'))
        proxy_ip10 = str(request.headers.get('X-Request-URI'))

        if request_ip in data.tor_ip_list:
            is_tor = True

        # vpnapi_info = (requests.get(f'https://vpnapi.io/api/{request_ip}?key=5d458b25a61345cdb4ed78563b82836c')).json()
        ipinfo = (requests.get(f'https://ipinfo.io/{request_ip}/privacy?token=861f5ef47b8113')).json()
        # ipdata = requests.get(
        #         f'https://api.ipdata.co/{request_ip}?api-key=2992ccd498bab4e86af5763df63bd10d7bf5f32665f3d26b68e3c823')

        return render(request, 'fingerprintapp/fingerprint.html',
                      context={'ip': request_ip,
                               'proxy_ip1': proxy_ip1,
                               'proxy_ip2': proxy_ip2,
                               'proxy_ip3': proxy_ip3,
                               'proxy_ip4': proxy_ip4,
                               'proxy_ip5': proxy_ip5,
                               'proxy_ip6': proxy_ip6,
                               'proxy_ip7': proxy_ip7,
                               'proxy_ip8': proxy_ip8,
                               'proxy_ip9': proxy_ip9,
                               'proxy_ip10': proxy_ip10,
                               'is_tor': is_tor,
                               'is_vpn': ipinfo['vpn'],
                               'is_proxy': ipinfo['proxy']}
                      )
