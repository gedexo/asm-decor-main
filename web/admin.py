from django.contrib import admin
from .models import Service,ServiceCategory,Contact,ServiceEnquiry,Update,Career,Project,Testimonial



@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
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

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=('name','designation', 'review')