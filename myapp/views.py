from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from myapp.my_forms import BookForm


def show_books(request):
    books = Book.objects.all() # select * from books
    return render(request, 'show_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book {request.POST.get('title')} Added Successfully')
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request,'add_book.html',{'form':form})




    # Create your views here.
   # Book.objects.create(title='River And The Source',
        #                       year=2021,
    #                          category='Fiction',
    #                         cost=600,
    #                          isbn='335543226',
    #                          published=True )
    #      Book.objects.create(title='Man of the People',
    #                          year=2020,
    #     #                     category='Politics',
        #                       cost=450,
        #                       isbn='456789034',
       #                        published=True)
def delete_book(request, id):
    book = Book.objects.get(id=id) # select * from books where id= 34
    book.delete() # delete from books where id=34
    messages.error(request, f'{book.title} Deleted Successfully')
    return redirect('show_books')


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} Updated Successfully')
            return redirect('show_books')
    else:
         form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})