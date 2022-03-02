from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView

from faculty.models import Faculty
from faculty.serializers import FacultyListSerializer, FacultySerializer

from .helper import faculties


class FacultyListView(ListAPIView):
    serializer_class = FacultyListSerializer
    queryset = Faculty.objects.all()


class FacultyView(RetrieveAPIView):
    serializer_class = FacultySerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"
    queryset = Faculty.objects.all()


class FacultyCreate(ListAPIView):
    serializer_class = FacultyListSerializer

    def get_queryset(self):
        for i in faculties.keys():
            if len(Faculty.objects.filter(name=i)) > 0:
                pass
            else:
                Faculty.objects.create(
                    name=i,
                    title=faculties[i]["title"],
                    email=faculties[i]["email"],
                    research_interests=faculties[i]["Research interests"],
                    subject_groups=faculties[i]["subject groups"],
                    pic=faculties[i]["pic"],
                )
        return Faculty.objects.all()
