from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    post_news = Post.objects.filter(post_type=Post.NEWS).order_by('created_at')
    template_name = 'news_list.html'
    return render(request, 'news_list.html', {'news': post_news})

def news_detail(request, pk):
    article = get_object_or_404(Post, id=pk)
    return render(request, 'news_detail.html', {'article': article})
