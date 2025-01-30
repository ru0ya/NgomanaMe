from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login

from jenga.models import Tutorial, Category, Step, Material, Comment
from jenga.forms import TutorialForm, StepForm, MaterialForm, SignUpForm


def home(request):
    categories = Category.objects.prefetch_related(
            Prefetch(
                'tutorials',
                queryset=Tutorial.objects.all()[:3]
                )
            )
    latest_tutorials = Tutorial.objects.select_related(
            'author', 'category'
            ).order_by('-created_at')[:6]

    return render(
            request, 'jenga/home.html',
            {
                'categories': categories,
                'latest_tutorials': latest_tutorials
                })


def tutorial_list(request, category_slug=None):
    category = None
    tutorials = Tutorial.objects.select_related('author', 'category')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tutorials = tutorials.filter(category=category)

    paginator = Paginator(tutorials, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jenga/tutorial_list.html', {
        'category': category,
        'page_obj': page_obj
        })


def tutorial_detail(request, slug):
    tutorial = get_object_or_404(
            Tutorial.objects.select_related('author', 'category')\
                    .prefetch_related(
                        'steps',
                        'materials',
                        'comments__author'
                        ), slug=slug
                    )
    
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                    tutorial=tutorial,
                    author=request.user,
                    content=content
                    )
            return redirect(tutorial.get_absolute_url())

    return render(request, 'jenga/tutorial_detail.html', {
        'tutorial': tutorial,
        })


@login_required
def tutorial_create(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.author = request.user
            tutorial.save()
            return redirect('tutorial_detail', slug=tutorial.slug)
    else:
        form = TutorialForm()

    return render(request, 'jenga/tutorial_form.html', {'form': form})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'jenga/comment_form.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
                'jenga: tutorial_detail', 
                kwargs={'slug': self.object.tutorial.slug}
                )


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'jenga/comment_confirm_delete.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
                'jenga: tutorial_detail',
                kwargs={'slug': self.object.tutorial.slug}
                )


def custom_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('jenga:home')
    else:
        form = SignUpForm()
    return render(request, 'jenga/signup.html', {'form': form})
