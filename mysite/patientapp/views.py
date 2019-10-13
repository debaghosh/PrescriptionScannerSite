from django.shortcuts import render
from .models import Prescription
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    presciption = Prescription.objects.all()
    return render(request, 'patientapp/home.html',context={'prescription':presciption})


class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'patientapp/home.html'
    context_object_name = 'prescription'
    ordering=['-date']

class PrescriptionDetailView(DetailView):
    model = Prescription
    

class PrescriptionCreateView(LoginRequiredMixin, CreateView):
    model = Prescription
    fields = ['medical_problem', 'doctor','image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

