from django.urls import path
from myapp import views

urlpatterns = [
    path('view/', views.BlogView, name= 'blog-view'),
    path('create/', views.BlogCreate, name = 'blog-create'),
    path('update/<int:id>/', views.BlogUpdate, name = 'blog-update'),
    path('delete/<int:id>/', views.BlogDelete, name = 'blog-delete'),
    path('comment/<int:id>',views.CommentAdd, name='comment-add'),
    path('view_comment/<int:id>', views.CommentView, name='comment-view'),
    path('delete_comment/<int:id>', views.CommentDelete, name='comment-delete'),
]
