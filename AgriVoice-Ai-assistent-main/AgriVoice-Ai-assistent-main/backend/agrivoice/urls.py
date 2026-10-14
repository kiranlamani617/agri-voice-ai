import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from api.views import home

ui_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'agrivoice-ui')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('auth/', include('users.urls')),
    path('api/auth/', include('users.urls')),
    path('api/', include('api.urls')),
    re_path(r'^(?P<path>(styles\.css|app\.js))$', serve, {'document_root': ui_dir}),
]
