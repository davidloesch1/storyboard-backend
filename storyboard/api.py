from storyboard.models import Plot, Submission
from rest_framework import viewsets, permissions
from .serializers import PlotSerializer, SubmissionSerializer


class PlotViewSet(viewsets.ModelViewSet):
    queryset = Plot.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlotSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubmissionSerializer