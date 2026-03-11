# from django.urls import path 
# from . import views 

# urlpatterns = [
#     path(' ', views.basehtml, name='basehtml'),  
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.basehtml, name='basehtml'),
]
