from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

router_version_1 = routers.DefaultRouter()

router_version_1.register('posts', PostViewSet, basename='posts')
router_version_1.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router_version_1.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_version_1.urls)),
]
