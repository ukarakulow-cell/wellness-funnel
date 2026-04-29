from django.urls import path
from . import views

urlpatterns = [
    # Ana kapı artık landing_page'e çıkıyor
    path('', views.landing_page, name='landing_page'), 
    
    path('quiz/<int:step>/', views.quiz_view, name='quiz_step'),
    path('save-goal/', views.save_goal, name='save_goal'),
    path('bridge/', views.bridge_page, name='bridge_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('page/<str:page_name>/', views.blank_page, name='blank_page'),
]
path('save-goal/', views.save_goal, name='save_goal'),