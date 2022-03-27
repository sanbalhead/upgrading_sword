from fileinput import filename
from xmlrpc.client import ResponseError
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django import template
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import status
from app.models import *
from .serializers import *
from app.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from upgrading_sword.settings import STATIC_ROOT
import mimetypes



def main(request):

    context = {}

    html_template = loader.get_template('main.html')

    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def game(request):

    context = {}

    html_template = loader.get_template('game.html')

    return HttpResponse(html_template.render(context, request))



def item(request):

    context = {}

    html_template = loader.get_template('item.html')

    return HttpResponse(html_template.render(context, request))



def shop(request):

    context = {}

    html_template = loader.get_template('shop.html')

    return HttpResponse(html_template.render(context, request))



def sign_in(request):

    context = {}

    html_template = loader.get_template('sign_in.html')

    return HttpResponse(html_template.render(context, request))


def ranking(request):

    context = {}

    html_template = loader.get_template('ranking.html')

    return HttpResponse(html_template.render(context, request))



def sign(request):

    context = {}

    
    form = Signform(request.POST or None)


    if request.method == "POST":
        print("회원가입 요청됨")
        
        

        if form.is_valid():
            print("id : %s" % form.cleaned_data.get("id"))


            userInputId = form.cleaned_data.get("id")
            userInputNickname = form.cleaned_data.get("nickname")
            pw = form.cleaned_data.get("password")
            pwcheck = form.cleaned_data.get("password_check")
            money = 100000

            if pw != pwcheck:
                return Response("Not Valid Data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            # 아이디 중복 체크
            userData = None
            try:
                userData = User.objects.get(id=userInputId)
            except ObjectDoesNotExist:
                pass

            if userData != None:
                print("아이디 중복")
                return Response("Duplicated ID", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

            # # 닉네임 중복 체크
            try:
                userData = User.objects.get(nickname=userInputNickname)
            except ObjectDoesNotExist:
                pass

            if userData != None:
                print("닉네임 중복")
                return Response("Duplicated NICKNAME", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            

            # DB에 저장
            newUser = User()
            newUser.id = userInputId
            newUser.pw = pw
            newUser.nickname = form.cleaned_data.get("nickname")
            newUser.money = money
            newUser.save()

            # 사용자의 검 생성
            newUserSword = UserSword()
            print("유저의 새 검 생성")
            newUserSword.user_id = userInputId
            newUserSword.sword_name = '그냥 검'
            newUserSword.sword_level = '1'
            newUserSword.save()
            print("저장 완료")
            
            # model(객체)을 사용해서 데이터를 저장, 조회, 수정하는 것을 ORM이라고 한다


        else:
            print("모든 정보가 입력되지 않음")
            return Response("Not Valid Data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    elif request.method == "GET":
        print("회원가입 페이지 조회")
        html_template = loader.get_template('sign.html')
        return HttpResponse(html_template.render(context, request))



@api_view(['GET'])
def sword(request):

    # ORM
    # 장고 ORM 데이터 가져오기
    # 하나씩 가져오기
    # swords = Sword.objects.get(sword_id=1)
    
    print('sword view로 들어옴')

    # GET request에서 매개변수(파라미터) 받는 법
    # GET의 매개변수는 key:value 형태이다
    id = request.GET.get('id', None)


    print("Sword Get 매개변수 확인 : id %s" % id)


    # id가 지정되서 들어오면 해당 데이터를 보여주고
    # id가 지정되지 않으면 10개의 데이터를 먼저 보여줌

    sword = None
    sword_string = None
    if id != None:
        # 하나의 해당 데이터 반환
        sword = Sword.objects.get(sword_id=1)
        sword_string = SwordSerializer(user)
        

    else:
        # 10개의 데이터 반환
        # 문자열, 리스트의 slice

        page = int(request.GET.get('page', 1))
        perPage = int(request.GET.get('perPage', 10))
        

        # page와 perPage를 이용해서 현재 필요한 인덱스 숫자 구하기
        # startIndex, endIndex를 구하기
        # perPage : 2
        # 1 page => startIndex : 0, endIndex : 2
        # 2 page => startIndex : 2, endIndex : 4
        # 3 page => startIndex : 4, endIndex : 6

        # 활용할 수 있는 값 => page, perPage
        endIndex = perPage * page
        startIndex = endIndex - perPage        

        sword = Sword.objects.order_by('sword_id')[startIndex:endIndex]
        sword_string = SwordSerializer(sword, many=True)
        
    return Response(sword_string.data)


@api_view(['GET'])
def user(request):
    print('user view로 들어옴')

    # GET request에서 매개변수(파라미터) 받는 법
    # GET의 매개변수는 key:value 형태이다
    id = request.GET.get('id', None)


    print("User Get 매개변수 확인 : id %s" % id)


    # id가 지정되서 들어오면 해당 데이터를 보여주고
    # id가 지정되지 않으면 10개의 데이터를 먼저 보여줌

    user = None
    user_string = None
    if id != None:
        # 하나의 해당 데이터 반환
        user = User.objects.get(user_id=1)
        user_string = UserSerializer(user)
        

    else:
        # 10개의 데이터 반환
        # 문자열, 리스트의 slice

        page = int(request.GET.get('page', 1))
        perPage = int(request.GET.get('perPage', 10))
        

        # page와 perPage를 이용해서 현재 필요한 인덱스 숫자 구하기
        # startIndex, endIndex를 구하기
        # perPage : 2
        # 1 page => startIndex : 0, endIndex : 2
        # 2 page => startIndex : 2, endIndex : 4
        # 3 page => startIndex : 4, endIndex : 6

        # 활용할 수 있는 값 => page, perPage
        endIndex = perPage * page
        startIndex = endIndex - perPage        

        user = User.objects.order_by('user_id')[startIndex:endIndex]
        user_string = UserSerializer(user, many=True)
        
    return Response(user_string.data)


@api_view(['GET'])
def level(request):
    print('user view로 들어옴')

    # GET request에서 매개변수(파라미터) 받는 법
    # GET의 매개변수는 key:value 형태이다
    id = request.GET.get('id', None)


    print("level Get 매개변수 확인 : id %s" % id)


    # id가 지정되서 들어오면 해당 데이터를 보여주고
    # id가 지정되지 않으면 10개의 데이터를 먼저 보여줌

    level = None
    level_string = None
    if id != None:
        # 하나의 해당 데이터 반환
        level = Level.objects.get(level_id=1)
        level_string = LevelSerializer(level)
        

    else:
        # 10개의 데이터 반환
        # 문자열, 리스트의 slice

        page = int(request.GET.get('page', 1))
        perPage = int(request.GET.get('perPage', 10))
        

        # page와 perPage를 이용해서 현재 필요한 인덱스 숫자 구하기
        # startIndex, endIndex를 구하기
        # perPage : 2
        # 1 page => startIndex : 0, endIndex : 2
        # 2 page => startIndex : 2, endIndex : 4
        # 3 page => startIndex : 4, endIndex : 6

        # 활용할 수 있는 값 => page, perPage
        endIndex = perPage * page
        startIndex = endIndex - perPage        


        level = Level.objects.order_by('level_id')[startIndex:endIndex]
        level_string = LevelSerializer(level, many=True)
        
    return Response(level_string.data)



@api_view(['GET'])
def user_sword(request):
    print('user_sword view로 들어옴')

    # GET request에서 매개변수(파라미터) 받는 법
    # GET의 매개변수는 key:value 형태이다
    id = request.GET.get('id', None)


    print("user_sword Get 매개변수 확인 : id %s" % id)


    # id가 지정되서 들어오면 해당 데이터를 보여주고
    # id가 지정되지 않으면 10개의 데이터를 먼저 보여줌

    user_sword = None
    user_sword_string = None
    if id != None:
        # 하나의 해당 데이터 반환
        user_sword = UserSword.objects.get(user_sword_id=1)
        user_sword_string = UserSwordSerializer(user_sword)
        

    else:
        # 10개의 데이터 반환
        # 문자열, 리스트의 slice


        userId = request.GET.get('userId')
        page = int(request.GET.get('page', 1))
        perPage = int(request.GET.get('perPage', 10))
        

        if userId == None:
            return Response([])
            # return ResponseError("No User Id")
        else:
            userId = int(userId)

        # page와 perPage를 이용해서 현재 필요한 인덱스 숫자 구하기
        # startIndex, endIndex를 구하기
        # perPage : 2
        # 1 page => startIndex : 0, endIndex : 2
        # 2 page => startIndex : 2, endIndex : 4
        # 3 page => startIndex : 4, endIndex : 6

        # 활용할 수 있는 값 => page, perPage
        endIndex = perPage * page
        startIndex = endIndex - perPage        


        # 장고 ORM을 이용한 데이터 조회
        user_sword = UserSword.objects.filter(user_id=userId).order_by('user_sword_id')[startIndex:endIndex]
      


        sql_str = 'SELECT *' + 'FROM user_sword' + 'WHERE user_id = ' + str(userId) + ' ' + 'ORDER BY sword_level DESC'

        # 순수 SQL문을 이용한 데이터 조회
        user_sword_by_sql = UserSword.objects.raw(sql_str)

      
        # 데이터를 직렬화
        user_sword_string = UserSwordSerializer(user_sword, many=True)
        
    return Response(user_sword_string.data)

@api_view(['GET'])
def image(request):
    

    pathStr = request.path_info


    print("요청된 URL: %s" % pathStr)

    # localhost:8000/image/image/sword.png
    pathStr = pathStr.replace('/image/', '')

    print("지워진 URL: %s" % pathStr)

    # image/sword.png

    # /res/image/sword.png

    filename = pathStr.split('/')[-1]
    fl_path =  STATIC_ROOT + '/{}'.format(pathStr)
    fl = open(fl_path, 'rb') # read binary file

    mime_type = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attatchment; filename%s" % filename
    return response