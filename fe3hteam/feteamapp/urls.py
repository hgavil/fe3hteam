from django.urls import include, path
from .views import *
# from .views import FeteamappCreate, FeteamappList, FeteamappDetail, FeteamappUpdate, FeteamappDelete, UnitCreate, UnitList, UnitDetail, UnitUpdate, UnitDelete, UnitClassCreate, UnitClassDetail, UnitClassDelete, UnitClassList, UnitClassUpdate

urlpatterns = [
	path('create-unit/', UnitCreate.as_view(), name='create-unit'),
        path('unit', UnitList.as_view()),
        path('unit/<int:pk>/', UnitDetail.as_view(), name='retrieve-unit'),
        path('update-unit/<int:pk>/', UnitUpdate.as_view(), name='update-unit'),
        # path('delete-unit/<int:pk>/', UnitDelete.as_view(), name='delete-unit'),

	path('create-unitclass/', UnitClassCreate.as_view(), name='create-unitclass'),
        path('unitclass', UnitClassList.as_view()),
        path('unitclass/<int:pk>/', UnitClassDetail.as_view(), name='retrieve-unitclass'),
        path('update-unitclass/<int:pk>/', UnitClassUpdate.as_view(), name='update-unitclass'),
        # path('delete-unitclass/<int:pk>/', UnitClassDelete.as_view(), name='delete-unitclass'),

        path('create-ability/', AbilityCreate.as_view(), name='create-ability'),
        path('ability', AbilityList.as_view()),
        path('ability/<int:pk>/', AbilityDetail.as_view(), name='retrieve-ability'),
        path('update-ability/<int:pk>/', AbilityUpdate.as_view(), name='update-ability'),
        # path('delete-ability/<int:pk>/', AbilityDelete.as_view(), name='delete-ability'),

        path('create-proficiency/', ProficiencyCreate.as_view(), name='create-proficiency'),
        path('proficiency', ProficiencyList.as_view()),
        path('proficiency/<int:pk>/', ProficiencyDelete.as_view(), name='retrieve-proficiency'),
        path('update-proficiency/<int:pk>/', ProficiencyUpdate.as_view(), name='update-proficiency'),
        # path('delete-proficiency/<int:pk>/', ProficiencyDelete.as_view(), name='delete-proficiency'),
]
