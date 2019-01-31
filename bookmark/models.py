from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)  # Null = false, black = false 옵션 추가 가능 기본
    url = models.URLField()

    def __str__ (self):
        # 인스턴스를 출력할때 사용되는 메서드
        return self.site_name + " : " + self.url

    # Todo : get_absolute_url method
    # 현재는 url패턴을 만들지 않았기 때문에 위 메쏘드를 쓸수가 없음

    class Meta:  # 옵션 클래스
        ordering = ['site_name']
        # 정렬을 어떤 기준으로 하느냐의 옵션값을 결정, 이또한 DB에 (migrate)반영되는 내용.

    def get_absolute_url(self):
        return reverse_lazy('bookmark_detail', args=[self.id])

    # models 필드의 종류
    # 1. DB에 어떤 형태로 어떤 제약 사항으로 데이터를 저장하느냐
    # 2. 프론트에서 어떤 형태로 어떤 제약 사항을 가지고 입력을 받을 것이냐
    # 위 두가지에 대한 것을 models 에서 어떤 Field 를 사용하느냐에 따라서 결정을 하게 됨
    # 커스텀 Field 도 만들어서 쓸 수 있음
