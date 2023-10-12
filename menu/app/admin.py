from django.contrib import admin
from django import forms
from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):

    fields = ['title', 'slug']
    list_display = ['title', ]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    fields = ['title', 'url', 'parent', 'category']
    list_display = ['title', 'category', 'parent']

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'url': forms.TextInput(attrs={'placeholder': 'URL разделять: /'})
        }
        return super().get_form(request, obj, **kwargs)
