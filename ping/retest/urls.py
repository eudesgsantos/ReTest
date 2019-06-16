from django.urls import path
from  .    import views
from django.conf.urls import url


urlpatterns = [
	url('login/',views.login, name='retest-login'),
    url('report/',views.report, name='retest-report'),
    url('enviar/',views.enviar, name='retest-enviar')
]


