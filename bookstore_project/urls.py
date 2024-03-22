from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user management
    path('accounts/', include('allauth.urls')),     # new

    # locals apps
    path('', include('pages.urls')),    # new, has your home and about page, 1
    path('accounts/', include('users.urls')),  # new, has your signup page, 2
    path('books/', include('books.urls')), # new, has your books page, 3
]
