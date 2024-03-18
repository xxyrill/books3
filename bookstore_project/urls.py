from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management
    path('accounts/', include('allauth.urls')),     # new

    # locals apps
    path('accounts/', include('users.urls')),   # new
    path('', include('pages.urls')),    # new
]
