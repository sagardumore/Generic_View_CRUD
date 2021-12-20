from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Laptop
from django.contrib.messages.views import SuccessMessageMixin

class AddLaptopView(SuccessMessageMixin,CreateView):
    model=Laptop
    fields = '__all__'
    success_url = '/laptop/showlaptop/'
    success_message = "Order Added successfully"
    #template_name = 'model_form.html'

class ShowLaptopView(ListView):
    model = Laptop
    # context_object_name = 'object_list'
    # template_name = 'model_list.html'

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/showlaptop/'
    # template_name - 'model_form.html'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url= '/laptop/showlaptop/'
    # template_name = 'model_confirm_delete.html'