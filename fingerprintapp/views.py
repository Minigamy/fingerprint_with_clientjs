from django.shortcuts import render
import requests

import data
from django.views import View


class Fingerprint(View):

    def get(self, request):
        is_tor = False

        request_ip = '61.7.195.194'
            # str(request.headers.get('X-Real-IP'))

        if request_ip in data.tor_ip_list:
            is_tor = True

        # vpnapi_info = (requests.get(f'https://vpnapi.io/api/{request_ip}?key=5d458b25a61345cdb4ed78563b82836c')).json()
        ipinfo = (requests.get(f'https://ipinfo.io/{request_ip}/privacy?token=861f5ef47b8113')).json()
        # ipdata = requests.get(
        #         f'https://api.ipdata.co/{request_ip}?api-key=2992ccd498bab4e86af5763df63bd10d7bf5f32665f3d26b68e3c823')

        return render(request, 'fingerprintapp/fingerprint.html',
                      context={'ip': request_ip,
                               'is_tor': is_tor,
                               'is_vpn': ipinfo['vpn'],
                               'is_proxy': ipinfo['proxy']}
                      )
