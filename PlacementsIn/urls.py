"""PlacementsIn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from design.views import home_view
from profiles.views import create,login,tips,feedback,google,Microsoft,tcs,cognizant,amazon,Accenture,gfilterone,gfiltertwo,gfilterthree,gfilterfour,LPA_filterone,LPA_filtertwo,LPA_filterthree,LPA_filterfour,LPA_filterfive,exams,product,service

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create',create),
    path('',home_view),
    path('google',google),
    path('microsoft',Microsoft),
    path('tcs',tcs),
    path('cognizant',cognizant),
    path('amazon',amazon),
    path('accenture',Accenture),
    path('filterone/<slug:orgname>',gfilterone),
    path('filtertwo/<slug:orgname>',gfiltertwo),
    path('filterthree/<slug:orgname>',gfilterthree),
    path('filterfour/<slug:orgname>',gfilterfour),
    path('lpafilterone/<slug:orgname>',LPA_filterone),
    path('lpafiltertwo/<slug:orgname>',LPA_filtertwo),
    path('lpafilterthree/<slug:orgname>', LPA_filterthree),
    path('lpafilterfour/<slug:orgname>', LPA_filterfour),
    path('lpafilterfive/<slug:orgname>', LPA_filterfive),
    path('exams',exams),
    path('product',product),
    path('service',service),
    path('feedback',feedback),
    path('login',login),
    path('tips',tips),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
