
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from Photogallery.models import Item, Category
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage



#Show Categories on main field

def index(request):
    Category.objects.get(id=1).item_set.all()

    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all()
    }

    return HttpResponse(template.render(context, request))


#Show Items of one category
def showPicturesfromCountry(request):
    Category.objects.get(id=1).item_set.all()
    your_parameter = request.GET['parameter']
    load_country = your_parameter



    template = loader.get_template('Country_view.html')
    context = {
        'categories': Category.objects.all().filter(name=load_country)
    }

    return HttpResponse(template.render(context, request))


#Access each itam via URL localhost/item/<id>
def item(request, item_Id):
    try:
        itm = Item.objects.get(id=item_Id)
    except Item.DoesNotExist:
        itm = None

    template = loader.get_template('item.html')
    context = {
        'item': itm

    }

    return HttpResponse(template.render(context, request))




from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Item

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Item( name=request.POST['name'],  description=request.POST['description'],    image=request.FILES['image'],  category_id=request.POST['category'])

            instance.save()
            return HttpResponseRedirect('item/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_via_form.html', {'form': form})




















#upload function with picture only but without the connection to the class item.
# function can be called with /upload and the data is stored in the media folder

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')






