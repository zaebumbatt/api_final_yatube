from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register('group', GroupViewSet)
v1_router.register('follow', FollowViewSet)
v1_router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
