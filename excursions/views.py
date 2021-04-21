from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Exscursion


def home(request):
    return render(request, 'excursions/index.html', {'section': 'excursions'})


class HomeExcursions(ListView):
    model = Exscursion
    template_name = 'excursions/index.html'
    context_object_name = 'excursions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'excursions'
        return context