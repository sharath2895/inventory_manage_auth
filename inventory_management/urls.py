
from django.contrib import admin
from django.urls import path,include
from authenticate import urls as authurls
from user import urls as userurls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/',include(authurls)),
    path('user/', include(userurls))
]
