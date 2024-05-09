from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    context = {'object_list': object_list}
    return render(request, 'diary/page_list.html', context=context)

def page_detail(request, page_id):
    context=dict()
    object = Page.objects.get(id=page_id)
    context["object"] = object

    return render(request, 'diary/page_detail.html', context=context)