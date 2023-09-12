from typing import Self
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreateUserForm, PostCreateForm,ProfileUpdateForm,UserUpdateForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from django.shortcuts import render
from .models import Category, Post
from rest_framework import  viewsets
from .post_serializer import PostSerializer
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy


def posts_by_author(request, username):
    author = get_object_or_404(User, username=username)
    
    posts = Post.objects.filter(author=author)
    
    context = {
        'author': author,
        'posts': posts,
    }
    
    return render(request, 'author.html', context)


def search_posts(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Post.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'results': results})

def about(request):
    return render(request, 'about.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_inquiry = form.save(commit=False)
            contact_inquiry.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('contact_us')  
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

class PostViews(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def category_blog(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    data = {
        'catData': category,
        'postData': posts
    }

    return render(request, 'category.html', data)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'base/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if category_id := self.request.POST.get('category'):
            category = get_object_or_404(Category, id=category_id)
            form.instance.category = category
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        if category_id := self.request.POST.get('category'):
            category = get_object_or_404(Category, id=category_id)
            form.instance.category = category

        response = super().form_valid(form)

        return redirect(reverse('index'))
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['name','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def get_success_url(self):
        return reverse_lazy('index')

def can_delete_post(user, post):
    return user.is_staff or user == post.author

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    @user_passes_test(lambda user: can_delete_post(user, Self.get_object()))
    def test_func(self):
        return True


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(user=user)
            messages.success(request, f'Account was created for {username}')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')

        else:
            messages.info(request,'username or password incorrect.')
    context={}
    return render(request, 'login.html',context)


def userlogout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def profile_view(request):
    try:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    except Profile.DoesNotExist:
        p_form = ProfileUpdateForm()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('index')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)



def polls(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/indexx.html', context)


def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('results', args=(question.id,)))