from django.contrib import admin
from .models import Choice,Question,Comments
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,               {'fields': ['auth']}),
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question picture',{'fields':['image']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Comments)
