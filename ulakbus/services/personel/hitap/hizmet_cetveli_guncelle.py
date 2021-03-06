# -*-  coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP Cetvel Guncelle

Hitap'a personelin Hizmet Cetvel Kayit bilgilerinin güncellemesini yapar.

"""

from ulakbus.services.personel.hitap.hitap_guncelle import HITAPGuncelle


class HizmetCetveliGuncelle(HITAPGuncelle):
    """
    HITAP Guncelleme servisinden kalıtılmış Hizmet Okul Bilgi Güncelleme servisi

    """
    HAS_CHANNEL = True

    def handle(self):
        """Servis çağrıldığında tetiklenen metod.

        Attributes:
            service_name (str): İlgili Hitap sorgu servisinin adı
            service_dict (dict): Request yoluyla gelen kayıtlar,
                    HizmetCetvelUpdate servisinin alanlarıyla eşlenmektedir.
                    Filtreden geçecek tarih alanları listede tutulmaktadır.
        """

        self.service_name = 'HizmetCetvelUpdate'
        self.service_dict = {
            'fields': {
                'kayitNo': self.request.payload.get('kayit_no', ''),
                'baslamaTarihi': self.request.payload.get('baslama_tarihi', ''),
                'bitisTarihi': self.request.payload.get('bitis_tarihi', ''),
                'emekliDerece': self.request.payload.get('emekli_derece', ''),
                'emekliKademe': self.request.payload.get('emekli_kademe', ''),
                'gorev': self.request.payload.get('gorev', ''),
                'unvanKod': self.request.payload.get('unvan_kod', ''),
                'hizmetSinifi': self.request.payload.get('hizmet_sinifi', ''),
                'kazanilmisHakAyligiDerece': self.request.payload.get(
                    'kazanilmis_hak_ayligi_derece', ''),
                'kazanilmisHakAyligiKademe': self.request.payload.get(
                    'kazanilmis_hak_ayligi_kademe', ''),
                'odemeDerece': self.request.payload.get('odeme_derece', ''),
                'odemeKademe': self.request.payload.get('odeme_kademe', ''),
                'emekliEkGosterge': self.request.payload.get('emekli_ekgosterge', ''),
                'kadroDerece': self.request.payload.get('kadro_derece', ''),
                'kazanilmisHakAyligiEkGosterge': self.request.payload.get(
                    'kazanilmis_hak_ayligi_ekgosterge', ''),
                'odemeEkGosterge': self.request.payload.get('odeme_ekgosterge', ''),
                'sebepKod': self.request.payload.get('sebep_kod', ''),
                'tckn': self.request.payload.get('tckn', ''),
                'ucret': self.request.payload.get('ucret', ''),
                'yevmiye': self.request.payload.get('yevmiye', ''),
                'kurumOnayTarihi': self.request.payload.get('kurum_onay_tarihi', '')
            },
            'date_filter': ['baslamaTarihi', 'bitisTarihi', 'kurumOnayTarihi'],
            'required_fields': ['kayitNo', 'emekliDerece', 'emekliKademe', 'gorev', 'unvanKod',
                                'hizmetSinifi', 'kazanilmisHakAyligiDerece',
                                'kazanilmisHakAyligiKademe', 'odemeDerece', 'odemeKademe',
                                'emekliEkGosterge', 'kadroDerece', 'kazanilmisHakAyligiEkGosterge',
                                'odemeEkGosterge', 'sebepKod', 'tckn', 'kurumOnayTarihi']
        }
        super(HizmetCetveliGuncelle, self).handle()
