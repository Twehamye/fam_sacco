from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fam_sacco_app.urls')),
]


# config Admin Page
admin.site.site_header ="FAMILY SACCO PANEL"
admin.site.site_title = "FAMILY SACCO WEBSITE"
admin.site.index_title ="Administration Area"