from django.contrib import admin
from blog.models import Topic, Entry

class TopicAdmin(admin.ModelAdmin):
  list_display = ("name","first_name", "text", "created_date")

admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry)
