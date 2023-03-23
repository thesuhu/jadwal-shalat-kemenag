import utils.helper as helper
import requests
from bs4 import BeautifulSoup


class JadwalShalat:

    # mendapatkan data provinsi
    def data_provinsi(self):
        response = requests.get(
            helper.BASE_URL+'/jadwalshalat', cookies=helper.getCookies())
        soup = BeautifulSoup(response.content, 'html.parser')

        provinsi = []
        for node in soup.select('#search_prov option'):
            if node.text != 'PUSAT':
                provinsi.append({
                    'value': node['value'],
                    'text': node.text,
                })
        return provinsi

    # mendapatkan data kabupaten/kota by provinsi
    def data_kabupaten_kota(self, provinsiId: str) -> list:
        client = requests.Session()
        client.headers.update(
            {'Content-Type': 'application/x-www-form-urlencoded'})
        response = client.post(helper.BASE_URL + '/ajax/getKabkoshalat',
                               data={'x': provinsiId}, cookies=helper.getCookies())
        soup = BeautifulSoup(response.content, 'html.parser')
        kabkota = []
        for option in soup.select('option'):
            kabkota.append({'value': option['value'], 'text': option.text})
        return kabkota

    # mendapatkan data jadwal sholat by kabupaten/kota dalam 1 bulan
    def jadwal_shalat(self, provinsi_id: str, kabkota_id: str, bulan: int, tahun: int) -> dict:  # type: ignore
        client = requests.Session()
        payload = {
            'x': provinsi_id,
            'y': kabkota_id,
            'bln': bulan,
            'thn': tahun
        }
        # print(payload)
        response = client.post(
            helper.BASE_URL + '/ajax/getShalatbln', cookies=helper.getCookies(), data=payload)
        return response.json()

    # menampilkan jadwal shalat