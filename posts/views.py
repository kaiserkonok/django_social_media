from django.shortcuts import render
from .models import Post


def home(request):
	return render(request, 'home.html', context={
		'posts': Post.objects.all()
	})
