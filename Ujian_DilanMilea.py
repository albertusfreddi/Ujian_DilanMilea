import requests

api = '4so5q9zrJyhfJHCqYpmlZWVZBn5ocQTcQ9wMmtGPZk7nTiFTum5zyKb3JiLcEZPH'
urlProvinsi = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
urlKodePos = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'


dataProvinsi = requests.get(urlProvinsi).json()
dataKodePos = requests.get(urlKodePos).json()


ProvinsiDilan = 'BANTEN'
KabupatenDilan = 'TANGERANG'
KecamatanDilan = 'CISAUK'
KelurahanDilan = 'SAMPORA'
ProvinsiMilea = 'JAWA BARAT'
KabupatenMilea = 'BANDUNG'
KecamatanMilea = 'BANDUNG WETAN'
KelurahanMilea = 'CITARUM'

kodeProvinsi = []
listProvinsi = []
for data in dataProvinsi.keys():
    kodeProvinsi += [data]
for data in dataProvinsi.values():
    listProvinsi += [data]

if ProvinsiDilan in listProvinsi:
    index = listProvinsi.index(ProvinsiDilan)
    indexDilan = kodeProvinsi[index]
if ProvinsiMilea in listProvinsi:
    index = listProvinsi.index(ProvinsiMilea)
    indexMilea = kodeProvinsi[index]

for dataDict in dataKodePos[indexDilan]:
    if dataDict['urban'] == KelurahanDilan:
        if dataDict['sub_district'] == KecamatanDilan:
            if dataDict['city'] == KabupatenDilan:
                kodePosDilan = dataDict['postal_code']

for dataDict in dataKodePos[indexMilea]:
    if dataDict['urban'] == KelurahanMilea:
        if dataDict['sub_district'] == KecamatanMilea:
            if dataDict['city'] == KabupatenMilea:
                kodePosMilea = dataDict['postal_code']

urlJarak =  f'https://www.zipcodeapi.com/rest/{api}/distance.json/{kodePosDilan}/{kodePosMilea}/km'
dataJarak = requests.get(urlJarak).json()
JarakDilanMilea = dataJarak['distance']

print(f'Kode Pos lokasi Dilan adalah {kodePosDilan}')
print(f'Kode Pos lokasi Milea adalah {kodePosMilea}')
print(f'Jarak Dilan & Milea adalah {JarakDilanMilea} km')
