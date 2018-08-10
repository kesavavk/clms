from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import contractor, Master


class IndextView( generic.ListView ):
    template_name = 'index.html'
    context_object_name = 'cont_list'

    def get_queryset(self):
        return contractor.objects.all()

class DetailView( generic.DetailView):
    model = contractor
    template_name = 'cont_detail.html'

class CreateCont( CreateView ):
    model = contractor
    fields = ['cid', 'cname', 'firmname', 'vendor_code', 'mobile', 'service_type', 'region']

class CreateCl( CreateView ):
    model = Master
    fields = ['contid', 'uid' ]