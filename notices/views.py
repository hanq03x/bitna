from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from users import models as user_models
from notices import models


class PostListView(ListView):
    """ Post ListView Definition """
    
    model = models.Post
    paginate_by = 10
    ordering = "created"
    context_object_name = "postlist"


def post_detail(request, pk):
    post = models.Post.objects.get(pk=pk)
    return render(request, "notices/post_detail.html", {'pk':post.pk, 'post':post})
    

def go_upload(request):
    admin = user_models.User.objects.get(username="admin")
    if request.user == admin:
        return render(request, "notices/post_upload.html")
    return redirect(reverse("core:home"))
    
    
def upload_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        contents = request.POST.get("contents")
        photo = request.POST.get("photo", None)
        post = models.Post.objects.create(
            title=title,
            contents=contents,
            photo=photo
        )
        post.save()
        return redirect(reverse('notices:list'))
    
