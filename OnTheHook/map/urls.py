from django.urls import path
from django.views.decorators.cache import cache_page
from map import views

app_name = "map"

urlpatterns = [
    path(
        "",
        cache_page(60 * 1)(views.MapView.as_view()),
        name="map",
    ),
]
