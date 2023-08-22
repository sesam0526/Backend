from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Feed
# Create your views here.

class Main(APIView):  
    def get(self, request):  # overriding
        feed_list = Feed.objects.all()  # 모든 정보 가져와서 저장

        for feed in feed_list:
            print(feed)  # terminal에서 오류 확인가능

        return render(request, "content/main.html", {   # 화면에 띄울 주소
            'feed_list': feed_list,  # main.html에 넘겨줄 요소
        })
    
    
class Post(APIView):
    def get(self, request):
        return render(request, "content/post.html")  # 요청받으면 띄움
    
    def post(self, request):
        content=request.POST.get('content')  # 정보를 가져옴, 위의 def get과 다름
        nickname=request.POST.get('nickname')
        image=request.POST.get('image')
        profile=request.POST.get('profile')

        feed = Feed()  # 데이터베이스에 가져온 정보를 저장
        feed.content = content
        feed.nickname = nickname
        feed.image = image
        feed.profile = profile
        feed.save()  # 데이터베이스에 갱신

        return redirect('content:main')  # 편의성을 위해 사용, 저장 후 다시 main 페이지로 돌아감
    # content 앱의 main 페이지로 감
class Modify(APIView):
    def post(self, request, pk):
        content=request.POST.get('content')  
        nickname=request.POST.get('nickname')
        image=request.POST.get('image')
        profile=request.POST.get('profile')

        feed = Feed.objects.get(id=pk)  # feed에서 해당 id에 해당하는 데이터 가져옴
        feed.content = content
        feed.nickname = nickname
        feed.image = image
        feed.profile = profile
        feed.save() 

        return redirect('content:main')

    def get(self, request, pk):
        feed = Feed.objects.get(id=pk)   # id가 pk와 같은 데이터 하나만 가져옴, cf) filter는 데이터 여러개 가져옴(중복 허용), get은 데이터 하나만 가져옴
        # = SELECT * FROM Feed WHERE id=pk
        return render(request, "content/modify.html", {
            'feed': feed,   # 'feed'라는 이름으로 feed 정보를 넘겨줌(사실상 json과 유사)
        })
    
def delete(request, pk):   # class로 해도 가능, POST로 밖에 하지 않아서 함수로 하는 것이 편함
    if request.method == 'POST':
        feed = Feed.objects.get(id=pk)
        feed.delete()
    return redirect('content:main')

def isGood(request, pk):
    if request.method == 'POST':
        s = request.POST.get('isGood')   # post방식으로 form안에 있는 button의 value 받아옴
        feed = Feed.objects.get(id=pk)
        if s == '좋아요':
            feed.like_count = feed.like_count+1
            print('좋아요')
        elif s == '싫어요' and feed.like_count>0:
            feed.like_count = feed.like_count-1
            print('싫어요')
        feed.save()
    return redirect('content:main')