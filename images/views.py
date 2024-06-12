import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from images.forms import UploadForm
from images.models import Image
from images.tables import ImageTable


logger = logging.getLogger(__name__)


def index_view(request):
    images = Image.objects.all()
    image_table = ImageTable(images)
    upload_form = UploadForm()

    return render(request, 'images/index.html', {
        'images': images,
        'image_table': image_table,
        'upload_form': upload_form,
    })


@require_http_methods(["POST"])
def upload_view(request):
    upload_form = UploadForm(data=request.POST, files=request.FILES)

    if upload_form.is_valid():
        upload_form.save(commit=True)
    else:
        logger.warning("Something went wrong with uploading the file.")
        logger.warning(request.POST)
        logger.warning(request.FILES)

    return redirect('images-index')


def testing(request):
    return render(request, "test.html", {})

def home(request):
    return render(request, "home.html", {})


from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Prepare the dictionary with all the fields
    blog_details = {
        'title': blog.title,
        'category': blog.category,
        'priority': blog.priority,
        'date': blog.date,
        'keywords': blog.keywords,
        'heading': blog.heading,
        'sub_heading': blog.sub_heading,
        'sub_heading_2': blog.sub_heading_2,
        'contexts': [getattr(blog, f'context_{i}') for i in range(1, 6)],
        'images': [getattr(blog, f'image_{i}') for i in range(1, 6)]
    }

    return render(request, 'blog_detail.html', {'blog_details': blog_details})
