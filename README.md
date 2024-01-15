# Projekta_darbs

## Apraksts 

Izveidot programmu, kas automātiski atlasa lietotāja izvēlētiem kritērijiem atbilstošus īres dzīvokļus Rīgā no tīmekļa vietnes ss.lv un izveido CSV failu, kurā ievieto datus par atlasītajiem dzīvokļiem

Lietotājs ievada vēlamo Rīgas reģionu, maksimālo īres cenu, minimālo istabu skaitu un izvēlas kolonnu pēc kuras izveidotais dzīvokļu saraksts tiks sakārtots.

CSV failam jābūt veidotam šādā veidā: 

```csv

adrese, istabu skaits, platība m2, cena, hipersaite

```

Atkarībā no izvēlētās secības kolonnas (`adrese`, `istabu skaits`, `platība m2`, `cena`) sarakstam ir jābūt sakārtotam augošā secībā

## Programmas izpilde

Lietotājs terminālī ievada sev vēlamos kritērijus dzīvokļu atlasei šādā secībā:

```shell
python find.py <reģions> <max-īre> <min-istabu skaits> <secības-kolonna>
```

Piemērs:

```shell
python find.py Āgenskalns 500 2 cena
```

## Izmantotās bibliotēkas

scrapy

## Papildus avoti 

https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/
