from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField()   # 텍스트로 된 속성
    image = models.TextField()
    profile = models.TextField()
    nickname = models.TextField()
    like_count = models.IntegerField(default=0)   # 데이터베이스에 저장될 때 기본값을 0으로 함
    created_at = models.DateTimeField(auto_now_add=True)   # auto_now_add는 생성한 첫 시간을 Asia/Seoul 기준으로 넣음
    updated_at = models.DateTimeField(auto_now=True)   # auto_now는 수정해서 바뀐 시간을 넣어줌

    def __str__(self):   # 주석처리하면 첫번째 게시글이 아니라 Feed object라고 터미널에 뜸
        return self.content  # 보기 좋게 하는 용도
    
    def content_length(self):
        return len(self.content)
    content_length.short_description = '글자수'