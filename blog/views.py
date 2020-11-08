from django.views import generic
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def home(request, username=None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by('-pub_date')

    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'blog\index.html', {'posts': posts,'first_name': first_name,'last_name': last_name})


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('pub_date')
    template_name = 'blog\index.html'


#class PostDetail(generic.DetailView):
 #   model = Post
  #  template_name = 'post_detail.html'

def post_detail(request):
    template_name = 'blog\post_detail.html'
    post = get_object_or_404(Post)
    comments = post.comments.order_by("pub_date")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {"post": post,
         "comments": comments,
         "new_comment": new_comment,
         "comment_form": comment_form, },)
