from rest_framework import generics, viewsets, permissions
from .serializers import PlotSerializer, CharacterSerializer, SubmissionSerializer
from .models import Plot, Character, Submission
from django.contrib.auth.models import User


class StoryLibrary(generics.ListCreateAPIView):
    queryset = Plot.objects.all().order_by('created_at')
    serializer_class = PlotSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permissions_classes = [permissions.IsAuthenticated]

class CharacterLibrary(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def perform_create(self, serializer):
        serializer.save()

class Submissions(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlotSubmissions(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer 

    def get_queryset(self):
        return Submission.objects.filter(plot=self.kwargs["plot"]).order_by('id')



