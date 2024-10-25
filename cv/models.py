
from django.db import models
from django.contrib.auth.models import User

# Personal Information model
class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    bio = models.TextField(blank=True, null=True)  # Brief about you
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Bio(models.Model):
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.bio

# Education model
class Education(models.Model):
    institution_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # If still studying, can be blank

    def __str__(self):
        return f'{self.degree} at {self.institution_name}'


# Work Experience model
class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    linked_in = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    employment_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('intern', 'Intern'),
        ('contract', 'Contract')
    ], default='full-time')
    def __str__(self):
        return f'{self.job_title} at {self.company_name}'


# Skills model
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)  # Can be Beginner, Intermediate, Expert, etc.
    icon = models.CharField(max_length=50)
    def __str__(self):
        return self.skill_name


# Projects model
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)  # Example: Python, Django, JavaScript
    project_url = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.project_title


class projectImages(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.project.project_title


class WorkDescription(models.Model):
    work = models.ForeignKey(WorkExperience, default=None, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.work.company_name