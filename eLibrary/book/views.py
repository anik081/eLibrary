from django.shortcuts import render,redirect
from  django.views import generic
from .models import Book
from django.contrib import messages
from django.urls import reverse_lazy
from  django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.db.models.query import Q
from django.contrib.auth.models import User,auth
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'book/index.html'
	context_object_name = 'all_books'

	def get_queryset(self):
		request = self.request
		query = request.GET.get('q')
		if query is not  None:
			return Book.objects.filter(Q(book_author__icontains =query)  | Q(book_title__icontains =query) | Q(book_publisher__icontains =query))
		return Book.objects.all()

class BookDetails(generic.DetailView):
	book = Book
	template_name='book/book_details.html'
	def get_queryset(self):
		return Book.objects.all()


class AddBook(CreateView):
	model = Book
	fields = ['book_title', 'book_author' , 'book_publisher' , 'book_image']
	success_url =reverse_lazy('book:index')

class DeleteBook(DeleteView):
	model = Book
	success_url =reverse_lazy('book:index')

class UpdateBook(UpdateView):
	model = Book
	fields = ['book_title', 'book_author' , 'book_publisher' , 'book_image' ]
	success_url =reverse_lazy('book:index')

class Register(View):
	form_class = UserForm
	template_name = 'book/register.html'

	#blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process from data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit= False)

			#cleaned/normalizeed data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#login
			user = authenticate(username =username, password =password)

			if user is not None:
				if user.is_active:

					login(request,user)
					return redirect('book:index')
		return render(request, self.template_name, {'form': form})



def Login(request):
	template_name = 'book/login.html'
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password= password)

		if user is not None:
			auth.login(request,user)
			return redirect('book:index')
		else:
			messages.info(request,'invalid')
	else:
		return render(request,template_name)




