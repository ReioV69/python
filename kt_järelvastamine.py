#Reio Viikmaa 07.01.25
#KT järelvastamine
#Jootraha kalkulaator

#Restoranis on tavaks jätta teenindajale jootraha, mis moodustab tavaliselt vähemalt 15% arve summast.
#Programm küsib kasutajalt summa sõnena formaadis ##.##€ (kus iga # tähistab numbrit), eemaldab euro märgi (€) ja teisendab summa ujukomaarvuks (float). Näiteks, kui kasutaja sisestab 50.00€, tagastab programm 50.0.
#Eeldatakse, et kasutaja sisestab väärtused alati nõutud formaadis.
Jootraha_summa = input("Sisesta summa sõnena formaadis ##.##€: ")
summ = float(Jootraha_summa.replace("€", ""))
jootraha = summ * 0.15
print(f"Jootraha 15% on {jootraha}€")


# 5 Deep Thought
"""
Failis deep.py loo programm, mis küsib kasutajalt vastust Elu, universumi ja kõige suurele küsimusele.
    Kui kasutaja sisestab 42, forty-two või forty two (tõstutundetuseta), väljastab programm Yes.
    Kõigil muudel juhtudel väljastab programm No.
Eeldatakse, et kasutaja sisestab vastuse tekstina või arvuna.
"""

vastus = input("Mis on Elu, universumi ja kõige suurem küsimus? ")

if vastus == "42" or vastus == "forty-two" or vastus == "forty two":
    print("Yes")
else:
    print("No")


# 6 Faililaiendid
"""
Kuigi Windows ja macOS peidavad neid vahel, on enamikul failidel laiendid – järelliited, mis algavad punktiga (.) ja asuvad faili nime lõpus. Näiteks lõpevad GIF-failide nimed .gif ja JPEG-failide nimed .jpg või .jpeg laienditega. Topeltklõpsuga failil otsustab sinu arvuti selle laiendi põhjal, millist programmi faili avamiseks kasutada.

Veebibrauserid seevastu kasutavad failide kuvamiseks meediatüüpe (varasemalt tuntud kui MIME-tüübid). Faili allalaadimisel saadab veebiserver koos failiga HTTP päise, mis sisaldab faili meediatüüpi. Näiteks on GIF-faili meediatüüp image/gif ja JPEG-failil image/jpeg. Meediatüübi määramiseks vaatab veebiserver tavaliselt faili laiendit ja seostab selle vastava meediatüübiga.

Levinumate meediatüüpide kohta leiad infot:
developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

Failis laiendid.py loo programm, mis küsib kasutajalt faili nime ja väljastab selle faili meediatüübi, kui faili nimi lõpeb (tõstutundetuseta) mõne järgmistest laienditest:

    .gif → image/gif
    .jpg → image/jpeg
    .jpeg → image/jpeg
    .png → image/png
    .pdf → application/pdf
    .txt → text/plain
    .zip → application/zip

Kui faili nimi lõpeb mõne muu laiendiga või puudub laiend täielikult, väljastab programm:
application/octet-stream

Eeldatakse, et kasutaja sisestab failinime õigesti vormindatuna.
"""
Laiendid = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
failinimi = input("Sisesta failinimi: ")
faililaiend =  "." + failinimi.split(".")[-1]
if faililaiend in Laiendid:
    print(Laiendid[faililaiend])
else:
    print("application/octet-stream")