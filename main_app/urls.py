from django.urls import path
from .views import Home, BirdList, BirdDetail, FeedingDetail, FeedingListCreate, SpecieListCreate, SpecieDetail, AddSpecieToBird, RemoveSpecieFromBird, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("birds/", BirdList.as_view(), name="bird-list"),
    path("birds/<int:id>/", BirdDetail.as_view(), name="bird-detail"),
    path("birds/<int:id>/feedings", FeedingListCreate.as_view(), name="feeding-list-create"),
    path("birds/<int:id>/feedings/<int:bird_id>/", FeedingDetail.as_view(), name="bird-detail"),
    path('species/', SpecieListCreate.as_view(), name='species-list-create'),
    path('birds/<int:bird_id>/', SpecieDetail.as_view(), name="specie-detail"),
    path('birds/<int:bird_id>/add_specie/<int:specie_id>/', AddSpecieToBird.as_view(), name='add-toy-to-cat'),
    path('birds/<int:bird_id>/remove_specie/<int:spece_id>/', RemoveSpecieFromBird.as_view(), name="remove-speie-from-bird"),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),

]