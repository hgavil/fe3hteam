from rest_framework import serializers
from .models import Feteamapp, Unit, UnitClass, Ability, Proficiency

class FeteamappSerializer(serializers.ModelSerializer):

	class Meta:
		model = Feteamapp
		fields = ['pk', 'name', 'created']

class UnitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Unit
		fields = ['pk', 'name', 'academyImage', 'warImage', 'gender', 'house', 'defaultClass', 'personalAbility']

class UnitClassSerializer(serializers.ModelSerializer):

	class Meta:
		model = UnitClass
		fields = ['pk', 'name', 'description', 'sprite', 'genderLocked', 'level', 'classAbs', 'uniqueTo']

class AbilitySerializer(serializers.ModelSerializer):

	class Meta:
		model = Ability
		fields = ['pk', 'name', 'description', 'icon', 'type']

class ProficiencySerializer(serializers.ModelSerializer):

	class Meta:
		model = Proficiency
		fields = ['pk', 'profIdentifier', 'type', 'charex', 'classex', 'abex', 'prof', 'level']