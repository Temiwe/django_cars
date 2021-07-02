from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from car.models import Car, CarModel, Company
from car.forms import CarForm, CarModelForm, CompanyForm
from django.views.generic.edit import CreateView


# Create your views here.
class CarListView(ListView):

    template_name = "car_list.html"

    model = Car
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of cars",
            "list_len": len(context["car_list"])
            })
        return context


class CarDetailView(DetailView):

    template_name = "car.html"
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CarCreateView(CreateView):

    template_name = "car_create.html"

    model = Car


def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        print("post")
        if form.is_valid():
            form.save()
            return redirect("car-detail", pk=form.instance.pk)
    form = CarForm()
    return render(request, "car_create.html", {"form":form})


class CarModelListView(ListView):

    template_name = "carmodel_list.html"

    model = CarModel
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of car models"
            })
        return context


class CarModelDetailView(DetailView):

    template_name = "carmodel.html"
    model = CarModel

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)

        return context


class CarModelCreateView(CreateView):

    template_name = "modelcar_create.html"
    model = CarModel
    form_class = CarModelForm


def carmodel_create(request):
    if request.method == "POST":
        form = CarModelForm(request.POST)
        print("post")
        if form.is_valid():
            form.save()
            return redirect("car-models-detail", pk=form.instance.pk)
    form = CarModelForm()
    return render(request, "modelcar_create.html", {"form":form})


class CompanyListView(ListView):

    template_name = "company_list.html"

    model = Company
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of car companies"
            })
        return context


class CompanyDetailView(DetailView):

    template_name = "company.html"
    model = Company

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)

        return context


class CompanyCreateView(CreateView):
    template_name = "company_create.html"
    model = Company
    form_class = CompanyForm

def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        print("post")
        if form.is_valid():
            form.save()
            return redirect("company-detail", pk=form.instance.pk)
    form = CompanyForm()
    return render(request, "company_create.html", {"form": form})