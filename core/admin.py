from django.contrib import admin
from .models import User, Teacher, Student,Event, EventMember

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)