from django.contrib import admin
from fanfics.models import Keyword, FanFic

class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 3

class FanFicAdmin(admin.ModelAdmin):
    fields = ['title', 'pub_date']
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    inlines = [KeywordInline]

admin.site.register(FanFic, FanFicAdmin)
#keyword isn't registering correctly 
#"no such table: fancis_keyword"
admin.site.register(Keyword)