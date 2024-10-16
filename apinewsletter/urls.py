from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SubscribeViewset, InterestViewset, ArticleViewset,
                    )

router = DefaultRouter()
router.register(r'subscribers', SubscribeViewset)
router.register(r'interests', InterestViewset)
router.register(r'articles', ArticleViewset)
# router.register(r'preferences', SubscriberPreferenceViewSet)
# router.register(r'emaillogs', EmailLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]