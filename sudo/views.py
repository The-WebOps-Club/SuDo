from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context import Context, RequestContext

@login_required
def home(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))