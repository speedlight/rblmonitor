from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

from rbls.forms import AddrForm
from rbls.models import Rbllist
from rbls.bin.blcheck import _ipstatus

rbls = Rbllist.objects.all()


class RBLView(generic.TemplateView):
    template_name = 'rbl_list.html'

    def get(self, request):
        addrform = AddrForm()

        data = { 'rbls': rbls, 'form': addrform }

        return render(request, self.template_name, data)

class RBLCheck(generic.TemplateView):
    template_name = 'rbl_check.html'

    def get(self, request):

        if request.method == 'GET':
            addrform = AddrForm(request.GET)
        if addrform.is_valid():
            address = addrform.cleaned_data['address']

            # import bin/blcheck.py and get an array of [rbl,state]
            result = _ipstatus(address)
            data = {
                'rbls': rbls,
                'address': address,
                'result': result,
            }

            return render(request, self.template_name, data)

        else:
            addrform = AddrForm()
            return HttpResponseRedirect('/rbls/list')

        return HttpResponseRedirect('/rbls/list')
