from django.conf.urls import url
from Basic_app import views

app_name= 'Basic_app'

urlpatterns=[
        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),
]
