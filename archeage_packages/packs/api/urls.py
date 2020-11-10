from django.urls import path
from .views import PackList, PackDetails, add_pack_view

urlpatterns = [
    path('', PackList.as_view()),
    path('add/', add_pack_view),
    path('<int:pk>/', PackDetails.as_view()),
]
