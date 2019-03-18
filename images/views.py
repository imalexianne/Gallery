from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image, Location, Category


def welcome(request):
    images = Image.objects.all()
    return render(request, 'welcome.html',{"images":images})

# def all_images(request):
#     images = Image.objects.all()
#     return render(request, 'welcome.html',{"images":images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        images = Image.objects.get(id = image_id)
        locations = Location.objects.all()
        image_category = Image.objects.filter(category__image_category = category_name)
    except DoesNotExist:
        raise Http404()
    return render(request,"images.html", {"image":image,'image_category':image_category, 'locations':locations})

def search_result(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_images = Image.search_img(search_term)
        message = f"{search_term}"

        return render(request, 'location.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'location.html',{"message":message})


    return render(request, 'location.html', { 'images':images, 'locations':locations})


