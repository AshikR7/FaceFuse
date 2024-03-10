from django import forms
class compare_photos_forms(forms.Form):
    firstPhoto= forms.ImageField()
    secondPhoto=forms.ImageField()

class face_detection_forms(forms.Form):
    face=forms.ImageField()