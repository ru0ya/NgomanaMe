from django.urls import path

from jenga.views import (
        home,
        tutorial_list,
        tutorial_detail,
        tutorial_create,
        CommentUpdateView,
        CommentDeleteView
        )


app_name = 'jenga'

urlpatterns = [
        path('', home, name='home'),
        path(
            'tutorials/',
            tutorial_list,
            name='tutorial_list'
            ),
        path(
            'category/<slug:category_slug>/',
            tutorial_list,
            name='tutorial_list_by_category'
            ),
        path(
            'tutorial/<slug:slug>/',
            tutorial_detail,
            name='tutorial_detail'
            ),
        path(
            'tutorial/create/',
            tutorial_create,
            name='tutorial_create'
            ),
        path(
            'comment/<int:pk>/edit/',
            CommentUpdateView.as_view(),
            name='comment_update'
            ),
        path(
            'comment/<int:pk>/delete/',
            CommentDeleteView.as_view(),
            name='comment_delete'
            ),
        ]
