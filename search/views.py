from .models import Video
from django.shortcuts import render
from .filters import VideoFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

def search(request):

    video_list = Video.objects.all()
    video_filter = VideoFilter(request.GET, queryset=video_list)

    page = request.GET.get('page', 1)

    paginator = Paginator(video_filter.qs, 3)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    if len(video_filter.qs)==0:
        return render(request, 'search/no_videos.html', { 'videos': videos ,'filter':video_filter, })
    if len(video_list)==len(video_filter.qs):
        return render(request, 'search/unfiltered.html', { 'videos': videos ,'filter':video_filter, })
    return render(request, 'search/user_list.html', { 'videos': videos ,'filter':video_filter, })

def home(request):
    return render(request,'home.html')

def detail(request, url_title):
    try:
        video = Video.objects.get(url_title=url_title)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    return render(request, 'search/detail.html', {'video': video})

def blog(request):
    return render(request,'search/blog.html')
