from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm



def homepage(request):
    titles = BlogPost.objects.order_by("date_added")
    context = {"titles": titles}
    return render(request, "blog_app/homepage.html", context)


@login_required
def new_post(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            return HttpResponseRedirect(reverse("blog_app:homepage"))
    context = {"form": form}
    return render(request, "blog_app/new_post.html", context)


@login_required
def edit_post(request, post_id):
    # title = BlogPost.objects.get(id=post_id)
    title = get_object_or_404(BlogPost, id=post_id)
    if title.owner != request.user:
        mess = {'ERROR': 'SORRY, This post is not your.'}
        return JsonResponse(mess)
    if request.method != "POST":
        form = BlogForm(instance=title) 
    else:
        form = BlogForm(instance=title, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog_app:homepage"))
        
    context = {"title": title, "form": form} #form要記得傳阿....忘了傳 卡在這好久幹
    return render(request, "blog_app/edit_post.html", context)
        
