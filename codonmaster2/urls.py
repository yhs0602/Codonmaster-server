"""codonmaster2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'rankings', RankingViewSet)
# router.register(r'announcements', AnnouncementViewSet)
# router.register(r'serverstatus', ServerStatusViewSet)

# router.register(r'gameplay', )
# router.register(r'enroll', )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
