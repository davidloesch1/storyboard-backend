from django.urls import path
from . import views
from .views import StoryLibrary, StoryDetails
from rest_framework import routers
from .api import PlotViewSet


router = routers.DefaultRouter()
router.register(r'api/stories', PlotViewSet, 'stories')

# patterns
urlpatterns = [
    path('stories/', views.StoryLibrary.as_view(), name='story_library'),
    path('story/details/<int:pk>', views.StoryDetails.as_view(), name='story_details'),
    path('characters/', views.CharacterLibrary.as_view(), name='character_library'),
    path('submissions/', views.Submissions.as_view(), name='submissions'),
    path('submissions/<int:plot>', views.PlotSubmissions.as_view(), name='submissions'),
]


