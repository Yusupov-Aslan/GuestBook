from django.urls import path

from GuestBook.views import index_view, add_view, update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add'),
    path('update/<int:pk>/', update_view, name='update')

]
