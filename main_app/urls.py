from django.urls import path
from .views import Home, BirdList, BirdDetail, FeedingDetail, FeedingListCreate

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("birds/", BirdList.as_view(), name="bird-list"),
    path("birds/<int:id>/", BirdDetail.as_view(), name="bird-detail"),
    path("birds/<int:id>/feedings", FeedingListCreate.as_view(), name="feeding-list-create"),
    path("birds/<int:id>/feedings/<int:bird_id>/", FeedingDetail.as_view(), name="bird-detail"),

]