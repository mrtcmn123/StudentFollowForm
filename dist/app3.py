import sys
from PyQt5 import QtWidgets
import os
from datetime import datetime
import sqlite3
from math import *
import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi = QtWidgets.QLabel("TYT-AYT sınavı için Kalan süre")
        self.sure = QtWidgets.QLabel()

        liste = [self.yazi,self.sure]
        for eleman in liste:
            eleman.setStyleSheet(""" QLabel {
        color: black;              
        font-size: 20px;         
        font-weight: bold;        
        border: 2px solid green;    
        border-radius: 10px;     
        padding: 10px;            
    }
""")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.sure)
        v_box.addStretch()
        self.setLayout(v_box)

        zaman = datetime(2025,6,6,9)
        su_an = datetime.now()
        a_fark = zaman.month - su_an.month
        if a_fark < 0 :
            a_fark = a_fark + 12
        g_fark = zaman.day - su_an.day
        if g_fark<0:
            g_fark = g_fark + 30
        s_fark = zaman.hour - su_an.hour
        if s_fark<0:
            s_fark = s_fark+24
        h_fark =zaman.minute-su_an.minute
        if h_fark < 0:
            h_fark = h_fark + 60

        self.sure.setText(" {} ay , {} gün , {} saat , {} dakika".format(a_fark,g_fark,s_fark,h_fark))



