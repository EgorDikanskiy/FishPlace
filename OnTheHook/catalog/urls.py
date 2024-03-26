from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework import routers

from catalog import api, views

app_name = "catalog"

router = routers.DefaultRouter()
router.register("spots", api.CatalogViewSet)

router_main_image = routers.DefaultRouter()
router_main_image.register("main_images", api.MainImageViewSet)

router_regions = routers.DefaultRouter()
router_regions.register("regions", api.RegionViewSet)

urlpatterns = [
    path(
        "",
        cache_page(60 * 1)(views.SpotListView.as_view()),
        name="spot_list",
    ),
    path(
        "<int:pk>/",
        cache_page(120 * 1)(views.SpotDetailView.as_view()),
        name="spot_detail",
    ),
    path(
        "create/",
        views.CreateFishingPlaceView.as_view(),
        name="create_spot",
    ),
    path(
        "created/",
        cache_page(60 * 1)(views.CreatedPlace.as_view()),
        name="created_spot",
    ),
    path(
        "created/<int:pk>/edit/",
        views.EditPalce.as_view(),
        name="edit_palce",
    ),
    path(
        "region/<int:region>/",
        cache_page(60 * 1)(views.RegionView.as_view()),
        name="region",
    ),
    path(
        "api/",
        include(router.urls),
    ),
    path(
        "api/",
        include(router_main_image.urls),
    ),
    path(
        "api/",
        include(router_regions.urls),
    ),
    path(
        "api-auth/",
        include(
            "rest_framework.urls",
            namespace="rest_framework",
        ),
    ),
]
