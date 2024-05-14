from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Page
from .forms import PageForm

# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)

#     page_number = request.GET.get('page') # 쿼리 스트링의 key 값으로 현재 page 받아오기

#     if page_number is None:
#         page_number = 1
    
#     page = paginator.page(page_number)
#     return render(request, 'diary/page_list.html', {'page': page})

class PageListView(ListView):
    model = Page
    template_name = 'diary/page_list.html'
    context_object_name = 'object_list'
    ordering = ['-dt_created']
    paginate_by = 8
    page_kwarg = 'page'

# def page_detail(request, page_id):
#     context=dict()
#     object = get_object_or_404(Page, id=page_id)
#     context["object"] = object

#     return render(request, 'diary/page_detail.html', context=context)

class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'object'

def info(request):
    return render(request, 'diary/info.html')

# def page_create(request):
#     if request.method == 'POST':
#         # new_page = Page(
#         #     title = request.POST['title'],
#         #     content = request.POST['content'],
#         #     feeling = request.POST['feeling'],
#         #     score = request.POST['score']
#         # )
#         # new_page.save()
#         page_form = PageForm(request.POST)
#         if page_form.is_valid():
#             new_page = page_form.save()
#             return redirect('page-detail', page_id=new_page.id)
    
#     else:
#         # GET
#         page_form = PageForm()

#     return render(request, 'diary/page_form.html', {'form': page_form})

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})

# def page_update(request, page_id):
#     object = get_object_or_404(Page, id=page_id)
#     if request.method == 'POST':
#         page_form = PageForm(request.POST, instance=object)
#         if page_form.is_valid():
#             page_form.save()
#             return redirect('page-detail', page_id=object.id)
        
#     else:
#         # GET
#         page_form = PageForm(instance=object)

#     return render(request, 'diary/page_form.html', {'form': page_form})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})

# def page_delete(request, page_id):
#     object = get_object_or_404(Page, id=page_id)
#     if request.method == 'POST':
#         object.delete()
#         return redirect('page-list')
#     else:
#         # GET
#         return render(request, 'diary/page_confirm_delete.html', {'object': object})
    
class PageDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm_delete.html'
    context_object_name = 'object'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-list')