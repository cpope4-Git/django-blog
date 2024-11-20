from django.http.response import HttpResponse
from django.shortcuts import render
from blogging.models import Post
from django.http import Http404


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Keyword args:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects
    posts = published.order_by('-published_date')
    #print(f'number of posts {len(posts)}')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)