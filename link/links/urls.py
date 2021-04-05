from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register,name='test'),
    path('new',views.sh,name='links'),
    path('<slug:slug>',views.fetch,name='fetch'),
]
