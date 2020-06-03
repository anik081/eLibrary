from django.urls import path
from . import views

app_name = 'book'

urlpatterns =[
	#index
	path('',views.IndexView.as_view(), name ='index'),
	#book/1
	path('<int:pk>',views.BookDetails.as_view(), name ='book_details'),
	#book/add
	path('book/add',views.AddBook.as_view(), name ='book-add'),
		#book/delete
	path('book/<int:pk>/delete/',views.DeleteBook.as_view(), name ='book-delete'),
		#book/delete
	path('book/<int:pk>/update/',views.UpdateBook.as_view(), name ='book-update'),
	#books/register
	path('register/',views.Register.as_view(), name ='register'),
	path('login/',views.Login, name ='login'),


	
]