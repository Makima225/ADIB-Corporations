from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', ListHouseInfoView.as_view()),
    path('blog/<int:pk>/', DetailHouseInfoView.as_view()),
    path('contact/', CreateContactView.as_view()),

]