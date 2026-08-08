from django.contrib import admin

from .models import Job, Application


class Jobadmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'salary', 'posted_by', 'date_posted']
    list_filter = ['location', 'salary', 'date_posted']
    search_fields = ['title', 'company_name', 'location']

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'date_applied']
    list_filter = ['date_applied']
    search_fields= ['job__title', 'applicant__username']


admin.site.register(Job, Jobadmin)
admin.site.register(Application, ApplicantAdmin)
