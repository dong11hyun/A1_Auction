# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 관리자 페이지에서 우리 회원 모델을 어떻게 보여줄지 설정하는 부분입니다.
class CustomUserAdmin(UserAdmin):
    # 기존 회원 정보 밑에 'Custom Fields'라는 제목으로 
    # 닉네임과 신용도(reputation_score)를 추가해서 보여줍니다.
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('nickname', 'reputation_score')}),
    )

# 장고에게 등록!
admin.site.register(User, CustomUserAdmin)