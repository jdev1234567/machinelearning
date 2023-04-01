from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from playground.models import Image
import base64
from django.core.files.base import ContentFile
from playground.digitmodel import Digit
from playground.lettermodel import Paint
# Create your views here.
def say_hello(request):
    return render(request,'imagerecognitaion.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def uploadImage(request):
    if request.method == 'POST':
        #newEntry = Image(request.POST,request.FILES)
        letter= request.GET['letter']
        #print(letter)
        format, imgstr = str(request.body).split(';base64,')
        print(imgstr)
        print(len(imgstr))
        ext = format.split('/')[-1]

        #data = ContentFile(base64.b64decode(imgstr))
        file_name = "myphoto." + ext
        #print(str(base64.b64decode(imgstr)))
        #f = open(file_name, "w")
        #f.write(str(imgstr))

        decoded_data=''
        # decode base64 string data
        try:
            decoded_data = base64.b64decode(imgstr)
        except:
            try:
                decoded_data=base64.b64decode(imgstr + '=' * (-len(imgstr) % 4))
            except:
                return JsonResponse({'text':
                                     'try again'})
        # write the decoded data back to original format in  file
        img_file = open(file_name, 'wb')
        img_file.write(decoded_data)
        img_file.close()
        if(str(letter)=='digit'):
            digi=Digit()
            #digi.model()
            return JsonResponse({'text': digi.model()})
        else:
            lettermodel=Paint()
            lettermodel.guess_image("myphoto.png")
            return JsonResponse({'text':lettermodel.guess_image("myphoto.png")})
