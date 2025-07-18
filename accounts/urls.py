from django.urls import path
from .views import CustomLoginView, signup, handle_profile, edit_profile
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('profile/', views.handle_profile, name='handle_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/setup/', views.profile_setup, name='profile_setup'),  # 👈 also needed
]





#from django.urls import path
#from .views import CustomLoginView
#from .views import signup
#from django.contrib.auth.views import LogoutView
#from . import views

#urlpatterns = [
   # path('signup/', signup, name='signup'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    #path('profile/', views.profile_view, name='profile'),
    #path('profile/edit/', views.edit_profile, name='edit_profile'), 
#]
