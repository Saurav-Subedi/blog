from django.contrib import admin
from .models import ContactInquiry
from . models import *
from .models import Question, Choice
from django.utils.html import format_html

# Register your models here.

# admin.site.register(Post)
admin.site.register(Profile) 
admin.site.site_header = " Admin"
admin.site.site_title = " Admin Area"
admin.site.index_title = "Welcome to the admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-timestamp',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=['name','slug','show_image']
    prepopulated_fields={'slug':('name',)}
    search_fields=['name','slug']

    def show_image(self,obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="80"/>')
        else:
            return 'No Image'
        

@admin.register(Post)
class AdminCategory(admin.ModelAdmin):
    list_display=['category','name','slug','description','date_posted','author']
    prepopulated_fields={'slug':('name',)}
    search_fields=['name','slug']
