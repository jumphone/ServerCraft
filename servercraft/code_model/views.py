VIEWS=r'''

from django.shortcuts import render
# -*- coding: utf-8 -*- 
import sys,os,subprocess
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime,time
from django.http import Http404, HttpResponseRedirect
from django.template import Template, Context
import uuid
import datetime
from datetime import tzinfo
from subprocess import Popen
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import Handler  
from django.template import RequestContext

APP_NAME='__APP_NAME__'
SCRIPT_PATH= os.path.join(os.getcwd(), APP_NAME, 'scripts/script.py')

INDEX_HTML='__APP_NAME___index.html'
DETAIL_HTML='__APP_NAME___handler_detail.html'

TIMEOUT=100
MAX_COUNT=10

INPUT_DIR='__APP_NAME___input'
OUTPUT_DIR='__APP_NAME___output'




# Create your views here


def index(request):

    processing_count = Handler.objects.filter(status='Processing').count()
    if processing_count >= MAX_COUNT:
        is_full = True
    else:
        is_full = False


    return render_to_response(INDEX_HTML, locals(),context_instance=RequestContext(request))


def handler_start(request):
    for h in Handler.objects.filter(status='Processing'):
        if os.path.exists(h.dist_path):
            h.status = 'Finish'
            
            h.save()
     



    if Handler.objects.filter(status='Processing').count() >= MAX_COUNT:
        return HttpResponse('Too many visitors! Please try again later.')

    input_text = request.POST.get('input_text')
    input_file = request.FILES.get('input_file')
    input_condition = request.POST.get('conditions')

    if input_file:
        input_text = input_file.read()

    if not input_text:
        return HttpResponseRedirect('/'+APP_NAME)
    
    input_text = "##Condition:" + str(input_condition) + "\n"+ input_text


    h = Handler()
    h.name = ''
    h.id=abs(hash(input_text))
    try:
        h.save()
    except Exception,e :
        return HttpResponseRedirect('/'+APP_NAME+'/handler/%s/' % h.id)

    dist_path = os.path.join(os.getcwd(), 'static', OUTPUT_DIR , str(h.id)) 
    input_path =  os.path.join(os.getcwd(), 'static', INPUT_DIR, str(h.id))

    try:
        open(input_path, 'wb').write(input_text)
    except UnicodeEncodeError:
        input_text = input_text.encode('utf8')
        open(input_path, 'wb').write(input_text)

    p = Popen(['python', SCRIPT_PATH, input_path, dist_path])

    h.pid = p.pid
    h.status = 'Processing'
    h.input_data = input_text
    h.dist_path = dist_path
    h.save()

    return HttpResponseRedirect('/'+APP_NAME+'/handler/%s/' % h.id)




def handler_detail(request, hid):
    h = Handler.objects.get(id=hid)
    if os.path.exists(h.dist_path):
        h.output_data = open(h.dist_path, 'rb').read()
        h.status = 'Finish'
        print 'finish'
    elif datetime.datetime.now() - h.create_time.replace(tzinfo=None) > datetime.timedelta(seconds=TIMEOUT):
        try:
            os.kill(int(h.pid), 9)
            h.status = 'Timeout'
            print 'timeout'
        except OSError, e:
            h.status = 'Failed'
    
    h.save()
    return render_to_response(DETAIL_HTML, locals())





def handler_download(request, hid):
    h = Handler.objects.get(id=hid)
    return HttpResponseRedirect('/static/'+OUTPUT_DIR+'/%s' % h.id)
'''


