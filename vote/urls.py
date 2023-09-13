from django.urls import path
from .views import  index, detail,ResultView, vote
app_name='vote'
urlpatterns=[
    path('', index, name='home'),
    path('detail/<int:id>/',detail,name='detail'),
    path('<int:pk>/result/',ResultView.as_view(), name='result'),
    path('<int:id>/vote/', vote, name='vote'),
]