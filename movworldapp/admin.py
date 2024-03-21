from django.contrib import admin

from movworldapp.models import MovieCategory, MovieList


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'c_slug']
    prepopulated_fields = {'c_slug': ('category',)}


admin.site.register(MovieCategory, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'm_slug', 'release_date', 'category', 'added_by']
    prepopulated_fields = {'m_slug': ('title',)}
    list_editable = ['release_date', 'category']
    list_per_page = 20


admin.site.register(MovieList, MovieAdmin)
