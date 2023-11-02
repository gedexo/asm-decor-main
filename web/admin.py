from django.contrib import admin
from .models import Service,ServiceCategory,Contact,ServiceEnquiry



@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(ServiceEnquiry)
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name",)