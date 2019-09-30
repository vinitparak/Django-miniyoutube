from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.core.files.storage import FileSystemStorage
from .forms import VibgForm
from .models import Vibg
from .filters import UserFilter
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(TemplateView):
	template_name = 'home.html'

def book_list(request):
    books = Vibg.objects.all()
    return render(request, 'vide_list.html', {
        'books': books
    })
@login_required    
def upload(request):
	if request.method == 'POST':
		form = VibgForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('book_list')
	else:
		form = VibgForm()
	return render(request, 'upload.html',{'form': form})
@login_required
def edit_post(request, pk):
	post = get_object_or_404(Vibg, pk=pk)
	if request.method == 'POST':
		form = VibgForm(request.POST, instance=post)
		try:
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('book_list'))
		except Exception as e:
			messages.warning(request, 'your video is not updated:{}'.format(e))
	else:
		form = VibgForm(instance=post)
	context = {
		'form':form
	}
	return render(request, 'upload.html', context)
			
@login_required	
def delete_book(request, pk):
	if request.method == 'POST':
		book = Vibg.objects.get(pk=pk)
		book.delete()
	return redirect('book_list')

def search(request):
	user_list = Vibg.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'user_list.html', {'filter': user_filter})