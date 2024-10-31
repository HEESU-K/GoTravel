from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView
from django.views import View

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('inputdata', views.inputData),
    
    path('selectcity', views.selectcity),


    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    
    path('planning/<str:region>', views.planning, name="planning"), #동적 URL 패턴
   # path('get-ai-recommendations', views.get_ai_recommendations, name='get_ai_recommendations'), #openAI api로 여행지 리스트 추출
    
    path('optimize_schedule/', views.optimize_schedule, name='optimize_schedule'), # 완성된 테이블의 테이를 이용해서 openAI api로 완성된 추천 여행 루트를 받음
    path('schedule/',views.schedule, name='schedule'), # 받은 여행 루트를 표시하는 페이지
    path('test/', views.test),
]