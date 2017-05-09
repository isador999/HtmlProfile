from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from time import strftime
import datetime
import json



def homepage(request):
    # try:
    #     radio = Webradio.objects.get(selected=1)
    # except Webradio.DoesNotExist:
    #     radio = None

    # try:
    #     music = Music.objects.get(selected=1)
    # except Music.DoesNotExist:
    #     music = None

    # try:
    #     artist = Artist.objects.get(selected=1)
    # except Artist.DoesNotExist:
    #     artist = None
    currentdate = datetime.date.today()
    birthdate = datetime.date(1989, 9, 17)
    nb_days = currentdate - birthdate
    nb_days = nb_days/365
    age = str(nb_days).split(" ")
    age = age[0]

    clock = strftime("%H:%M:%S")
    return render(request, 'homepage.html', {'clock': clock,
                                             'date': currentdate,
                                             'age': age})

def pro_experiences(request):
    experiences_modals = ['modals/modalPJ.html', 'modals/modalSII.html', 'modals/modalALU.html', 'modals/modalSIBIO.html', 'modals/modalSANDVIK.html', 'modals/modalVH.html']
    return render(request, 'pro_experiences.html', {'experiences_modals': experiences_modals})


def formations(request):
    formations_modals = ['modals/modalENI.html', 'modals/modalAFTEC.html', 'modals/modalSTPAUL.html']
    return render(request, 'formations.html', {'formations_modals': formations_modals})


def association(request):
    return render(request, 'association.html')


def pdf_cv(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv_jean-baptiste.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "CV JPH")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

