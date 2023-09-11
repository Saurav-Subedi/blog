from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.PostViews)


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('category/<slug>',views.category_blog,name='category'),
    path('api', include(router.urls)),
    path('contact/', views.contact_us, name='contact_us'),
    path('search-posts/', views.search_posts, name='search-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('author/<str:username>/', views.posts_by_author, name='posts-by-author'),

    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('about/', views.about, name='about'),
    path('polls/', views.polls, name='indexx'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('profile/', views.profile_view, name='profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

