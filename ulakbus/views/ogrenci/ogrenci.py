# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

import random
from collections import OrderedDict

from pyoko import form
from zengine.lib.forms import JsonForm
from zengine.views.crud import CrudView
from ulakbus.services.zato_wrapper import MernisKimlikBilgileriGetir
from ulakbus.services.zato_wrapper import KPSAdresBilgileriGetir
from ulakbus.models.ogrenci import Ogrenci


class KimlikBilgileriForm(JsonForm):
    class Meta:
        include = ['tckn', "ad", "soyad", "cinsiyet", "dogum_tarihi", "dogum_yeri", "uyruk", "medeni_hali", "baba_adi",
                   "ana_adi",
                   "cuzdan_seri", "cuzdan_seri_no", "kayitli_oldugu_il", "kayitli_oldugu_ilce",
                   "kayitli_oldugu_mahalle_koy",
                   "kayitli_oldugu_cilt_no", "kayitli_oldugu_aile_sıra_no", "kayitli_oldugu_sira_no",
                   "kimlik_cuzdani_verildigi_yer",
                   "kimlik_cuzdani_verilis_nedeni", "kimlik_cuzdani_kayit_no",
                   "kimlik_cuzdani_verilis_tarihi"]

    kaydet = form.Button("Kaydet", cmd="save")
    mernis_sorgula = form.Button("Mernis Sorgula", cmd="mernis_sorgula")


class KimlikBilgileri(CrudView):
    class Meta:
        model = "Ogrenci"

    def kimlik_bilgileri(self):
        self.form_out(KimlikBilgileriForm(self.object, current=self.current))

    def mernis_sorgula(self):
        servis = MernisKimlikBilgileriGetir(tckn=self.object.tckn)
        kimlik_bilgisi = servis.zato_request()
        self.object(**kimlik_bilgisi)
        self.object.save()


class IletisimBilgileriForm(JsonForm):
    class Meta:
        include = ["ikamet_il", "ikamet_ilce", "ikamet_adresi", "posta_kodu", "eposta", "tel_no"]

    kaydet = form.Button("Kaydet", cmd="save")
    kps_sorgula = form.Button("KPS Sorgula", cmd="kps_sorgula")


class IletisimBilgileri(CrudView):
    class Meta:
        model = "Ogrenci"

    def iletisim_bilgileri(self):
        self.form_out(IletisimBilgileriForm(self.object, current=self.current))

    def kps_sorgula(self):
        servis = KPSAdresBilgileriGetir(tckn=self.object.tckn)
        iletisim_bilgisi = servis.zato_request()
        self.object(**iletisim_bilgisi)
        self.object.save()


class OncekiEgitimBilgileriForm(JsonForm):
    class Meta:
        include = ["okul_adi", "diploma_notu", "mezuniyet_yili"]

    kaydet = form.Button("Kaydet", cmd="save")


class OncekiEgitimBilgileri(CrudView):
    class Meta:
        model = "OncekiEgitimBilgisi"

    def onceki_egitim_bilgileri(self):
        self.form_out(OncekiEgitimBilgileriForm(self.object, current=self.current))


def ogrenci_bilgileri(current):
    current.output['client_cmd'] = ['show', ]
    ogrenci = Ogrenci.objects.get(user_id=current.user_id)

    kimlik_bilgileri = OrderedDict({
        'Ad Soyad': "%s %s" % (ogrenci.ad, ogrenci.soyad),
        'Cinsiyet': ogrenci.cinsiyet,
        'Kimlik No': ogrenci.tckn,
        'Uyruk': ogrenci.tckn,
        'Doğum Tarihi': '{:%d.%m.%Y}'.format(ogrenci.dogum_tarihi),
        'Doğum Yeri': ogrenci.dogum_yeri,
        'Baba Adı': ogrenci.baba_adi,
        'Anne Adı': ogrenci.ana_adi,
        'Medeni Hali': ogrenci.medeni_hali
    })

    iletisim_bilgileri = {
        'Eposta': ogrenci.e_posta,
        'Telefon': ogrenci.tel_no,
        'Sitem Kullanıcı Adı': current.user.username
    }

    current.output['object'] = [
        {
            "title": "Kimlik Bilgileri",
            "type": "table",
            "fields": kimlik_bilgileri
        },
        {
            "title": "İletişim Bilgileri",
            "type": "table",
            "fields": iletisim_bilgileri
        }
    ]
