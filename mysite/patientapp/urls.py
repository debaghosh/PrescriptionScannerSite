
from django.urls import path
from . import views
from .views import PrescriptionListView, PrescriptionDetailView, PrescriptionCreateView

urlpatterns = [
    #path('', PrescriptionListView.as_view() , name='home'),
    path('prescription/<int:pk>/',PrescriptionDetailView.as_view(),name='prescription_detail'),
    path('prescription/new/',PrescriptionCreateView.as_view(),name='prescription_create'),






]