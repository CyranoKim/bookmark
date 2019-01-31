from django.urls import path

from .views import BookmarkList
from .views import BookmarkUpdate
from .views import BookmarkDetail
from .views import BookmarkCreate
from .views import BookmarkDelete

urlpatterns = [
    path('', BookmarkList.as_view(), name='bookmark_list'),  # url, view, 1의 별명(생략가능)
    path('update/<int:pk>', BookmarkUpdate.as_view(), name='bookmark_update'),
    path('detail/<int:pk>', BookmarkDetail.as_view(), name='bookmark_detail'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name='bookmark_delete'),
    path('create/', BookmarkCreate.as_view(), name='bookmark_create'),
]