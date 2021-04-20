from django.contrib import admin
from .models import Exscursion


class ExscursionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'type')
    # fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    save_on_top = True


admin.site.register(Exscursion, ExscursionAdmin)
