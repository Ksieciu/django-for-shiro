from django.urls import path
from .views import adding_pack_view, ShowPackDetails

urlpatterns = [
    path('add/', adding_pack_view),
    path('<int:pk>/', ShowPackDetails.as_view()),
]
