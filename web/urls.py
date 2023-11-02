from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("update/", views.UpdateView.as_view(), name="update"),
    # path("update-detail/<slug>/", views.update_detail, name="update_detail"),
    path("career/", views.CareerView.as_view(), name="career"),
    path("service/", views.ServiceCategoryListView.as_view(), name="service"),
    path("services/<slug:category_slug>/", views.ServiceSingleView.as_view(), name="service-single"),
    path("service/<slug>/", views.ServiceDetailView.as_view(), name="service-detail"),

]