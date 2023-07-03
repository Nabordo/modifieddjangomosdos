from django.urls import path
from . import views
from .views import signup
from .views import registration_success
from .views import verify_account
from .views import logout_view


urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', views.login_view, name='login'),
    path('', views.login_view, name='root'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', signup, name='signup'),
    path('registration/success/', registration_success, name='registration_success'),
    path('verify/<str:uidb64>/<str:token>/', verify_account, name='verify_account'),

]