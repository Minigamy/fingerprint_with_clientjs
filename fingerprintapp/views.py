from django.shortcuts import render

from django.views import View


class Fingerprint(View):
    def get(self, request):
        ip = request.headers.get('X-Real-IP')
        return render(request, 'fingerprintapp/fingerprint.html', context={'ip': ip})
