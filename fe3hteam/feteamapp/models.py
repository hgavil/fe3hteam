from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Feteamapp(models.Model):
	name = models.CharField("Name", max_length=240)
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


# PROFICIENCIES - the options for each skill
class Proficiency(models.Model):

	# Short explanation of what the proficiency is for organization
	profIdentifier = models.CharField(max_length=200)

	# Determines what kind of proficiency/requirement it is
	TYPE_CHOICES = [
		('gen', 'General'),
		('char', 'Character Ability'),
		('classab', 'Class Mastery'),
		('class', 'Class Requierment')
	]
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)


	# Charex / Classex / Abex - A proficiency may or may not be tied to a Unit, Class, or Ability

	# If this requirement is tied to a Unit, specify here
	charex = models.ForeignKey(
		'Unit',
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)
	# If this requirement is tied to a Class, specify here
	classex = models.ForeignKey(
		'UnitClass',
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)
	# If this requirement is tied to an Ability, specify here
	abex = models.ForeignKey(
		'Ability',
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)

	# Specifies the type of skill
	PROF_CHOICES = [
		('sword', 'Sword'),
		('lance', 'Lance'),
		('axe', 'Axe'),
		('bow', 'Bow'),
		('brawl', 'Brawl'),
		('reason', 'Reason'),
		('faith', 'Faith'),
		('authority', 'Authority'),
		('riding', 'Riding'),
		('flying', 'Flying'),
		('armor', 'Armor')
	]
	prof = models.CharField(max_length=20, choices=PROF_CHOICES, null=True, blank=True)

	# Specifies the skill level needed
	LEVEL_CHOICES = [
		('e', 'E'),
		('e+', 'E+'),
		('d', 'D'),
		('d+', 'D+'),
		('c', 'C'),
		('c+', 'C+'),
		('b', 'B'),
		('b+', 'B+'),
		('a', 'A'),
		('a+', 'A+'),
		('s', 'S'),
		('s+', 'S+'),
		('mastery', 'Mastery'),
		('bud', 'Budding Talent')
	]
	level = models.CharField(max_length=20, choices=LEVEL_CHOICES, null=True, blank=True)

	def __str__(self):
		if (self.type != 'classab'):
			return "%s - %s %s" % (self.profIdentifier, self.prof, self.level)
		else: 
			return "%s - %s" % (self.profIdentifier, self.type)


# UNIT - all the characters
class Unit(models.Model):
	name = models.CharField("Name", max_length=240) # Unit name
	academyImage = models.ImageField(upload_to='images', blank=True) # Academy portrait
	warImage = models.ImageField(upload_to='images', blank=True) # War portrait

	GENDER_CHOICES = [
		('female', 'Female'),
		('male', 'Male')
	]
	gender = models.CharField("Gender", max_length=10, choices=GENDER_CHOICES, blank=True) # Gender

	HOUSE_CHOICES = [
		('eagles', 'Black Eagles'),
		('lions', 'Blue Lions'),
		('deer', 'Golden Deer'),
		('wolves', 'Ashen Wolves'),
		('church', 'Church of Seiros')
	]
	house = models.CharField("House", max_length=50, choices=HOUSE_CHOICES, blank=True) # House/affiliation (Black Eagles, Blue Lions, Golden Deer, Ashen Wolves, Church of Seiros
	defaultClass = models.ForeignKey( # Default Class (foreign key from Class model)
		'UnitClass',
		on_delete=models.CASCADE,
		null=True,
	)
	personalAbility = models.ForeignKey( # Personal Ability (foreign key from Ability model)
		'Ability',
		on_delete=models.CASCADE,
		limit_choices_to={'type' : 'personal'},
		null=True,
		blank=True
	)

	def __str__(self):
		return self.name


# CLASS - all the classes
class UnitClass(models.Model):
	name = models.CharField("Name", max_length = 240) # Class name
	description = models.TextField("Description", blank=True) # Class description
	sprite = models.ImageField(upload_to="images", blank=True) # Sprite

	GENDERLOCKED_CHOICES = [
		('female', 'Female'),
		('male', 'Male')
	]
	genderLocked = models.CharField("Genderlocked", max_length=50, blank=True, choices=GENDERLOCKED_CHOICES) # Whether the class is genderlocked or not and what gender

	LEVEL_CHOICES = [
		('base', 'Base'),
		('unique', 'Unique'),
		('beginner', 'Beginner'),
		('intermediate', 'Intermediate'),
		('advanced', 'Advanced'),
		('dlc', 'DLC'),
		('master', 'Master')
	]
	level = models.CharField("Level", max_length=50, choices=LEVEL_CHOICES, blank=True) # Class level
	classAbs = models.ManyToManyField( # Class Abilities - up to 3
		'Ability', 
		blank=True,
	)
	uniqueTo = models.ForeignKey( # Optional column that determines whether a class is unique to a specific unit (lords and jeritza)
		'Unit',
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)


	def __str__(self):
		return self.name


# ABILITY - all the abilities
class Ability(models.Model):
	name = models.CharField("Name", max_length=240) # Ability name
	description = models.TextField("Description", blank=True) # Ability description
	icon = models.ImageField(upload_to="images", blank=True) # Icon
	
	TYPE_CHOICES = [
		('personal', 'Personal'), # Personal abilities - only one unit is allowed to have this, and it will not show up in the regular Ability pool
		('class', 'Class'), # Class abilities - abilities that are exclusive to the equipped class, and they will not show up in the regular Ability pool
		('standard', 'Standard'), # Standard abilities - abilities that can be obtained through training or class mastery, and fill the Ability pool
		('character', 'Character Exclusive') # Character exclusive abilities - abilities that only certain/specific characters can get, will only appear in those characters' pools
	]
	type = models.CharField("Type", max_length=50, choices=TYPE_CHOICES, blank=True) # Types

	def __str__(self):
		return self.name
