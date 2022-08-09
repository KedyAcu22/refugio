from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MVT.views import index, padre, inicio, en_construccion

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", index, name="index"),
    path("padre/", padre, name="padre"),
    path("inicio/", inicio, name="inicio"),
    path("en-construccion/", en_construccion, name="en_construccion"),
    path("", include("Apps.Mascota.urls")),
    path("", include("Apps.Refugio.urls")),
    # path("", include("Usuario.urls")),
    path("", include("Apps.Veterinaria.urls"))
]
