from django.urls import path

from GuestBook.views import index_view

urlpatterns = [
    path('', index_view, name='index')

]
