import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
       return None


    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class', 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        # Mengambil data magnitudo
        result = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
def tampilkan_data(result):
    if result is None:
        print("Sorry the data could not be displayed")

    print(f"Tanggal :  {result['tanggal']}")
    print(f"Waktu :  {result['waktu']}")
    print(f"Magnitudo :  {result['magnitudo']}")
    print(f"Kedalaman :  {result['kedalaman']}")
    print(f"lokasi :  {result['lokasi']}")
    print(f"koordinat : LS =  {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"dirasakan : {result['dirasakan']}")


if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)