class Tyt_tur(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(500,500)





    def init_ui(self):
        self.yazi = QtWidgets.QLabel("TYT Türkçe Konuları")
        self.sozukte_yapi = QtWidgets.QCheckBox("Sözcükte Yapı")
        self.anlatim_bozukluk = QtWidgets.QCheckBox("Anlatım Bozukluğu")
        self.tamlama = QtWidgets.QCheckBox("Tamlamalar")
        self.ses_bilgisi = QtWidgets.QCheckBox("Ses Bilgisi")
        self.noktalama = QtWidgets.QCheckBox("Noktalama İşaretleri")
        self.yazim_kurallari = QtWidgets.QCheckBox("Yazım Kuralları")
        self.paragraf = QtWidgets.QCheckBox("Paragraf")
        self.fiiller = QtWidgets.QCheckBox("Fiiller")
        self.cumle_cesit = QtWidgets.QCheckBox("Cümle Çeşitleri")
        self.ekler = QtWidgets.QCheckBox("Ekler")
        self.sozukte_anlam = QtWidgets.QCheckBox("Sözcükte Anlam")
        self.sozcuk_tur = QtWidgets.QCheckBox("Sözcük Türleri")
        self.cumlede_anlam = QtWidgets.QCheckBox("Cümlede Anlam")
        self.cumle_oge = QtWidgets.QCheckBox("Cümlenin Ögeleri")
        self.hesapla = QtWidgets.QPushButton("Hesapla")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.genel = QtWidgets.QLabel()
        self.genel.setStyleSheet("""
            QLabel {
                text-align: center; /* Yatayda ortalama */
                background-color: #CBAACB; /* Gri arka plan */
                font-size: 18px; /* Yazı boyutu */
                color: #000000; /* Yazı rengi */
                padding: 5px; /* İç boşluk */
                border-radius: 4px; /* Köşe yuvarlama */
            }
        """)

        self.yazi.setStyleSheet("""
            QLabel {
                text-align: center; /* Yatayda ortalama */
                background-color: #A9A9A9; /* Gri arka plan */
                font-size: 18px; /* Yazı boyutu */
                color: #000000; /* Yazı rengi */
                padding: 5px; /* İç boşluk */
                border-radius: 4px; /* Köşe yuvarlama */
            }
        """)
        a = [self.hesapla,self.kaydet]
        for eleman in a:
            eleman.setStyleSheet("""
            QPushButton {
                text-align: center; /* Yatayda ortalama */
                background-color: #A9A9A9; /* Gri arka plan */
                font-size: 18px; /* Yazı boyutu */
                color: #000000; /* Yazı rengi */
                padding: 5px; /* İç boşluk */
                border-radius: 4px; /* Köşe yuvarlama */
                border: 1px solid #808080; /* Hafif gri çerçeve */
            }
            
            QPushButton:hover {
                background-color: #B0B0B0; /* Hover'da daha açık gri */
                color: #333333; /* Yazı rengi biraz daha koyu */
            }
            
            QPushButton:pressed {
                background-color: #808080; /* Basıldığında daha koyu gri */
                color: #FFFFFF; /* Yazı rengi beyaz */
            }
""")


        liste0 = [self.sozukte_yapi,self.anlatim_bozukluk,self.ses_bilgisi,self.tamlama,self.noktalama,self.yazim_kurallari,self.paragraf,self.cumle_cesit,self.fiiller,self.ekler,
                 self.sozukte_anlam,self.sozcuk_tur,self.cumlede_anlam,self.cumle_oge]
        liste1 = [self.yazi,self.sozukte_yapi, self.anlatim_bozukluk, self.ses_bilgisi, self.tamlama, self.noktalama,
                  self.yazim_kurallari, self.paragraf, self.cumle_cesit, self.fiiller, self.ekler,
                  self.sozukte_anlam, self.sozcuk_tur, self.cumlede_anlam, self.cumle_oge,self.hesapla,self.kaydet,self.genel]

        for eleman in liste0:

            eleman.setStyleSheet( """
        QCheckBox {
            background-color: #d3d3d3; 
            font-size: 14px;
            padding: 5px;
            border-radius: 4px;
        }
        QCheckBox::indicator:checked {
            background-color: #000000; 
            border: 2px solid #2E7D32;
        }
        QCheckBox::indicator:unchecked {
            background-color: white; 
            border: 2px solid #757575;
        }
        """)
        v_box = QtWidgets.QVBoxLayout()
        for eleman in liste1:
            v_box.addWidget(eleman)

        self.setLayout(v_box)

        self.setWindowTitle("Tyt_Turkce")
        
        app_dir = os.path.dirname(os.path.realpath(__file__))


        db_file = os.path.join(app_dir, 'asım.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM tyt")
        data = self.cursor.fetchall()
        liste3 = [self.sozukte_yapi,self.anlatim_bozukluk,self.ses_bilgisi,self.tamlama,self.noktalama,self.yazim_kurallari,self.paragraf,self.cumle_cesit,self.fiiller,self.ekler,
                 self.sozukte_anlam,self.sozcuk_tur,self.cumlede_anlam,self.cumle_oge]
        index = 0
        for id,isim,durum in data:
            if durum == 1:
                liste3[index].setChecked(True)
            else:
                index = index + 1

        self.hesapla.clicked.connect(self.istatistik)
        self.kaydet.clicked.connect(self.kayit)

        self.show()

    def istatistik(self):
        self.yuzde = 0
        liste = [self.sozukte_yapi,self.anlatim_bozukluk,self.ses_bilgisi,self.tamlama,self.noktalama,self.yazim_kurallari,self.paragraf,self.cumle_cesit,self.fiiller,self.ekler,
                 self.sozukte_anlam,self.sozcuk_tur,self.cumlede_anlam,self.cumle_oge]

        for eleman in liste:
            if eleman.isChecked():
                self.yuzde = self.yuzde + 7.142857142857143
        self.yuzde = str(self.yuzde)
        self.genel.setText("Konuların bitme yüzdesi  %{}".format(self.yuzde))

    def kayit(self):
        id = 1
        liste2 = [self.sozukte_yapi,self.anlatim_bozukluk,self.ses_bilgisi,self.tamlama,self.noktalama,self.yazim_kurallari,self.paragraf,self.cumle_cesit,self.fiiller,self.ekler,
                 self.sozukte_anlam,self.sozcuk_tur,self.cumlede_anlam,self.cumle_oge]
        app_dir = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(app_dir, 'asım.db')

        self.con = sqlite3.connect(db_file)
        for eleman in liste2:
             self.cursor.execute("UPDATE Tyt set id = ? ,isim = ? , durum = ? where id = ?",(id,eleman.text(),eleman.isChecked(),id))
             id = id+1
        self.con.commit()
        self.genel.setText("Kaydetme işleminiz başarılı olmuştur..")
        self.con.close()


class Ayt_tur(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(500, 500)
        self.setGeometry(700, 30, 500, 700)

    def init_ui(self):
        self.yazi = QtWidgets.QLabel("AYT EDEBİYAT KONULARI")
        self.anlam_bilgisi = QtWidgets.QCheckBox("Anlam Bilgisi")
        self.dil_bilgisi = QtWidgets.QCheckBox("Dil Bilgisi")
        self.guzel = QtWidgets.QCheckBox("Güzel Sanatlar ve Edebiyat")
        self.metin = QtWidgets.QCheckBox("Metinlerin Sınıflandırılması")
        self.şiir = QtWidgets.QCheckBox("Şiir Bilgisi")
        self.edebi = QtWidgets.QCheckBox("Edebi Sanatlar")
        self.turk = QtWidgets.QCheckBox("Türk Edebiyatı Dönemleri")
        self.islamiyet = QtWidgets.QCheckBox("İslamiyetten Öncesi Türk Edebiyatı")
        self.halk = QtWidgets.QCheckBox("Halk Edebiyatı")
        self.divan = QtWidgets.QCheckBox("Divan Edebiyatı")
        self.tanzimat = QtWidgets.QCheckBox("Tanzimat Edebiyatı")
        self.servet = QtWidgets.QCheckBox("Servet-i Fünun Edebiyatı")
        self.fecr = QtWidgets.QCheckBox("Fecr-i Ati Edebiyatı")
        self.milli = QtWidgets.QCheckBox("Milli Edebiyat")
        self.cumhuriyet = QtWidgets.QCheckBox("Cumhuriyet Dönemi Edebiyatı")
        self.akim = QtWidgets.QCheckBox("Edebi Akımlar")
        self.dunya = QtWidgets.QCheckBox("Dünya Edebiyatı")
        self.hesapla = QtWidgets.QPushButton("HESAPLA")
        self.kaydet = QtWidgets.QPushButton("KAYDET")
        self.genel = QtWidgets.QLabel()
        liste0 = [ self.anlam_bilgisi, self.dil_bilgisi, self.guzel, self.metin,
                  self.şiir, self.edebi, self.turk, self.islamiyet, self.halk,
                  self.divan, self.tanzimat, self.servet, self.fecr,self.milli,self.cumhuriyet,self.akim,self.dunya]

        liste1 = [self.yazi, self.anlam_bilgisi, self.dil_bilgisi, self.guzel, self.metin,
                  self.şiir, self.edebi, self.turk, self.islamiyet, self.halk,
                  self.divan, self.tanzimat, self.servet, self.fecr,self.milli,self.cumhuriyet,self.akim,self.dunya,self.hesapla,self.kaydet,self.genel]

        for eleman in liste0:
            eleman.setStyleSheet("""
                QCheckBox {
                    background-color: #d3d3d3; 
                    font-size: 14px;
                    padding: 5px;
                    border-radius: 4px;
                }
                QCheckBox::indicator:checked {
                    background-color: #000000; /* Siyah kutu işaretli */
                    border: 2px solid #2E7D32;
                }
                QCheckBox::indicator:unchecked {
                    background-color: white; /* Beyaz kutu işaretsiz */
                    border: 2px solid #757575;
                }
                """)

        a = [self.hesapla, self.kaydet]
        for eleman in a:
            eleman.setStyleSheet("""
                    QPushButton {
                        text-align: center; /* Yatayda ortalama */
                        background-color: #A9A9A9; /* Gri arka plan */
                        font-size: 18px; /* Yazı boyutu */
                        color: #000000; /* Yazı rengi */
                        padding: 5px; /* İç boşluk */
                        border-radius: 4px; /* Köşe yuvarlama */
                        border: 1px solid #808080; /* Hafif gri çerçeve */
                    }

                    QPushButton:hover {
                        background-color: #B0B0B0; /* Hover'da daha açık gri */
                        color: #333333; /* Yazı rengi biraz daha koyu */
                    }

                    QPushButton:pressed {
                        background-color: #808080; /* Basıldığında daha koyu gri */
                        color: #FFFFFF; /* Yazı rengi beyaz */
                    }
        """)

        v_box = QtWidgets.QVBoxLayout()
        for eleman in liste1:
            v_box.addWidget(eleman)


        self.setLayout(v_box)
        self.genel.setStyleSheet("""
                    QLabel {
                        text-align: center; 
                        background-color: #CBAACB; 
                        font-size: 18px; 
                        color: #000000; 
                        padding: 5px; 
                        border-radius: 4px; 
                    }
                """)

        self.yazi.setStyleSheet("""
                    QLabel {
                        text-align: center;
                        background-color: #A9A9A9; 
                        font-size: 18px; 
                        color: #000000; 
                        padding: 5px; 
                        border-radius: 4px; 
                    }
                """)

        self.setWindowTitle("Ayt Edebiyat")
        
        app_dir = os.path.dirname(os.path.realpath(__file__))


        db_file = os.path.join(app_dir, 'turkce_ayt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM ayt")
        data = self.cursor.fetchall()
        liste3 = [self.anlam_bilgisi, self.dil_bilgisi, self.guzel, self.metin,
                  self.şiir, self.edebi, self.turk, self.islamiyet, self.halk,
                  self.divan, self.tanzimat, self.servet, self.fecr, self.milli, self.cumhuriyet, self.akim, self.dunya]

        index = 0
        for id, isim, durum in data:
            if durum == 1:
                liste3[index].setChecked(True)
            else:
                index = index + 1

        self.kaydet.clicked.connect(self.click)
        self.hesapla.clicked.connect(self.hesap)

        self.show()


    def click(self):
        id =1
        liste3 = [self.anlam_bilgisi, self.dil_bilgisi, self.guzel, self.metin,
                  self.şiir, self.edebi, self.turk, self.islamiyet, self.halk,
                  self.divan, self.tanzimat, self.servet, self.fecr, self.milli, self.cumhuriyet, self.akim, self.dunya]
        app_dir = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(app_dir, 'turkce_ayt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        for eleman in liste3:
            self.cursor.execute("UPDATE ayt set id = ?, isim = ? , durum = ? where id = ?",(id, eleman.text(), eleman.isChecked(),id))
            self.con.commit()
            self.genel.setText("Kaydetme işleminiz başarılı olmuştur..")
            id = id + 1
        self.con.close()

    def hesap(self):
        self.yuzde = 0
        liste3 = [self.anlam_bilgisi, self.dil_bilgisi, self.guzel, self.metin,
                  self.şiir, self.edebi, self.turk, self.islamiyet, self.halk,
                  self.divan, self.tanzimat, self.servet, self.fecr, self.milli, self.cumhuriyet, self.akim,
                  self.dunya]

        for eleman in liste3:
            if eleman.isChecked():
                self.yuzde = self.yuzde + 5.882352941176480
        self.yuzde = str(self.yuzde)
        self.genel.setText("Konuların bitme yüzdesi  %{}".format(self.yuzde))



class Tyt_mat(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 700)
        self.setGeometry(700, 30, 500, 700)
        self.setWindowTitle("Tyt_Matematik")
        self.init_ui()

    def init_ui(self):
        self.yazi = QtWidgets.QLabel("Tyt Matematik Konuları")
        self.konu1 = QtWidgets.QCheckBox("Temel kavramlar")
        self.konu2 = QtWidgets.QCheckBox("Sayı Basamakları")
        self.konu3 = QtWidgets.QCheckBox("Bölme ve Bölünebilme")
        self.konu4 = QtWidgets.QCheckBox("EBOK VE EKOK")
        self.konu5 = QtWidgets.QCheckBox("Rasyonel Sayılar")
        self.konu6 = QtWidgets.QCheckBox("Basit Eşitsizlikler")
        self.konu7 = QtWidgets.QCheckBox("Multak Değer")
        self.konu8 = QtWidgets.QCheckBox("Mutlak Değer")
        self.konu9 = QtWidgets.QCheckBox("Üstlü Sayılar")
        self.konu10 = QtWidgets.QCheckBox("Köklü Sayılar")
        self.konu11 = QtWidgets.QCheckBox("Çarpanlara Ayırma")
        self.konu12 = QtWidgets.QCheckBox("Oran Orantı")
        self.konu13 = QtWidgets.QCheckBox("Denklem Çözme")
        self.konu14 = QtWidgets.QCheckBox("Sayı Problemleri")
        self.konu15 = QtWidgets.QCheckBox("Kesir Problemler")
        self.konu16 = QtWidgets.QCheckBox("Yaş Problemleri")
        self.konu17 = QtWidgets.QCheckBox("Hareket-Hız Problemleri")
        self.konu18 = QtWidgets.QCheckBox("İşçi Emek Problemleri")
        self.konu19 = QtWidgets.QCheckBox("Yüzde Problemleri")
        self.konu20 = QtWidgets.QCheckBox("Kar ve Zarar Problemleri")
        self.konu21 = QtWidgets.QCheckBox("Karışım Problemleri")
        self.konu22 = QtWidgets.QCheckBox("Grafik Problemleri")
        self.konu23 = QtWidgets.QCheckBox("Kümeler")
        self.konu24 = QtWidgets.QCheckBox("Mantık")
        self.konu25 = QtWidgets.QCheckBox("Fonksiyonlar")
        self.konu26 = QtWidgets.QCheckBox("Polinomlar")
        self.konu27 = QtWidgets.QCheckBox("2. Dereceden Denklemler")
        self.konu28 = QtWidgets.QCheckBox("Permütasyon")
        self.konu29 = QtWidgets.QCheckBox("Kombinasyon")
        self.konu30 = QtWidgets.QCheckBox("Olasılık")
        self.konu31 = QtWidgets.QCheckBox("Veri-İstatistik")
        self.hesapla = QtWidgets.QPushButton("HESAPLA")
        self.kaydet = QtWidgets.QPushButton("KAYDET")
        self.genel = QtWidgets.QLabel()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.hesapla)
        h_box.addSpacing(10)
        h_box.addWidget(self.kaydet)
        h_box.addSpacing(10)
        h_box.addWidget(self.genel)
        liste1 = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7, self.konu8,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box)
        for eleman in liste1:
            v_box.addWidget(eleman)



        self.setLayout(v_box)

        a = [self.genel,self.hesapla,self.kaydet]
        for eleman in a:
            eleman.setStyleSheet("""
                            QLabel {
                                text-align: center; /* Yatayda ortalama */
                                background-color: #CBAACB; /* Gri arka plan */
                                font-size: 18px; /* Yazı boyutu */
                                color: #000000; /* Yazı rengi */
                                padding: 5px; /* İç boşluk */
                                border-radius: 4px; /* Köşe yuvarlama */
                            }
                            QPushButton {
                                text-align: center; /* Yatayda ortalama */
                                background-color: #A9A9A9; /* Gri arka plan */
                                font-size: 18px; /* Yazı boyutu */
                                color: #000000; /* Yazı rengi */
                                padding: 5px; /* İç boşluk */
                                border-radius: 4px; /* Köşe yuvarlama */
                                border: 1px solid #808080; /* Hafif gri çerçeve */
                            }
                            
                            QPushButton:hover {
                                background-color: #B0B0B0; /* Hover'da daha açık gri */
                                color: #333333; /* Yazı rengi biraz daha koyu */
                            }
                            
                            QPushButton:pressed {
                                background-color: #808080; /* Basıldığında daha koyu gri */
                                color: #FFFFFF; /* Yazı rengi beyaz */
                            }

                        """)

        self.yazi.setStyleSheet("""
                            QLabel {
                                text-align: center; /* Yatayda ortalama */
                                background-color: #A9A9A9; /* Gri arka plan */
                                font-size: 18px; /* Yazı boyutu */
                                color: #000000; /* Yazı rengi */
                                padding: 5px; /* İç boşluk */
                                border-radius: 4px; /* Köşe yuvarlama */
                            }
                        """)

        for eleman in liste1:
            eleman.setStyleSheet("""
                 QCheckBox {
                     background-color: #d3d3d3; 
                     font-size: 14px;
                     padding: 0px;
                     border-radius: 0px;
                 }
                 QCheckBox::indicator:checked {
                     background-color: #000000; /* Siyah kutu işaretli */
                     border: 1px solid #2E7D32;
                 }
                 QCheckBox::indicator:unchecked {
                     background-color: white; /* Beyaz kutu işaretsiz */
                     border: 1px solid #757575;
                 }
                 """)
            
        app_dir = os.path.dirname(os.path.realpath(__file__))


        db_file = os.path.join(app_dir, 'mat_tyt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM mat_tyt")
        data = self.cursor.fetchall()
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7, self.konu8,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]

        index = 0
        for id, isim, durum in data:
            if durum == 1:
                liste[index].setChecked(True)
            else:
                index = index + 1

        self.kaydet.clicked.connect(self.click2)
        self.hesapla.clicked.connect(self.hesap2)


        self.show()

    def click2(self):
        id = 1
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7, self.konu8,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]
        app_dir = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(app_dir, 'mat_tyt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        for eleman in liste:
            self.cursor.execute("UPDATE mat_tyt set id = ?, isim = ? , durum = ? where id = ?",
                                (id, eleman.text(), eleman.isChecked(), id))
            self.con.commit()
            self.genel.setText("Kaydetme işleminiz başarılı olmuştur..")
            id = id + 1
        self.con.close()

    def hesap2(self):
        self.yuzde = 0
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7, self.konu8,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]

        for eleman in liste:
            if eleman.isChecked():
                self.yuzde = self.yuzde + 3.226
        self.yuzde = str(self.yuzde)
        self.genel.setText("Konuların bitme yüzdesi  %{}".format(self.yuzde))


class Ayt_mat(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setGeometry(750,20,500,0)
        self.setWindowTitle("AYT Matematik")
        self.init_ui()



    def init_ui(self):
        self.yazi = QtWidgets.QLabel("AYT Matematik Konuları")
        self.konu1 = QtWidgets.QCheckBox("Temel kavramlar")
        self.konu2 = QtWidgets.QCheckBox("Sayı Basamakları")
        self.konu3 = QtWidgets.QCheckBox("Bölme ve Bölünebilme")
        self.konu4 = QtWidgets.QCheckBox("EBOK VE EKOK")
        self.konu5 = QtWidgets.QCheckBox("Rasyonel Sayılar")
        self.konu6 = QtWidgets.QCheckBox("Basit Eşitsizlikler")
        self.konu7 = QtWidgets.QCheckBox("Multak Değer")
        self.konu9 = QtWidgets.QCheckBox("Üstlü Sayılar")
        self.konu10 = QtWidgets.QCheckBox("Köklü Sayılar")
        self.konu11 = QtWidgets.QCheckBox("Çarpanlara Ayırma")
        self.konu12 = QtWidgets.QCheckBox("Oran Orantı")
        self.konu13 = QtWidgets.QCheckBox("Denklem Çözme")
        self.konu14 = QtWidgets.QCheckBox("Problemler")
        self.konu15 = QtWidgets.QCheckBox("Kümeler")
        self.konu16 = QtWidgets.QCheckBox("Kartezyen Çarpım")
        self.konu17 = QtWidgets.QCheckBox("Mantık")
        self.konu18 = QtWidgets.QCheckBox("Fonksiyonlar")
        self.konu19 = QtWidgets.QCheckBox("Polinomlar")
        self.konu20 = QtWidgets.QCheckBox("İkinci Derece Denklemler")
        self.konu21 = QtWidgets.QCheckBox("Permütasyon")
        self.konu22 = QtWidgets.QCheckBox("Kombinasyon")
        self.konu23 = QtWidgets.QCheckBox("Binom ve Olasılık")
        self.konu24 = QtWidgets.QCheckBox("İstatistik")
        self.konu25 = QtWidgets.QCheckBox("Karmaşık Sayılar")
        self.konu26 = QtWidgets.QCheckBox("İkinci Derece Eşitsizlikler")
        self.konu27 = QtWidgets.QCheckBox("Parabol")
        self.konu28 = QtWidgets.QCheckBox("Trigonometri")
        self.konu29 = QtWidgets.QCheckBox("Logaritma")
        self.konu30 = QtWidgets.QCheckBox("Limit")
        self.konu31 = QtWidgets.QCheckBox("Türev")
        self.konu31 = QtWidgets.QCheckBox("İntegral")
        self.hesapla = QtWidgets.QPushButton("HESAPLA")
        self.kaydet = QtWidgets.QPushButton("KAYDET")
        self.genel = QtWidgets.QLabel()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.konu1)
        v_box.addWidget(self.konu2)
        v_box.addWidget(self.konu3)
        v_box.addWidget(self.konu4)
        v_box.addWidget(self.konu5)
        v_box.addWidget(self.konu6)
        v_box.addWidget(self.konu7)
        v_box.addWidget(self.konu9)
        v_box.addWidget(self.konu10)
        v_box.addWidget(self.konu11)
        v_box.addWidget(self.konu12)
        v_box.addWidget(self.konu13)
        v_box.addWidget(self.konu14)
        v_box.addWidget(self.konu15)
        v_box.addWidget(self.konu16)
        v_box.addWidget(self.konu17)
        v_box.addWidget(self.konu18)
        v_box.addWidget(self.konu19)
        v_box.addWidget(self.konu20)
        v_box.addWidget(self.konu21)
        v_box.addWidget(self.konu22)
        v_box.addWidget(self.konu23)
        v_box.addWidget(self.konu24)
        v_box.addWidget(self.konu25)
        v_box.addWidget(self.konu26)
        v_box.addWidget(self.konu27)
        v_box.addWidget(self.konu28)
        v_box.addWidget(self.konu29)
        v_box.addWidget(self.konu30)
        v_box.addWidget(self.konu31)
        v_box.addWidget(self.hesapla)
        v_box.addWidget(self.kaydet)
        v_box.addWidget(self.genel)
        self.setLayout(v_box)

        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]

        a = [self.hesapla, self.kaydet]
        for eleman in a:
            eleman.setStyleSheet("""
                    QPushButton {
                        text-align: center; /* Yatayda ortalama */
                        background-color: #A9A9A9; /* Gri arka plan */
                        font-size: 18px; /* Yazı boyutu */
                        color: #000000; /* Yazı rengi */
                        padding: 5px; /* İç boşluk */
                        border-radius: 4px; /* Köşe yuvarlama */
                        border: 1px solid #808080; /* Hafif gri çerçeve */
                    }

                    QPushButton:hover {
                        background-color: #B0B0B0; /* Hover'da daha açık gri */
                        color: #333333; /* Yazı rengi biraz daha koyu */
                    }

                    QPushButton:pressed {
                        background-color: #808080; /* Basıldığında daha koyu gri */
                        color: #FFFFFF; /* Yazı rengi beyaz */
                    }
        """)

        self.genel.setStyleSheet("""
                                    QLabel {
                                        text-align: center; /* Yatayda ortalama */
                                        background-color: #CBAACB; /* Gri arka plan */
                                        font-size: 18px; /* Yazı boyutu */
                                        color: #000000; /* Yazı rengi */
                                        padding: 5px; /* İç boşluk */
                                        border-radius: 4px; /* Köşe yuvarlama */
                                    }
                                """)

        self.yazi.setStyleSheet("""
                                    QLabel {
                                        text-align: center; /* Yatayda ortalama */
                                        background-color: #A9A9A9; /* Gri arka plan */
                                        font-size: 18px; /* Yazı boyutu */
                                        color: #000000; /* Yazı rengi */
                                        padding: 5px; /* İç boşluk */
                                        border-radius: 4px; /* Köşe yuvarlama */
                                    }
                                """)

        for eleman in liste:
            eleman.setStyleSheet("""
                         QCheckBox {
                             background-color: #d3d3d3; 
                             font-size: 14px;
                             padding: 0px;
                             border-radius: 0px;
                         }
                         QCheckBox::indicator:checked {
                             background-color: #000000; /* Siyah kutu işaretli */
                             border: 1px solid #2E7D32;
                         }
                         QCheckBox::indicator:unchecked {
                             background-color: white; /* Beyaz kutu işaretsiz */
                             border: 1px solid #757575;
                         }
                         """)
            
        app_dir = os.path.dirname(os.path.realpath(__file__))


        db_file = os.path.join(app_dir,'mat_ayt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM mat_ayt")
        data = self.cursor.fetchall()
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]

        index = 0
        for id, isim, durum in data:
            if durum == 1:
                liste[index].setChecked(True)
            else:
                index = index + 1

        self.kaydet.clicked.connect(self.click2)
        self.hesapla.clicked.connect(self.hesap2)



        self.show()

    def hesap2(self):
        self.yuzde = 0
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]

        for eleman in liste:
            if eleman.isChecked():
                self.yuzde = self.yuzde + 3.333
        self.yuzde = str(self.yuzde)
        self.genel.setText("Konuların bitme yüzdesi  %{}".format(self.yuzde))

    def click2(self):
        id = 1
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29, self.konu30,
                 self.konu31]
        app_dir = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(app_dir, 'mat_ayt.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        for eleman in liste:
            self.cursor.execute("UPDATE mat_ayt set id = ?, isim = ? , durum = ? where id = ?",
                                (id, eleman.text(), eleman.isChecked(), id))
            self.con.commit()
            self.genel.setText("Kaydetme işleminiz başarılı olmuştur..")
            id = id + 1
        self.con.close()


class Geometri(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setGeometry(750, 20, 500, 0)
        self.setWindowTitle("AYT Geometri")
        self.init_ui()

    def init_ui(self):
        self.yazi = QtWidgets.QLabel("AYT Geometri Konuları")
        self.konu1 = QtWidgets.QCheckBox("Doğruda Açılar")
        self.konu2 = QtWidgets.QCheckBox("Üçgende Açılar")
        self.konu3 = QtWidgets.QCheckBox("Dik Üçgen")
        self.konu4 = QtWidgets.QCheckBox("İkizkenar Üçgen")
        self.konu5 = QtWidgets.QCheckBox("Eşkenar Üçgen")
        self.konu6 = QtWidgets.QCheckBox("Açıortay")
        self.konu7 = QtWidgets.QCheckBox("KenarOrtay")
        self.konu9 = QtWidgets.QCheckBox("Üçgende Alan")
        self.konu10 = QtWidgets.QCheckBox("Üçgende Benzerlik")
        self.konu11 = QtWidgets.QCheckBox("Açı Kenar Bağlantıları")
        self.konu12 = QtWidgets.QCheckBox("Çokgenler")
        self.konu13 = QtWidgets.QCheckBox("Deltoid")
        self.konu14 = QtWidgets.QCheckBox("Paralelkenar")
        self.konu15 = QtWidgets.QCheckBox("Eşkenar Dörtgen")
        self.konu16 = QtWidgets.QCheckBox("Dikdörtgen")
        self.konu17 = QtWidgets.QCheckBox("Kare")
        self.konu18 = QtWidgets.QCheckBox("İkizkenar")
        self.konu19 = QtWidgets.QCheckBox("Yamuk")
        self.konu20 = QtWidgets.QCheckBox("Noktanın Analitiği")
        self.konu21 = QtWidgets.QCheckBox("Doğrunun Analitiği")
        self.konu22 = QtWidgets.QCheckBox("Dönüşüm Geometrisi")
        self.konu23 = QtWidgets.QCheckBox("Dikdörtgen Prizması")
        self.konu24 = QtWidgets.QCheckBox("Küp")
        self.konu25 = QtWidgets.QCheckBox("Silindir")
        self.konu26 = QtWidgets.QCheckBox("Piramit")
        self.konu27 = QtWidgets.QCheckBox("Koni")
        self.konu28 = QtWidgets.QCheckBox("Küre")
        self.konu29 = QtWidgets.QCheckBox("Çemberin Analitiiği")
        self.hesapla = QtWidgets.QPushButton("HESAPLA")
        self.kaydet = QtWidgets.QPushButton("KAYDET")
        self.genel = QtWidgets.QLabel()

        liste1 = [self.yazi,self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                  self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29,self.hesapla,self.kaydet,self.genel]

        v_box = QtWidgets.QVBoxLayout()
        for eleman in liste1:
            v_box.addWidget(eleman)

        self.setLayout(v_box)

        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29]

        self.genel.setStyleSheet("""
                                           QLabel {
                                               text-align: center; /* Yatayda ortalama */
                                               background-color: #CBAACB; /* Gri arka plan */
                                               font-size: 18px; /* Yazı boyutu */
                                               color: #000000; /* Yazı rengi */
                                               padding: 5px; /* İç boşluk */
                                               border-radius: 4px; /* Köşe yuvarlama */
                                           }
                                       """)

        self.yazi.setStyleSheet("""
                                           QLabel {
                                               text-align: center; /* Yatayda ortalama */
                                               background-color: #A9A9A9; /* Gri arka plan */
                                               font-size: 18px; /* Yazı boyutu */
                                               color: #000000; /* Yazı rengi */
                                               padding: 5px; /* İç boşluk */
                                               border-radius: 4px; /* Köşe yuvarlama */
                                           }
                                       """)

        for eleman in liste:
            eleman.setStyleSheet("""
                                QCheckBox {
                                    background-color: #d3d3d3; 
                                    font-size: 14px;
                                    padding: 0px;
                                    border-radius: 0px;
                                }
                                QCheckBox::indicator:checked {
                                    background-color: #000000; /* Siyah kutu işaretli */
                                    border: 1px solid #2E7D32;
                                }
                                QCheckBox::indicator:unchecked {
                                    background-color: white; /* Beyaz kutu işaretsiz */
                                    border: 1px solid #757575;
                                }
                                """)

        a = [self.hesapla, self.kaydet]
        for eleman in a:
            eleman.setStyleSheet("""
                    QPushButton {
                        text-align: center; /* Yatayda ortalama */
                        background-color: #A9A9A9; /* Gri arka plan */
                        font-size: 18px; /* Yazı boyutu */
                        color: #000000; /* Yazı rengi */
                        padding: 5px; /* İç boşluk */
                        border-radius: 4px; /* Köşe yuvarlama */
                        border: 1px solid #808080; /* Hafif gri çerçeve */
                    }

                    QPushButton:hover {
                        background-color: #B0B0B0; /* Hover'da daha açık gri */
                        color: #333333; /* Yazı rengi biraz daha koyu */
                    }

                    QPushButton:pressed {
                        background-color: #808080; /* Basıldığında daha koyu gri */
                        color: #FFFFFF; /* Yazı rengi beyaz */
                    }
        """)
        app_dir = os.path.dirname(os.path.realpath(__file__))


        db_file = os.path.join(app_dir, 'geometri.db')


        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM geometri")
        data = self.cursor.fetchall()
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29]

        index = 0
        for id, isim, durum in data:
            if durum == 1:
                liste[index].setChecked(True)
            else:
                index = index + 1

        self.kaydet.clicked.connect(self.click2)
        self.hesapla.clicked.connect(self.hesap2)

        self.show()

    def hesap2(self):
        self.yuzde = 0
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29]

        for eleman in liste:
            if eleman.isChecked():
                self.yuzde = self.yuzde + 3.571428571428570
        self.yuzde = str(self.yuzde)
        self.genel.setText("Konuların bitme yüzdesi  %{}".format(self.yuzde))

    def click2(self):
        id = 1
        liste = [self.konu1, self.konu2, self.konu3, self.konu4, self.konu5, self.konu6, self.konu7,
                 self.konu9, self.konu10, self.konu11, self.konu12,
                 self.konu13, self.konu14, self.konu15, self.konu16, self.konu17, self.konu18, self.konu19, self.konu20,
                 self.konu21, self.konu22, self.konu23,
                 self.konu23, self.konu24, self.konu25, self.konu26, self.konu27, self.konu28, self.konu29]
        app_dir = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(app_dir, 'geometri.db')

        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()
        for eleman in liste:
            self.cursor.execute("UPDATE geometri set id = ?, isim = ? , durum = ? where id = ?",
                                (id, eleman.text(), eleman.isChecked(), id))
            self.con.commit()
            self.genel.setText("Kaydetme işleminiz başarılı olmuştur..")
            id = id + 1
        self.con.close()


