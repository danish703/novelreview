from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from novel.models import Novel
from comment.forms import CommentForm
from comment.models import Comment
from novel.models import Category
# from reviewclassification.nlp import ReadDataSet



def home(request):
   # rd = ReadDataSet('data.csv')
   # rd.displayDataSet()
    query = request.GET.get('title')
    allnovels = None
    if query:
        allnovels=Novel.objects.filter(name__icontains=query)
    else:
        allnovels = Novel.objects.all()

    allcategorys = Category.objects.all()
    context = {
        'novels':allnovels,
        'category':allcategorys,

    }
    return render(request,'index.html',context);


def about(request):
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

    return render(request,'about.html');

def feedback(request):
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
        form = FeedbackForm()
        context = {
            'form': form
        }
        return render(request, 'feedback.html', context);
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.add_message(request, messages.SUCCESS, "Feedback Sent")
            return redirect('feedback')
        else:
            return render(request, 'feedback.html', {'form': form})



def signup(request):
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


    if request.method=='GET':
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request,'signup.html',context);
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if request.POST["password1"]==request.POST["password2"]:
                data = form.save(commit=False)
                password = request.POST['password1']
                data.set_password(password)
                data.save()
                messages.add_message(request,messages.SUCCESS,"User Created Successfully")
                return redirect('signin')
            else:
                messages.add_message(request, messages.ERROR, "Password and Password Confirmation does not match")
                return render(request, 'signup.html', {'form': form})
        else:
            return render(request,'signup.html',{'form':form})

@login_required(login_url='signin')
def dashboard(request):

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

    return render(request, 'dashboard.html')

    # if request.user.is_authenticated:
      #  return render(request,'dashboard.html')
    # else:
      #  return redirect('signin')

def instruction(request):
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
    return render(request, 'instruction.html')


def signin(request):
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
        return render(request,'login.html');
    else:
        inputusername = request.POST['username']
        inputpassword = request.POST['pass']
        user=authenticate(username=inputusername,password=inputpassword)
        if user is not None:
            login(request,user=user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Username and Password does not match")
            return redirect('signin')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return render(request, 'logout.html');

@login_required(login_url='signin')
def changePassword(request):
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

    if request.method=='GET':
        return render(request,'changepassword.html')
    else:
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        if p1==p2:
            current_loguser = User.objects.get(id=request.user.id)
            current_loguser.set_password(p1)
            current_loguser.save()
            messages.add_message(request,messages.SUCCESS,"Password has been changed successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Password and Retype Password does not match")
            return render(request,'changepassword.html')




