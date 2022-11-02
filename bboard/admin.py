from typing import Sequence, Union, Callable, Any, Optional
from django.contrib import admin

from .models import Bb, Rubric

# Register your models here.
class BbAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable[[Any], Any]]] = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links: Optional[Sequence[Union[str, Callable[..., Any]]]] = ('title', 'content',)
    search_fields: Sequence[str] = ('title', 'content',)

class RubricAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable[[Any], Any]]] = ('name',)
    list_display_links: Optional[Sequence[Union[str, Callable[..., Any]]]] = ('name',)
    search_fields: Sequence[str] = ('name',)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
