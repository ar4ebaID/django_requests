from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('request.urls')),
                  path('autocomplete_cus/', include('request.urls')),
                  path('autocomplete_lec/', include('request.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('<str:pk>/update', include('request.urls')),
                  path('login/', include('request.urls')),
                  path('logout/', include('request.urls')),
                  path('report/', include('request.urls')),
                  path('report/export_excel', include('request.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