class Deneme_sonuc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Deneme Sonuçları")


    def init_ui(self):
        self.yazi = QtWidgets.QLabel("Deneme Sonuçları")
        self.yazi.setStyleSheet(""" QLabel {
                color: black;              
                font-size: 24px;          
                font-weight: bold;        
                border: 2px solid blue;    
                border-radius: 10px;      
                padding: 10px;            
            }
        """)
        self.setStyleSheet("background-color: #ced4da")
        self.tyt = QtWidgets.QLabel("TYT")
        self.ayt = QtWidgets.QLabel("AYT")
        tyt_ayt = [self.tyt,self.ayt]
        for eleman in tyt_ayt:
            eleman.setStyleSheet(""" QLabel {
                        color: black;              
                        font-size: 18px;        
                        font-weight: bold;        
                        border: 2px solid blue;    
                        border-radius: 10px;     
                        padding: 10px;            
                    }
                """)

        self.dogru = QtWidgets.QLabel("Doğru")
        self.yanlıs = QtWidgets.QLabel("Yanlış")
        self.net = QtWidgets.QLabel("Net")
        self.dogru2 = QtWidgets.QLabel("Doğru")
        self.yanlıs2 = QtWidgets.QLabel("Yanlış")
        self.net2 = QtWidgets.QLabel("Net ")
        self.turkce = QtWidgets.QLabel("Türkçe")
        self.d1 = QtWidgets.QLineEdit()
        self.y1 = QtWidgets.QLineEdit()
        self.n1 = QtWidgets.QLineEdit()
        self.edebiyat = QtWidgets.QLabel("Edebiyat")
        self.d10 = QtWidgets.QLineEdit()
        self.y10 = QtWidgets.QLineEdit()
        self.n10 = QtWidgets.QLineEdit()
        self.matematik = QtWidgets.QLabel("Matematik")
        self.d2 = QtWidgets.QLineEdit()
        self.y2 = QtWidgets.QLineEdit()
        self.n2 = QtWidgets.QLineEdit()
        self.cografya2 = QtWidgets.QLabel("Coğrafya2")
        self.d11 = QtWidgets.QLineEdit()
        self.y11 = QtWidgets.QLineEdit()
        self.n11 = QtWidgets.QLineEdit()
        self.tarih2 = QtWidgets.QLabel("Tarih2")
        self.d12 = QtWidgets.QLineEdit()
        self.y12 = QtWidgets.QLineEdit()
        self.n12 = QtWidgets.QLineEdit()
        self.tarih = QtWidgets.QLabel("Tarih")
        self.d6 = QtWidgets.QLineEdit()
        self.y6 = QtWidgets.QLineEdit()
        self.n6 = QtWidgets.QLineEdit()
        self.cografya = QtWidgets.QLabel("Coğrafya")
        self.d7 = QtWidgets.QLineEdit()
        self.y7 = QtWidgets.QLineEdit()
        self.n7 = QtWidgets.QLineEdit()
        self.fizik2 = QtWidgets.QLabel("Fizik2")
        self.d16 = QtWidgets.QLineEdit()
        self.y16 = QtWidgets.QLineEdit()
        self.n16 = QtWidgets.QLineEdit()
        self.din = QtWidgets.QLabel("Din ")
        self.d8 = QtWidgets.QLineEdit()
        self.y8 = QtWidgets.QLineEdit()
        self.n8 = QtWidgets.QLineEdit()
        self.kimya2 = QtWidgets.QLabel("Kimya2")
        self.d17 = QtWidgets.QLineEdit()
        self.y17 = QtWidgets.QLineEdit()
        self.n17 = QtWidgets.QLineEdit()
        self.felsefe = QtWidgets.QLabel("Felsefe")
        self.d9 = QtWidgets.QLineEdit()
        self.y9 = QtWidgets.QLineEdit()
        self.n9 = QtWidgets.QLineEdit()
        self.biyoloji2 = QtWidgets.QLabel("Biyoloji2")
        self.d18 = QtWidgets.QLineEdit()
        self.y18 = QtWidgets.QLineEdit()
        self.n18 = QtWidgets.QLineEdit()
        self.fizik = QtWidgets.QLabel("Fizik")
        self.d3 = QtWidgets.QLineEdit()
        self.y3 = QtWidgets.QLineEdit()
        self.n3 = QtWidgets.QLineEdit()
        self.matematik2 = QtWidgets.QLabel("Matematik2")
        self.d13 = QtWidgets.QLineEdit()
        self.y13 = QtWidgets.QLineEdit()
        self.n13 = QtWidgets.QLineEdit()
        self.kimya = QtWidgets.QLabel("Kimya")
        self.d4 = QtWidgets.QLineEdit()
        self.y4 = QtWidgets.QLineEdit()
        self.n4 = QtWidgets.QLineEdit()
        self.geometri = QtWidgets.QLabel("Geometri")
        self.d14 = QtWidgets.QLineEdit()
        self.y14 = QtWidgets.QLineEdit()
        self.n14 = QtWidgets.QLineEdit()
        self.biyoloji = QtWidgets.QLabel("Biyoloji")
        self.d5 = QtWidgets.QLineEdit()
        self.y5 = QtWidgets.QLineEdit()
        self.n5 = QtWidgets.QLineEdit()
        self.hesapla = QtWidgets.QPushButton("HESAPLA")
        self.gonder = QtWidgets.QPushButton("GÖNDER")
        self.tyt_sonuc = QtWidgets.QLabel()
        self.ayt_sonuc = QtWidgets.QLabel()
        self.ortalama = QtWidgets.QLabel("Ortalama : ")
        self.okul = QtWidgets.QLineEdit("0")

        line_edits = [
            self.d1, self.y1, self.n1, self.d10, self.y10, self.n10,
            self.d2, self.y2, self.n2, self.d11, self.y11, self.n11,
            self.d12, self.y12, self.n12, self.d6, self.y6, self.n6,
            self.d7, self.y7, self.n7, self.d16, self.y16, self.n16,
            self.d8, self.y8, self.n8, self.d17, self.y17, self.n17,
            self.d9, self.y9, self.n9, self.d18, self.y18, self.n18,
            self.d3, self.y3, self.n3, self.d13, self.y13, self.n13 , self.d4,self.y4,self.n4,self.d14,self.y14,self.n14]
        liste = [self.d5,self.y5,self.n5]
        for eleman in liste:
            eleman.setFixedHeight(34)
            eleman.setFixedWidth(172)
            eleman.setStyleSheet("""
                           QLineEdit {
                               border: 1px solid #ced4da;
                               border-radius: 5px;
                               padding: 5px;
                               font-size: 18px;
                               background-color: #f8f9fa;
                               color: #495057;
                           }
                           QLineEdit:focus {
                               border: 1px solid #80bdff;
                               background-color: #ffffff;
                           }
                       """)


        for line_edit in line_edits:
            line_edit.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #ced4da;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 18px;
                    background-color: #f8f9fa;
                    color: #495057;
                }
                QLineEdit:focus {
                    border: 1px solid #80bdff;
                    background-color: #ffffff;
                }
            """)

        self.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                font-family: Arial, sans-serif;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }""")
        self.tyt_sonuc.setStyleSheet("""
               QLabel {
                   font-size: 24px; 
                   font-weight: bold;
                   color: #2c3e50;
                   background-color: #ecf0f1; 
                   padding: 10px 20px; 
                   border: 2px solid #3498db; 
                   border-radius: 10px; 
                   width: fit-content; 
               }
               QLabel:hover {
                   background-color: #d6eaf8; 
                   transform: scale(1.05); 
               }
           """)

        h10_box = QtWidgets.QHBoxLayout()
        h10_box.addStretch()
        h10_box.addWidget(self.yazi)
        h10_box.addStretch()

        h09_box = QtWidgets.QHBoxLayout()
        h09_box.addStretch(3)
        h09_box.addWidget(self.tyt)
        h09_box.addStretch(4)
        h09_box.addWidget(self.ayt)
        h09_box.addStretch(2)

        h0_box = QtWidgets.QHBoxLayout()
        h0_box.addSpacing(75)
        h0_box.addWidget(self.dogru)
        h0_box.addSpacing(150)
        h0_box.addWidget(self.yanlıs)
        h0_box.addSpacing(200)
        h0_box.addWidget(self.net)
        h0_box.addStretch()
        h0_box.addWidget(self.dogru2)
        h0_box.addStretch()
        h0_box.addWidget(self.yanlıs2)
        h0_box.addStretch()
        h0_box.addWidget(self.net2)

        h1_box = QtWidgets.QHBoxLayout()
        h1_box.addSpacing(23)
        h1_box.addWidget(self.turkce)
        h1_box.addWidget(self.d1)
        h1_box.addWidget(self.y1)
        h1_box.addWidget(self.n1)
        h1_box.addStretch()
        h1_box.addStretch()
        h1_box.addWidget(self.edebiyat)
        h1_box.addWidget(self.d10)
        h1_box.addWidget(self.y10)
        h1_box.addWidget(self.n10)

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.matematik)
        h2_box.addWidget(self.d2)
        h2_box.addWidget(self.y2)
        h2_box.addWidget(self.n2)
        h2_box.addStretch(75)
        h2_box.addWidget(self.cografya2)
        h2_box.addWidget(self.d11)
        h2_box.addWidget(self.y11)
        h2_box.addWidget(self.n11)

        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addSpacing(19)
        h3_box.addWidget(self.tarih)
        h3_box.addStretch(80)
        h3_box.addWidget(self.d6)
        h3_box.addWidget(self.y6)
        h3_box.addWidget(self.n6)
        h3_box.addStretch(100)
        h3_box.addWidget(self.tarih2)
        h3_box.addStretch(40)
        h3_box.addWidget(self.d12)
        h3_box.addWidget(self.y12)
        h3_box.addWidget(self.n12)

        h4_box = QtWidgets.QHBoxLayout()
        h4_box.addSpacing(11)
        h4_box.addWidget(self.cografya)
        h4_box.addWidget(self.d7)
        h4_box.addWidget(self.y7)
        h4_box.addWidget(self.n7)
        h4_box.addStretch()
        h4_box.addWidget(self.fizik2)
        h4_box.addWidget(self.d16)
        h4_box.addWidget(self.y16)
        h4_box.addWidget(self.n16)

        h5_box = QtWidgets.QHBoxLayout()
        h5_box.addSpacing(45)
        h5_box.addWidget(self.din)
        h5_box.addWidget(self.d8)
        h5_box.addWidget(self.y8)
        h5_box.addWidget(self.n8)
        h5_box.addStretch()
        h5_box.addWidget(self.kimya2)
        h5_box.addWidget(self.d17)
        h5_box.addWidget(self.y17)
        h5_box.addWidget(self.n17)

        h6_box = QtWidgets.QHBoxLayout()
        h6_box.addSpacing(26)
        h6_box.addWidget(self.felsefe)
        h6_box.addWidget(self.d9)
        h6_box.addWidget(self.y9)
        h6_box.addWidget(self.n9)
        h6_box.addStretch()
        h6_box.addWidget(self.biyoloji2)
        h6_box.addWidget(self.d18)
        h6_box.addWidget(self.y18)
        h6_box.addWidget(self.n18)


        h7_box = QtWidgets.QHBoxLayout()
        h7_box.addSpacing(43)
        h7_box.addWidget(self.fizik)
        h7_box.addWidget(self.d3)
        h7_box.addWidget(self.y3)
        h7_box.addWidget(self.n3)
        h7_box.addStretch()
        h7_box.addWidget(self.matematik2)
        h7_box.addWidget(self.d13)
        h7_box.addWidget(self.y13)
        h7_box.addWidget(self.n13)

        h8_box = QtWidgets.QHBoxLayout()
        h8_box.addSpacing(30)
        h8_box.addWidget(self.kimya)
        h8_box.addWidget(self.d4)
        h8_box.addWidget(self.y4)
        h8_box.addWidget(self.n4)
        h8_box.addStretch()
        h8_box.addWidget(self.geometri)
        h8_box.addWidget(self.d14)
        h8_box.addWidget(self.y14)
        h8_box.addWidget(self.n14)

        h9_box = QtWidgets.QHBoxLayout()
        h9_box.addSpacing(16)
        h9_box.addWidget(self.biyoloji)
        h9_box.addWidget(self.d5)
        h9_box.addWidget(self.y5)
        h9_box.addWidget(self.n5)
        h9_box.addStretch()
        h9_box.addWidget(self.ortalama)
        h9_box.addWidget(self.okul)




        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h10_box)
        v_box.addLayout(h09_box)
        v_box.addLayout(h0_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h4_box)
        v_box.addLayout(h5_box)
        v_box.addLayout(h6_box)
        v_box.addLayout(h7_box)
        v_box.addLayout(h8_box)
        v_box.addLayout(h9_box)
        v_box.addWidget(self.hesapla)
        v_box.addWidget(self.gonder)
        v_box.addWidget(self.tyt_sonuc)
        v_box.addWidget(self.ayt_sonuc)
        self.setLayout(v_box)

        self.hesapla.clicked.connect(self.cal)
        self.gonder.clicked.connect(self.send)

        self.show()

    def cal(self):
        liste = [
            (self.d1, self.y1, self.n1),(self.d2, self.y2, self.n2), (self.d6, self.y6, self.n6),(self.d7, self.y7, self.n7), (self.d8, self.y8, self.n8),
            (self.d9, self.y9, self.n9),(self.d3, self.y3, self.n3), ( self.d4, self.y4, self.n4),(self.d5,self.y5,self.n5)]
        liste2 = [(self.d10, self.y10, self.n10),(self.d11, self.y11, self.n11),(self.d12, self.y12, self.n12), (self.d16, self.y16, self.n16),
                  (self.d17, self.y17, self.n17), (self.d18, self.y18, self.n18), (self.d14, self.y14,self.n14), (self.d13, self.y13, self.n13)]
        for dogru, yanlis, net in liste:
            try:
                dogru_value = float(dogru.text()) if dogru.text() else 0.0
                yanlis_value = float(yanlis.text()) if yanlis.text() else 0.0

                net.setText(str(dogru_value - (1.25 * yanlis_value)))
            except ValueError:
                net.setText("Geçersiz Girdi")

        for dogru1,yanlis1,net1 in liste2:
            try:
                dogru1_value = float(dogru1.text()) if dogru1.text() else 0.0
                yanlis1_value = float(yanlis1.text()) if yanlis1.text() else 0.0

                net1.setText(str(dogru1_value - (1.25 * yanlis1_value)))
            except ValueError:
                net1.setText("Geçersiz Girdi")

        liste3 = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9]

        liste4 = [ self.n10, self.n11,self.n12, self.n13, self.n14, self.n16, self.n17, self.n18]
        toplam = 0
        for eleman in liste3:
            try:
                value = float(eleman.text())
                toplam += value
            except ValueError:
                toplam += 0
        toplam2 = 0
        for eleman in liste4:
            try:
                value = float(eleman.text())
                toplam2 += value
            except ValueError:
                toplam2 += 0

        puan1 = (float(self.n1.text())*1.32) + (float(self.n2.text())*1.32) + (float(self.n3.text())*1.36) + (float(self.n4.text())*1.36) + (float(self.n5.text())*1.36)
        + (float(self.n6.text())*1.36 )+(float(self.n7.text())*1.36) +(float(self.n8.text())*1.36) + (float(self.n9.text())*1.36)

        puan2 = (float(self.n10.text()) * 3)+ (float(self.n11.text()) * 3.3)+ (float(self.n12.text()) * 2.8) + (float(self.n13.text()) * 3) + (float(self.n14.text()) * 3) +( float(self.n16.text()) * 2.85)
        + (float(self.n17.text()) * 3.07) + (float(self.n18.text()) * 3.07)

        puan3 = float(self.okul.text()) * 0.6

        self.tyt_sonuc.setText("Toplam Tyt netiniz = {},Toplam Ayt netiniz = {} , Toplam Puanınız = {}".format(str(toplam),str(toplam2),str(puan1+puan2+puan3+100)))

    def send(self):
        self.mesaj = MIMEMultipart()

        self.mesaj["From"] ="ozturksedat631@gmail.com"
        self.mesaj["To"] = "cimenmert7@gmail.com"
        self.mesaj["Subject"] = "Öğrenci_ismi,Öğrenci_Soyismi"


        metin = """
                                    TYT   
                                  Türkçe   
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                Matematik 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                   Tarih 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                 Coğrafya 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                     Din 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                  Felsefe 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                    Fizik 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                   Kimya 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                   Biyoloji 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                Ayt Sonuç
                                 Edebiyat  
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                 Coğrafya2   
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                   Tarih2 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                    Fizik2 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                   Kimya2 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                  Biyoloji2 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                 Matematik2 
                Doğru :: {}   Yanlış :: {}   Net :: {}
                                 Geometri 
                Doğru :: {}   Yanlış :: {}   Net :: {}
        
        
        Genel sonuç :: {}
        
        
        """.format(self.d1.text(),self.y1.text(),self.n1.text(),self.d2.text(),self.y2.text(),self.n2.text(), self.d6.text(), self.y6.text(), self.n6.text(),
                   self.d7.text(), self.y7.text(), self.n7.text(),self.d8.text(),self.y8.text(),self.n8.text(), self.d9.text(), self.y9.text(), self.n9.text(),
                   self.d3.text(),self.y3.text(), self.n3.text(),self.d4.text(),self.y4.text(),self.n4.text(),self.d5.text(), self.y5.text(),self.n5.text(),
                   self.d10.text(), self.y10.text(),self.n10.text(),self.d11.text(), self.y11.text(),self.n11.text(),self.d12.text(), self.y12.text(),self.n12.text(),
                   self.d16.text(), self.y16.text(),self.n16.text(),self.d17.text(), self.y17.text(),self.n17.text(),self.d18.text(), self.y18.text(),self.n18.text(),
                   self.d13.text(), self.y13.text(),self.n13.text(),self.d14.text(), self.y4.text(),self.n14.text(),self.tyt_sonuc.text())







        self.mesaj_gövdesi  = MIMEText(metin,"plain")
        self.mesaj.attach(self.mesaj_gövdesi)

        try:
            self.mail = smtplib.SMTP("smtp.gmail.com",587)
            self.mail.ehlo()
            self.mail.starttls()
            self.mail.login("ozturksedat631@gmail.com", "ekwc asow cgmb vujf")
            self.mail.sendmail(self.mesaj["From"], self.mesaj["To"],
            self.mesaj.as_string())
            print("Mail başarıyla gönderildi")
            self.ayt_sonuc.setText("Mailiniz başarıyla gönderilmiştir...")
            self.mail.close()

        except:
            sys.stderr.write("Mesaj gönderimi başarısız oldu")


