import os,subprocess
from code_model import *
from html_model import *

def prepare_server_center(server_center_dir, server_name='server_center'):   
    subprocess.Popen('cd '+server_center_dir+'; django-admin startproject '+server_name,shell=True).wait()
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/;mkdir ./static',shell=True).wait()
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/;mkdir ./templates',shell=True).wait()
    open(server_center_dir+'/'+server_name+'/run_server.sh','w').write('python manage.py runserver\n')
    open(server_center_dir+'/'+server_name+'/migrate.sh','w').write('python manage.py makemigrations\npython manage.py migrate\n')
  

def prepare_settings(settings_dir):
    fi=open(settings_dir)
    old_file=fi.read()
    old_file="import os\nHERE=os.path.dirname(os.path.dirname(__file__))\n"+old_file
    old_file=old_file.replace("DEBUG = True","DEBUG = False")
    old_file=old_file.replace("'DIRS': [],",r"'DIRS': [os.path.join(HERE,'templates').replace('\\','/'),],")
    old_file=old_file.replace('ALLOWED_HOSTS = []','ALLOWED_HOSTS = ["*"]')
    old_file=old_file + '\n'+r"STATICFILES_DIRS = (os.path.join(HERE, 'static').replace('\\','/'), )"+'\n'+r"STATIC_ROOT =os.path.join(HERE,'static').replace('\\','/')"+'\n'
    fi.close()
    os.remove(settings_dir)
    fo=open(settings_dir,'w')
    fo.write(old_file)
    #print old_file
    fo.close()



def prepare_urls(urls_dir):
    fi=open(urls_dir)
    old_file=fi.read()
    old_file='from django.conf.urls.static import static\n' + old_file
    old_file='from django.conf import settings\n' + old_file
    old_file=old_file.replace("]","url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),"+'\n'+r"]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)")
    fi.close()
    os.remove(urls_dir)
    fo=open(urls_dir,'w')
    fo.write(old_file)
    fo.close()



def build_server(server_center_dir, server_name='server_center'):
    print "adjango-server requires django==1.87 !!!"
    prepare_server_center(server_center_dir,server_name)
    prepare_settings(server_center_dir+'/'+server_name+'/'+server_name+'/settings.py')
    prepare_urls(server_center_dir+'/'+server_name+'/'+server_name+'/urls.py')



def add_app(server_center_dir, app_name, server_name='server_center'):
    settings_file=server_center_dir+'/'+server_name+'/'+server_name+'/settings.py'
    urls_file=server_center_dir+'/'+server_name+'/'+server_name+'/urls.py'
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'; python manage.py startapp '+app_name,shell=True).wait()
    old_file=open(settings_file).read()
    old_file=old_file.replace("INSTALLED_APPS = (","INSTALLED_APPS = (\n    '"+app_name+"',\n")
    os.remove(settings_file)
    open(settings_file,'w').write(old_file)
    old_file=open(urls_file).read()
    old_file=old_file.replace("urlpatterns = [","urlpatterns = [\n    "+r"url(r'^"+app_name+r"/', include('"+app_name+r".urls')),"+'\n')
    open(urls_file,'w').write(old_file)


    app_views_file=server_center_dir+'/'+server_name+'/'+app_name+'/views.py'
    app_urls_file=server_center_dir+'/'+server_name+'/'+app_name+'/urls.py'
    app_models_file=server_center_dir+'/'+server_name+'/'+app_name+'/models.py'
    app_scripts_file=server_center_dir+'/'+server_name+'/'+app_name+'/scripts/script.py'
    open(app_views_file,'w').write(VIEWS.replace('__APP_NAME__',app_name))
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/'+app_name+'; mkdir scripts',shell=True).wait()
    open(app_urls_file,'w').write(URLS)
    open(app_models_file,'w').write(MODELS)
    open(app_scripts_file,'w').write(SCRIPT)


    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/static; mkdir '+app_name+'_input',shell=True).wait()
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/static; mkdir '+app_name+'_output',shell=True).wait()
    app_base_file=server_center_dir+'/'+server_name+'/templates/'+app_name+'_base.html'
    app_index_file=server_center_dir+'/'+server_name+'/templates/'+app_name+'_index.html'
    app_handler_file=server_center_dir+'/'+server_name+'/templates/'+app_name+'_handler_detail.html'
    open(app_base_file,'w').write(BASE.replace('__APP_NAME__',app_name))
    open(app_index_file,'w').write(INDEX.replace('__APP_NAME__',app_name))
    open(app_handler_file,'w').write(HANDLER.replace('__APP_NAME__',app_name))
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/; python manage.py makemigrations',shell=True).wait()
    subprocess.Popen('cd '+server_center_dir+'/'+server_name+'/; python manage.py migrate',shell=True).wait()                   








