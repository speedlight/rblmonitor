from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

from rbls.models import Rbllist

class RBLView(generic.TemplateView):
    template_name = 'rbl_list.html'

    def get(self, request):
        rbls = Rbllist.objects.all()
        return render(request, self.template_name, {'rbls': rbls})