class Hesap(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()



    def init_ui(self):

        self.yazı1 = QtWidgets.QLineEdit()
        self.yazı2 = QtWidgets.QLineEdit()
        self.buton0 = QtWidgets.QPushButton("0")
        self.buton1 = QtWidgets.QPushButton("1")
        self.buton2 = QtWidgets.QPushButton("2")
        self.buton3 = QtWidgets.QPushButton("3")
        self.buton4 = QtWidgets.QPushButton("4")
        self.buton5 = QtWidgets.QPushButton("5")
        self.buton6 = QtWidgets.QPushButton("6")
        self.buton7 = QtWidgets.QPushButton("7")
        self.buton8 = QtWidgets.QPushButton("8")
        self.buton9 = QtWidgets.QPushButton("9")
        self.buton10 = QtWidgets.QPushButton("+")
        self.buton11 = QtWidgets.QPushButton("-")
        self.buton12 = QtWidgets.QPushButton("*")
        self.buton13 = QtWidgets.QPushButton("/")
        self.buton14 = QtWidgets.QPushButton("=")
        self.buton15 = QtWidgets.QPushButton("C")
        self.buton16 = QtWidgets.QPushButton(",")
        self.buton17 = QtWidgets.QPushButton("üst")
        self.buton18 = QtWidgets.QPushButton("kök")
        self.buton19 = QtWidgets.QPushButton("sin")
        self.buton20 = QtWidgets.QPushButton("cos")
        self.buton21 = QtWidgets.QPushButton("tan")
        self.buton22 = QtWidgets.QPushButton("cot")
        self.buton23 = QtWidgets.QPushButton("factorial")
        self.buton24 = QtWidgets.QPushButton("log10")
        self.buton14.setShortcut('Return')
        self.buton10.setShortcut('+')
        self.buton11.setShortcut('-')
        self.buton12.setShortcut('*')
        self.buton13.setShortcut('/')
        self.buton1.setShortcut('1')
        self.buton2.setShortcut('2')
        self.buton3.setShortcut('3')
        self.buton4.setShortcut('4')
        self.buton5.setShortcut('5')
        self.buton6.setShortcut('6')
        self.buton7.setShortcut('7')
        self.buton8.setShortcut('8')
        self.buton9.setShortcut('9')
        self.buton0.setShortcut('0')

        self.setStyleSheet("""
                    QWidget {
                        background-color: #000000;
                        font-family: Arial, sans-serif;
                        font-size: 18px;
                    }
                    QLineEdit {
                        background-color: #888888;
                        border: 1px solid #ccc;
                        padding: 10px;
                        margin: 5px;
                        font-size: 18px;
                        border-radius: 5px;
                    }
                    QPushButton {
                        background-color: #888888;
                        color: white;
                        border: 1px solid #4CAF50;
                        padding: 15px;
                        font-size: 20px;
                        margin: 5px;
                        border-radius: 5px;
                        min-width: 50px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QPushButton:pressed {
                        background-color: #388e3c;
                    }
                    QVBoxLayout {
                        margin: 20px;
                    }
                    QHBoxLayout {
                        margin: 5px;
                    }
                    #yazı1 {
                        background-color: #f5f5f5;
                        border: 2px solid #888;
                        font-size: 25px;
                        padding: 10px;
                    }
                    #yazı2 {
                        background-color: #fff;
                        border: 2px solid #888;
                        font-size: 25px;
                        padding: 10px;
                    }
                """)







        h4_box = QtWidgets.QHBoxLayout()
        h4_box.addWidget(self.yazı1)
        h4_box.addWidget(self.buton15)
        h4_box.addStretch()
        h4_box.addStretch()
        h4_box.addWidget(self.yazı2)




        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.buton7)
        h_box.addWidget(self.buton8)
        h_box.addWidget(self.buton9)
        h_box.addWidget(self.buton12)

        h1_box = QtWidgets.QHBoxLayout()
        h1_box.addWidget(self.buton4)
        h1_box.addWidget(self.buton5)
        h1_box.addWidget(self.buton6)
        h1_box.addWidget(self.buton11)


        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addWidget(self.buton1)
        h2_box.addWidget(self.buton2)
        h2_box.addWidget(self.buton3)
        h2_box.addWidget(self.buton10)

        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addWidget(self.buton0)
        h3_box.addWidget(self.buton16)
        h3_box.addWidget(self.buton14)
        h3_box.addWidget(self.buton13)

        h5_box = QtWidgets.QHBoxLayout()
        h5_box.addWidget(self.buton17)
        h5_box.addWidget(self.buton18)
        h5_box.addWidget(self.buton19)
        h5_box.addWidget(self.buton20)

        h6_box = QtWidgets.QHBoxLayout()
        h6_box.addWidget(self.buton21)
        h6_box.addWidget(self.buton22)
        h6_box.addWidget(self.buton23)
        h6_box.addWidget(self.buton24)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h4_box)
        v_box.addLayout(h_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h5_box)
        v_box.addLayout(h6_box)

        self.setLayout(v_box)

        self.buton0.clicked.connect(self.click)
        self.buton1.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click)
        self.buton3.clicked.connect(self.click)
        self.buton4.clicked.connect(self.click)
        self.buton5.clicked.connect(self.click)
        self.buton6.clicked.connect(self.click)
        self.buton7.clicked.connect(self.click)
        self.buton8.clicked.connect(self.click)
        self.buton9.clicked.connect(self.click)
        self.buton10.clicked.connect(self.click)
        self.buton11.clicked.connect(self.click)
        self.buton12.clicked.connect(self.click)
        self.buton13.clicked.connect(self.click)
        self.buton14.clicked.connect(self.click)
        self.buton15.clicked.connect(self.click)
        self.buton16.clicked.connect(self.click)
        self.buton17.clicked.connect(self.click)
        self.buton18.clicked.connect(self.click)
        self.buton19.clicked.connect(self.click)
        self.buton20.clicked.connect(self.click)
        self.buton21.clicked.connect(self.click)
        self.buton22.clicked.connect(self.click)
        self.buton23.clicked.connect(self.click)
        self.buton24.clicked.connect(self.click)


        self.show()

    def click(self):
        sender = self.sender()
        if sender.text() == "0":
            self.yazı1.setText(self.yazı1.text() + "0")

        elif sender.text() == "1":
            self.yazı1.setText(self.yazı1.text() + "1")

        elif sender.text() == "2":
            self.yazı1.setText(self.yazı1.text() + "2")

        elif sender.text() == "3":
            sayı = self.yazı1.setText(self.yazı1.text() + "3")

        elif sender.text() == "4":
            self.yazı1.setText(self.yazı1.text() + "4")

        elif sender.text() == "5":
            self.yazı1.setText(self.yazı1.text() + "5")

        elif sender.text() == "6":
            self.yazı1.setText(self.yazı1.text() + "6")

        elif sender.text() == "7":
            self.yazı1.setText(self.yazı1.text() + "7")
        elif sender.text() == "8":
            self.yazı1.setText(self.yazı1.text() + "8")
        elif sender.text() == "9":
            self.yazı1.setText(self.yazı1.text() + "9")

        elif sender.text() == "+":
            self.yazı1.setText(self.yazı1.text() + "+")
        elif sender.text() == "-":
            self.yazı1.setText(self.yazı1.text() + "-")
        elif sender.text() == "*":
            self.yazı1.setText(self.yazı1.text() + "*")
        elif sender.text() == "/":
            self.yazı1.setText(self.yazı1.text() + "/")

        elif sender.text() == ",":
            self.yazı1.setText(self.yazı1.text() + ".")

        elif sender.text() == "üst":
            self.yazı1.setText(self.yazı1.text() + "**")

        elif sender.text() == "kök":
            self.yazı1.setText(self.yazı1.text() + "**0.5")

        elif sender.text() == "sin":
            self.yazı1.setText(self.yazı1.text() + "sin()")

        elif sender.text() == "cos":
            self.yazı1.setText(self.yazı1.text() + "cos()")
        elif sender.text() == "cot":
            self.yazı1.setText(self.yazı1.text() + "cot()")

        elif sender.text() == "tan":
            self.yazı1.setText(self.yazı1.text() + "tan()")
        elif sender.text() == "factorial":
            self.yazı1.setText(self.yazı1.text() + "factorial()")
        elif sender.text() == "log10":
            self.yazı1.setText(self.yazı1.text() + "log10")



        elif sender.text() == "=":
            self.işlem()

        elif sender.text() == "C":
            self.yazı1.clear()
            self.yazı2.clear()



    def işlem(self):
        top = self.yazı1.text()
        try:
            top = eval(top)
            top = str(top)
            self.yazı2.setText(top)

        except:
            self.yazı2.setText("İşlem hatası")


