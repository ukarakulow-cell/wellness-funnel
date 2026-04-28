from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:step>/', views.quiz_view, name='quiz_step'),
    path('bridge/', views.bridge_page, name='bridge_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('page/<str:page_name>/', views.blank_page, name='blank_page'), # <-- EKLENEN YENİ YOL
]