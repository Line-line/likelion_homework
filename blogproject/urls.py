"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create', blog.views.create, name="create"),      # path만들었다고 html만 부르는것뿐만이 아니라 함수를 불러 줄 수 있다.
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
    
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),

    path('accounts/signup/', accounts.views.signup, name = 'signup'),
    path('accounts/login/', accounts.views.login, name = 'login'),
    path('accounts/logout/', accounts.views.logout, name = 'logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# path을 설정해주는건데 몇백개가 있을때 하나하나 다 해줘야하는데 귀찮으니까 각 게시물에 아이디를 넣어줄 공간을 만들어줌 <intLblog_id>이거 각각의 아이디를 넣어준다고 생각하면 된다.
# 가로안에 써놓은게 path 컴퍼터?라는건데 여러개의 url을 다룰때 사용
# 어떤것을 지정했을 때 그것을 지정한 값을 넣어라?
# 1번째 값을 넣을 때 1번 값이 나오게~ 이렇게?
# 자체적으로 아이디를 받아서 보여주는 것
# blogobject라는 목록들을 바로 보게끔 하려는데 많아지면 복잡하니까 장고 내에서 제공해준 블로그에 있는 값을 자동으로 아이디로 넣어준다.

