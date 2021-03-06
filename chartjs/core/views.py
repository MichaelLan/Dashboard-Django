from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse
from django.db.models import Sum
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

from .models import Proyecto
from .forms import ProyectoForm


def get_data_id(request, id):

    if Proyecto.objects.filter(id=id).exists():
        p_1 = Proyecto.objects.filter(id=id)[0].perfil_1
        p_2 = Proyecto.objects.filter(id=id)[0].perfil_2
        p_3 = Proyecto.objects.filter(id=id)[0].perfil_3
        p_4 = Proyecto.objects.filter(id=id)[0].perfil_4
        p_5 = Proyecto.objects.filter(id=id)[0].perfil_5
        loc = Proyecto.objects.filter(id=id)[0].localidad
        pro = Proyecto.objects.filter(id=id)[0].proyecto

        labels = ['perfil 1', 'perfil 2', 'perfil 3', 'perfil 4', 'perfil 5']
        datasets = {'localidad':loc, 'proyecto':pro, 'labels': labels, 'data':[p_1, p_2, p_3, p_4, p_5]}

    else:
        labels = ['None', 'None', 'None', 'None', 'None']
        datasets = {'localidad':None, 'proyecto':'Proyecto No Existe', 'labels': labels ,'data':[0, 0, 0, 0, 0]}

    return JsonResponse([datasets], safe=False)


def get_data_localidad(request, slug):

    loc = Proyecto.objects.filter(slug_localidad=slug).first().localidad
    labels = ['perfil 1', 'perfil 2', 'perfil 3', 'perfil 4', 'perfil 5']

    k_p1, v_p1 = list(Proyecto.objects.filter(slug_localidad=slug).aggregate(perfil_1=Sum('perfil_1')).items())[0]
    k_p2, v_p2 = list(Proyecto.objects.filter(slug_localidad=slug).aggregate(perfil_2=Sum('perfil_2')).items())[0]
    k_p3, v_p3 = list(Proyecto.objects.filter(slug_localidad=slug).aggregate(perfil_3=Sum('perfil_3')).items())[0]
    k_p4, v_p4 = list(Proyecto.objects.filter(slug_localidad=slug).aggregate(perfil_4=Sum('perfil_4')).items())[0]
    k_p5, v_p5 = list(Proyecto.objects.filter(slug_localidad=slug).aggregate(perfil_5=Sum('perfil_5')).items())[0]


    datasets = {'localidad':loc, 'labels': labels, 'data': [v_p1, v_p2, v_p3, v_p4, v_p5]}

    return JsonResponse([datasets], safe=False)


class ProjectView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['localidades'] = set([x.localidad for x in Proyecto.objects.all()])
        return context


class NewProjectView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'create.html'
    success_url = reverse_lazy('core:home')



    
