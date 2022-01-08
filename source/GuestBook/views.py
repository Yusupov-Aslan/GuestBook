from django.shortcuts import render, redirect
from GuestBook.models import Guest, STATUS_CHOICES

# Create your views here.


def index_view(request):
    guest = Guest.objects.order_by("-created_at").filter(status="active")
    context = {'guests': guest}
    return render(request, 'index.html', context)
