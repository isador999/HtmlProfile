from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from webgui.models import *
import os
from django.http import HttpResponse
from time import strftime
import datetime
import locale


def homepage(request):
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    currentdate = datetime.date.today()
    birthdate = datetime.date(1989, 9, 17)
    nb_days = currentdate - birthdate
    nb_days = nb_days/365
    age = str(nb_days).split(" ")
    age = age[0]

    clock = strftime("%H:%M:%S")

    skills = Skill.objects.all()
    tags = Tag.objects.all()

    return render(request, 'homepage.html', {'clock': clock,
                                             'date': currentdate,
                                             'age': age,
                                             'skills': skills,
                                             'tags': tags})


def pro_experiences(request):
    try:
        experiences_list = Experience.objects.all()
        for experience in experiences_list:
            locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
            experience.start_date = experience.start_date.strftime("%B %Y")
            experience.end_date = experience.end_date.strftime("%B %Y")
    except Experience.DoesNotExist:
        experiences_list = None
    return render(request, 'pro_experiences.html', {'experiences_list': experiences_list})


def formations(request):
    try:
        formations_list = Formation.objects.all()
        for formation in formations_list:
            locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
            formation.start_date = formation.start_date.strftime("%B %Y")
            formation.end_date = formation.end_date.strftime("%B %Y")
    except Formation.DoesNotExist:
        formations_list = None
    return render(request, 'formations.html', {'formations_list': formations_list})


def association(request):
    try:
        leisures = Leisure.objects.all()
    except Leisure.DoesNotExist:
        leisures = None

    return render(request, 'association.html', {'leisures':leisures})


# def pdf_cv(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="cv_jean-baptiste.pdf"'

    # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawString(100, 100, "CV JPH")

    # Close the PDF object cleanly, and we're done.
    # p.showPage()
    # p.save()
    # return response