class Question(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi = QtWidgets.QLabel("Bu alan çözülen soru sayısı göndermek veya mesaj göndermek için kullanılmalıdır.")
        self.gonderen = QtWidgets.QLabel("Gönderen")
        self.kisi = QtWidgets.QLineEdit()
        self.alan = QtWidgets.QTextEdit()
        self.gonder = QtWidgets.QPushButton("Gönder")
        self.yazi2 = QtWidgets.QLabel()

        style = """
        QWidget {
            background-color: #f7f7f7; /* Arka plan rengi */
            font-family: Arial, Helvetica, sans-serif; /* Yazı tipi */
            font-size: 14px; /* Genel yazı boyutu */
            color: #333; /* Genel yazı rengi */
        }

        QLabel {
            font-size: 16px; /* Label yazı boyutu */
            color: #555; /* Label yazı rengi */
            margin-bottom: 5px; /* Alt boşluk */
        }

        QLineEdit, QTextEdit {
            border: 2px solid #ccc; /* Kenarlık */
            border-radius: 5px; /* Köşe yuvarlama */
            padding: 8px; /* İç boşluk */
            font-size: 14px; /* Yazı boyutu */
            background-color: #fff; /* Giriş alanı arka plan rengi */
            color: #333; /* Yazı rengi */
        }

        QLineEdit:focus, QTextEdit:focus {
            border: 2px solid #0078d7; /* Odaklanınca kenarlık rengi */
            outline: none; /* Çerçeve kaldır */
        }

        QPushButton {
            background-color: #0078d7; /* Düğme rengi */
            color: #fff; /* Düğme yazı rengi */
            font-size: 15px; /* Düğme yazı boyutu */
            padding: 8px 15px; /* Düğme iç boşluk */
            border: none; /* Kenarlık kaldır */
            border-radius: 5px; /* Köşe yuvarlama */
        }

        QPushButton:hover {
            background-color: #005a9e; /* Üzerine gelince düğme rengi */
        }

        QPushButton:pressed {
            background-color: #004578; /* Tıklandığında düğme rengi */
        }

        QLabel#yazi2 {
            color: #0078d7; /* Mesaj yazısı rengi */
            font-style: italic; /* Eğik yazı */
            margin-top: 10px; /* Üst boşluk */
        }
        """
        self.setStyleSheet(style)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.gonderen)
        h_box.addWidget(self.kisi)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box)
        v_box.addWidget(self.alan)
        v_box.addWidget(self.gonder)
        v_box.addWidget(self.yazi2)

        self.setLayout(v_box)

        self.gonder.clicked.connect(self.soru_gonder)



        self.show()


    def soru_gonder(self):
        self.mesaj = MIMEMultipart()

        self.mesaj["From"] = "ozturksedat631@gmail.com"
        self.mesaj["To"] = "cimenmert7@gmail.com"
        self.mesaj["Subject"] = "Mesaj bildirimi.."
        metin = "Gönderen kişi: " + self.kisi.text() + ",\n" + self.alan.toPlainText()


        self.mesaj_govdesi = MIMEText(metin, "plain")
        self.mesaj.attach(self.mesaj_govdesi)

        try:
            self.mail = smtplib.SMTP("smtp.gmail.com", 587)
            self.mail.ehlo()
            self.mail.starttls()
            self.mail.login("ozturksedat631@gmail.com", "ekwc asow cgmb vujf")
            self.mail.sendmail(self.mesaj["From"], self.mesaj["To"], self.mesaj.as_string())
            print("Mail başarıyla gönderildi")
            self.yazi2.setText("Mailiniz başarıyla gönderilmiştir...")
            self.mail.close()

        except:
            sys.stderr.write("Mesaj gönderimi başarısız oldu")
            self.yazi2.setText("Mail gönderilemedi lütfen bilikişiye raporlayınız...")


