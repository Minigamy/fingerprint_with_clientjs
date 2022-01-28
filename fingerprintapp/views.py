from django.shortcuts import render

from django.views import View


class Fingerprint(View):
    def get(self, request):
        return render(request, 'fingerprintapp/fingerprint.html')