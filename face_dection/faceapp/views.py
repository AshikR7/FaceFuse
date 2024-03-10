
import face_recognition
from django.shortcuts import render,redirect
from django.http import HttpResponse
import math
from PIL import Image, ImageDraw


from .forms import *


# Create your views here.

def index(request):
    return render(request,'index.html')


def compare_view(request):
    if request.method=='POST':
        a=compare_photos_forms(request.POST,request.FILES)
        if a.is_valid():
            try:
                first_pic=a.cleaned_data['firstPhoto']
                second_pic=a.cleaned_data['secondPhoto']

                img_1=face_recognition.load_image_file(first_pic)
                img_2=face_recognition.load_image_file(second_pic)

                img_1_encoding=face_recognition.face_encodings(img_1)[0]
                img_2_encoding=face_recognition.face_encodings(img_2)[0]

                known_encodings=[
                    img_1_encoding,
                    img_2_encoding
                ]
                img_test=face_recognition.load_image_file(first_pic)
                img_test_encoding=face_recognition.face_encodings(img_test)[0]
                face_distances = face_recognition.face_distance(known_encodings, img_test_encoding)
                balance=1-face_distances[1]
                percentage=math.ceil((balance/1)*100)
                return render(request,'result.html',{'face_distances':percentage})
            except:
                return render(request,'error.html')
        else:
            return HttpResponse("something went wrong")
    return render(request,'compare.html')





def face_detection(request):
    if request.method=='POST':
        a=face_detection_forms(request.POST,request.FILES)
        z=request.FILES['face']
        filename=z.name
        if a.is_valid():
            face_pic=a.cleaned_data['face']
            face_1 = face_recognition.load_image_file(face_pic)
            face_locations = face_recognition.face_locations(face_1)
            face_encodings = face_recognition.face_encodings(face_1, face_locations)
            pil_image = Image.fromarray(face_1)
            draw = ImageDraw.Draw(pil_image)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            pil_image.show()
            return redirect(face_detection)
        else:
            return HttpResponse("no")
    return render(request,'face_detection.html')


