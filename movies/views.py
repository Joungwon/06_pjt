from django.shortcuts import render, redirect,get_object_or_404
# from .forms import MovieForm, CommentForm
# from .models import Movie, Comment
from django.views.decorators.http import require_POST,require_GET,require_http_methods
# from django.contrib.auth.decorators import login_required #로그인상태에서만 보이게

# Create your views here.
@require_GET
def index(request): #메인페이지
    # movies = Movie.objects.all()
    # context ={
    #     'movies':movies
    # }
    return render(request, 'movies/index.html')
