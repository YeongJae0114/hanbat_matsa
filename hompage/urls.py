
from django.contrib import admin
from django.urls import path, include
from hanbat import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('joinus/', views.joinus, name = 'joinus'),
    path('accounts/',include('accounts.urls')),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('joinus/submit/', views.submit, name = 'submit'),
    path('detail/<int:pyth_id>', views.detail, name = 'detail'),
    path('delete/<int:pyth_id>', views.delete, name = 'delete'),
]
