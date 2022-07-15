from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
# Create your views here.
from .models import Post,Comment
from .forms import CommentForm,PostForm


def search(request):

    if request.method=="POST":

        searched = request.POST['searched']

        results = Post.objects.filter(title__icontains = searched)
        
        return render (request,'blog/post/search.html',{'searched':searched,'results':results})

def post_list(request):

    posts = Post.published.all()


    

    return render (request,'blog/post/list.html',{'posts':posts})


    

def post_detail(request,year, month , day , post):

    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)

            new_comment.post = post

            new_comment.save()

    else:
        comment_form = CommentForm()

    return render (request,'blog/post/detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})