from django.shortcuts import render
import requests

import data
from django.views import View


class Fingerprint(View):

    def get(self, request):
        is_tor = False

        request_ip = str(request.headers.get('X-Real-IP'))

        if request_ip in data.tor_ip_list:
            is_tor = True

        vpnapi_info = (requests.get(f'https://vpnapi.io/api/{request_ip}?key=5d458b25a61345cdb4ed78563b82836c')).json()

        return render(request, 'fingerprintapp/fingerprint.html',
                      context={'ip': request_ip,
                               'is_tor': is_tor,
                               'is_vpn': vpnapi_info['security']['vpn'],
                               'is_proxy': vpnapi_info['security']['proxy']}
                      )
