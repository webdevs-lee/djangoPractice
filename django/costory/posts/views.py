from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return redirect('post-list')

# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     current_page_number = request.GET.get('page')

#     if current_page_number is None:
#         current_page_number = 1

#     page = paginator.page(current_page_number)
#     return render(request, 'posts/post_list.html', {'page': page})

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {'post': post}

#     return render(request, 'posts/post_detail.html', context=context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
    
#     def post(self, request):  
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#         else:
#             return render(request, 'posts/post_form.html', {'form': post_form})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:
#         #GET
#         post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form': post_form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         # GET
#         return render(request, 'posts/post_confirm_delete.html', {'post': post})
    

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-list')