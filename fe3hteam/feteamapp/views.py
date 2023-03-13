from django.shortcuts import render
from .models import Feteamapp, Unit, UnitClass, Ability, Proficiency
from rest_framework import generics
from .serializers import FeteamappSerializer, UnitSerializer, UnitClassSerializer, AbilitySerializer, ProficiencySerializer

# Create your views here.

# API endpoint that allows creation
class FeteamappCreate(generics.CreateAPIView):
	queryset = Feteamapp.objects.all(),
	serializer_class = FeteamappSerializer

# API endpoint that lists all
class FeteamappList(generics.ListAPIView):
	queryset = Feteamapp.objects.all()
	serializer_class = FeteamappSerializer

# API endpoint that returns a single entry
class FeteamappDetail(generics.RetrieveAPIView):
	queryset = Feteamapp.objects.all()
	serializer_class = FeteamappSerializer

# API endpoint that allows an entry to be updated
class FeteamappUpdate(generics.RetrieveUpdateAPIView):
	queryset = Feteamapp.objects.all()
	serializer_class = FeteamappSerializer

# API endpoing that allows an entry to be deleted
class FeteamappDelete(generics.RetrieveDestroyAPIView):
	queryset = Feteamapp.objects.all()
	serializer_class = FeteamappSerializer


# UNIT #

# API endpoint that allows creation
class UnitCreate(generics.CreateAPIView):
        queryset = Unit.objects.all(),
        serializer_class = UnitSerializer

# API endpoint that lists all
class UnitList(generics.ListAPIView):
        queryset = Unit.objects.all()
        serializer_class = UnitSerializer

# API endpoint that returns a single entry
class UnitDetail(generics.RetrieveAPIView):
        queryset = Unit.objects.all()
        serializer_class = UnitSerializer

# API endpoint that allows an entry to be updated
class UnitUpdate(generics.RetrieveUpdateAPIView):
        queryset = Unit.objects.all()
        serializer_class = UnitSerializer

# API endpoing that allows an entry to be deleted
class UnitDelete(generics.RetrieveDestroyAPIView):
        queryset = Unit.objects.all()
        serializer_class = UnitSerializer


# CLASS #

# API endpoint that allows creation
class UnitClassCreate(generics.CreateAPIView):
        queryset = UnitClass.objects.all(),
        serializer_class = UnitClassSerializer

# API endpoint that lists all
class UnitClassList(generics.ListAPIView):
        queryset = UnitClass.objects.all()
        serializer_class = UnitClassSerializer

# API endpoint that returns a single entry
class UnitClassDetail(generics.RetrieveAPIView):
        queryset = UnitClass.objects.all()
        serializer_class = UnitClassSerializer

# API endpoint that allows an entry to be updated
class UnitClassUpdate(generics.RetrieveUpdateAPIView):
        queryset = UnitClass.objects.all()
        serializer_class = UnitClassSerializer

# API endpoing that allows an entry to be deleted
class UnitClassDelete(generics.RetrieveDestroyAPIView):
        queryset = UnitClass.objects.all()
        serializer_class = UnitClassSerializer


# ABILITY #

# API endpoint that allows creation
class AbilityCreate(generics.CreateAPIView):
        queryset = Ability.objects.all(),
        serializer_class = AbilitySerializer

# API endpoint that lists all
class AbilityList(generics.ListAPIView):
        queryset = Ability.objects.all()
        serializer_class = AbilitySerializer

# API endpoint that returns a single entry
class AbilityDetail(generics.RetrieveAPIView):
        queryset = Ability.objects.all()
        serializer_class = AbilitySerializer

# API endpoint that allows an entry to be updated
class AbilityUpdate(generics.RetrieveUpdateAPIView):
        queryset = Ability.objects.all()
        serializer_class = AbilitySerializer

# API endpoing that allows an entry to be deleted
class AbilityDelete(generics.RetrieveDestroyAPIView):
        queryset = Ability.objects.all()
        serializer_class = AbilitySerializer


# Proficiency #

# API endpoint that allows creation
class ProficiencyCreate(generics.CreateAPIView):
        queryset = Proficiency.objects.all(),
        serializer_class = ProficiencySerializer

# API endpoint that lists all
class ProficiencyList(generics.ListAPIView):
        queryset = Proficiency.objects.all()
        serializer_class = ProficiencySerializer

# API endpoint that returns a single entry
class ProficiencyDetail(generics.RetrieveAPIView):
        queryset = Proficiency.objects.all()
        serializer_class = ProficiencySerializer

# API endpoint that allows an entry to be updated
class ProficiencyUpdate(generics.RetrieveUpdateAPIView):
        queryset = Proficiency.objects.all()
        serializer_class = ProficiencySerializer

# API endpoing that allows an entry to be deleted
class ProficiencyDelete(generics.RetrieveDestroyAPIView):
        queryset = Proficiency.objects.all()
        serializer_class = ProficiencySerializer
