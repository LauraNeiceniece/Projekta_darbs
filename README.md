# Projekta_darbs

Bieži vien, it īpaši tikko studēt sākušiem jauniešiem, vai cilvēkiem, kuriem kādu dzīves apstākļu dēļ, piemēram, darba maiņas rezultātā nākas meklēt ērtāku dzīvesvietu, kas būs izdevīgāka jaunajiem apstākļiem, tāpēc, lai atvieglotu dzīvokļu meklēšanas procesu, tika radīta programma, kas palīdzētu lietotājam atrast sev piemērotāko dzīvokli ātrāk un ērtāk.

## Apraksts 

Darba mērķis bija izveidot programmu, kas automātiski atlasa lietotāja izvēlētiem kritērijiem atbilstošus īres dzīvokļus Rīgā no tīmekļa vietnes ss.lv (https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/) un izveido CSV failu, kurā ievieto datus par atlasītajiem dzīvokļiem

Kā atlases kritērijus lietotājs ievada vēlamo Rīgas reģionu, maksimālo īres cenu, minimālo istabu skaitu

CSV failam jābūt veidotam šādā veidā: 

```csv

adrese, istabu_skaits, platība_m2, cena, hipersaite, publicēšanas_datums

```

Atkarībā no publicēšanas datuma sarakstam ir jābūt sakārtotam no jaunākajiem ierakstiem augšgalā līdz vecākajiem ierakstiem lejā.

## Programmas izpilde

Lietotājs terminālī ievada sev vēlamos kritērijus dzīvokļu atlasei šādā secībā:

```shell
python project/dzivokli.py <reģions> <max-īre> <min-istabu skaits> 
```

Piemērs:

```shell
python project/dzivokli.py Āgenskalns 500 2 
```

Programma nolasa informāciju no vietnes https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/ un automātiski pārvietojas uz nākamo sludinājumu lapu, līdz sasniegta beidzamā vietnes lapa. 

Nolasot informāciju par dzīvokļiem(adrese, istabu skaits, platība, stāvs, sērija, cena) šīs vērtības tiek izgūtas, kā saraksts, kur adrese ir elements[1], istabu skaits - elements[2] ... cena - elements[6], līdz ar to, csv failā tiek ievietoti tie elementi un to vērtības, kas atbilst nosacījumam un csv failā arī tiek ievietota no vietnes izgūtā hipersaite uz dzīvokļa sludinājumu. 

Atverot katra dzīvokļa sludinājuma lapu no tās tiek izgūts publicēšanas datums, pēc kura tiek sakārtoti ieraksti csv failā sākot ar jaunākajiem. 

Rezultātā tiek izveidots csv fails, kurā ir kritērijiem atbilstošie dzīvokļi sakārtoti iepriekšminētajā secībā.

Programmas kods atrodas dzivokli.py failā un tiek izveidots csv fails ar nosaukumu dzivokli_data.csv

## Izmantotās bibliotēkas

scrapy - pielieto tīmekļa skrāpēšanai

csv - lieto csv failu lasīšanai un rakstīšanai

sys - nodrošina piekļuvi sistēmas specifiskiem parametriem un funkcijām

datetime - tika pielietota, lai formatētu datumu un laiku

urljoin - tikai pielietota, lai iegūtu pilnu hipersaiti, izgūtu no tīmekļa vietnes

