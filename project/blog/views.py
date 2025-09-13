
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Comment,Article_category
from django.core.paginator import Paginator
 
 
def blog(request):
    article_cetegory = Article_category.objects.all()
    blog = Article.objects.filter(published = True)
    paginator = Paginator(blog, 12) 
    page_number = request.GET.get('page')    #first get is a dict sec is keys value
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog.html', {'blog' : blog, 'article_cetegory':article_cetegory, 'page_obj': page_obj})


def single_blog(request, blog_id):
    blog = get_object_or_404(Article, id = blog_id)
    comments = blog.comment.filter(parent__isnull = True).order_by('-created_at') and Comment.objects.filter(published = True)    # همه کامنت‌های این پست
    user = request.user
    if request.method == 'POST' and 'like' in request.POST:
        if not request.user.is_authenticated:
            return redirect('user_login')
        else:
            if request.user in blog.like.all():
                blog.like.remove(user)
            else:
                blog.like.add(user)
                blog.save()
        return redirect('single_blog', blog_id=blog_id)
    elif request.method == 'POST' and 'comment_submit' in request.POST:
        if not request.user.is_authenticated:
            return redirect('user_login')
        else:
            name = request.user.username
            text = request.POST.get('text')
            email = request.user.email
            parent = request.POST.get('parent')
    
            parent_obj = None
            if parent:
                try:
                    parent_obj = Comment.objects.get(id = parent)
                except Comment.DoesNotExist:
                    parent_obj = None
            Comment.objects.create(

                article=blog,

                name=name,

                email=email,

                text=text,

                parent=parent_obj

            )
        
            return redirect('single_blog', blog_id =blog_id)



    return render (request , 'single_blog.html',    context = {
        'blog': blog,
        'comments': comments})

  
def search_blog(request):
    query = request.GET.get('b')
    result =[]
    if not query :
        return redirect('blog')
    else:
        result = Article.objects.filter(title__icontains = query)
    return render(request, 'search_blog.html' , {'result' : result , 'query' : query})

