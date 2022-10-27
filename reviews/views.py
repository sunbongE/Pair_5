from django.shortcuts import redirect, render

from reviews.models import Review
from reviews.forms import ReviewForm, CommentForm
# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request,'reviews/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    
    context = {
        'form':form,
    }
    return render(request, 'reviews/create.html', context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review,
    }
    return render(request, 'reviews/detail.html', context)

def delete(request,pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')

def update(request,pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:index', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form':form,
        'review':review
    }
    return render(request, 'reviews/create.html', context)