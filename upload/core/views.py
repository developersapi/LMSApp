from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.core.mail import send_mail

from .forms import BookForm
from .models import Book, Video


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        send_mail(
            'Estudante',
            'Você tem Arquivos Salvos!',
            'lucassilva.fatec@gmail.com',
            ['antoniojames3452@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'Estudante',
                'Você tem Livros Novos!',
                'lucassilva.fatec@gmail.com',
                ['antoniojames3452@gmail.com'],
                fail_silently=False,
            )
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'


class PillsListView(ListView):
    model = Video
    template_name = 'pills.html'
    context_object_name = 'video'


def video(request):
    videos = Video.objects.all()
    return render(request, 'pills.html', context={'videos': videos})
