from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

from rbls.forms import AddrForm
from rbls.models import Rbllist
from rbls.bin.blcheck import _ipstatus

rbls = Rbllist.objects.values_list('name', flat=True)
bls_url = Rbllist.objects.values_list('url', flat=True)


class RBLView(generic.TemplateView):
    template_name = 'rbl_list.html'

    def get(self, request):
        addrform = AddrForm()

        data = { 'rbls': rbls, 'form': addrform }

        return render(request, self.template_name, data)

class RBLCheck(generic.TemplateView):
    template_name = 'rbl_check.html'

    def get(self, request):

        check = []
        if request.method == 'GET':
            addrform = AddrForm(request.GET)
        if addrform.is_valid():
            address = addrform.cleaned_data['address']

            for bl in bls_url:
                check.append(_ipstatus(address, bl))

            data = {
                'bls': bls_url,
                'address': address,
                'check': check,
            }

            return render(request, self.template_name, data)

        else:
            addrform = AddrForm()
            return HttpResponseRedirect('/rbls/list')

        return HttpResponseRedirect('/rbls/list')
