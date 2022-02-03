from django.shortcuts import render
# import requests

import data
from django.views import View


class Fingerprint(View):

    def get(self, request):
        is_tor = False

        request_ip = str(request.headers.get('X-Real-IP'))

        if request_ip in data.tor_ip_list:
            is_tor = True

        return render(request, 'fingerprintapp/fingerprint.html', context={'ip': request_ip, 'is_tor': is_tor})

# vpnapi = requests.get(f'https://vpnapi.io/api/{ip}?key=5d458b25a61345cdb4ed78563b82836c')
# ipinfo = requests.get(f'https://ipinfo.io/{ip}/privacy?token=861f5ef47b8113')
# ipdata = requests.get(f'https://api.ipdata.co/{ip}?api-key=2992ccd498bab4e86af5763df63bd10d7bf5f32665f3d26b68e3c823')
#
# print(vpnapi.json()['security'])
# print()
# print(ipinfo.json())
# print()
# print(ipdata.json()['threat'])
