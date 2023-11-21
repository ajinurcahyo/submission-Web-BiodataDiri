# from django.shortcuts import render

# from django.db.models import Q
# from .models import Rth
# from .models import Penghijauan
# from .models import Taman
# # Create your views here.

# # ruang terbuka hijau ( Rth )
# def index1(request): 
#     r = request.GET.get('q', '')
#     data = Rth.objects.all()

#     if r:
#         data = data.filter(
#             Q(kecamatan__icontains=r) | 
#             Q(kode_kelurahan__icontains=r) | 
#             Q(kelurahan__icontains=r) | 
#             Q(lokasi_rth__icontains=r) |
#             Q(jenis_rth__icontains=r)
#         )
        
#         try:
#             r = int(r) 
#             data |= Rth.objects.filter(luas_rth=r)
#         except ValueError:
#             pass

#     context = {
#         'rth': data
#     }
#     return render(request, 'dashboard/rth.html', context)

# # Penghijauan
# def index2(request):
#     p = request.GET.get('q', '')
#     data = Penghijauan.objects.all()
#     if p:
#         data = data.filter(
#             Q(kecamatan__icontains=p) | 
#             Q(kode_kelurahan__icontains=p) | 
#             Q(kelurahan__icontains=p) |
#             Q(jenis_pohon__icontains=p) |
#             Q(lokasi_penanaman__icontains=p)
#         )
#         try:
#             p = int(p) 
#             data |= Penghijauan.objects.filter(jumlah_pohon=p)
#         except ValueError:
#             pass
#     context = {
#         'penghijauan': data
#     }
#     return render(request, 'dashboard/penghijauan.html', context)

# # Taman
# def index3(request):
#     t = request.GET.get('q', '')
#     data = Taman.objects.all()
#     if t:
#         data = data.filter(
#             Q(kecamatan__icontains=t) | 
#             Q(kode_kelurahan__icontains=t) |
#             Q(kelurahan__icontains=t) |
#             Q(nama_taman__icontains=t) |
#             Q(lokasi_taman__icontains=t)
#         )
#         try:
#             t = int(t) 
#             data |= Taman.objects.filter(luas_taman=t)
#         except ValueError:
#             pass
#     context = {
#         'taman': data
#     }
#     return render(request, 'dashboard/taman.html', context)

from django.shortcuts import render
from django.db.models import Q
from .models import Rth, Penghijauan, Taman

def search_data(request, model, template_name, fields):
    q = request.GET.get('q', '')
    data = model.objects.all()

    if q:
        filter_query = Q()
        for field in fields:
            filter_query |= Q(**{field + '__icontains': q})

        try:
            q_int = int(q)
            filter_query |= Q(**{fields[0] + '__exact': q_int})
        except ValueError:
            pass

        data = data.filter(filter_query)

    context = {
        'data': data,
        'query': q
    }
    return render(request, template_name, context)

def index1(request):
    fields = ['kecamatan', 'kode_kelurahan', 'kelurahan', 'lokasi_rth', 'jenis_rth', 'luas_rth']
    return search_data(request, Rth, 'dashboard/rth.html', fields)

def index2(request):
    fields = ['kecamatan', 'kode_kelurahan', 'kelurahan', 'jenis_pohon', 'lokasi_penanaman', 'jumlah_pohon']
    return search_data(request, Penghijauan, 'dashboard/penghijauan.html', fields)

def index3(request):
    fields = ['kecamatan', 'kode_kelurahan', 'kelurahan', 'nama_taman', 'lokasi_taman', 'luas_taman']
    return search_data(request, Taman, 'dashboard/taman.html', fields)
