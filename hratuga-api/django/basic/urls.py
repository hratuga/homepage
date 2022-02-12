from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'group', views.GroupViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'faq', views.FaqViewSet)
router.register(r'packing-list-tag', views.PackingListTagViewSet)
router.register(r'packing-list', views.PackingListViewSet)
router.register(r'packing-list-item', views.PackingListItemViewSet)
router.register(r'news-box', views.NewsBoxViewSet)

urlpatterns = [
    path('basic/', include(router.urls)),
]