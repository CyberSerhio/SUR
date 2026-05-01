from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("/", include("apps.default.urls")),
    path("/game", include("apps.game.urls")),
]
