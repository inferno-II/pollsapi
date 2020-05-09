from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
# from .apiviews import PollList, PollDetail
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls
