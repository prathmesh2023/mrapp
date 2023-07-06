from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path("",views.dashboard, name="dashboard"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),


    path('mrlist', views.mrlist, name="mrlist"),
    path('create_mr', views.create_mr, name="create_mr"),
    path('update_mr/<int:id>', views.update_mr, name="update_mr"),
    path('search_mr', views.search_mr, name="search_mr"),


    path('dr_list', views.dr_list, name="dr_list"),
    path('create_dr', views.create_dr, name="create_dr"),
    path('update_dr/<int:id>', views.update_dr, name="update_dr"),
    path('search_dr', views.search_dr, name="search_dr"),

    path('add_slide', views.add_slide, name="add_slide"),
    path('all_slides', views.all_slides, name="all_slides"),
    path('search_slides', views.search_slides, name="search_slides"),
    path('delete_slide/<int:id>', views.delete_slide, name="delete_slide"),


    path('report',views.report, name="report"),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 