class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,400,400,100)
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)




        menu_bar = self.menuBar()
        menu1 = menu_bar.addMenu("Kazanımlarım")
        menu2 = menu_bar.addMenu("Diğer işlemler")
        menu3 = menu_bar.addMenu("Mesaj Gönder")

        tyt = menu1.addMenu("TYT")
        ayt = menu1.addMenu("AYT")

        turkce_tyt = QtWidgets.QAction("Türkçe",self)
        mat_tyt = QtWidgets.QAction("Matematik",self)
        turkce_ayt = QtWidgets.QAction("Türkçe",self)
        mat_ayt = QtWidgets.QAction("Matematik",self)
        geo_ayt = QtWidgets.QAction("Geometri",self)
        hesap = QtWidgets.QAction("Hesap Makinesi",self)
        deneme_sonuc = QtWidgets.QAction("Deneme sonuç",self)
        soru = QtWidgets.QAction("Soru Gönder",self)



        tyt.addAction(turkce_tyt)
        tyt.addAction(mat_tyt)
        ayt.addAction(turkce_ayt)
        ayt.addAction(mat_ayt)
        ayt.addAction(geo_ayt)
        menu2.addAction(hesap)
        menu3.addAction(deneme_sonuc)
        menu3.addAction(soru)


        self.setWindowTitle("Kişisel takip")

        turkce_tyt.triggered.connect(self.tik)
        turkce_ayt.triggered.connect(self.tik2)
        mat_tyt.triggered.connect(self.tik3)
        mat_ayt.triggered.connect(self.tik4)
        geo_ayt.triggered.connect(self.tik5)
        hesap.triggered.connect(self.tik6)
        deneme_sonuc.triggered.connect(self.tik7)
        soru.triggered.connect(self.tik8)


        self.show()

    def tik(self):
        self.tyt_tur = Tyt_tur()

    def tik2(self):
        self.ayt_tur = Ayt_tur()

    def tik3(self):
        self.tyt_mat = Tyt_mat()

    def tik4(self):
        self.ayt_mat = Ayt_mat()

    def tik5(self):
        self.geo_mat = Geometri()

    def tik6(self):
        self.hesap = Hesap()


    def tik7(self):
        self.deneme_sonuc = Deneme_sonuc()

    def tik8(self):
        self.soru = Question()



app = QtWidgets.QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())







