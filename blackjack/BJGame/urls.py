from django.urls import path
from . import views

urlpatterns = [
    path('game/',views.game,name='game'),
    path('howto/',views.howto,name='howto'),
    path('inquiry/',views.InquiryView.as_view(),name='inquiry'),
]