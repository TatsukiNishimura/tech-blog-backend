"""tech_blog_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from blog import views as blog_views
from blog.auth.views import TokenObtainPairWithExpiredDateView

router = DefaultRouter()
router.register(r'blogs', blog_views.BlogViewSet, basename="blogs")

main_url_patterns = [
    path('auth/token/', TokenObtainPairWithExpiredDateView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(main_url_patterns))
]
