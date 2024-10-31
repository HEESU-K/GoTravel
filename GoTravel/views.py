import requests
import openai
import re
import os
import json
import logging

from . import funcs
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


#from config import OPENAI_API_KEY

from .models import jeju, gyeongju, yeosu, jeonju 



openai_api_key = 'sk-proj-lmSIlMQn5cH8Sy8NM8dxT3BlbkFJxH6wGJB5EKd692ZPQ3ng'

client = OpenAI(
    api_key = "sk-proj-lmSIlMQn5cH8Sy8NM8dxT3BlbkFJxH6wGJB5EKd692ZPQ3ng"
)

logger = logging.getLogger(__name__)

destinations = [
# 리스트 데이터 입력
    
]

######  DB에 여행지 데이터 넣기용  #####
def inputData(request):
    funcs.input_data_toDB(destinations)
    return render(request, 'success.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    succes_url = reverse_lazy("gotravel/login")
    template_name = "registration/signup.html"


def selectcity(request): # 도시 선택 페이지
    destinations = []
    jeju_data = jeju.objects.first()
    gyeongju_data = gyeongju.objects.first()
    yeosu_data = yeosu.objects.first()
    jeonju_data = jeonju.objects.first()

    if jeju_data:
        destinations.append({
            'region': 'jeju',
            'kor_name': jeju_data.kor_name,
            'thumbnail': jeju_data.thumbnail,
        })

    if gyeongju_data:
        destinations.append({
            'region': 'gyeongju',
            'kor_name': gyeongju_data.kor_name,
            'thumbnail': gyeongju_data.thumbnail,
        })

    if yeosu_data:
        destinations.append({
            'region': 'yeosu',
            'kor_name': yeosu_data.kor_name,
            'thumbnail': yeosu_data.thumbnail,
        })

    if jeonju_data:
        destinations.append({
            'region': 'jeonju',
            'kor_name': jeonju_data.kor_name,
            'thumbnail': jeonju_data.thumbnail,
        })
    return render(request, 'selectcity.html', {'destinations': destinations})


def planning(request, region): # 세부 플래닝 페이지
    # region에 따라 다르게 처리
    if region == 'jeju':
        data = jeju.objects.all()
        context = {'destination': '제주도',
                    'data': data
        }
    elif region == 'gyeongju':
        data = gyeongju.objects.all()
        context = {'destinatoin': '경주',
                    'data': data,
        }
    elif region == 'yeosu':
        data = yeosu.objects.all()
        context = {'destinatoin': '여수',
                    'data': data
        }
    elif region == 'jeonju':
        data = jeonju.objects.all()
        context = {'destinatoin': '전주',
                    'data': data
        }
    else:
        context = {'destination': '알 수 없는 지역'}

    return render(request, 'planning.html', context)




def optimize_schedule(request):
    if request.method == 'POST':
        dates = request.POST.getlist('date')
        places = request.POST.getlist('place')
        times = request.POST.getlist('time')

        if not dates or not places:
            return JsonResponse({"error": "데이터가 부족합니다."}, status=400)

        schedule_data = []
        for data, place, time in zip(dates,places, time):
            schedule_date.append({
                'data': date,
                'places': place.split(','),
                'time': time
            })
        
        print(f"추출된 데이터 : {schedule_data}")

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # GPT-3 엔진 사용
            prompt=f"날짜, 시간, 장소를 고려해서 최적의 여행 일정을 생성해줘. 일정: {schedule_data}",
            max_tokens=1500
        )

        optimized_schedule = response.choices[0].text.strip()


        return render(request, 'schedule.html', {'optimized_schedule': optimized_schedule})

    return JsonResponse({"error": "Invaild request method"}, status=400)



# 최적화된 일정을 보여주는 페이지
def schedule(request):
    # 최적화된 일정 데이터를 받아서 페이지에 표시
    return render(request, 'schedule.html')



# openAI api를 활용해서 추천 여행지 리스트 추출
def get_ai_recommendations(request):
    destination = request.GET.get('destination', 'Jeju Island')

    # OpenAI 또는 다른 AI API에 요청을 보냅니다
    ai_api_key = 'sk-proj-lmSIlMQn5cH8Sy8NM8dxT3BlbkFJxH6wGJB5EKd692ZPQ3ng'
    headers = {
        'Authorization': f'Bearer {ai_api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "gpt-3.5-turbo-instruct",  # 모델 설정
        "prompt": f"{destination}의 가장 인기있는 여행지와 맛집을 알려줘.",
        "max_tokens": 1000
    }

    response = requests.post(
        'https://api.openai.com/v1/completions',
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        # 응답을 JSON 형태로 전송
        ai_response = response.json().get('choices')[0]['text']
        recommendations = ai_response.split("\n")  # 추천지를 목록화
        json_result = funcs.convert_to_json(recommendations) #name, description 파싱
        return JsonResponse({"places": json_result})
    else:
        return JsonResponse({"error": "AI API 요청 실패"}, status=500)


def test(request):
    return render(request, 'test.html')