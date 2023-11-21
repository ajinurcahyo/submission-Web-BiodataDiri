from django.db import models

class Rth(models.Model): # data ruang terbuka hijau(rth) kec cicendo th 2020
    kecamatan = models.CharField(max_length=100)
    kode_kelurahan = models.CharField(max_length=100)
    kelurahan = models.CharField(max_length=100)
    lokasi_rth = models.CharField(max_length=100)
    jenis_rth = models.CharField(max_length=100)
    luas_rth = models.IntegerField(db_column='luas_rth(m2)')
    
class Penghijauan(models.Model): # data penghijauan kec bojongloa kidul th 2019
    kecamatan = models.CharField("kecamatan", max_length=100, db_column='Kecamatan')
    kode_kelurahan = models.CharField("kode kelurahan", max_length=100, db_column='Kode Kelurahan')
    kelurahan = models.CharField("kelurahan", max_length=100, db_column='Kelurahan')
    jenis_pohon = models.CharField("jenis pohon", max_length=100, db_column='Jenis Pohon Yang Ditanam')
    lokasi_penanaman = models.CharField("lokasi penanaman", max_length=100, db_column='Lokasi Penanaman (RW)')
    jumlah_pohon = models.IntegerField(db_column='Jumlah Pohon Ditanam')

class Taman(models.Model): # data taman kec mandalajati th 2020
    kecamatan = models.CharField("kecamatan", max_length=100, db_column='Kecamatan')
    kode_kelurahan = models.CharField("kode kelurahan", max_length=100, db_column='Kode Kelurahan')
    kelurahan = models.CharField("kelurahan", max_length=100, db_column='Kelurahan')
    nama_taman = models.CharField("nama taman", max_length=200, db_column='Nama Taman')
    lokasi_taman = models.CharField("lokasi taman", max_length=200, db_column='Lokasi Taman')
    luas_taman = models.IntegerField(db_column='Luas Taman (m2)')
