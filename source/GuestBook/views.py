from django.shortcuts import render, redirect
from GuestBook.forms import GuestForm
from GuestBook.models import Guest, STATUS_CHOICES

# Create your views here.


def index_view(request):
    guest = Guest.objects.order_by("-created_at").filter(status="active")
    context = {'guests': guest}
    return render(request, 'index.html', context)


def add_view(request, **kwargs):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'guest_create.html', {"form": form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('author_name')
            author_mail = form.cleaned_data.get('author_mail')
            text_notes = form.cleaned_data.get('text_notes')
            guest = Guest.objects.create(author_name=author_name, author_mail=author_mail, text_notes=text_notes)
            return redirect("index")
        else:
            return render(request, 'guest_create.html', {"form": form})

