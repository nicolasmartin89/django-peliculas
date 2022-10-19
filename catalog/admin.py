from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Movie, MovieInstance, Language

"""Minimal registration of Models.
admin.site.register(Movie)
admin.site.register(Author)
admin.site.register(MovieInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)


class MoviesInline(admin.TabularInline):
    """Defines format of inline movie insertion (used in AuthorAdmin)"""
    model = Movie


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of movies in author view (inlines)
    """
    list_display = ('last_name',
                    'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [MoviesInline]


class MoviesInstanceInline(admin.TabularInline):
    """Defines format of inline movie instance insertion (used in MovieAdmin)"""
    model = MovieInstance


class MovieAdmin(admin.ModelAdmin):
    """Administration object for Movie models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of movie instances in movie view (inlines)
    """
    list_display = ('title', 'author', 'display_genre')
    inlines = [MoviesInstanceInline]


admin.site.register(Movie, MovieAdmin)


@admin.register(MovieInstance)
class MovieInstanceAdmin(admin.ModelAdmin):
    """Administration object for MovieInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('movie', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('movie', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
