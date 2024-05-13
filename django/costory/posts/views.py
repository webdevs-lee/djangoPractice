from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return redirect('post-list')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}

    return render(request, 'posts/post_detail.html', context=context)

def post_create(request):
    if request.method == 'POST':
        # title = request.POST['title']
        # content = request.POST['content']
        # new_post = Post(
        #     title = title,
        #     content = content
        # )
        # new_post.save()
        post_form = PostForm(request.POST) # Binding
        if post_form.is_valid(): # 유효성 검사를 통과
            new_post = post_form.save()
            return redirect('post-detail', post_id=new_post.id)
        
    else:
        # GET
        post_form = PostForm()

    return render(request, 'posts/post_form.html', {'form': post_form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        #GET
        post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        # GET
        return render(request, 'posts/post_confirm_delete.html', {'post': post})
    
    