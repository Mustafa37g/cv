from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *


def cv_view(request):
    personal_info = PersonalInfo.objects.first()
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    projects = Project.objects.filter().order_by('-start_date')
    bio = Bio.objects.all().order_by('id')
    work_experiences_with_descriptions = [
        {
            'work_experience': work,
            'descriptions': WorkDescription.objects.filter(work=work)
        }
        for work in work_experiences
    ]

    # Create a dictionary of projects with associated images
    project_images = {
        project.id: projectImages.objects.filter(project=project)
        for project in projects
    }

    context = {
        'personal_info': personal_info,
        'skills': skills,
        'work_experiences': work_experiences_with_descriptions,
        'educations': educations,
        'projects': projects,
        'project_images': project_images,
        'current_year': datetime.now().year,
        'bio': bio,
    }

    return render(request, 'home.html', context)
