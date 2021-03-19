from .models import  *
from  .forms import  ContactFormForm
def main(request):
    form  =ContactFormForm()
    content = {
        'form':form
    }
    return content