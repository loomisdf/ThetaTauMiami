from django.db import models

# Create your models here.

class PledgeClass(models.Model):
    year = models.CharField(max_length=4)
    semester = models.CharField(max_length=10)
    bidOffer = models.DateField()
    initiation = models.DateField()
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.year + " " + self.semester
    
class Brother(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    pledgeClass = models.ForeignKey(PledgeClass)
    uniqueId = models.CharField(max_length=10)
    graduationYear = models.CharField(max_length=4)
    isAlumni = models.BooleanField()
    isPledge = models.BooleanField()
    phone = models.CharField(max_length=15)
    picture = models.URLField()
    resume = models.URLField()
    address = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    
    def __unicode__(self):
        return str(self.pledgeClass) + " " + self.lastName + ", " + self.firstName + " " + self.middleName
     
class Department(models.Model):
    abbrev = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    def __unicode__(self):
        return self.abbrev
       
class Major(models.Model):
    department = models.ForeignKey(Department)
    majorName = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.majorName

class HasMajor(models.Model):
    brother = models.ForeignKey(Brother)
    major = models.ForeignKey(Major)
    
    def ___unicode__(self):
        return str(self.brother) + " " + str(self.major)