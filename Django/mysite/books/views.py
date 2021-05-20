from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from books.forms import ContactForm

# Create your views here.
def search_form(request):
    return render(request, 'search.html')

def search(request):
    errors = []
    if 'book_name' in request.GET:
        book_name = request.GET['book_name']
        if not book_name:  # 用于检查用户提交的值是否为空
            errors.append('Enter a search term.')
        elif len(book_name) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__contains=book_name)
            return render(request, 'search_results.html',
                          {'books': books, 'query': book_name})
    return render(request, 'search.html', {'errors': errors})

# def contact(request):
#     errors = []
#     if request.method == "POST":
#         if not request.POST.get('subject', ''):
#             errors.append("Please enter a subject.")
#         if not request.POST.get('message', ''):
#             errors.append("Please enter a message.")
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append("Please enter a valid e-mail address.")
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['jasminia@163.com',],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request, 'contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', '')
#         })

# 使用forms框架重写contact
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['jasminia@163.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})