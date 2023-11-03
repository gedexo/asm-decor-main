from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import urllib.parse
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from .models import ServiceCategory,Service,Update,Project
from .forms import ContactForm,ServiceEnquiryForm,CareerForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "web/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicescategories"] = ServiceCategory.objects.all()
        context["updates"] = Update.objects.all()
        context['is_index'] = True
        return context
    

class AboutView(TemplateView):
    template_name = "web/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_about"] = True
        return context
    
    




class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_project"] = True
        return context



class UpdatesListView(ListView):
    model = Update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class UpdateDetailView(DetailView):
    model = Update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context





class ServiceCategoryListView(ListView):
    model = ServiceCategory
    context_object_name="servicescategories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_service"] = True
        return context


class ServiceSingleView(TemplateView):
    template_name="web/service-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(ServiceCategory, slug=category_slug)
        context["services"] = Service.objects.filter(category=category)

        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_service"] = True
        return context


class ServiceDetailView(DetailView,FormView):
    model = Service
    form_class = ServiceEnquiryForm

    def form_valid(self, form):
        service = self.get_object()
        form.instance.service = service
        form.save()
        message = (
            f"service Name: {service.title}\n"
            f'Name: {form.cleaned_data["name"]}\n'
            f'Phone: {form.cleaned_data["phone"]}\n'
            f'Email: {form.cleaned_data["email"]}\n'
        )

        whatsapp_api_url = "https://api.whatsapp.com/send"
        phone_number = "918943915070"
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

        messages.success(self.request, "Successfully saved")
        return redirect(whatsapp_url)

    def form_invalid(self, form):
        response_data = {"error": "Invalid form submission"}
        return JsonResponse(response_data, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_service"] = True
        return context
    

class ContactView(FormView):
    template_name = "web/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        response_data = {"message": "Your message has been submitted successfully!"}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"error": "Invalid form submission"}
        return JsonResponse(response_data, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_contact"] = True
        return context
    

class CareerView(FormView):
    template_name = "web/career.html"
    form_class=CareerForm

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Successfully Submitted","message": "Message successfully updated",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_career"] = True
        return context
    

