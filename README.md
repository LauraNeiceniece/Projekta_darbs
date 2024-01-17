# Projekta_darbs

## Apraksts 

Izveidot programmu, kas automātiski atlasa lietotāja izvēlētiem kritērijiem atbilstošus īres dzīvokļus Rīgā no tīmekļa vietnes ss.lv un izveido CSV failu, kurā ievieto datus par atlasītajiem dzīvokļiem

Lietotājs ievada vēlamo Rīgas reģionu, maksimālo īres cenu, minimālo istabu skaitu

CSV failam jābūt veidotam šādā veidā: 

```csv

adrese, istabu_skaits, platība_m2, cena, hipersaite, publicēšanas_datums

```

Atkarībā no publicēšanas datuma sarakstam ir jābūt sakārtotam no jaunākajiem ierakstiem līdz vecākajiem 

## Programmas izpilde

Lietotājs terminālī ievada sev vēlamos kritērijus dzīvokļu atlasei šādā secībā:

```shell
python project.py <reģions> <max-īre> <min-istabu skaits> 
```

Piemērs:

```shell
python project.py Āgenskalns 500 2 
```

## Izmantotās bibliotēkas

scrapy

## Papildus avoti 

https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/
