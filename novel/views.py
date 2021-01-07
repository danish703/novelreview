from django.shortcuts import render,redirect
from .models import Novel,Category
from comment.forms import Comment,CommentForm
from django.contrib import messages
from reviewclassification.nlp import commentPredict

# Create your views here.
def details(request,id):
    query = request.GET.get('title')
    allnovels = None
    if query:
        allnovels = Novel.objects.filter(name__icontains=query)
        allcategorys = Category.objects.all()
        context = {
            'novels': allnovels,
            'category': allcategorys,
        }
        return render(request, 'index.html', context);

    if request.method == 'GET':
        a = Novel.objects.get(pk=id)
        comments = Comment.objects.filter(novel=a)
        commentform = CommentForm()
        context = {
            'novel':a,
            'commentform': commentform,
            'comments':comments
        }
        return render(request,'details.html',context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)
                data.user = request.user
                data.novel_id = id
                x = commentPredict(request.POST['comment_message'])
                if x[0]==1:
                    data.status = 'positive'
                else:
                    data.status = 'negative'
                data.percentage = x[1]*100;
                data.save()
                messages.add_message(request,messages.SUCCESS,"Successfully Commented")
                return redirect('details',id)
            except:
                messages.add_message(request, messages.ERROR, "You have already commented on this novel")
                return redirect('details', id)
        else:
            messages.add_message(request,messages.ERROR,"Ensure this value is between 1 to 5")
            return render(request, 'details.html',{'commentform':form})


def genreNovelList(request,cid):
    genre = Category.objects.get(pk=cid)
    query = request.GET.get('title')
    allnovels = None
    if query:
        allnovels = Novel.objects.filter(name__icontains=query,category=genre)
        context = {
            'title': genre.title,
            'novels': allnovels,
        }
        return render(request, 'genrenovels.html', context);

    genre = Category.objects.get(pk=cid)
    context = {
        'title': genre.title,
        'novels': Novel.objects.filter(category=genre)
    }
    return render(request,'genrenovels.html',context)
