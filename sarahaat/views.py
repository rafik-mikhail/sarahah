from django.shortcuts import render
from .models import Sarahaat
from accounts.models import CustomUser
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def sarahah_create_view(self):
    if self.method == 'GET':
        return render(self, 'sarahah_new.html')
    elif self.method == 'POST':
        sarahah = Sarahaat()
        sarahah.secret = self.POST.get('secret')
        usrs = CustomUser.objects
        name = self.POST.get('forwhm')
        usr = usrs.get(username=name)
        sarahah.forwhm = usr
        sarahah.save()
        return HttpResponseRedirect(reverse('sarahah_detail', args=[str(sarahah.id)]))


def sarahah_detail_view(self, pk):
    s = Sarahaat.objects.get(pk=pk)
    return render(self, 'sarahah_detail.html', {'object': s})


def sarahah_list_view(self):
    usr = self.user
    ss = Sarahaat.objects.filter(forwhm=usr)
    return render(self, 'sarahah_list.html', {'object_list': ss})
