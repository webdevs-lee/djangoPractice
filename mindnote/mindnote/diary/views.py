from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PageForm

# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

def page_list(request):
    object_list = Page.objects.all()
    context = {'object_list': object_list}
    return render(request, 'diary/page_list.html', context=context)

def page_detail(request, page_id):
    context=dict()
    object = get_object_or_404(Page, id=page_id)
    context["object"] = object

    return render(request, 'diary/page_detail.html', context=context)

def info(request):
    return render(request, 'diary/info.html')

def page_create(request):
    if request.method == 'POST':
        # new_page = Page(
        #     title = request.POST['title'],
        #     content = request.POST['content'],
        #     feeling = request.POST['feeling'],
        #     score = request.POST['score']
        # )
        # new_page.save()
        page_form = PageForm(request.POST)
        if page_form.is_valid():
            new_page = page_form.save()
            return redirect('page-detail', page_id=new_page.id)
    
    else:
        # GET
        page_form = PageForm()

    return render(request, 'diary/page_form.html', {'form': page_form})

def page_update(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        page_form = PageForm(request.POST, instance=object)
        if page_form.is_valid():
            page_form.save()
            return redirect('page-detail', page_id=object.id)
        
    else:
        # GET
        page_form = PageForm(instance=object)

    return render(request, 'diary/page_form.html', {'form': page_form})

def page_delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        # GET
        return render(request, 'diary/page_confirm_delete.html', {'object': object})
    
    