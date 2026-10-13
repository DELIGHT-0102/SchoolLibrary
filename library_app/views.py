
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Book
from .forms import BookForm, RegisterForm


def home(request):
    return render(request, 'library_app/home.html')


def book_list(request):
    books = Book.objects.all().order_by('-date_added')

    return render(request,'library_app/book_list.html',{'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    return render(request,'library_app/book_detail.html',{'book': book})


@login_required
def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES )

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(request,'library_app/add_book.html',{'form': form})


@login_required
def edit_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(
            request.POST,
            request.FILES,
            instance=book
        )

        if form.is_valid():
            form.save()
            return redirect(
                'book_detail',
                id=book.id
            )

    else:
        form = BookForm(instance=book)

    return render(
        request,
        'library_app/edit_book.html',
        {
            'form': form,
            'book': book
        }
    )


@login_required
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(
        request,
        'library_app/delete_book.html',
        {'book': book}
    )


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            login(request, user)

            return redirect('profile')

    else:
        form = RegisterForm()

    return render(
        request,
        'library_app/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('profile')

        return render(
            request,
            'library_app/login.html',
            {
                'error':
                'Incorrect username or password.'
            }
        )

    return render(
        request,
        'library_app/login.html'
    )


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):

    return render(
        request,
        'library_app/profile.html'
    )