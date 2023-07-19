from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from website.language import set_language 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('UniversityConnect.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
    ] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)